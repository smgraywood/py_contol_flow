# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Please enter a letter from the alphabet (a-z or A-Z):').lower()
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while True:
    input_length = len(input('Please enter a word or phrase:'))
    print(f'What you entered is {input_length} characters long')
    if input() == 'quit':
        break
    else:
        continue

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

dog_age = int(input("Input a dog's age:"))
if dog_age < 3:
    puppy_age = dog_age * 10
    print(f"The dog's age in dog years is {puppy_age}")
elif dog_age >= 3:
    adult_age = 20 + ((dog_age - 2) * 7)
    print(f"The dog's age in dog years is {adult_age}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


a = input("Enter the length of side a: ")
b = input("Enter the length of side b: ")
c = input("Enter the length of side c: ")

if a == b == c:
    triangle_type = "equilateral"
elif a != b != c != a:
    triangle_type = "scalene"
else:
    triangle_type = "isosceles"

print(f'A triangle with sides of {a}, {b}, and {c} is a {triangle_type} triangle.')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

num_terms = 50

term_1 = 0
term_2 = 1

print(f'term: 0 / number: {term_1}')
print(f'term: 1 / number: {term_2}')

for i in range(2, num_terms):
    next = term_1 + term_2
    print(f'term: {i} / number: {next}')
    term_1, term_2 = term_2, next




# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

input_month = input('Enter the month of the year (Jan - Dec):')
input_day = input('Enter the day of the month:')

if input_month in ('Dec', 'Jan', 'Feb') or (input_month == 'Mar' and input_day <= 19):
    season = 'Winter'
elif (input_month == 'Mar' and input_day >= 20) or (input_month in ('Apr', 'May', 'Jun')):
    season = 'Spring'
elif (input_month == 'Jun' and input_day >= 21) or (input_month in ('Jul', 'Aug', 'Sep')):
    season = 'Summer'
elif (input_month == 'Sep' and input_day >= 22) or (input_month in ('Oct', 'Nov', 'Dec')):
    season = 'Fall'
else:
    season = 'Unknown'

print(f"{input_month} {input_day} is in {season}.")
