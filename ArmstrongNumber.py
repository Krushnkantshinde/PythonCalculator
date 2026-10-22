def main():
    num1 =(input("enter a number :"))
    num2 = 0

    for i in num1:
        num2 = num2 + (int(i) ** 3)

    if num1 == num2:
        print(f" {num1} is Armsrong number..")
    else:
        print("NOT Armstrong number...")


if __name__=="__main__":
    main()