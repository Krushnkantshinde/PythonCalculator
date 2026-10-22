def main():

    num = int(input("Enter a number :"))
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} : number not prime number...")
            break

        else:
            print(f"{num} : number is prime number...")
            break

if __name__ =="__main__":
    main()