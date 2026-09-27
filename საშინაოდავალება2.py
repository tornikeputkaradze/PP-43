raw_username = "  Super_Coder_2026  "

username = raw_username.strip().lower().replace("_", "-")

print("მომხმარებლის სახელი:", username)
print("სიგრძე:", len(username))
print("იწყება 'super'-ით:", username.startswith("super"))
print("ტირეების რაოდენობა:", username.count("-"))

without_dash = username.replace("-", "")
print("მხოლოდ ასოები და ციფრები:", without_dash.isalnum())



card = "4111222233334444"
phone = "599123456"

# ბარათის შენიღბვა
masked = "**** **** **** " + card[-4:]
print("შენიღბული:", masked)

# პირველი 4 ციფრი
print("პირველი 4 ციფრი:", card[:4])

# ციფრების რაოდენობა
print("ციფრების რაოდენობა:", len(card))

# შებრუნებული ნომერი
print("შებრუნებული:", card[::-1])

# ტელეფონის ფორმატირება
formatted_phone = phone[:3] + " " + phone[3:5] + " " + phone[5:7] + " " + phone[7:]
print("ტელეფონი:", formatted_phone)