def fibonacci(num):
    if(num == 0):
        return 0
    elif (num == 1):
        return 1
    elif(num>1):
        ans = fibonacci(num-1)+fibonacci(num-2)
        return ans

num = int(input("Enter a Number: "))
print(fibonacci(num))