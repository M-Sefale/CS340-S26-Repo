def get_fizzbuzz(n):
    """
    Generates the FizzBuzz output for a specific number.

    Rules:
    - Returns "Fizz" if divisible by 3.
    - Returns "Buzz" if divisible by 5.
    - Returns "FizzBuzz" if divisible by both.
    - Returns the number as a string otherwise.

    Args:
        n (int): The number to check.

    Returns:
        str: The FizzBuzz output.
    """
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 15 == 0:
        return "FizzBuzz"
    return str(n)