# this is the main program.
class tasks:
    nro_tasks: int = 0
    def __init__(self) -> None:
        self.nro_tasks = 0
    
    def build(self) -> None:
        pass

# Import the libraries
import sys
import os
from module.text import *
from module.commands import *

# Send the text
title("Planify")

# execute a loop
while True:
    command: str = len_command()
    pass