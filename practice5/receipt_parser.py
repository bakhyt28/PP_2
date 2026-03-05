import re   # module for working with text patterns (regular expressions)
import json # module to create JSON formatted output

# open the receipt file and read all text
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()  # store the whole receipt text in variable


# 1 Extract prices

# find all prices after the symbol "x"
# example: 2,000 x 154,00 → extract 154,00
prices = re.findall(r"\d+,\d+\s*x\s*([\d\s]+,\d+)", text)

# remove spaces inside numbers (example: 1 200,00 → 1200,00)
prices = [p.replace(" ", "") for p in prices]


# 2 Extract product names

# product names appear after numbers like:
# 1.
# product name
products = re.findall(r"\d+\.\n([^\n]+)", text)


# 3 Calculate total amount

total = 0  # variable to store total price

for p in prices:
    value = float(p.replace(",", "."))  # convert price string to float
    total += value  # add price to total


# 4 Extract date and time

# search for date format: dd.mm.yyyy hh:mm:ss
datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)
date_time = datetime_match.group() if datetime_match else None


# 5 Find payment method

# check if payment was made by bank card
payment = re.search(r"Банковская карта", text)
payment_method = payment.group() if payment else "Unknown"


# 6 Create JSON output

# store all extracted information in dictionary
result = {
    "products": products,
    "prices": prices,
    "total_calculated": total,
    "date_time": date_time,
    "payment_method": payment_method
}

# print the result as formatted JSON
print(json.dumps(result, indent=4, ensure_ascii=False))