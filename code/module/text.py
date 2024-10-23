from colorama import init, Fore, Style
init(autoreset=True)

def title(string: str) -> None:
    lon: int = len(string)
    print(" "*lon + "#" + "="*(lon+2) + "#")
    print(" "*lon + f"║ {string} ║")
    print(" "*lon + "#" + "="*(lon+2) + "#")
    print("")

def subtittle(string: str) -> None:
    lon: int = len(string)
    print(" "*lon + f"  {string}  ")
    print(" "*lon + "=" + "="*(lon+2) + "=")

def alert(string: str) -> None:
    print(f"{Fore.YELLOW} {string} {Style.RESET_ALL}")

def success(string: str) -> None:
    print(f"{Fore.GREEN} {string} {Style.RESET_ALL}" )