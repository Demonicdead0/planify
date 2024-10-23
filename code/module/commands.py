import json

routedata: str = '../data/data.json'
data: json

with open(routedata, encoding='utf8') as ruta:
    data = json.load(ruta)


def commands() -> list:
    element: list = []
    element.append('add')
    element.append('delete')
    element.append('show')
    element.append('planify')
    element.append('exit')
    return element

def len_command() -> list:
    element: str = input(">")
    element = element.lower()
    for elemen in commands():
        if element.startswith(elemen):
            return [elemen, element[len(elemen)+1:]]
    return ["error",'0']

def get_parameters(command: str) -> list:
    string: list = command.split(':')
    parameters: list = []
    for i in range(len(string)-1):
        st: str = string[i].rsplit(' ',1)
        parameters.extend(st)
    parameters.append(string[-1])

    return parameters

def get_command(command: str, parameters: str) -> None:
    message, *code = get_parameters(parameters)
    print(message)
    print(code)