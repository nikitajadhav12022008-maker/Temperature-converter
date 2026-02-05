temp = float(input("enter temperature:"))
unit  = input("C OR F:").upper()

if(unit == "C"):
    print((temp * 9/5) + 32)
else:
    print((temp - 32) * 5/9)