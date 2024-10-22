import datetime

class task:
    idtask: int
    create_task: datetime
    name: str
    idpriority: int
    limit_date: datetime
    duration_expect: float
    complete: bool
    dependency: int
    son: int
    father: int
    idproject: int
    duration_complete: int
    idfolder: int

    def __init__(self, id, name) -> None:
        self.idtask = id
        self.create_task = datetime.datetime.today()
        self.name = name

class priority:
    idpriority: int
    name: str
    value: int

    def __init__(self, id: int, name: str, value: int) -> None:
        self.idpriority = id
        self.name = name
        self.value = value
    
    def __str__(self) -> str:
        return self.name

class projects:
    idproject: int
    name: str
    start_project: datetime
    end_project: datetime
    nro_task: int
    nro_completed: int
    def __init__(self, id: int, name: str) -> None:
        self.idproject = id
        self.name = name

class slots:
    idslots: int
    name: str
    idproject: int 
    hours: list

    def __init__(self, id: int, name: str, idproject: str, hours: list = []) -> None:
        self.idslots = id
        self.name = name
        self.idproject = idproject
        self.hours = hours
    
class folder:
    idfolder: int
    name: str
    idproject: int
    father: int
    son: int
    def __init__(self, id, name, idproject, father, son) -> None:
        self.idfolder = id
        self.name = name
        self.idproject = idproject
        self.father = father
        self.son = son
            
