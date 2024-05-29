# Step 6

## Introduction

Now that we have a list of animals to work with, we need to be able to display them on screen.

To do this, we can simply use `print(animals)`.

It won't look very nice to the user, but we will fix this later.

We will need to display the list of animals on two separate occasions within our program:

1. When the user presses 1 to *Print Animals List*.
2. When the user presses 3 to *Delete Animal* (to show them a list before they delete one).

When coding we should try to avoid repeating code.

With this in mind, instead of writing the same code in two different places to display the animal list, we will put the code inside a *function*, and *call* that function if the user presses 1 or 3.

## Objective(s)

- Create a function
- Call the function

## Background Information

### Functions

To create a simple function in Python, you use the following syntax:

```
def function_name():
 # Insert code here
```

For example:

```
def greet():
 print("Hello, world!")
```

You can then call this function from anywhere in your program like so:

```
greet()
```

## Steps

1. Edit your zoo-manager.py file.
2. Above all other code, create a function called *display_animals()*.
3. Inside the function add a `print` statement that prints the `animals` list variable.
4. Make it so that when the user enters "1" at the menu, instead of printing `You entered 1`, the `display_animals()` function is called.
5. Save and run your program. If you enter `1` at the menu, do you see your animal list?

## More Information

- [W3Schools: Python Functions](https://www.w3schools.com/python/python_functions.asp)
