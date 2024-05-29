# Step 13

## Introduction

Now that we have imported the `json` library, we can use it to load our animal list from a file. This step will replace the manually created animal list with one that is loaded from an `animals.json` file.

## Objective(s)

- Load the animal list from a `json` file.

## Background Information

### Reading JSON Files

To read data from a JSON file in Python, you can use the `json.load()` function. This function reads the file and parses the JSON data into a Python object (like a list or dictionary).

Here's an example:

```
import json

data_file = open('data.json', 'r')
data = json.load(data_file)
data_file.close()
print(data)
```

In this example:
- The `open` function is used to open the file `data.json` in read mode (`'r'`).
- `json.load(data_file)` reads the JSON data from the file and converts it into a Python object.
- The `data` variable now contains the data from `data.json`.
- Finally, we close the file using `data_file.close()`.

## Steps

1. Create an `animals.json` file in the same directory as your `zoo-manager.py` file. This file should contain a JSON array of animal names, like this:

```
["Tiger", "Rhino", "Elephant", "Octopus", "Polar Bear"]
```

2. Edit your `zoo-manager.py` file.
3. Delete the line where you manually create the animal list:

```
animals = ['Tiger', 'Rhino', 'Elephant', 'Octopus', 'Polar Bear']
```

4. Replace it with the appropriate code to load the animal list from `animals.json`.
5. Save your file. When you enter 1 at the menu, do you see the animal list loaded from the `animals.json` file?

By doing this, your program will now load the animal list from the `animals.json` file, making the data persistent.

## More Information

- [W3Schools: Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [W3Schools: Python JSON](https://www.w3schools.com/python/python_json.asp)
