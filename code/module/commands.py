def get_command() -> list:
    element: list = []
    element.append('add')
    element.append('delete')
    element.append('show')
    element.append('planify')
    element.append('exit')
    return element

def len_command() -> str:
    element: str = input(">")
    element = element.lower()
    for elemen in get_command():
        if elemen == element:
            return element
    return "error"