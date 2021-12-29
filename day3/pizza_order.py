size = "L"
pepperoni = "Y"
extra_cheese = "Y"

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if pepperoni == "Y" and size == "S":
  bill += 2
elif pepperoni == "Y" and size != "S":
  bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")