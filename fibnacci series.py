def fibonacci(n):
    a, b = 0, 1 
    for i in range(n):
        a, b = b, a + b 
    return a  
n=8
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")



a = "j a j"
if a == a[::-1]:
        print ("true")
else:
        print ("false")