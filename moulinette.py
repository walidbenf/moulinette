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
    tests = [
        {
            "sources": ['w_functions/main_w_putchar.c', 'w_functions/w_putchar.c'],
            "executable": 'test_w_putchar',
            "output": None
        },
        {
            "sources": ['tester_functions/main_putchar.c', 'tester_functions/ft_putchar.c'],
            "executable": 'test_putchar',
            "output": None
        },
        {
            "sources": ['w_functions/main_w_print_alphabet.c', 'w_functions/w_putchar.c', 'w_functions/w_print_alphabet.c'],
            "executable": 'test_w_print_alphabet',
            "output": None
        },
        {
            "sources": ['tester_functions/main_print_alphabet.c', 'tester_functions/ft_putchar.c', 'tester_functions/ft_print_alphabet.c'],
            "executable": 'test_print_alphabet',
            "output": None
        },
        {
            "sources": ['w_functions/main_w_print_reverse_alphabet.c', 'w_functions/w_putchar.c', 'w_functions/w_print_reverse_alphabet.c'],
            "executable": 'test_w_reverse_print_alphabet',
            "output": None
        },
        {
            "sources": ['tester_functions/main_print_reverse_alphabet.c', 'tester_functions/ft_putchar.c', 'tester_functions/ft_print_reverse_alphabet.c'],
            "executable": 'test_reverse_print_alphabet',
            "output": None
        },
        {
            "sources": ['w_functions/main_w_print_numbers.c', 'w_functions/w_putchar.c', 'w_functions/w_print_numbers.c'],
            "executable": 'test_w_print_numbers',
            "output": None
        },
        {
            "sources": ['tester_functions/main_print_numbers.c', 'tester_functions/ft_putchar.c', 'tester_functions/ft_print_numbers.c'],
            "executable": 'test_print_numbers',
            "output": None
        }
    ]
    
    # Compile and execute the tests
    for test in tests:
        compile_file(test["sources"], test["executable"])
        test["output"] = execute_file(test["executable"])
    
    # Compare the outputs
    differences = compare_outputs(tests[0]["output"], tests[1]["output"])
    if differences:
        print("Differences found in putchar tests:")
        display_differences(differences)
    else:
        print("No differences found in putchar tests.")
    
    differences = compare_outputs(tests[2]["output"], tests[3]["output"])
    if differences:
        print("Differences found in print_alphabet tests:")
        display_differences(differences)
    else:
        print("No differences found in print_alphabet tests.")
    
    differences = compare_outputs(tests[4]["output"], tests[5]["output"])
    if differences:
        print("Differences found in reverse_print_alphabet tests:")
        display_differences(differences)
    else:
        print("No differences found in reverse_print_alphabet tests.")
    
    differences = compare_outputs(tests[6]["output"], tests[7]["output"])
    if differences:
        print("Differences found in print_numbers tests:")
        display_differences(differences)
    else:
        print("No differences found in print_numbers tests.")

if __name__ == "__main__":
    main()