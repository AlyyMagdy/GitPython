def add(a, b):
    return a+b

# New Comment
num=add(5,5)
print(f"Number equals to ========= {num}\n")

# Open a file named "output.log" in write mode ('w')
with open('output.log', 'w') as file:
    # Write "Hello, World!" to the file
    file.write(f'Hello, World! , the function returns {num}')

# Print "Hello, World!" to the console
print('Hello, World!')

#Testing new commit jenkins