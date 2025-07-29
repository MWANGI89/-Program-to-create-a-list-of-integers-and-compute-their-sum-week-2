# Program to create a list of integers and compute their sum

# Accept user input
numbers = input("Enter a list of integers separated by spaces: ")
# Convert input string to a list of integers
int_list = [int(num) for num in numbers.split()]

# Compute the sum
total_sum = sum(int_list)

# Display the result
print(f"The sum of the integers is: {total_sum}")

# Tuple containing names of favorite books
favorite_books = (
    "1984",
    "To Kill a Mockingbird",
    "The Great Gatsby",
    "Moby Dick"
)

# Print each book name on a separate line
for book in favorite_books:
    print(book)

# Program to store information about a person in a dictionary

# Create an empty dictionary
person_info = {}

# Accept user input
person_info['name'] = input("Enter your name: ")
person_info['age'] = input("Enter your age: ")
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary
print("Person Information:")
print(person_info)

# Program to create two sets of integers and find common elements

# Accept user input for the first set
set1_input = input("Enter the first set of integers separated by spaces: ")
set1 = {int(num) for num in set1_input.split()}

# Accept user input for the second set
set2_input = input("Enter the second set of integers separated by spaces: ")
set2 = {int(num) for num in set2_input.split()}

# Create a new set with common elements
common_elements = set1.intersection(set2)

# Display the result
print("Common elements:", common_elements)

# Program to filter words with an odd number of characters

# List of words
words = ["apple", "Orange", "cherry", "fig", "grape"]

# List comprehension to create a new list with words
# that have an odd number of characters
odd_length_words = [
    word for word in words if len(word) % 2 != 0
]

# Display the result
print("Words with an odd number of characters:", odd_length_words)
