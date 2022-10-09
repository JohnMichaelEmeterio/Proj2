

Sum = 0

print("Please Enter Your Score Here: \n")
i = 1
while (i <= 10):
    num = int(input("Quiz %d = " % i))
    Sum = Sum + num
    i = i + 1

avg = Sum / 10

print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)
