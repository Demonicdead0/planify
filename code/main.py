# Import the libraries
import sys
import os
from module.text import *
from module.commands import *
from module.classes import *
import json

# Send the text
title("Planify")

# verify if the datas exists 
routetask: str = '../data/task.json'
routeproject: str = '../data/project.json'
routepriority: str = '../data/priority.json'

d_task: json
d_project: json
d_priority: json

with open(routetask, encoding='utf8') as tasks:
    d_task = json.load(tasks)

with open(routeproject, encoding='utf8') as projects:
    d_project = json.load(projects)

with open(routepriority, encoding='utf8') as priorities:
    d_priority = json.load(priorities)
print(d_task)

alert("no existe archivos json")

# execute a loop
while True:
    subtittle("Task")
    command: str = len_command() 
    pass