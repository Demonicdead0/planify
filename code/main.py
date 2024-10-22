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
alert("no existe archivos json")

# execute a loop
while True:
    subtittle("Task")
    command: str = len_command()
    pass