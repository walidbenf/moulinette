import subprocess
import difflib

def compile_file(sources, executable):
    subprocess.run(['gcc'] + sources + ['-o', executable], check=True)

def execute_file(executable):
    result = subprocess.run(['./' + executable], capture_output=True, text=True)
    return result.stdout.splitlines()

def compare_outputs(output1, output2):
    diff = difflib.unified_diff(output1, output2, lineterm='')
    return list(diff)

def display_differences(differences):
    for line in differences:
        print(line)

def main():
    sources1 = ['w_functions/main_w_putchar.c', 'w_functions/w_putchar.c']
    sources2 = ['tester_functions/main_putchar.c', 'tester_functions/ft_putchar.c']
    executable1 = 'test_w_putchar'
    executable2 = 'test_putchar'
    
    # Compile the files with the different sources
    compile_file(sources1, executable1)
    compile_file(sources2, executable2)
    
    # Execute the files and capture the outputs
    output_w_putchar = execute_file(executable1)
    output_putchar = execute_file(executable2)
    
    # Compare the outputs
    differences = compare_outputs(output_w_putchar, output_putchar)
    
    if differences:
        print("Differences found:")
        display_differences(differences)
    else:
        print("No differences found.")

if __name__ == "__main__":
    main()