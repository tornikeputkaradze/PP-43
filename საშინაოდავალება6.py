orders = ["ყავა", "ჩაი", "ყავა", "წვენი", "ჩაი", "ყავა", "წყალი"]
unique_orders = []
for item in orders:
    if item not in unique_orders:
        unique_orders.append(item)
print("უნიკალური:", unique_orders)

frequencies = [(item, orders.count(item)) for item in unique_orders]
print("სიხშირე:", frequencies)
max_product = ""
max_count = 0

for product, count in frequencies:
    if count > max_count:
        max_count = count
        max_product = product
print(f"ყველაზე პოპულარული: {max_product} ({max_count}-ჯერ)")

recent_three = orders[:-4:-1]
print("ბოლო 3 შეკვეთა:", recent_three)