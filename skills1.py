# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd_list = []
    for num in some_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for num in some_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) >= 4:
            new_list.append(word)
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    some_list.sort()
    return some_list[0]

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    some_list.sort()
    return some_list[-1]

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for num in some_list:
        half_num = num / 2
        new_list.append(half_num)
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list:
        length = len(word)
        new_list.append(length)
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    num_sum = 0
    for num in numbers:
        num_sum += num
    return num_sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    multiple = 1
    for num in numbers:
        multiple = multiple * num
    return multiple

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    all_strings = ""
    for string in string_list:
        all_strings += string + " "
    return all_strings

# Write a function that takes a list of integers and returns the average number(without using the avg method)
def average(numbers):
    total_number_of_numbers = len(numbers)
    sum_of_numbers = sum_numbers(numbers) # call on sum_numbers() function
    average_of_numbers = float(sum_of_numbers)/total_number_of_numbers
    return average_of_numbers


# function calls with test lists
some_list = [4, 9, 10, 13, 50, 5, 14, 73]
word_list = ['I', 'have', 'a', 'dog', 'named', 'Jersey.']

print all_odd(some_list)

print all_even(some_list)

print long_words(word_list)

print smallest(some_list)

print largest(some_list)

print halvesies(some_list)

print word_lengths(word_list)

print sum_numbers(some_list)

print mult_numbers(some_list)

print join_strings(word_list)

print average(some_list)
