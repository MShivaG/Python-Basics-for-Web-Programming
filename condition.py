#condition statements can be used to check and perform certain operations
a = int(input("Enter a number:"))
if a > 0:
    print(f"{a} is a Positive integer")
elif a < 0: #elif can be used for multiple if branches
    print(f"{a} is a Negative integer")
else: 
    print("Zero")