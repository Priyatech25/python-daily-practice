import random

# Products and months
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_data = {}

# Generate random sales
for month in months:
    sales_data[month] = {}
    for product in products:
        sales_data[month][product] = random.randint(10000, 50000)

print("\n----- SALES DATA -----")
for month in sales_data:
    print(month, sales_data[month])

# Total Revenue
total_revenue = 0
for month in sales_data:
    for product in sales_data[month]:
        total_revenue += sales_data[month][product]

print("\nTotal Revenue:", total_revenue)

# Best Product
product_total = {}

for month in sales_data:
    for product, value in sales_data[month].items():
        product_total[product] = product_total.get(product, 0) + value

best_product = max(product_total, key=product_total.get)

print("Best Selling Product:", best_product)

# Monthly Growth
print("\n----- MONTHLY GROWTH -----")
previous = None

for month in months:
    month_total = sum(sales_data[month].values())
    if previous is not None:
        growth = ((month_total - previous) / previous) * 100
        print(f"{month} Growth: {growth:.2f}%")
    previous = month_total