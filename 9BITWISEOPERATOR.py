#BITWISE OPRERATOR
#OR,AND,NOT,
#first change the data in the form of binary
#ande then do the operation and again change t into the decimal.
try:
    a=int(input("enter the firsyt no= "))
    b=int(input("enter the second no= "))
    print(a&b)
    print(a|b)
    print(a^b)
    print(~a)
    print(a<<2)#right 00 add
    print(a>>2)
except:
    print("invalid input")
            
