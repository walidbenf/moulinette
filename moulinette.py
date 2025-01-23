import sys
import getpass
import random
import subprocess
import os

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Global variables
current_score = 0
current_level = 0
current_exercise = None
EXERCISE_TESTS = {
    #Level 0
    "aff_a": [
        {"args": ["abc"], "expected": "a\n"},
        {"args": ["dubO a POIL"], "expected": "a\n"},
        {"args": ["zz sent le poney"], "expected": "\n"},
        {"args": [], "expected": "a\n"}
    ],
    "aff_first_param": [
        {"args": ["vincent", "mit", "l'ane", "dans", "un", "pre", "et", "s'en", "vint"], "expected": "vincent\n"},
        {"args": ["j'aime le fromage de chevre"], "expected": "j'aime le fromage de chevre\n"},
        {"args": [], "expected": "\n"}
    ],
    "aff_last_param": [
        {"args": ["zaz", "mange", "des", "chats"], "expected": "chats\n"},
        {"args": ["j'aime le savon"], "expected": "j'aime le savon\n"},
        {"args": [], "expected": "\n"}
    ],
    "aff_z": [
        {"args": ["abc"], "expected": "z\n"},
        {"args": ["dubO a POIL"], "expected": "z\n"},
        {"args": ["zaz sent le poney"], "expected": "z\n"},
        {"args": [], "expected": "z\n"},
        {"args": ["abc", "def"], "expected": "z\n"}
    ],
    "ft_countdown": [
        {"args": [], "expected": "9876543210\n"}
    ],
    "ft_print_numbers": [
        {"args": [], "expected": "0123456789\n"}
    ],
    "hello": [
        {"args": [], "expected": "Hello World!\n"}
    ],
    "maff_alpha": [
        {"args": [], "expected": "aBcDeFgHiJkLmNoPqRsTuVwXyZ\n"}
    ],
    "maff_revalpha": [
        {"args": [], "expected": "zYxWvUtSrQpOnMlKjIhGfEdCbA\n"}
    ],
    "only_a": [
        {"args": [], "expected": "a\n"}
    ],
    "only_z": [
        {"args": [], "expected": "z\n"}
    ],
    
     #Level 1
    "first_word": [
        {"args": ["FOR PONY"], "expected": "FOR\n"},
        {"args": ["this        ...       is sparta, then again, maybe    not"], "expected": "this\n"},
        {"args": ["   "], "expected": "\n"},
        {"args": ["a", "b"], "expected": "\n"},
        {"args": ["  lorem,ipsum  "], "expected": "lorem,ipsum\n"}
    ],
    "fizzbuzz": [
        {"args": [], "expected": "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n16\n17\nfizz\n19\nbuzz\nfizz\n22\n23\nfizz\nbuzz\n26\nfizz\n28\n29\nfizzbuzz\n31\n32\nfizz\n34\nbuzz\nfizz\n37\n38\nfizz\nbuzz\n41\nfizz\n43\n44\nfizzbuzz\n46\n47\nfizz\n49\nbuzz\nfizz\n52\n53\nfizz\nbuzz\n56\nfizz\n58\n59\nfizzbuzz\n61\n62\nfizz\n64\nbuzz\nfizz\n67\n68\nfizz\nbuzz\n71\nfizz\n73\n74\nfizzbuzz\n76\n77\nfizz\n79\nbuzz\nfizz\n82\n83\nfizz\nbuzz\n86\nfizz\n88\n89\nfizzbuzz\n91\n92\nfizz\n94\nbuzz\nfizz\n97\n98\nfizz\nbuzz\n"}
    ],
    "ft_putstr": [
        {"args": [], "expected": "Hello World!\n"}
    ],
    "ft_strcpy": [
        {"args": [], "expected": "World\n"}
    ],
    #Level 2
    "alpha_mirror": [
        {"args": ["abc"], "expected": "zyx\n"},
        {"args": ["My horse is Amazing."], "expected": "Nb slihv rh Znzarmt.\n"},
        {"args": [], "expected": "\n"},
        {"args": ["abcABCxyzXYZ"], "expected": "zyxZYXabcABC\n"}
    ],
    "do_op": [
        {"args": ["123", "*", "456"], "expected": "56088\n"},
        {"args": ["9828", "/", "234"], "expected": "42\n"},
        {"args": ["1", "+", "-43"], "expected": "-42\n"},
        {"args": [], "expected": "\n"},
        {"args": ["42", "%", "4"], "expected": "2\n"},
        {"args": ["10", "-", "5"], "expected": "5\n"}
    ]
}
LEVEL_0_EXERCISES = [
    "aff_a",
    "aff_first_param",
    "aff_last_param",
    "aff_z", 
    "ft_countdown",
    "ft_print_numbers",
    "hello",
    "maff_alpha",
    "maff_revalpha",
    "only_a",
    "only_z",
]

LEVEL_1_EXERCISES = [
    "first_word",
    "fizzbuzz",
    "ft_putstr",
    "ft_strcpy",
    "ft_strlen",
    "ft_swap",
    "repeat_alpha",
    "rev_print",
    "rot_13",
    "rotone",
    "search_and_replace",
    "ulstr"
]
LEVEL_2_EXERCISES = [
"alpha_mirror",
"do_op",
"ft_atoi",
"ft_strcmp",
"ft_strdup",
"ft_strrev",
"inter",
"last_word",
"union"
]

LEVEL_3_EXERCISES = [
    "ft_atoi_base"
]
def check_credentials():
    login = input("Login: ")
    password = getpass.getpass("Password: ")
    
    if login == "exam" and password == "exam":
        return True
    else:
        print("Invalid credentials")
        return False

def get_random_exercise():
    global current_level
    if current_level == 0:
        return random.choice(LEVEL_0_EXERCISES)
    elif current_level == 1:
        return random.choice(LEVEL_1_EXERCISES)
    elif current_level == 2:
        return random.choice(LEVEL_2_EXERCISES)
    elif current_level == 3:
        return random.choice(LEVEL_3_EXERCISES)
    return None

def check_submission():
    if current_exercise is None:
        print("No exercise currently assigned. Launch examshell first.")
        return False
    
    submission_path = f"rendu/{current_exercise}/{current_exercise}.c"
    if not os.path.exists(submission_path):
        print(f"No submission found at {submission_path}")
        return False
    
    reference_path = f"exam/level{current_level}/{current_exercise}/{current_exercise}.c"
    if not os.path.exists(reference_path):
        print(f"Reference solution not found at {reference_path}")
        return False
    
    return True

def is_program(source_file):
    with open(source_file, 'r') as f:
        content = f.read()
        return 'main' in content

def compile_and_run(source_file, output_file, args=None):
    try:
        if is_program(source_file):
            subprocess.run(['gcc', source_file, '-o', output_file], 
                         check=True, 
                         stderr=subprocess.DEVNULL,
                         stdout=subprocess.DEVNULL)
        else:
            test_main = f"exam/level{current_level}/{current_exercise}/main.c"
            subprocess.run(['gcc', source_file, test_main, '-o', output_file], 
                         check=True, 
                         stderr=subprocess.DEVNULL,
                         stdout=subprocess.DEVNULL)
        
        cmd = [f'./{output_file}']
        if args:
            cmd.extend(args)
            
        result = subprocess.run(cmd, 
                              capture_output=True, 
                              text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def grade_exercise():
    if not check_submission():
        return
    
    submission_path = f"rendu/{current_exercise}/{current_exercise}.c"
    reference_path = f"exam/level{current_level}/{current_exercise}/{current_exercise}.c"
    
    # Get test cases for current exercise
    test_cases = EXERCISE_TESTS.get(current_exercise, [{"args": [], "expected": ""}])
    
    for test in test_cases:
        submission_output = compile_and_run(submission_path, "submission_exe", test["args"])
        reference_output = compile_and_run(reference_path, "reference_exe", test["args"])
        
        if submission_output is None:
            print(f"{RED}Failure{RESET}")
            return
        
        if submission_output != reference_output:
            print(f"{RED}Failure{RESET}")
            return
    
    print(f"{GREEN}Success!{RESET}")
    update_score()

def display_subject(exercise):
    subject_path = f"exam/level{current_level}/{exercise}/subject.txt"
    if os.path.exists(subject_path):
        with open(subject_path, 'r') as f:
            print("\nSubject:")
            print(f.read())
            print()

def launch_examshell():
    print("Launching exam environment...")
    global current_score, current_level, current_exercise
    current_score = 0
    current_level = 0
    current_exercise = get_random_exercise()
    display_score()
    print(f"Submit your code in: rendu/{current_exercise}/{current_exercise}.c")
    print(f"Level {current_level} - Exercise: {current_exercise}")
    display_subject(current_exercise)

def display_help():
    print("\nAvailable commands:")
    print("help     - Display this help message")
    print("examshell- Launch exam environment")
    print("grademe  - Grade current exercise")
    print("exit     - Quit the program\n")

def display_score():
    print(f"\nCurrent Score: {current_score}/100")
    print(f"Current Level: {current_level}")

def update_score():
    global current_score, current_level, current_exercise
    previous_level = current_level
    
    if current_score < 100:
        current_score += 25
        
        # Check for level progression
        if current_score >= 75 and current_level == 2:
            current_level = 3
            print(f"\n{GREEN}Congratulations! You've reached level 3!{RESET}")
            current_exercise = get_random_exercise()
        elif current_score >= 50 and current_level == 1:
            current_level = 2
            print(f"\n{GREEN}Congratulations! You've reached level 2!{RESET}")
            current_exercise = get_random_exercise()
        elif current_score >= 25 and current_level == 0:
            current_level = 1
            print(f"\n{GREEN}Congratulations! You've reached level 1!{RESET}")
            current_exercise = get_random_exercise()
        
        if current_level != previous_level:
            print(f"New exercise: {current_exercise}")
            print(f"Submit your code in: rendu/{current_exercise}/{current_exercise}.c")
        
        display_score()

def interactive_shell():
    while True:
        command = input("> ").lower().strip()
        
        if command == "help":
            display_help()
        elif command == "examshell":
            launch_examshell()
        elif command == "grademe":
            grade_exercise()
        elif command == "exit":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Unknown command. Type 'help' for available commands.")

def main():
    if not check_credentials():
        sys.exit(1)
    
    print("\nAuthentication successful!")
    display_help()
    interactive_shell()

if __name__ == "__main__":
    main()