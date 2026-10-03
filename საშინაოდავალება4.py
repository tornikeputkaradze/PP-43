# amount = float(input("ყიდვის თანხა (ლარი): "))
# promo = input("პრომო-კოდი (თუ არ გაქვთ — Enter): ")
#
# if amount >= 200:
#     discount = 20
# elif amount >= 100:
#     discount = 10
# elif amount >= 50:
#     discount = 5
# else:
#     discount = 0
#
# price = amount - (amount * discount / 100)
#
# if promo.lower() == "vip":
#     price -= 5
#     print("🎁 VIP კოდი: დამატებით -5 ლარი")
#
# print(f"ფასდაკლება: {discount}%")
# print(f"გადასახდელი: {price:.2f} ლარი")
#
#
# print("=== სტუდენტის შეფასების სისტემა ===")
#
# try:
#     name = input("სტუდენტის სახელი: ").strip()
#
#     if not name:
#         raise ValueError("სახელი ცარიელია")
#
#     score = int(input("მიღებული ქულა: "))
#     max_score = int(input("მაქსიმალური ქულა: "))
#
#     if max_score == 0:
#         raise ZeroDivisionError
#
#     if score < 0 or score > max_score:
#         raise ValueError("არასწორი დიაპაზონი")
#
#     percent = score / max_score * 100
#     initial = name[0]
#
#     if percent >= 91:
#         grade = "A"
#     elif percent >= 81:
#         grade = "B"
#     elif percent >= 71:
#         grade = "C"
#     elif percent >= 61:
#         grade = "D"
#     elif percent >= 51:
#         grade = "E"
#     elif percent >= 41:
#         grade = "FX"
#     else:
#         grade = "F"
#
# except ValueError as error:
#     if str(error) == "სახელი ცარიელია":
#         print("❌ სახელი ცარიელი ვერ იქნება")
#     elif str(error) == "არასწორი დიაპაზონი":
#         print("❌ ქულა არასწორ დიაპაზონშია")
#     else:
#         print("❌ ქულები მთელი რიცხვებით ჩაწერეთ")
#
# except ZeroDivisionError:
#     print("❌ მაქსიმალური ქულა 0 ვერ იქნება")
#
# else:
#     print(f"✅ {initial}. {name} — {percent:.1f}% — შეფასება: {grade}")
#
# finally:
#     print("შეფასების სისტემამ მუშაობა დაასრულა")