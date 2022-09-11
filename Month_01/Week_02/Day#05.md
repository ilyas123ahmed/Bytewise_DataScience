# Mini Projects in Python

## Quiz GAME

```python
print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ").lower()

if playing != 'yes':
    quit()

print("Okay! Let's play : )")
score = 0
answer = input("What does CPU stands for? ").lower()
if answer == 'central processing unit':
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

answer=input("What does GPU stands for? ").lower()
if answer=='graphic processing unit':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')


answer=input("What does GUI stands for? ").lower()
if answer=='graphical user interface':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')


answer=input("What does RAM stands for? ").lower()
if answer=='random access memory':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')


answer=input("What does AI stands for? ").lower()
if answer=='artificial intelligence':
    print('Correct!')
    score += 10
else:
    print('Incorrect!')

print("You got "+str(score) + " question correct!")
print("You got "+str((score/5)*100) + "%")
```


## Guessing Number GAME

```python
import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0:
        print('Please type a number larger then zero!')
        quit()
else:
    print('Type a number next time!')
    quit()
    
random_number = random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess = input('Make a guess ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type a number next time!')
        continue
    if user_guess==random_number:
        print("You got it correctly")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in "+str(guesses)+' Guesses')
```


## Rock, Paper, Scissor GAME

```python
import random
user_wins = 0
computer_wins = 0
options = ['rock','paper','scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    #0:rock,1:paper,2:scissors
    computer_pick = options[random_number]
    print('computer picked',computer_pick+".")
    if user_input == "rock" and (computer_pick =='scissors' or computer_pick =='paper'):
        print("you won")
        user_wins += 1
        continue
    elif user_input == "paper" and (computer_pick == 'rock' or computer_pick =='scissors'):
        print("you won")
        user_wins += 1
        continue
    elif user_input == "scissors" and (computer_pick == 'paper' or computer_pick =='rock'):
        print("you won")
        user_wins += 1
        continue
    else:
        print("you lost")
        computer_wins += 1
print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Have a wounderful day")
```


## Choose Your Own Adventure 

```python
name = input("Type your name: ")
print("welcome",name,"to this adventure")

answer = input('you are on a direct road, it has come to end and you can go left or right.'
               ' Which way would you like to go? ').lower()
if answer == 'left':
    answer=input("you come to a river, you can walk around it or swim across?"
                 " Type walk to walk around and swim to swim across:  ").lower()
    if answer == "swim":
        print('you swam across & were eaten by an alligator')
    elif answer == "walk":
        print('you want many miles,ran out of water and you lost the game')
    else:
        print("Not a Valid option. You lose")


elif answer == 'right':
    answer = input("you come to a bridge, it looks wobbly,do you want to cross it"
                   " or head back (cross/back) ?").lower()
    if answer == "back":
        print('you go back & lose')
    elif answer == "cross":
       answer=input('You cross the bridge and met a stranger. Do you talk to them (Yes/No) ').lower()
       if answer=='yes':
           print('you talk to stranger and they give you gold. you Win!')
       elif answer=='no':
           print('you ignore the stranger and you lose!')
       else:
           print("Not a Valid option. You lose")
    else:
        print("Not a Valid option. You lose")
else:
    print("Not a Valid option. You lose")


print("Thank You for trying",name)
```


## Password Mangment

```python
from cryptography.fernet import  Fernet
# def write_key():
#     key=Fernet.generate_key()
#     with open('key.key','wb')as key_file:
#         key_file.write(key)
def load_key():
    file=open('key.key','rb')
    key=file.read()
    file.close()
    return key
master_pwd=input("what is the master password? ")
key=load_key() + master_pwd.encode()
fer=Fernet(key)
def view():
    with open('password.txt','r') as f:
         for line in f.readlines():
             data=line.rstrip()
             user, passw = data.split("|")
             print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())
def add():
    name=input('Account name: ')
    pwd=input('password: ')
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
while True:
 mode=input("would you like to add a new password or view existing one(view,add) or press q for quit? ").lower()
 if mode=='q':
     break
 if mode == 'view':
    view()
 elif mode == 'add':
    add()
 else:
    print('Invaid Mode')
    continue
```
