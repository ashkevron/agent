from functions.get_files_info import get_files_info

print("Test 1: calculator, .")
print(get_files_info("calculator", "."))

print("Test 2: calculator, pkg")
print(get_files_info("calculator", "pkg"))

print("Test 3: calculator, /bin")
print(get_files_info("calculator", "/bin"))

print("Test 4: calculator, ../")
print(get_files_info("calculator", "../"))