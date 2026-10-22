def countdown(start):
    while start > 0:
        yield start
        start -= 1
    yield "სტარტი! 🚀"


def squares_up_to(limit):
    n = 1
    while n * n <= limit:
        yield n * n
        n += 1


launch = countdown(3)
print(next(launch))
print(next(launch))
print(list(launch))
print(list(launch))

print(list(squares_up_to(50)))
print(sum(squares_up_to(100)))

for square in squares_up_to(20):
    print(square, end=" ")
print()




orders = [
    ("ხაჭაპური", 2, 12.5),
    ("ლობიანი", 1, 7.0),
    ("ლიმონათი", 3, 3.5),
    ("ხინკალი", 20, 1.2),
    ("ჩაი", 2, 2.5),
]

revenue = sum(qty * price for _, qty, price in orders)
items_count = sum(qty for _, qty, _ in orders)
has_big_order = any(qty >= 10 for _, qty, _ in orders)
biggest_line = max(qty * price for _, qty, price in orders)
first_cheap = next((name for name, _, price in orders if price < 3), None)
first_very_cheap = next((name for name, _, price in orders if price < 1), "ასეთი არ არის")
several = ", ".join(name for name, qty, _ in orders if qty > 1)
expensive_names = tuple(name for name, _, price in orders if price > 5)

print("შემოსავალი:", round(revenue, 2), "₾")
print("ერთეულები:", items_count)
print("დიდი შეკვეთა (10+)?", has_big_order)
print("ყველაზე დიდი ხაზი:", biggest_line, "₾")
print("პირველი 3 ₾-ზე იაფი:", first_cheap)
print("პირველი 1 ₾-ზე იაფი:", first_very_cheap)
print("რამდენიმე ცალი:", several)
print(expensive_names)