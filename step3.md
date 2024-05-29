# Step 3

## Introduction

So far we have displayed a menu to the user and asked them to enter a selection.

Next, we will add the code that checks which number they have entered.

For now, if the user enters "1", we will just print "You entered 1" on the screen and take no further action. Same for "2", "3", and "4".

Later on, we will make our application do something more useful when the user makes a choice.

## Objective(s)

- Create conditionals (if/elif) to check whether the user typed 1, 2, 3, or 4

## Background Information

### if / elif / else

In Python, the `if`, `elif` (short for "else if"), and `else` statements are used for conditional execution. They allow you to control the flow of your program based on certain conditions.

Let's look at a simple example to start:

```
age = 40

if age > 35:
 print("Wow you are old!")
```

This is good for checking whether a single condition is true and then taking an action if so.

Sometimes we need a more complex set of checks. For example:

```
fruit = "Mango"

if fruit == "Apple":
 print("The fruit is an apple. OK.")

elif fruit == "Watermelon":
 print("The fruit is a watermelon. Yum.")

elif fruit == "Mango":
 print("The fruit is a mango. Meh.")

else:
 print("The fruit is not an apple, watermelon, or mango. Boo.")
```

In this example, the program evaluates the conditions in order. If `fruit` is equal to `"Apple"`, the first block is executed. Otherwise, if `fruit` is equal to `"Watermelon"`, the second block is executed. Otherwise, if `fruit` is equal to `"Mango"`, the third block is executed. If none of the previous conditions were true, the *else* block is executed.

**Note:** A block of *if* statements:

- Must have **one** `if` statement to begin
- Can optionally have as many `elif` statements as you need (or none)
- Can optionally have **one** `else` statement at the end

## Steps

1. Edit your *zoo-manager.py* file.
2. At the end of your code, add an `if` statement to check if the user entered "1". If so, then print `You entered 1` on the screen.
3. Add an `elif` statement to check if the user entered "2". If so, then print `You entered 2` on the screen.
4. Add an `elif` statement to check if the user entered "3". If so, then print `You entered 3` on the screen.
5. Add an `elif` statement to check if the user entered "4". If so, then print `You entered 4` on the screen.
6. Save and run your program. If you enter 1, 2, 3, or 4, does it respond correctly?

## More Information

- [W3Schools: Python Conditions](https://www.w3schools.com/python/python_conditions.asp)

