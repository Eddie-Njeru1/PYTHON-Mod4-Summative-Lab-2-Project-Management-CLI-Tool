'''Parent Class'''
# Define Person class that holds common attributes 
class Person:
    def __init__(self, name, email):  #Dunder method to define the attributes for a new Person object once created. 
        self.name = name   #Attribute for person's name once an instance is created.
        self.email = email  #Attribute for person's email once an instance is created.
        
        @property # Decorator method to allow accessing email like a regular attribute
        def email(self): 
            return self.email # Returns value of person's email 
        
        @email.setter # Checks if created email meets validation criteria
        def email(self, value):
            if "@" not in value: # Flag email lacking '@'
                raise ValueError("Invalid! Email must contain '@'")
            self.email = value #Assigns valid email to person

        def __str__(self): # allows object to be coverted to a readable string
            return f"{self.name} <{self.email}>"
