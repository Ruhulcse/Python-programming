def even(divideby):
   try:
    return  42/divideby
   except ZeroDivisionError:
       print("Invalid")
print(even(2))
print(even(3))
print(even(0))
