name = input("what is your name? ")
birth_year = input("what is your birth year? ")

print(f"Hello {name}")

from datetime import datetime
current_year = datetime.now().year
age = current_year - int(birth_year)

print(f"you must be {age} years old")

print("Goodbye!")