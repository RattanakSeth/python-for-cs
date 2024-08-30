"""
02.1 Math Class
Write a python program to create your Math class with the following return functions: 
▪ factorial (one parameter of a number) 
▪ rectangleSurface (two parameters Width and Height) 
▪ circleSurface (one parameter of radius) 
▪ sum (*)
▪ multiply (*) ▪ max (*) ▪ min (*)
“*” means unlimited parameters.
"""

class Math:
    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact

    def rectangleSurface(width, height):
        return width + " x " + height
    
    def circleSurface(radius: float):
        return radius
    
    def sum(*arg):
        n: int = 0
        for val in arg:
            n = n + val
        return n

    def multiply(*arg):
        n: int = 0
        for val in arg:
            n = n * val
        return n

    def max(*arg):
        return max(arg)
    
    def min(*arg):
        return min(arg)


print(Math.sum(10, 11, 11, 11))
print(Math.max(2,3,4,5))
print(Math.min(4,5,6,7,8,9))
print(Math.factorial(8))