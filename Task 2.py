n=int(input("Enter the number to check Prime or not : \t"))
def check_prime(n):
    if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               print(n,"is not a Prime number\n",i,"*",n//i,"=",n)
               break
       else:
           print(n,"is a Prime number")

    else:
       print(n,"is not a Prime number")
check_prime(n)
