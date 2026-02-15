def calculate_average(numbers):
    """
    Calculates the arithmetic mean of a list of numbers.

    Args:
        numbers (list): A list of numerical values (int or float).

    Returns:
        float: The average value of the list.
    """
    total = sum(numbers)
    return total / len(numbers)