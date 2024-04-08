#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letter_password = ""
symbol_password = ""
number_password = ""

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#letter selection

for character in range(0, nr_letters):
  ran_choice = random.randint(0, len(letters))
  letter_password = letter_password + letters[ran_choice - 1]

#symbol selection

for symbol in range(0, nr_symbols):
  ran_symb = random.randint(0, len(symbols))
  symbol_password = symbol_password + symbols[ran_symb - 1]

#number selection

for number in range(0, nr_numbers):
  ran_numb = random.randint(0, len(numbers))
  number_password = number_password + numbers[ran_numb - 1]

#final password

final_password = letter_password + symbol_password + number_password

shuffled_password = "".join(random.sample(final_password, len(final_password)))

print(f"Your password is {shuffled_password} ")
