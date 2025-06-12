from functions.run_python import run_python_file

print("~~~ Test 1 ~~~")
print(run_python_file("calculator", "main.py"))

print("~~~ Test 2 ~~~")
print(run_python_file("calculator", "tests.py"))

print("~~~ Test 3 ~~~")
print(run_python_file("calculator", "../main.py"))

print("~~~ Test 4 ~~~")
print(run_python_file("calculator", "nonexistent.py"))