import random
import string

def generate_random_list(length, data_type='number'):
    """
    Generates a random list of specified length.

    Parameters:
    - length (int): The length of the list.
    - data_type (str): The type of data to generate ('number' or 'string').

    Returns:
    - list: The generated list.
    """
    if data_type == 'number':
        return [random.randint(1, 100) for _ in range(length)]
    elif data_type == 'string':
        return [''.join(random.choices(string.ascii_letters, k=5)) for _ in range(length)]
    else:
        raise ValueError("Invalid data type. Supported types are 'number' and 'string'.")

