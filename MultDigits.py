def MultDigits(number,steps):
    digitProduct = 1
    numArray = [int(x) for x in str(number)]
    if len(numArray) == 1:
        return steps
    for i in range(len(numArray)):
        digitProduct *= numArray[i]
    steps += 1
    return MultDigits(digitProduct, steps)

num = 1
bestSteps = 0
while True:
    steps = MultDigits(num,0)
    if steps > bestSteps:
        bestSteps = steps
        print("New best! | Number: "+str(num)+" | Steps: "+str(steps))
    num += 1
