# exercise 1
for i in range(1,1001):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
    elif i%3==0:
        print("Fuzz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# exercise 2
num = int(input("please enter a number: "))
for i in range(num-1):
    print("*" * (i+1))
for i in range(num):
    print("*"*(num-i))

# exercise 3
num = int(input("please enter a number: "))
ans = set({})
for i in range(2,num):
    if num%i==0:
        ans.add(True)
    else:
        ans.add(False)
if True in ans:
    print("is not a prime number")
else:
    print("is prime number")

# exercise 4
num = int(input("please enter a number: "))
for i in range(num):
    print(" "*(num-i),(str(i + 1)+" ") *i ,str(i+1),sep="")

# exercise 5
num = int(input("please enter a number: "))
reversed_num=int(str(num)[::-1])
if reversed_num==num:
    print("it's pelindrom")
else:
    print("it's not pelindrom")

# exercise 6
pass

# exercise 7


#6


#7
users = {}
a = "bla bla"
while True:
    step1 = input("please choice: \n1. enter the system\n2. create user\n3.exit the system\nto return to the main menu press *\n")
    if step1 == "1":
        user_name = input("enter User Name: ")
        if user_name in users.keys():
            attempt = 0
            while attempt <3:
                password = input("Enter password: ")
                attempt+=1
                if password==users[user_name]:
                    step2 = input(f"hi {users[user_name]} what you want?\n1.print the string\n2.change password\n3.delete user\n4.back to main menu\n5.exit system\n")
                    if step2 =="1":
                        print(a)
                    elif step2=="2":
                        choice_pass = input("enter your password: ")
                        users[user_name]=choice_pass
                        break
                    elif step2 == "3":
                        users.pop(user_name)
                    elif step2=="4":
                        break
                    elif step2 == "5":
                        exit()
                    break
        elif user_name=="*":
            continue
        else:
            print("user not found")
    elif step1 == "2" and len(users) < 3:
        create_user = input("enter your ID: ")
        choice_pass = input("enter your password: ")
        users[create_user]=choice_pass
    elif step1 == "2" and len(users) == 3:
        print("Cannot register another user")
    elif step1 == "3":
        break
    elif step1 == "*":
        continue
    else:
        print("invalid choice")
