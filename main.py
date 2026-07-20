
#Import libraries, models and utils
import argparse #module for parsing command-line arguments and options.
from rich.console import Console #For formatted terminal output
from rich.table import Table
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import save_data, load_data

DATA_FILE = "data/data.json" #Path to application's data file
console = Console() #Rich console object to display formatted output

def add_user(args): #Create new user
    try:
        user = User(args.name, args.email) #New User object
        console.print(f"Created user: {user}")
    except ValueError as e: #Handle error
        console.print(f"Error!: {e}.")

def add_project(args): #Create new project
    user = User.find_by_name(args.user) #Find user who owns project
    if not user:
        console.print(f"Error!: '{args.user}' not found.")
        return 
    project = Project(args.title, args.description, args.due_date, user) #New proect object
    console.print(f"Created project: {project}.")

def add_task(args): #Create new task
    project = Project.find_by_title(args.project) #Find the project which the task belons to
    if not project:
        console.print(f"Error!: project '{args.project}' not found")
        return
    task = Task(args.title, args.status, args.assigned_to, project) #new task object
    console.print(f"Created task: {task}.")

def complete_task(args): #Mark task as completed
    task = Task.find_by_title(args.title) #finf task by title
    if not task:
        console.print(f"Error!: task '{args.title}' not found.")
        return
    task.complete() #update status
    console.print(f"Marked complete: {task}.")

def list_projects(args): #Show project list
    projects = Project.get_all() #get all projects
    if args.user: #filter by user using available username
        project = [p for p in projects if p.owner.name == args.user]
    table = Table(title="Projects") #Create table to show project details
    table.add_column("ID"); table.add_column("Tasks") #add columns
    for project in projects:#add each project's detail to table 
        table.add_row(str(project.id), project.title, project.owner.name, project.due_date, str(len(project.tasks)))
    console.print(table)

def build_parser(): # Build the CLI argument parser
    parser = argparse.ArgumentParser(description="Project Management CLI") #Main parser
    subparsers = parser.add_subparsers(dest="command", required=True) #Sub parser commands

    #Define add_user commands
    p= subparsers.add_parser("add-user")
    p.add_argument("--name", required=True); p.add_argument("--email", required=True)
    p.set_defaults(func=add_user)

    #Define add_project commands
    p= subparsers.add_parser("add-project")
    p.add_argument("--user", required=True); p.add_argument("--title", required=True)
    p.add_argument("--description", required=True); p.add_argument("--due-date", dest="due_date", required=True)
    p.set_defaults(func=add_project)

    #Define add_task commands
    p= subparsers.add_parser("add-task")
    p.add_argument("--project", required=True); p.add_argument("--title", required=True)
    p.add_argument("--status", required=True); p.add_argument("--assigned-to", dest="assigned_to", required=True)
    p.set_defaults(func=add_task)
    
    #Define complete_task commands
    p= subparsers.add_parser("complete-task")
    p.add_argument("--title", required=True)
    p.set_defaults(func=complete_task)
    
    #Define list_projects commands
    p= subparsers.add_parser("list-projects")
    p.add_argument("--user", required=False)
    p.set_defaults(func=list_projects)
    return parser #Return completed parser

def main(): #To run the CLI
    load_data(DATA_FILE) #Load saved data 
    parser = build_parser() #Build CLI parser
    args= parser.parse_args() #Read CLI arguments
    args.func(args) #Execute command 
    save_data(DATA_FILE) #save updated data 

if __name__ == "__main__": #Run the program only when file is executed directly.
    main()


    








            

