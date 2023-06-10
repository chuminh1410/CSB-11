def print_fibo(n):
    fibo_list = [1, 1]  
    for i in range(2, n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2]) 
    print("First", n, "Fibonacci numbers:", " ".join(str(num) for num in fibo_list))

n = int(input("Input a number: "))
print_fibo(n)
