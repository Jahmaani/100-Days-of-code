height = int(input("Give your height: "))

if height >= 120:
  print("You can ride!")
  age = int(input("Give your age: "))
  if age < 12:
    print("please pay $5.")
  elif age >= 12 and age <= 18:
    print("please pay $7.")
  else:
    print("please pay $12.")
else:
  print("you cant ride.")