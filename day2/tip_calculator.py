bill = input("What was the total bill?: ")
precentage = input("What precentage tip would you like to give? 10, 12, or 15: ")
people = input("How many people to split the bill?: ")

if bill[0] == "$":
  bill = bill[1:]

sum = float(bill)*(1+(int(precentage)/100))

sum /= int(people)

round_sum = round(sum, 2)

result = f"Each person should pay: ${round_sum}"

print(result)