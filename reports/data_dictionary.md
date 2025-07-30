# 🧾 Data Dictionary – Hotel Booking Demand Cleaned Dataset

This file describes the columns in the cleaned dataset (`hotel_bookings_cleaned.csv`), including data types, explanations, and transformations made during cleaning.

| Column Name | Description | Data Type | Transformation |
|-------------|-------------|-----------|----------------|
| hotel | Type of hotel (Resort Hotel or City Hotel) | object | None |
| is_canceled | 1 if the booking was canceled, 0 otherwise | int64 | None |
| lead_time | Number of days between booking and arrival | int64 | Outliers removed using IQR |
| arrival_date_year | Year of arrival | int64 | None |
| arrival_date_month | Month of arrival (e.g., July) | object | None |
| arrival_date_week_number | Week number of the year | int64 | None |
| arrival_date_day_of_month | Day of the month | int64 | None |
| stays_in_weekend_nights | Nights stayed over the weekend | int64 | Outliers removed using IQR |
| stays_in_week_nights | Nights stayed during the week | int64 | Outliers removed using IQR |
| adults | Number of adults | int64 | Removed rows where adults + children + babies = 0 |
| children | Number of children | float64 → int | Missing values filled with 0 |
| babies | Number of babies | int64 | None |
| meal | Type of meal booked (e.g., BB, HB, SC) | object | 'Undefined' replaced with 'SC' |
| country | Country of origin | object | Missing values replaced with 'Unknown' |
| market_segment | Booking origin channel (e.g., Online TA, Corporate) | object | None |
| distribution_channel | How the booking was distributed (e.g., Direct, TA/TO) | object | None |
| is_repeated_guest | 1 if the guest has stayed before | int64 | None |
| previous_cancellations | Number of previous cancellations by the customer | int64 | None |
| previous_bookings_not_canceled | Previous bookings not canceled | int64 | None |
| reserved_room_type | Room type reserved by the customer | object | None |
| assigned_room_type | Room type actually assigned | object | None |
| booking_changes | Number of changes to the booking | int64 | None |
| deposit_type | Type of deposit made (e.g., No Deposit, Non Refund) | object | None |
| agent | ID of booking agent | float64 → int | Missing values filled with 0 |
| company | ID of company that made the booking | float64 → int | Missing values filled with 0 |
| days_in_waiting_list | Number of days booking was on the waiting list | int64 | None |
| customer_type | Type of customer (e.g., Transient, Group) | object | None |
| adr | Average Daily Rate (price per night) | float64 | Outliers removed using IQR |
| required_car_parking_spaces | Number of parking spaces required | int64 | None |
| total_of_special_requests | Number of special requests made by the customer | int64 | None |
| reservation_status | Status of the booking (e.g., Check-Out, Canceled) | object | None |
| reservation_status_date | Date of last status update | object → datetime | Converted to datetime |
