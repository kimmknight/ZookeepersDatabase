# Step 10

## Introduction

Now that we've implemented the functionality to add a new animal to the list, let's add the ability to delete an animal from the list. When the user presses 3 at the main menu, we will display the animal list, prompt the user to enter the number of the animal they want to delete, and then remove that animal from the list.

## Objective(s)

- Display the animal list when the user presses 3 at the main menu.
- Prompt the user to enter the number of the animal they want to delete.
- Remove the selected animal from the list.

## Background Information

### Deleting Items from a List

In Python, you can remove an item from a list using the `del` statement. Here's how you can do it:

```
fruits = ["Apple", "Banana", "Orange"]
fruit_to_delete = 1  # Index of the item to delete (0-based index)
del fruits[fruit_to_delete]
```

In this example:
- `fruits` is an existing list containing `"Apple"`, `"Banana"`, and `"Orange"`.
- `fruit_to_delete` is the index of the item to delete, which is `1` (corresponding to `"Banana"`).
- `del fruits[fruit_to_delete]` removes the item at index `1` from the `fruits` list.

Which fruit do you think will be deleted? Apple? Banana? Orange?

While you might have assumed Apple, the correct answer is **Banana**.

This is because Python lists are zero-indexed, meaning the first item in the list has an index of 0, the second item has an index of 1, and so on. In the example above:
- `"Apple"` is at index 0.
- `"Banana"` is at index 1.
- `"Orange"` is at index 2.

## Steps

1. Edit your `zoo-manager.py` file.
2. Locate the section where the main menu is displayed to the user.
3. Make it so that when the user enters `3` at the menu, instead of printing `You entered 3`, it does the following:
    1. Call the function you created earlier that displays the animal list.
    2. Prompt the user to enter the number of the animal they want to delete.
    3. Convert the user's input from a string to an integer using int().
    4. Use the `del` statement to remove the selected animal from the animal list. Remember to adjust for the 0-based index by subtracting 1 from the user's input.
4. Save and run your program. When you press 3 at the menu, are you able to see the animal list, enter the number of the animal to delete, and see the updated list _without_ the deleted animal?

## More Information

- [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [W3Schools: Python List del Statement](https://www.w3schools.com/python/gloss_python_del.asp)
