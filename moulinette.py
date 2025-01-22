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

def compile_and_run(source_file, output_file):
    try:
        # Redirect stderr to /dev/null to hide compilation errors
        subprocess.run(['gcc', source_file, '-o', output_file], 
                      check=True, 
                      stderr=subprocess.DEVNULL,
                      stdout=subprocess.DEVNULL)
        result = subprocess.run([f'./{output_file}'], 
                              capture_output=True, 
                              text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def grade_exercise():
    if not check_submission():
        return
    
    submission_output = compile_and_run(f"rendu/{current_exercise}/{current_exercise}.c", "submission_exe")
    reference_output = compile_and_run(f"exam/level{current_level}/{current_exercise}/{current_exercise}.c", "reference_exe")
    
    if submission_output is None:
        print(f"{RED}Failure{RESET}")
        return
    
    if submission_output == reference_output:
        print(f"{GREEN}Success!{RESET}")
        update_score()
    else:
        print(f"{RED}Failure{RESET}")

def launch_examshell():
    print("Launching exam environment...")
    global current_score, current_level, current_exercise
    current_score = 0
    current_level = 0
    current_exercise = get_random_exercise()
    display_score()
    print(f"Level {current_level} - Exercise: {current_exercise}")

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
    global current_score
    if current_score < 100:
        current_score += 25
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