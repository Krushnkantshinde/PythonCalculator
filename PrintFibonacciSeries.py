def main():

    a = 0
    b = 1

    # for i in range(11):
    #     print(a)
    #     a,b = b , a+b

    i = 1
    while(i >= 10):
        print(a)
        a,b = a,a+b
        i +=1 



if __name__ =="__main__":
    main()