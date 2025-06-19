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