EXTRA_PRICES = {"popcorn": 6, "cola": 3, "nachos": 7}

def book_tickets(movie, *seats, discount=0, **extras):

    valid_seats = list(filter(
        lambda s: (
            len(s) >= 2
            and s[0] in "ABCDE"
            and s[1:].isdigit()
            and 1 <= int(s[1:]) <= 10
        ),
        seats
    ))

    rejected = len(seats) - len(valid_seats)


    seat_prices = list(map(
        lambda s: 15 if s[0] in "AB" else 10,
        valid_seats
    ))

    tickets_total = sum(seat_prices)

    tickets_after_discount = tickets_total * (1 - discount / 100)


    extras_total = 0
    for item, quantity in extras.items():
        extras_total += EXTRA_PRICES.get(item, 0) * quantity

    total = round(tickets_after_discount + extras_total, 2)

    return {
        "movie": movie,
        "seats": valid_seats,
        "rejected": rejected,
        "total": total
    }



order1 = book_tickets("ოპენჰაიმერი", "A5", "C3", "Z1", "B12", "E10")
order2 = book_tickets("დიუნა", "B1", "B2", discount=20, popcorn=2, cola=2)
order3 = book_tickets("ინტერსტელარი", "D4", nachos=1)
order4 = book_tickets("ბარბი")

for order in [order1, order2, order3, order4]:
    print(f"{order['movie']}: ადგილები {order['seats']}, უარყოფილი: {order['rejected']}, სულ: {order['total']} ლარი")