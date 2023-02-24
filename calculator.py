num1 = input("put first number: ")
num2 = input("put second number: ")
operation = input("what do you want to do? choose 1 for add, 2 for subtract, 3 for divide and 4 for multiply:")
num1 = int(num1)
num2 = int(num2)



def calculator():
    while True:
        if operation == "1":    
            print("Your number added together is:",num1 + num2)
            break
        elif operation == "2":
            print("Your number subtracted is:",num1 - num2)
            break
        elif operation == "3":
            print("Your number divided is: ", num1/num2)
            break
        elif operation == "4":
            print("Your number multiplied is: ",num1*num2)
            break
        else:
            print("Put in a valid operation.")
            break
    return num1 and num2 

calculator()
    

