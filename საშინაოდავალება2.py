raw_username = "  Super_Coder_2026  "
username = raw_username.strip()
username = username.lower()
username = username.replace("_", "-")

print("მომხმარებლის სახელი:", username)
print("სიგრძე:", len(username))
print("იწყება 'super'-ით:", username.startswith("super"))
print("ტირეების რაოდენობა:", username.count("-"))

without_dash = username.replace("-", "")
print("მხოლოდ ასოები და ციფრები:", without_dash.isalnum())