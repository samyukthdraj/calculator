#calculator

#Addition
def add(n1,n2):
    """A+B"""
    return n1+n2

#Subraction
def sub(n1,n2):
    """A-B"""
    return n1-n2

#Multiplication
def mul(n1,n2):
    """A*B"""
    return n1*n2

#Division
def div(n1,n2):
    """A/B"""
    return n1/n2

operations={"+":add,
            "-":sub,
            "*":mul,
            "/":div,
            }
result=0 #here the result is first initialised as 0, this is before all the calculations start 
def clear():
    print("\n"*110)
def calculation1():
    global result
    num1=int(input("ENTER THE FIRST NUMBER: "))
    num2=int(input("ENTER THE SECOND NUMBER: "))
    print("WHICH OPERATION DO YOU WANT TO DO WITH THESE NUMBERS?\n")
    for i in operations:
        print(i)
    op=input("\nENTER YOUR DESIRED OPERATION HERE: ")    
    calcuate=operations[op]
    result=calcuate(num1,num2)
    print(f"YOUR CALCULATION IS : {num1} {op} {num2} = {result}\n")


calculation1()

switch= True
while switch==True:
    continue_use=input("Do you want to continue or use a new calculator? Type 'y' to continue or 'n' for new calcuator, type 'e' to exit: ")
    if continue_use=='y':
        print(f"YOUR CURRENT RESULT IS {result}\n ")
        print("THESE ARE THE OPERATIONS\n")
        for i in operations:
            print(i)
        new_op=input("ENTER YOUR OPERATION HERE\n")
        num3=int(input("ENTER THE NUMBER YOU WANT TO DO THIS OPERATION WITH\n"))
        calcuate=operations[new_op]
        result2=calcuate(result,num3)    
        print(f"{result} {new_op} {num3} = {result2}")
    elif continue_use=='n':
        clear()
        print("\nNEW CALCULATOR...")
        calculation1()
    elif continue_use=='e':
        print("\nTHANK YOU FOR USING OUR CALCULATOR HAVE A GOOD DAY\n")    
        switch=False
    else:
        print("PLEASE ENTER A VALID LETTER\n")    