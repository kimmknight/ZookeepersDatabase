# Step 5

## Introduction

Now that we have our menu working, it's time to create a variable that will store the list of zoo animals while the application is running.

To do this, we will create a *list* variable with some animals added to it as a starting point.

## Objective(s)

- Create a list variable containing the names of some animals

## Background Information

### Lists

In Python, a standard variable can store one thing. For example:

```
username = "amy.smith"
```

or

```
total = 5
```

If we need to store multiple pieces of information, we *could* create more than one variable. For example:

```
user1 = "amy.smith"
user2 = "james.boo"
```

This approach is impractical and hard to manage as the number of items increases.

To handle multiple pieces of data more efficiently, Python offers lists. Lists are ordered collections of items.

Lists are created like any other variable except each item in the collection must be separated by a comma, and the collection must be surrounded with square brackets. For example:

```
users = ["amy.smith", "james.boo"]
```

Lists are mutable, meaning that after the list is created, you can modify, add, or remove items.

To add items to a list, you can use the `append()` method to add an item to the end of the list:

```
users.append("frank.doe")
```

The `users` list would now look like this: `["amy.smith", "james.boo", "frank.doe"]`

To remove items from a list, you can use the `remove()` method to delete a specific item:

```
users.remove("amy.smith")
```

The `users` list would now look like this: `["james.boo", "frank.doe"]`

You can sort a list using the `sort()` method, which arranges the items in ascending order by default:

```
letters = ['C', 'A', 'D', 'B', 'F', 'E', 'G']
letters.sort()
```

After doing this, `letters` would look like this: `['A', 'B', 'C', 'D', 'E', 'F', 'G']`

## Steps

1. Edit your zoo-manager.py file.
2. Above all the other code, create a list called `animals` with the names of three (or more) types of animals added. For example: "Tiger", "Dolphin", "Monkey".
3. After the list is created, sort it using the `.sort()` function.
4. Save your program.

## More Information

- [W3Schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)

