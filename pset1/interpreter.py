opr = input("Expression: ")

x, y, z = opr.split()

if y == "+":
    print(float(int(x) + int(z)))

elif y == "-":
    print(float(int(x) - int(z)))

elif y == "*":
    print(float(int(x) * int(z)))

else:
    print(float(int(x) / int(z)))
