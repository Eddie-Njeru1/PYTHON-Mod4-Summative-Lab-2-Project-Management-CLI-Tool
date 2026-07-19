
# Import the class Person from person.py for object inheritance 
from models.person import Person
# Import the project class for object inheritance to get projects from saved data
from models.project import Project

# Define User class that inherits from Person class
class User(Person):
    _id_counter = 1 #Assigns users with unique ID  
    all_users = [] #Stores all User objects

    def __init__(self, name, email): #Dunder method to define the attributes for a new User object. 
        super().__init__(name, email) # Calls the parent Person class
        self.id = User._id_counter #Assign unique Id to user
        User._id_counter += 1 #Counter increases for next user
        self.projects = [] #Empty list to store user projects
        User.all_users.append(self) #Add created user to list of users

    def add_project(self, project): #Add project to user's project list
        self.projects.append(project)

    @classmethod # decorator method to modify class attributes
    def get_all(cls):
        return cls.all_users #List of all users
    
    @classmethod
    def find_by_name(cls, name): #search for user by name 
        for user in cls.all_users:
            if user.name == name:
                return user
        return None #When no match is found
    
    def to_dict(self): #Convert User object into dictionary for file saving
        return {
            "id": self.id, "name": self.name, "email": self.email,
            "projects": [p.to_dict() for p in self.projects], #Convert each project to dictionary
        }
    
    @classmethod
    def from_dict(cls, data): #Create a user object from saved dictionary
        user = cls(data["name"], data["email"]) #Creates new user using saved name and email
        user.id = data["id"] #restore the original user ID
        cls._id_counter = max(cls._id_counter, data["id"] + 1) #update ID counter prevent duplications
        for project_data in data["projects"]: #Recreate projects belonging to user
            Project.from_dict(project_data, user)
        return user #Return new user object
        
    def __repr__(self):
        return f"user(id={self.id}, name={self.name}, email={self.email}, projects={len(self.projects)})" #Display User object
    
