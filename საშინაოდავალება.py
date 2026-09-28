celsius = float(input("შეიყვანე ტემპერატურა ცელსიუსით: "))

fahrenheit = celsius * 9 / 5 + 32

print("ფარენჰაიტით:", fahrenheit)


seconds = int(input("შეიყვანე წამების რაოდენობა: "))
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds_left = remaining % 60
print(hours, "საათი", minutes, "წუთი", seconds_left, "წამი")


bill = float(input("ჩეკის თანხა: "))
tip_percent = int(input("ჩაის ფული (%): "))
people = int(input("ადამიანების რაოდენობა: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print("ჩაის ფული:", round(tip, 2))
print("სულ გადასახდელი:", round(total, 2))
print("თითო ადამიანზე:", round(per_person, 2))