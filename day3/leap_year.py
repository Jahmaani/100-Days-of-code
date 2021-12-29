# jaollinen 4
# paitsi jos on jaollinen 100
# mutta jos se on jaollinen 400

year = 1989

if year % 4 == 0:
  if year % 100 == 0 and year % 400 != 0:
    print("not leap")
  else:
    print("leap")
else:
  print("not leap")
