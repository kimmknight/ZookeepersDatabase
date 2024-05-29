# Step 12

## Introduction

To make our animal list persistent, we need to save it to a file. This way, the list is not lost when the program ends, and we can load it back the next time the program runs. For this purpose, we will use the `json` library to read and write the animal list into a JSON file.

## Objective(s)

- Import the `json` library.

## Background Information

### Importing Libraries

In Python, you can use the `import` statement to include external libraries or modules in your program. These libraries provide additional functionality that you can use in your code.

For example, to import the `json` library, you would write:

```
import json
```

The `json` library allows you to work with JSON data, which is a common format for storing and exchanging data. We'll use it to read and write our animal list to a file.

## Steps

1. Edit your `zoo-manager.py` file.
2. At the very top of your file, add the following import statement:

```
import json
```

3. Save your file.

That's it for this step! In future steps, we will use the `json` library to save and load the animal list to and from a file.

## More Information

- [W3Schools: Python Modules](https://www.w3schools.com/python/python_modules.asp)
- [W3Schools: Python JSON](https://www.w3schools.com/python/python_json.asp)
