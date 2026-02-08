#!/usr/bin/env python3
"""Test script to verify custom scenarios are merging correctly."""

import pandas as pd
from scenario_manager import ScenarioManager

# Load Excel data
print("📊 Loading Excel data...")
excel_file = pd.ExcelFile("Coach_Training_Scenarios_ICF_PCC.xlsx")
data = {}
for sheet_name in excel_file.sheet_names:
    data[sheet_name] = pd.read_excel("Coach_Training_Scenarios_ICF_PCC.xlsx", sheet_name=sheet_name)
    print(f"  - {sheet_name}: {len(data[sheet_name])} scenarios")

print("\n" + "="*80)

# Load custom scenarios
print("\n📚 Loading custom scenarios...")
manager = ScenarioManager()
stats = manager.get_stats()
print(f"  - Total custom: {stats['total']}")
print(f"  - Categories: {stats['by_category']}")

print("\n" + "="*80)

# Merge
print("\n🔀 Merging data...")
if stats['total'] > 0:
    merged_data = manager.merge_with_excel_data(data)

    print("\n✅ After merge:")
    for category, df in merged_data.items():
        if 'Source' in df.columns:
            custom_count = len(df[df['Source'] == 'Real Transcript'])
            if custom_count > 0:
                print(f"  - {category}: {len(df)} total ({custom_count} custom)")

                # Show the custom scenario IDs
                custom_scenarios = df[df['Source'] == 'Real Transcript']
                for idx, row in custom_scenarios.iterrows():
                    print(f"    • {row['ID']}: {row['Client Question / Scenario'][:60]}...")
else:
    print("❌ No custom scenarios to merge")

print("\n" + "="*80)
print("\n✅ Test complete! Check output above.")
