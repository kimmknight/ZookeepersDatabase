# Step 7

## Introduction

So now we have a function that displays our animal list on the screen like so:

```
['Aligator', 'Crocodile', 'Emu']
```

This is functional, however, it doesn't look very nice to the user.

It would be ideal if each animal was displayed on its own line, with a number next to it. For example:

```
1. Aligator
2. Crocodile
3. Emu
```

We can achieve this using a ***for loop***.

*For* loops allow us to run code a certain number of times. In our case, we will *loop* through each animal in the list: The code inside the loop will run _once_ for each animal.

## Objective(s)

- Create a for loop to display the animal list numbered, line-by-line

## Background Information

In Python, a for loop allows you to *iterate* over a list and perform an action for each item. Here is the basic syntax:

```
for item in list_name:
 # Perform action with item
```

For example:

```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
 print(fruit)
```

In this example:

- `fruits` is the list we are iterating over.

- `fruit` is the loop variable. It takes on the value of each item in the list, one at a time. So, in the first *iteration* (the first time the loop runs), fruit will be "apple", in the second iteration, fruit will be "banana", and in the third iteration, fruit will be "cherry".

You can use any name for the loop variable, but it's good practice to use a name that makes sense in the context of the items in the list.

### Adding a Number

In this step, you will add a number to the start of each animal listed on the screen. The number will start at `1` and go up by one for the next animal (the next loop *iteration*). We can do this by creating a variable, setting it to `1`, and adding one to it each time the loop runs. Here is an example:

```
fruits = ["apple", "banana", "cherry"]
index = 1

for fruit in fruits:
 print(index, fruit)
 index += 1
```

## Steps

1. Edit your zoo-manager.py file.
2. Find the print_all_animals() function.
3. Inside the function:
    1. Delete the existing print statement
    2. Create a variable (`index` for example) to keep track of the animal number, starting from 1.
    3. Create a *for* loop that iterates through each animal in the list.
    4. Inside the *for* loop, print both the number variable and the current animal.
4. Save and run your program. When you enter 1 at the menu, do you see your formatted animal list?

## More Information

- [W3Schools: Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
