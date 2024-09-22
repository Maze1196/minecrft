import subprocess
import time
import tqdm
import colorama
from colorama import Fore, Style
from datetime import datetime
import os

colorama.init(autoreset=True)

def clear_terminal():
    # Clear the terminal based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def push():
    clear_terminal()
    print(f'{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}] {Fore.YELLOW}Initiating Push Sequence...')
    
    with open('push.txt', 'a') as file:
        # Run the subprocess and redirect stdout and stderr to the file
        result = subprocess.run(['bash', 'push.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        file.write(result.stdout + result.stderr)
    
    print(f'{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}] {Fore.GREEN}Push Complete{Style.RESET_ALL}')
    
    # Get the last push time and format it to IST
    ist_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    
    # Get the number of commits from the git log (assuming you are in a git repository)
    commits = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, text=True).stdout.strip()
    
    # Display last push time and number of commits
    print(f'{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}] {Fore.YELLOW}Last Push Time (IST): {Fore.CYAN}{ist_time}')
    print(f'{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}] {Fore.YELLOW}Number of Commits: {Fore.CYAN}{commits}')

def run(Time):
    push()
    sci_fi_bar = tqdm.tqdm(total=Time, desc=f"{Fore.MAGENTA}Next Push After {Time} seconds", 
                           bar_format="{l_bar}{bar}{r_bar}", 
                           ascii="░▒▓", ncols=100)
    for i in range(Time, 0, -1):
        minutes = i // 60
        seconds = i % 60
        sci_fi_bar.set_description(f"{Fore.MAGENTA}Next Push after {Fore.CYAN}{minutes} {Fore.MAGENTA}minutes {Fore.CYAN}{seconds} {Fore.MAGENTA}seconds")
        sci_fi_bar.update(1)
        time.sleep(0.999999) # 0.0000001 sec for some delay due to code

while True:
    run(300)