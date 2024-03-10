**Installation:**

No installation is required. Simply import the `generate_random_list` function from the `random_generator` module.

```python
from random_generator import generate_random_list
```

**Usage:**

### `generate_random_list(length, data_type='number')`

Generates a random list of the specified length and data type.

**Parameters:**
- `length` (int): The length of the list.
- `data_type` (str): The type of data to generate ('number' or 'string'). Default is 'number'.

**Example:**

```python
from random_generator import generate_random_list

# Generate a random list of numbers
number_list = generate_random_list(5)
print("Random Number List:", number_list)

# Generate a random list of strings
string_list = generate_random_list(5, data_type='string')
print("Random String List:", string_list)
```

Note: You can pass the optional parameter `data_type` to specify the type of data to generate.

**Usage in a Python file:**

1. Save the code above in a file named `random_generator.py`.
2. Create a new Python script in the same directory.
3. Import and use the `generate_random_list` function as shown in the example above.
