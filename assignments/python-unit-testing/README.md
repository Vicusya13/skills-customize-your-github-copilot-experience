# 📘 Assignment: Testing Python Functions with unittest

## 🎯 Objective

Write and run automated tests for simple Python functions using the standard-library `unittest` module. Practice test cases, assertions, and checking both typical and edge-case inputs without installing extra packages.

## 📝 Tasks

### 🛠️	Write Your First Unit Tests

#### Description
Create a file named `test_math_utils.py` in the same folder as the provided `math_utils.py` file. Write unit tests for `add_two_numbers()` using Python's built-in `unittest` framework.

#### Requirements
Completed program should:

- Import `unittest` and `add_two_numbers` from `math_utils`.
- Define a test class that inherits from `unittest.TestCase`.
- Include at least two test methods whose names begin with `test_`.
- Use `self.assertEqual()` to check the results of adding different numbers.
- Run the tests from this folder with `python -m unittest -v` and confirm they pass.


### 🛠️	Test Even and Odd Numbers

#### Description
Add tests for `is_even()` and check that the function behaves correctly for typical and edge-case values.

#### Requirements
Completed program should:

- Test an even number and an odd number using `self.assertTrue()` and `self.assertFalse()`.
- Include tests for zero and at least one negative number.
- Keep each check in a clearly named test method that starts with `test_`.
- Run `python -m unittest -v` again and confirm that all tests pass.