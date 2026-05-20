import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd

# --- AUTOMATIC PATH CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Google Service Account Key File (This file must be added to .gitignore for security)
KEY_FILE = os.path.join(BASE_DIR, "credentials.json")

# --- TARGET E-COMMERCE CONFIGURATION ---
# Note: In production, change this to your specific Google Search Console Property
TARGET_SITE_URL = "sc-domain:example-ecommerce.com"
OUTPUT_FILE = os.path.join(BASE_DIR, "SEO_Page2_Opportunities_Report.xlsx")


def run_seo_opportunity_analysis():
    """Fetches Google Search Console data via API, filters Page 2 keywords

    (positions 11-20) with high impressions, and exports an automation report.
    """
    try:
        # 1. Authentication Check
        if not os.path.exists(KEY_FILE):
            print(f"❌ AUTH ERROR: '{KEY_FILE}' not found!")
            print(
                "Please place your Google Service Account credentials.json in the same directory."
            )
            return

        creds = service_account.Credentials.from_service_account_file(KEY_FILE)
        service = build("searchconsole", "v1", credentials=creds)

        # 2. Data Request Payload (Last 3 Months Analytics)
        request_body = {
            "startDate": "2025-12-15",
            "endDate": "2026-03-15",
            "dimensions": ["query", "page"],
            "rowLimit": 5000,
        }

        print(f" Fetching API data for {TARGET_SITE_URL}...")
        response = (
            service.searchanalytics()
            .query(siteUrl=TARGET_SITE_URL, body=request_body)
            .execute()
        )

        # 3. Data Processing & Analytical Filtering
        if "rows" in response:
            df = pd.DataFrame([
                {
                    "Keyword": row["keys"][0],
                    "Target_Page": row["keys"][1],
                    "Clicks": row["clicks"],
                    "Impressions": row["impressions"],
                    "Position": round(row["position"], 1),
                }
                for row in response["rows"]
            ])

            # Filtering Page 2 Opportunities (Positions between 10.1 and 20.0)
            # These are high-intent keywords that can be easily pushed to Page 1 via E-E-A-T or Internal Linking
            opportunities_df = df[
                (df["Position"] > 10.0) & (df["Position"] <= 20.0)
            ].copy()

            # Sorting by highest impressions to capture 'Low-Hanging Fruits' first
            opportunities_df = opportunities_df.sort_values(
                by="Impressions", ascending=False
            )

            # 4. Exporting Business Intelligence Report
            opportunities_df.to_excel(OUTPUT_FILE, index=False)
            print(f"\n SUCCESS: SEO Opportunity Report generated successfully!")
            print(f" Output Directory: {OUTPUT_FILE}")
            print(
                f" Uncovered {len(opportunities_df)} high-potential Page 2 keywords."
            )

        else:
            print("\n API WARNING: No data returned from Search Console!")
            print(
                "Verify that the Service Account Email has 'Full/Owner' permissions in GSC."
            )

    except Exception as e:
        print(f"\n❌ Operational Error: {e}")


if __name__ == "__main__":
    print("--- Starting E-Commerce Marketing Analytics Automation ---")
    run_seo_opportunity_analysis()
