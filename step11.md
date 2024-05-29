# Step 11

## Introduction

Now that we've implemented the functionality to delete an animal from the list, let's add the ability for the user to exit the program. When the user presses 4 at the main menu, we will "break" from the loop, which will end the program.

## Objective(s)

- Exit the program when the user presses 4 at the main menu.

## Background Information

### Breaking Out of a Loop

In Python, you can use the `break` statement to exit a loop prematurely. Here's an example:

```
while True:
    user_input = input("Enter 'exit' to end the loop: ")
    if user_input == 'exit':
        break
    print("You entered:", user_input)
```

In this example:
- The `while True` loop runs indefinitely.
- The loop repeatedly prompts the user to enter a value.
- If the user enters `'exit'`, the `break` statement is executed, which exits the loop.
- Otherwise, the program prints the entered value and continues the loop.

## Steps

1. Edit your `zoo-manager.py` file.
2. Locate the section where the main menu is displayed to the user.
3. Make it so that when the user enters "4" at the menu, instead of printing `You entered 4`, it calls `break`.
4. If the user input is "4", use the `break` statement to exit the loop.
5. Save and run your program. When you press 4 at the menu, does the program exit?

## More Information

- [W3Schools: Python while Loops](https://www.w3schools.com/python/python_while_loops.asp)
- [W3Schools: Python break Statement](https://www.w3schools.com/python/ref_keyword_break.asp)
