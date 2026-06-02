from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday mmddyy")
if birthday in pi_string:
    print("Dale a data ta no pi")
else:
    print("Não aparece")