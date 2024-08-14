# Python Fibonacci sequence

"""
Fibonacci sequence ek mathematical sequence hai jo ek specific tareeqay se numbers ko
generate karta hai. Is sequence mein har number apnay do peechay walay numbers ka sum hota hai.
"""


a = 8
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result
print("The result of Fibonacci:", fibonacci(8))
print("The range of Fibonacci: ", range(a))
print("In details we can see how 'Fibonacci' works (Using Loop)")
for i in range(a):  # add 1 numberrange(a+1), if we want to check the full result jo akhri may 21 dikha raha hai
        print(fibonacci(i))  # () brackets function k liay astamaal hote hai aur list k liay []




# here is how it works
"""
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
fibonacci(6) = fibonacci(5) + fibonacci(4) = 5 + 3 = 8
fibonacci(7) = fibonacci(6) + fibonacci(5) = 8 + 5 = 13
fibonacci(8) = fibonacci(7) + fibonacci(6) = 13 + 8 = 21
fibonacci(9) = fibonacci(8) + fibonacci(7) = 21 + 13 = 34
"""