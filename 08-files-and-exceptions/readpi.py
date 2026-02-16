from pathlib import Path

path = Path('pi_million_digits.txt')
lines = path.read_text().splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

#print(f'{pi_string[:100]}')
#print(len(pi_string))

date = input("Enter your birthday (mmddyy): ")

if date in pi_string:
    print("Your birthday is in the 1st million digits of pi")
else:
    print("Your birthday is not there")