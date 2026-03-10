from colorama import init, Fore, Style
import pyfiglet
from datetime import datetime

init(autoreset=True)

class Printer:
    HEADER = Fore.MAGENTA
    INFO = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    BOLD = Style.BRIGHT
    
    @staticmethod
    def show_banner():
        banner = pyfiglet.figlet_format("SQLPwn", font="slant")
        print(Fore.RED + Style.BRIGHT + banner)
        print(Fore.YELLOW + "=" * 60)
        print(Fore.GREEN + Style.BRIGHT + "      Advanced SQL Injection Framework")
        print(Fore.CYAN + "      Author: Bahrul Rozak")
        print(Fore.YELLOW + "      Version: 1.0.0")
        print(Fore.RED + "      GitHub: @bahrul-rozak")
        print(Fore.YELLOW + "=" * 60 + Style.RESET_ALL)
        print()
    
    @staticmethod
    def print_info(msg):
        print(f"{Fore.CYAN}[*] {msg}{Style.RESET_ALL}")
    
    @staticmethod
    def print_success(msg):
        print(f"{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")
    
    @staticmethod
    def print_warning(msg):
        print(f"{Fore.YELLOW}[!] {msg}{Style.RESET_ALL}")
    
    @staticmethod
    def print_error(msg):
        print(f"{Fore.RED}[-] {msg}{Style.RESET_ALL}")
    
    @staticmethod
    def print_result(msg, data):
        print(f"{Fore.MAGENTA}[>] {msg}: {Fore.WHITE}{data}{Style.RESET_ALL}")