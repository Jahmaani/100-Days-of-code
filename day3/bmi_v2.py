height = input("height: ")
weight = input("weight: ")

result = float(weight) / float(height)**2

if result < 18.5:
  print("underweight")
elif result < 25:
  print("normal weight")
elif result < 30:
  print("overweight")
elif result < 35:
  print("obese")
else:
  print("clinically obese")

print(int(result))