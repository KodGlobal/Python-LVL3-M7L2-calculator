import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Unknown operation."

'''
Task. At the moment, there are 3 implemented unit-tests:
We test the correctness of addition and division operations as well as the handling of the unknown operation
Your task is to add at least two tests for the following operations:
1. Subtraction
2. Multiplication
However, it would be great if you could come up with and write some additional tests!
'''
