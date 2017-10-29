import  sys
while True:
    print("Do you want to terminate the programme?")
    print("if yes, type exit")
    yes=input()
    if yes=='exit':
        sys.exit()
    print('You typed'+yes+'.')
