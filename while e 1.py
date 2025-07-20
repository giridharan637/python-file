"""
i = 10
while(i<=200):
    print(i, end =" ,")
    i = i+10
   
i = 10
while(i>=1):
    print(i)
    i = i-1

n = int(input("Enetr n :"))
i = n
fact = 1
while(i>=1):
    fact = fact*i
    i = i-1
print(n,"fact value is:",fact)
"""
n = int(input("Enter n:"))
fact = 1
for i in range(1,n+1):
        fact = fact*i
print(fact)

