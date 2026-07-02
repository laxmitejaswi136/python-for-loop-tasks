# ==========================================
# Python For Loop Assignment
# Author: Tejaswi Singu
# ==========================================

# Task 1: Calculate the sum of all numbers in a list

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]

print("Task 1: Sum of Numbers")
print("Numbers:", numbers)
print("Sum =", calculate_sum(numbers))


# Task 2: Print each character of a string

print("\nTask 2: Print Each Character")

text = "Python"

for ch in text:
    print(ch)


# Task 3: Print only even numbers from a list

print("\nTask 3: Even Numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        print(num)


# Task 4: Print the length of each word

print("\nTask 4: Length of Each Word")

def print_word_lengths(words):
    for word in words:
        print(word, "=", len(word))

words = ["Python", "Java", "HTML", "Programming"]

print_word_lengths(words)


# Task 5: Calculate the average of numbers in a list

print("\nTask 5: Average of Numbers")

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average =", average)

print("\nAssignment Completed Successfully!")