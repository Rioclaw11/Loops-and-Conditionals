secret = 5
guess = 9
if secret == guess:
    print("You got it right")
elif secret < guess:
    print("Too high")
elif secret > guess:
    print("Too low")

small = True
green = False
if small:
    if green:
        print("This is a pea")
    else:
        print("This is a cherry")
else:
    if green:
        print("This is a watermelon")
    else:
        print("This is a pumpkin")

for x in range(3, -1, -1):
    print(x)
3
2
1
0
guess_me = 7
number = 1
while guess_me > number:
    if guess_me > number:
        print("It's too low.")
    elif guess_me == number:
        print("Thats right!")
        break
    elif guess_me < number:
        print("It's too high.")
    number += 1
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break