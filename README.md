# Matrix Multiplication Program

This is a Python program that allows the user to input two matrices and multiply them. The program uses the `os` and `time` libraries to clear the console and pause the execution for a few seconds to simulate a loading animation.

## Installation

1. Make sure you have Python 3 installed on your system.
2. Download the `matrix_multiplication.py` file to your computer.
3. Open a terminal or command prompt and navigate to the directory where the `matrix_multiplication.py` file is located.
4. Run the program by typing `python matrix_multiplication.py` and pressing enter.

## Usage

1. Upon running the program, you will be prompted to enter the rows of the first matrix. You can switch to the second matrix by typing "second" and pressing enter. You can submit the matrices for multiplication by typing "done" and pressing enter.
2. Each row should consist of a comma-separated list of numbers (e.g. "1,2,3,4"). If a row has a different number of elements than the previous rows, an error will be displayed and you will have to re-enter the row.
3. Once both matrices have been submitted, the program will display the resulting matrix.

## Limitations

- The program currently only supports integer matrices.
- The program assumes that the user inputs valid matrices for multiplication (i.e. the number of columns of the first matrix equals the number of rows of the second matrix).

Feel free to modify the program to add more features or to support additional data types.
