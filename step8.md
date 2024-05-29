# Step 8

## Introduction

Now that we've improved our `print_all_animals` function to display the animal list in a more user-friendly format, let's take it a step further. It would be helpful for the user to know the total number of animals in the list after displaying them.

## Objective(s)

- Display the total number of animals at the end of the animal list.

## Background Information

## The len() Function

The len() function in Python returns the _length_ of an object. For lists, _it returns the number of items in the list_. Here is how you can use it:

```
fruits = ["apple", "banana", "cherry"]
number_of_fruits = len(fruits)
print(number_of_fruits)
```

In this example:

- `fruits` is a list with three items: "apple", "banana", and "cherry".
- `len(fruits)` returns the number of items in the `fruits` list, which is 3.

### String Joining

You can join (concatenate) strings and variables using the + operator. For example:

```
fruits = ["apple", "banana", "cherry"]
number_of_fruits = len(fruits)
print("Number of fruits: " + str(number_of_fruits))
```

In this example:

- `fruits` is a list with three items: "apple", "banana", and "cherry".
- `len(fruits)` returns the number of items in the fruits list, which is 3.
- We then use string concatenation to join the string "Number of fruits: " with the `number_of_fruits`.

Python requires that all parts being joined with a `+` are strings, but `number_of_fruits` is a number, not a string. To make it work, we use `str(number_of_fruits)` which ensures `number_of_fruits` is treated as a string.

Without `str()`, trying to join a string with a non-string (like an integer) would result in an error.

## Steps

1. Edit your `zoo-manager.py` file.
2. Modify the `print_all_animals()` function.
3. After the `for` loop that prints each animal, use the `len()` function to get the total number of animals in the `animals` list.
4. Use a print statement to display the total number of animals.
5. Save and run your program. When you enter 1 at the menu, do you see your formatted animal list followed by the total number of animals?

## More Information

- [W3Schools: Python String Concatenation](https://www.w3schools.com/python/python_string_concatenation.asp)
