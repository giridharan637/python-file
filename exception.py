try:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a/b
except Exception as e:
    print("somthing",e)
else:
    print("Your code is correct")
finally:
    print("program is complete")
