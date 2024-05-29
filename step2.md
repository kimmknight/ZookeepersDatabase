# Step 2

## Introduction

So far, we have displayed a menu to the user, but then the program stops.

Next, we will make it so that the user can enter their menu selection.

The goal is that after the menu is shown, the user is asked to make a selection:

```
Zookeeper's Database
**********************

1:  Print Animals List
2:  Add Animal
3:  Delete Animal
4:  Exit

**********************

Please make a selection: |
```

This will wait for the user to type something and then press enter.

In this step, our application won't actually take any action based on what they type. We will deal with that later.

## Objective(s)

- Ask the user to enter some text (a menu item number) using an `input()` statement

## Background Information

### input()

In Python, the `input()` statement is used to receive user input from the keyboard. It allows a program to pause and wait for the user to enter data, which can then be stored in a variable.

For example:

```
person_name = input("Enter your name: ")

print("Your name is: ")
print(person_name)
```

In this example, the input() function displays the message `Enter your name:` and waits for the user to type something. The entered text is then stored in a variable called `person_name` and later used in a `print()` statement.

## Steps

1. Edit your *zoo-manager.py* file.
2. Add an `input()` statement (at the end) so that your program asks the user to make a selection.
3. Save and run your program. Does it ask for the user to type something as expected?

## More Information

- [W3Schools: Python input() Function](https://www.w3schools.com/python/ref_func_input.asp)

