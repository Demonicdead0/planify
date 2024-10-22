def get_command() -> list:
    element: list = []
    element.append('add')
    element.append('delete')
    element.append('show')
    element.append('planify')
    return element

def len_command() -> str:
    element: str = input()
    for elemen in get_command():
        if element == element:
            return element
    return "error"