# text = "Python არის მარტივი, Python არის ძლიერი და Python პოპულარულია."
#
# text = text.lower()
# text = text.replace(",", "")
# text = text.replace(".", "")
#
# words = text.split()
#
# word_count = {}
#
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# for word in word_count:
#     print(f"{word}: {word_count[word]}")
#
# most_common_word = ""
# max_count = 0
#
# for word in word_count:
#     if word_count[word] > max_count:
#         max_count = word_count[word]
#         most_common_word = word
#
# print(f"ყველაზე ხშირი: '{most_common_word}' ({max_count}-ჯერ)")
#
# print(f"სხვადასხვა სიტყვა: {len(word_count)}")
#



# prices = {
#     "ლეპტოპი": 2500,
#     "მაუსი": 40,
#     "კლავიატურა": 120,
#     "მონიტორი": 650
# }
#
# stock = {
#     "ლეპტოპი": 2,
#     "მაუსი": 10,
#     "კლავიატურა": 1,
#     "მონიტორი": 3
# }
#
# orders = [
#     ("ნინო", "ლეპტოპი", 1),
#     ("გიორგი", "მაუსი", 3),
#     ("ანა", "კლავიატურა", 1),
#     ("ნინო", "მაუსი", 2),
#     ("გიორგი", "კლავიატურა", 1),
#     ("ანა", "ტელეფონი", 1),
#     ("ლუკა", "ლეპტოპი", 1),
#     ("ლუკა", "მონიტორი", 5),
# ]
#
# user_expenses = {}
# failed_users = set()
# total_revenue = 0
#
# print("▶ შედეგი")
#
#
# for customer, product, quantity in orders:
#
#     if product not in prices:
#         print(f"❌ {customer}: '{product}' არ იყიდება")
#         failed_users.add(customer)
#
#
#     elif stock[product] < quantity:
#         print(f"⚠️ {customer}: {product} — მარაგში მხოლოდ {stock[product]} ცალია")
#         failed_users.add(customer)
#
#     else:
#         cost = prices[product] * quantity
#         stock[product] -= quantity
#         total_revenue += cost
#
#
#         user_expenses[customer] = user_expenses.get(customer, 0) + cost
#
#         print(f"✅ {customer}: {product} x{quantity} = {cost} ლარი")
#
#
# out_of_stock = [product for product, count in stock.items() if count == 0]
#
# print("--- ანგარიში ---")
#
# for customer, spent in user_expenses.items():
#     print(f"{customer}: {spent} ლარი")
#
# print(f"შემოსავალი: {total_revenue} ლარი")
# print(f"ამოიწურა: {sorted(out_of_stock)}")
# print(f"წარუმატებელი შეკვეთა ჰქონდათ: {sorted(list(failed_users))}")