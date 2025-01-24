import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)


from modules.examples import hello_function, argument_example_function


def test_hello_function(capsys):
    """Testing the print output
    Args:
        capsys (_type_): To capture the output of the print function
    """
    # Call the function
    hello_function()
    # Capture the output
    captured = capsys.readouterr()
    # Check if the output is "Hello world!"
    assert captured.out == "Hello world!\n"


def test_argument_example_function_simple():
    """Testing a simple integer and string"""
    result = argument_example_function(5, " apples")
    assert result == "5 apples"


def test_argument_example_function_negative_number():
    """Testing a negative integer and string"""
    result = argument_example_function(-3, " oranges")
    assert result == "-3 oranges"


def test_argument_example_function_zero():
    """Testing zero as integer and empty string"""
    result = argument_example_function(0, "")
    assert result == "0"


def test_argument_example_function_big_number():
    """Testing a large integer and string with text"""
    result = argument_example_function(123456789, " is a big number.")
    assert result == "123456789 is a big number."
