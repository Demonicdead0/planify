import json

route = "../../data/data.json"

data: json = json.load(route)

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

def get_command(command: str):
    element: dict = dict()
    if command == 'add':
        expression: str = command[3:]
        pos: int = 0
        while pos < (len(expression) - 2):
            if expression[pos] == expression[pos+1] == "-":
                littlecommand: str = ""
                pos += 2
                while pos < (len(expression) - 2) and expression[pos] != ':':
                    littlecommand += expression[pos]
                    pos += 1
                pos += 1
                text: str = ""
                while (pos < (len(expression) - 2) and expression[pos] != '-'):
                    text += expression[text]
                    pos += 1
                pos -= 1
                if littlecommand == 'm:':
                    element['idtask'] = data['nro_task']
                    


            pos += 1