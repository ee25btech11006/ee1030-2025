import subprocess

# Run the compiled C program
result = subprocess.run(
    ['./code'],   # executable created from code.c
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)
