print("a-- Decimal to Binary \t\t b--Decimal to Octal \t\t c-- Decimal to Hexadecimal")
print("d-- Binary to Decimal \t\t e--Binary to Octal \t\t f-- Binary to Hexadecimal")
print("i-- Octal to Binary \t\t j--Octal to Decimal \t\t k-- Octal to Hexadecimal")
print("l-- Hexadecimal to Binary \t m--Hexadecimal to Octal \t n-- Hexadecimal to Decimal\n")
conversion= input("Enter as Manual:").strip()

if conversion.isupper():
    conversion=conversion.lower()

num=input("Enter the number:")


   #Decimal to Binary
if (conversion == 'a'):
    num=int(num)
    answer=bin(num)
    print("Answer is :{}".format(answer[2::]))

#Decimal to Octal  
if (conversion == 'b'):
    num=int(num)
    answer=oct(num)
    print("Answer is :{}".format(answer[2::]))

#Decimal to Hexadecimal
if (conversion == 'c'):
    num=int(num)
    answer=hex(num)
    print("Answer is :{}".format(answer[2::]))    

#Binary to Decimal  
if (conversion == 'd'):
    answer=int(num,2)
    answer=int(answer)
    print("Answer is :{}".format(answer)) 

#Binary to Octal
if (conversion == 'e'):
    answer=int(num,2)
    answer=oct(answer)
    print("Answer is :{}".format(answer[2::])) 

#Binary to Hexadecimal
if (conversion == 'f'):
    answer=int(num,2)
    answer=hex(answer)
    print("Answer is :{}".format(answer[2::])) 

#Octal to Binary
if (conversion == 'i'):
    answer=int(num,8)
    answer=bin(answer)
    print("Answer is :{}".format(answer[2::]))

#Octal to Decimal
if (conversion == 'j'):
    answer=int(num,8)
    answer=int(answer)
    print("Answer is :{}".format(answer))

#Octal to Hexadecimal
if (conversion == 'k'):
    answer=int(num,8)
    answer=hex(answer)
    print("Answer is :{}".format(answer[2::]))

#Hexadecimal to Binary
if (conversion == 'l'):
    answer=int(num,16)
    answer=bin(answer)
    print("Answer is :{}".format(answer[2::]))

#Hexadecimal to Octal
if (conversion == 'm'):
    answer=int(num,16)
    answer=oct(answer)
    print("Answer is :{}".format(answer[2::]))

#Hexadecimal to Decimal
if (conversion == 'n'):
    answer=int(num,16)
    answer=int(answer)
    print("Answer is :{}".format(answer))


