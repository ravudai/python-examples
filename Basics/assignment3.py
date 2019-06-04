# find prime number
inNumber = int(input(
    "Enter a number to list all prime numbers below this number: "))

primeFlag = False

for num in range(2, inNumber):
    if (inNumber % num) == 0:
        primeFlag = True
        numberDivided = num

if (primeFlag):
    print("Entered number is prime ", numberDivided)
else:
    print("Entered number is not prime")
