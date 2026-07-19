
# Import JSON to save and laod data in JSON format
import json
from models.user import User

def save_data(filepath): #Save all data to a JSON file
    data = {"users": [u.to_dict() for u in User.get_all()]} #Convert users to dictinaries for saving
    try: 
        with open(filepath, "w") as f: #File will open in write mode
            json.dump(data, f, indent=2) #Write data to file in JSON
    except OSError as e: #Handle any error when saing file
        print(f"Error! Could not save data: {e}")

def load_data(filepath):  #Load data from a JSON file
    try:
        with open(filepath, "r") as f: #Read and convert JSON data to Python object
            data = json.load(f)
    except FileNotFoundError: #Handle any error when file is absent
        return
    except json.JSONDecodeError: #Handle corrupted JSON data
        print(f"Error: {filepath} is corrupted, starting with empty data")
        return
    for user_data in data.get("users", []): #Recreate all users and their projects and tasks
        User.from_dict(user_data)
    