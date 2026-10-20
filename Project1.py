def main():
    print("====================PYTHON CALCULATOR=====================")

    Line ="=========================================================="
    print(Line)

    print("=====CHOICECODES=====")
    print("1.Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    print(Line)

    Number1 = int(input("Enter first number:"))
    print(Line)

    choicecode = int(input("Enter a CHOOICECODE  Between (1 - 4)...:"))
    print(Line)

    Number2 = int(input("Enter secod number:"))
    print(Line)

    
    print(Line)

    if choicecode == 1:
        print("Additionn is:",Number1 + Number2)

    elif choicecode == 2:
        print("subtraction is:",Number2 - Number1)

    elif choicecode == 3:
        print("Mltiplication is:",Number1 * Number2)

    elif choicecode == 4:
        print("Division is:",Number2 * Number1)

    else:
        print("Enter correct CHOICECODE...: ")
    

    print("==========THANK YOUUU=========")
    
if __name__ =="__main__":
    main()