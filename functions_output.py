print("Hello World\n")
print("hi")
def names_function(fname,lname):
    first=fname.title()
    last=lname.title()
    return  f"Welcome {first} {last}"
name1=input("Enter the first name \n")
name2=input("Enter the last name\n")
result= names_function(name1, name2)
print(result)