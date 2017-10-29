while True:
    print("who are you??",end=' ')
    print("Enter your name")
    name=input()
    if name!='ruhul':
        print("sorry your name is incorrect")
        continue
    print("Hi ruhul enter your password",end=' ')
    password=input()
    if password!=123:
        continue
    print("Access granted.")
