#Functions goes here
def multiplication(num):

    for i in range(1,26):
        #tables.append(i*num)
        print(num, "*",i,"=",num*i)
    
    
def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        smallerAns = factorial(num - 1)
        Ans = num * smallerAns
        return Ans  
     
#driver code    
num = int(input("Enter the Value: "))
print(multiplication(num))
print(factorial(num))