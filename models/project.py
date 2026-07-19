
# Define a Project class
class Project:
    _id_counter = 1 #Assigns project with unique ID  
    all_projects = [] #Stores all project objects

    def __init__(self, title, description, due_date, owner): #Dunder method to define the attributes for a new project object.
        self.title = title #Assign a title attribute to the project
        self.description = description #Assign a project description attribute
        self.due_date = due_date #Assign a due date attribute to the project
        self.owner = owner #Assign a owner attribute to the project
        self.id = Project._id_counter #Assign unique ID to project
        Project._id_counter += 1 #Increase counter for next  project
        self.tasks = [] #empty list to store project tasks
        Project.all_projects.append(self) #Add project to ist of projects
        owner.add_project(self) #Add project to owner's project list

    @property # Decorator method to get the project title
    def title(self):
        return self._title
    
    @title.setter #Validates the project title
    def title(self, value):
        if not value:
            raise ValueError("Error! Title cannot be empty") #Flag empty title
        self._title = value 

    def add_task(self, task): #Add task to project
        self.tasks.append(task)
        
    @classmethod
    def get_all(cls):
        return cls.all_projects #Return list of all projects
    
    @classmethod
    def find_by_title(cls, title): #Find a project using title
        for project in cls.all_projects:
            if project.title == title:
                return project #When found
            return None #When not found
        
        def __repr__(self):
            return f"Project(id={self.id}, title={self.title}, owner={self.owner.name}, tasks={len(self.tasks)})" #Display project object
        
