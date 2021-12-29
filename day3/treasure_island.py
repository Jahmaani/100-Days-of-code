print("Welcome to treasure island! Your mission is to find the treasure")
i = 0
i = int(input("1 or 2: "))
b = False

if(i == 1):
  print("Game over!")
else:
  i = int(input("1 or 2: "))
  if(i == 1):
    print("Game over!")
  else:
    i = int(input("1, 2 or 3: "))
    if i == 1 or i == 2:
      print("Game over!")
    else:
      print("You find treasure!")



