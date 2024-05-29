# Step 9

## Introduction

Now that we've implemented the functionality to display the fruit list when the user presses 1 at the main menu, let's enhance our program further. In this step, we will enable the user to add a new fruit to the list by pressing 2 at the main menu.

## Objective(s)

- Prompt the user to enter the name of the new fruit.
- Add the new fruit to the fruit list.
- Sort the fruit list.

## Background Information

### Adding Items to a List

In Python, you can add a new item to an existing list using the `append()` method. Here's how you can do it:

```python
fruits = ["Apple", "Banana", "Orange"]
new_fruit = input("Enter the name of the new fruit: ")
fruits.append(new_fruit)
```

In this example:
- `fruits` is an existing list containing `"Apple"`, `"Banana"`, and `"Orange"`.
- `new_fruit` is a variable storing the name of the new fruit entered by the user.
- `fruits.append(new_fruit)` adds the new fruit to the end of the `fruits` list.

## Steps

1. Edit your `zoo-manager.py` file.
2. Locate the section where the main menu is displayed to the user.
3. Make it so that when the user enters "2" at the menu, instead of printing `You entered 2`, it does the following:
    1. Prompts the user to enter the name of the new animal using the `input()` function.
    2. Add the new animal to the animal list using the `append()` method.
    3. Sort the animal list using the `sort()` method.
8. Save and run your program. When you press 2 at the menu, are you prompted to enter the name of a new animal? Is the new animal added to the list and is the list sorted afterwards?

## More Information

- [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools: Python List append() Method](https://www.w3schools.com/python/ref_list_append.asp)
- [W3Schools: Python List sort() Method](https://www.w3schools.com/python/ref_list_sort.asp)
