import subprocess
import io
import os

tests = [
    ("equal([10,10,10])", "1"),
    ("equal([4,5,4])", "0"),
    ("equal([])", "1"),
    ("equal(tail([100,100,100,100]))", "1"),
    ("equal(divide(3,[3,6,9]))", "0"),
    ("equal(append(1,tail([1,1,1,1])))", "1"),
    ("equal(divide(2,[4,6,8]))", "0"),
    
    ("sum([2,4,6])", "12"),
    ("sum([])", "0"),
    ("sum(tail([10,20,30]))", "50"),
    ("sum(divide(3,[3,6,9,10]))", "18"),
    ("sum(append(7,divide(2,[4,6,8])))", "25"),
    ("sum(append(3,tail([10,20,30])))", "53"),
    ("sum(divide(5,tail([50,25,10,15])))", "50"),
    ("sum(append(equal([2,2]),divide(2,[4,6])))", "11"),
    
    ("42", "42")
]

for file_input, output in tests:
    with open("input", "w") as f:
        f.write(file_input)
    
    process = subprocess.Popen(
        ['./list', 'input'],  # Replace with your executable
        stdout=subprocess.PIPE,  # Capture stdout if needed
        stderr=subprocess.PIPE   # Capture stderr if needed
    )
    stdout, stderr = process.communicate()
    stdout = stdout.decode("utf-8")[:-1]
    if stderr:
        stderr = stderr.decode("utf-8")[:-1]
        print(f"{file_input}. Error: {stderr}.")
        continue
    if output != stdout:
        print(f"{file_input}. Expected: {output}. Got: {stdout}.")

os.remove("input")