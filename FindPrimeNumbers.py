def main():

    list1 = []

    num = int(input("Enter a number :"))

    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                # print(f"{j} : number not prime number...")
                break

        else:
            print(f"{i} : number is prime number...")

            list1.append(i)
                # break

    print("Prime numbers are:",list1)
if __name__ =="__main__":
    main()

    