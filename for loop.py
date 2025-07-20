"""
sum = 0
a = int(input("enter a number:"))
for i in range(a):
    b = int(input())
    sum = sum+b
print("the sum is:",sum)
avg = sum/a
print("the average is :",avg)
    """
sum =0
a = []
n = int(input("Enetr n value:"))
print("Enter n natural numbers:" )
for i in range(n):
    b = int(input())
    a.append(b)
    sum = sum+b
print("the sum is:",sum)
avg = sum/n
print("the average is:",avg)

