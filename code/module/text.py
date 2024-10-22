def title(string: str) -> None:
    lon: int = len(string)
    print(" "*lon + "#" + "="*(lon+2) + "#")
    print(" "*lon + f"║ {string} ║")
    print(" "*lon + "#" + "="*(lon+2) + "#")
