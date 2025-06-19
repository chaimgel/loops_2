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

