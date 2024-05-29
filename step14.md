# Step 14

## Introduction

To ensure the animal list is saved and updated for future use, we need to save it back into the `animals.json` file when the user exits the program. This way, any changes made to the list during the program's run are saved.

In a previous step, we made it so that if the user presses `4` at the main menu, the loop _breaks_ and the program ends. We will need to add some code above the `break` statement that will save our animal list back to the `animals.json` file.

## Objective(s)

- Save (dump) the animal list to a `json` file when the user exits the program.

## Background Information

### Writing JSON Files

To write data to a JSON file in Python, you can use the `json.dump()` function. This will allow us to convert our `animals` list into JSON format and save it to a file.

Here's an example:

```
import json

data = ["apple", "banana", "cherry"]
data_file = open('data.json', 'w')
json.dump(mylist, filename)
data_file.close()
```

In this example:
- The `open` function is used to open the file `data.json` in write mode (`'w'`).
- `json.dump(mylist, filename)` writes the `data` list to the file in JSON format.
- Finally, we close the file using `data_file.close()`.

## Steps

1. Edit your `zoo-manager.py` file.
2. Locate the section of code where the user presses "4" to exit the program.
3. Before the loop breaks, add the appropriate code to save the `animals` list to `animals.json`.
4. Save your file.
5. Run your program. Make changes to the animal list by adding or deleting animals, then exit the program by pressing 4. Check the `animals.json` file to see if the changes have been saved. Run your program again and list the animals. Have they been saved from last time?

By doing this, your program will now save the animal list back to the `animals.json` file before exiting, ensuring that all changes are preserved.

## More Information

- [W3Schools: Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
- [W3Schools: Python JSON](https://www.w3schools.com/python/python_json.asp)
