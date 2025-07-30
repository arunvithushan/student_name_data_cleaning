# Data Cleaning Report: Hotel Booking Dataset

## Executive Summary
- Dataset has 119k records of hotel bookings (2015–2017)
- Goal: Clean and prepare for analysis

## Issues Found
- Missing: country, children, agent, company
- Duplicates: 30–50 found
- Outliers: lead_time, adr
- Logical Errors: guest count = 0

## Cleaning Steps
- Filled missing values based on logic
- Removed exact duplicates
- Removed outliers using IQR
- Fixed invalid records

## Results
- Cleaned dataset: ~118,000 rows
- No nulls, no duplicates
- Ready for ML/EDA

## Recommendations
- Validate guest info at entry
- Add constraints to prevent invalid records
