# Project Management CLI Tool
This is a command-line application for managing projects and tasks. 
It allows an administrator to create users, assign projects to those users, and organise each project into individual tasks. 
All data is stored in a local JSON file, so information is preserved between sessions without requiring a database.

# Features

* Create and manage users.
* Assign projects to users.
* Create tasks within projects.
* Mark tasks as completed.
* View all projects or projects assigned to a specific user.
* Persist application data using a local JSON file.

# Project Structure
project_management_cli/
├── main.py                 # CLI entry point
├── models/
│   ├── person.py           # Base class for User
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   └── file_io.py          # JSON save/load functions
├── data/
│   └── data.json           # Persistent application data
├── tests/
│   └── test_models.py
├── Pipfile
├── Pipfile.lock
└── requirements.txt 

### Data Model
* A **User** owns one or more **Projects**.
* Each **Project** contains one or more **Tasks**.
* Relationships between users, projects, and tasks are created automatically when new records are added through the CLI.

# Prerequisites
Before running the project, ensure you have the following installed:

* **Python 3.x**
* **Pipenv**

If Pipenv is not already installed:

```bash
pip install pipenv
```

# Installation
Clone the repository and create the virtual environment:

```bash
git clone https://github.com/Eddie-Njeru1/PYTHON-Mod4-Summative-Lab-2-Project-Management-CLI-Tool.git
cd PYTHON-Mod4-Summative-Lab-2-Project-Management-CLI-Tool
pipenv install --dev
pipenv shell
```
The **Pipfile** defines the project's dependencies, while **Pipfile.lock** ensures consistent package versions across different development environments.

# Dependencies

## Runtime Dependency

### **rich**

Used to provide formatted console output and display project information in tables. Install manually if needed:

```bash
pipenv install rich
```
## Development Dependency

### **pytest**

Used for running the project's automated test suite. Install manually if needed:

```bash
pipenv install --dev pytest
```
 **Note:** A `requirements.txt` file is included for environments that use `pip`. It contains only the runtime dependencies, while development dependencies remain managed through Pipenv.

# Running the Application

Run all commands from the project root directory.
**Note:**For testing purposes, there is a placeholder user named "Eddie" with corresponding email, date, tasks, projects, etc. Adjust with new data to add new user

## Create a User

```bash
python main.py add-user --name "Eddie" --email "eddie@email.com"
```

## Create a Project

```bash
python main.py add-project \
    --user "Eddie" \
    --title "CLI Tool" \
    --description "Build the tool" \
    --due-date "2026-08-01"
```

## Create a Task

```bash
python main.py add-task \
    --project "CLI Tool" \
    --title "Implement add-task" \
    --status "pending" \
    --assigned-to "Eddie"
```

## Mark a Task as Complete

```bash
python main.py complete-task --title "Implement add-task"
```

## View Projects

Display all projects:

```bash
python main.py list-projects
```

Display projects for a specific user:

```bash
python main.py list-projects --user "Eddie"
```
**Note:** Users and projects must exist before they can be referenced. If a requested user or project cannot be found, the application displays an error message instead of terminating unexpectedly.

# Running the Tests

Execute the test suite with:

```bash
pipenv run python -m pytest tests/
```

The tests verify:

* Email validation for users.
* Relationships between users, projects, and tasks.
* Task completion behaviour.
* Saving and loading application data from JSON.

# Current Limitations
The current version intentionally keeps the feature set simple.

* Users, projects, and tasks cannot be edited or deleted after they are created.
* Only projects can be listed. There are currently no `list-users` or `list-tasks` commands.
* Projects and tasks are identified by their titles, so duplicate titles may produce unexpected results.
* Validation is intentionally minimal, with basic checks for email format and required fields.

# Author
Eddie Njeru

