

print("Grade Computation")

Name = input("Enter Your Name :")
Pre = int(input("What is your Pre-lim :"))
Mid = int(input("What is your Mid-term :"))
Fin = int(input("What is your Final :"))


add = Pre+Mid+Fin
avg = add/3

if avg >= 90 and avg <= 100:
    print("Your Grade is A")
elif avg >= 80 and avg < 90:
    print("Your Grade is A-")
elif avg >= 75 and avg < 80:
    print("Your Grade is B+")
elif avg < 74:
    print("You Faild")
else:
    print("Invalid Input!")

print("Your Average Grade is: ", avg)
