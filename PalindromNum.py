def main():
    sum = ""

    num = input("Enter a number :")
    for i in num:
        sum =i + sum

    if num == sum:
        print(f" {num} Number is palindrom number...")

    else:
        print(f" {num} Number is NOT  palindrom number...")

if __name__ =="__main__":
    main()