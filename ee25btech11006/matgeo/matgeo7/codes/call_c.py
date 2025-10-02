import subprocess
import os

# Name of the compiled executable
executable_name = 'lambda_program'
if os.name == 'nt':  # For Windows
    executable_name += '.exe'

# Path to the executable (current directory)
executable_path = os.path.join('.', executable_name)

# Run the C program
result = subprocess.run(
    [executable_path],
    capture_output=True,
    text=True,
    check=True
)

# Print the captured output
print(result.stdout)