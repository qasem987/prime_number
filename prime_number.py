

counter = 0
for number in range(1,1000):
    for i in range(2,number):
        if number % i == 0:
            break
        i =i+1
    else:
        print(str(number))
        counter =counter +1

print("the number of prime numbers between 1 and 1000 is :" + str(counter))


