from datetime import datetime, timedelta

# 1. Subtract five days from current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("=== Task 1 ===")
print("Current date:", today)
print("5 days ago:", five_days_ago)


# 2. Print yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\n=== Task 2 ===")
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3. Drop microseconds from datetime
no_microseconds = today.replace(microsecond=0)

print("\n=== Task 3 ===")
print("Original:", today)
print("Without microseconds:", no_microseconds)


# 4. Calculate difference between two dates in seconds
date1 = datetime(2025, 1, 1, 0, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)

difference = date2 - date1

print("\n=== Task 4 ===")
print("Difference in seconds:", difference.total_seconds())