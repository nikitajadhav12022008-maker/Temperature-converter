#python based temp converter
#input temp
temp = float(input("enter temperature:"))
#input unit
unit  = input("C OR F:").upper()

#conditions
if(unit == "C"):
    print((temp * 9/5) + 32)
else:

    print((temp - 32) * 5/9)
