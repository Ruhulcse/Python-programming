number=[]
for i in range(0,100):
    number.append(i)
even_number=[]
for i in number:
    if i%2==0:
        even_number.append(i)
print(even_number,end=' ')
