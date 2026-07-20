
# Define a Task class 
class Task:
    _id_counter = 1 #Assigns task with unique ID  
    all_tasks = [] #Stores all task objects
    
    def __init__(self, title, status, assigned_to, project): #Dunder method to define the attributes for a new task object.
        self.title = title #Assign a title attribute to the task
        self.status = status #Set task status 
        self.assigned_to = assigned_to #Reference who the task is assigned to
        self.project = project #Assign a project attribute to the task
        self.id = Task._id_counter #Assign unique ID to task
        Task._id_counter += 1 #Increase counter for next  task
        Task.all_tasks.append(self) #Add task to ist of tasks
        project.add_task(self) #Link task to project 

    @property # Decorator method to get the task status
    def status(self):
        return self._status
    
    @status.setter #Validates the task status
    def status(self, value):
        if not value:
            raise ValueError("Error! Status cannot be empty") #Flag empty status
        self._status = value 

    def complete(self): #Check task completion
        self.status = "complete."
        
    @classmethod
    def get_all(cls):
        return cls.all_tasks #Return list of all tasks
    
    @classmethod
    def find_by_title(cls, title): #Find a task using title
        for task in cls.all_tasks:
            if task.title == title:
                return task #When found
        return None #When not found
    
    def to_dict(self): #Convert Task object into dictionary for file saving
        return {"id": self.id, "title": self.title, "status": self.status, "assigned_to": self.assigned_to}

    @classmethod
    def from_dict(cls, data, project): #Create a task object from saved dictionary
        task = cls(data["title"], data["status"], data["assigned_to"], project) #Create a new task using saved data
        task.id = data["id"]  #restore the original task ID                                     
        cls._id_counter = max(cls._id_counter, data["id"] + 1) #update ID counter prevent duplications
        return task #Return new task object
        
    def __repr__(self):
            return f"Task(id={self.id}, title={self.title}, status={self.status}, assigned_to={self.assigned_to})" #Display task object
        
