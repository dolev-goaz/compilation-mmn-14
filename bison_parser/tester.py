import subprocess
import io
import os

tests = [
    ("equal([10,10,10])", "1"),
    ("equal([4,5,4])", "0"),
    ("equal(tail([1]))", "1"), # equals of empty list
    ("equal(tail([50,100,100,100]))", "1"),
    ("equal(tail([50,100,80,100]))", "0"),
    ("equal(divide(3,[3,6,9]))", "0"),
    ("equal(append(1,tail([1,1,1,1])))", "1"),
    ("equal(append(2,tail([1,1,1,1])))", "0"),
    ("equal(divide(2,[5,8,11]))", "1"),
    ("equal([12,4,100])", "0"), # example from assignment
    ("equal([7,7,7])", "1"),    # example from assignment
    
    ("sum([2,4,6])", "12"),
    ("sum(tail([8]))", "0"), # sum of empty list
    ("sum(tail([10,20,30]))", "50"),
    ("sum(divide(3,[3,6,9,10]))", "18"),
    ("sum(append(7,divide(2,[4,6,8])))", "25"),
    ("sum(append(3,tail([10,20,30])))", "53"),
    ("sum(divide(5,tail([50,25,10,15])))", "50"),
    ("sum(append(equal([2,2]),divide(2,[4,6])))", "11"),
    ("sum(append(equal([3,3]),divide(10,[30,8,50])))", "81"), # example from assignment
    ("sum([100,4,12])", "116"),                               # example from assignment
    
    ("42", "42")
]

error_count = 0
for file_input, output in tests:
    with open("input", "w") as f:
        f.write(file_input)
    
    process = subprocess.Popen(
        ['./list', 'input'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    stdout = stdout.decode("utf-8")[:-1]
    if stderr:
        stderr = stderr.decode("utf-8")[:-1]
        print(f"{file_input}. Error: {stderr}.")
        error_count+=1
        continue
    if output != stdout:
        print(f"{file_input}. Expected: {output}. Got: {stdout}.")
        error_count+=1

os.remove("input")
if error_count == 0:
    print("✅ Tests passed successfuly!")
else:
    print("❌ Tests failed!")