# Step 1

## Introduction

The first thing we will get our application to do is simply display some text to the user.

The text we want to display is:

```
Zookeeper's Database
**********************

1:  Print Animals List
2:  Add Animal
3:  Delete Animal
4:  Exit

**********************
```

At this stage, our program won't do anything else. It will just show the text and then exit.

## Objective(s)

- Display some text (a menu) to the user using the `print()` statement

## Background Information

### print()

In Python, we can use the `print()` statement to display text on the screen. Whatever we put in between the brackets will be printed on the screen.

For example:

```
print("Hello World")
```

The output of this would be:

```
Hello World
```

Notice how the text is enclosed in double quotes? This is because it is a *string*. A *string* is a piece of text.

If we want to print a blank line, we can simply write `print()`.

In our case, we want to display a menu (shown above) that is multiple lines of text. How do we display multiple lines? We could use multiple print statements:

```
print("This is line 1. The next line will be blank.")
print()
print("This is line 3.")
```

Or instead, we could use a single `print()` statement with a *multi-line string*. A multi-line string starts with three double-quote marks and ends with three double-quote marks. For example:

```
print("""
This is line 1. The next line will be blank.")

This is line 3.
""")
```

Using either approach is valid.

## Steps

1. Create a new Python file for your project. Give it the name: *zoo-manager.py*
2. Add one or more print statements so that your program displays the text provided above.
3. Save and run your program. Does it display the menu as expected?

## More Information

- [W3Schools: Python print() Function](https://www.w3schools.com/python/ref_func_print.asp)

