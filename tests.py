from functions.get_file_content import get_file_content

print("Test 1: calculator, lorem.txt")
print(get_file_content("calculator", "main.py"))

print("Test 2: calculator, pkg/calculator.py")
print(get_file_content("calculator", "pkg/calculator.py"))

print("Test 3: calculator, /bin/cat")
print(get_file_content("calculator", "/bin/cat"))