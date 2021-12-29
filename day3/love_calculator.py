n1 = "kate"
n2 = "jack"


true = 0
love = 0


true += (n1+n2).count("t")
true += (n1+n2).count("r")
true += (n1+n2).count("u")
true += (n1+n2).count("e")

love += (n1+n2).count("l")
love += (n1+n2).count("o")
love += (n1+n2).count("v")
love += (n1+n2).count("e")

result = str(true) + str(love)

result_to_int = int(result)

if result_to_int < 10 or result_to_int > 90:
  print((f"true love {result_to_int}"))
elif result_to_int > 40 and result_to_int < 50:
  print((f"love {result_to_int}"))
else:
  print((f"not love {result_to_int}"))
