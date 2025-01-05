import subprocess
import io
import os

tests = [
    ("equal([10, 10, 10])", "1"), # All elements in the list [10, 10, 10] are equal, so equal returns 1
    ("equal([4, 5, 4])", "0"), # The elements in the list [4, 5, 4] are not all equal, so equal returns 0
    ("equal([])", "1"), # An empty list always evaluates to 1 for equal
    ("equal(tail([100, 100, 100, 100]))", "1"), # tail([100, 100, 100, 100]) results in [100, 100, 100], and equal([100, 100, 100]) returns 1
    ("equal(divide(3, [3, 6, 9]))", "0"), # divide(3, [3, 6, 9]) results in [3, 6, 9] (all divisible by 3), but they are not equal, so equal returns 0
    ("equal(append(1, tail([1, 1, 1, 1])))", "1"), # tail([1, 1, 1, 1]) results in [1, 1, 1], and append(1, [1, 1, 1]) results in [1, 1, 1, 1]. Since all elements are equal, equal returns 1
    ("equal(divide(2, [4, 6, 8]))", "0"), # divide(2, [4, 6, 8]) results in [4, 6, 8]. The elements are not equal, so equal returns 0
    
    ("sum([2, 4, 6])", "12"), # The sum of [2, 4, 6] is 2 + 4 + 6 = 12
    ("sum([])", "0"), # An empty list always evaluates to 0 for sum
    ("sum(tail([10, 20, 30]))", "50"), # tail([10, 20, 30]) results in [20, 30], and sum([20, 30]) computes 20 + 30 = 50
    ("sum(divide(3, [3, 6, 9, 10]))", "18"), # divide(3, [3, 6, 9, 10]) results in [3, 6, 9], and sum([3, 6, 9]) computes 3 + 6 + 9 = 18
    ("sum(append(7, divide(2, [4, 6, 8])))", "25"), # divide(2, [4, 6, 8]) results in [4, 6, 8]. Adding 7 results in [4, 6, 8, 7], and their sum is 4 + 6 + 8 + 7 = 25
    ("sum(append(3, tail([10, 20, 30])))", "53"), # tail([10, 20, 30]) results in [20, 30]. Adding 3 results in [20, 30, 3], and their sum is 20 + 30 + 3 = 53
    ("sum(divide(5, tail([50, 25, 10, 15])))", "50"), # tail([50, 25, 10, 15]) results in [25, 10, 15], and divide(5, [25, 10, 15]) results in [25, 10, 15]. Their sum is 25 + 10 + 15 = 50
    ("sum(append(equal([2, 2]), divide(2, [4, 6])))", "11"), # equal([2, 2]) returns 1, and divide(2, [4, 6]) results in [4, 6]. Adding 1 results in [4, 6, 1], and their sum is 4 + 6 + 1 = 11
    
    ("42", "42") # The input is a number, and its value is directly returned as the result.
]

for file_input, output in tests:
    with open("input", "w") as f:
        f.write(file_input)
    
    process = subprocess.Popen(
        ['./list', 'input'],  # Replace with your executable
        stdin=subprocess.PIPE,  # Pass input through stdin
        stdout=subprocess.PIPE,  # Capture stdout if needed
        stderr=subprocess.PIPE   # Capture stderr if needed
    )
    stdout = process.communicate()[0].decode("utf-8")[:-1]
    if output != stdout:
        print(f"{file_input}. Expected: {output}. Got: {stdout}.")

os.remove("input")