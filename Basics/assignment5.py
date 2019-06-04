userUpperLimit = int(input("Enter a number: "))
upperLimit = 100
counter = 0
while (counter <= userUpperLimit):
    if (counter % 10 == 0):
        counter += 1
        continue
    if (counter >= upperLimit):
        print("Reached max upper limit of 100, stopping")
        break
    print(counter)
    counter += 1
