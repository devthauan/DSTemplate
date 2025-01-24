def hello_function():
    """function that prints "Hello world!" """
    print("Hello world!")


def argument_example_function(argument_1: int, argument_2: str) -> str:
    """Function that converts the first argument into a string and concatenates it with the second argument.

    Args:
        argument_1 (int): The first argument of the function
        argument_2 (str): The second argument of the function

    Returns:
        str: A concatenation of both arguments
    """
    return str(argument_1) + argument_2
