
#Import pytest module and project modules to test
import pytest
from models.user import User
from models.project import Project
from models.task import Task

@pytest.fixture(autouse=True) #Reset model data beofre every test
def reset():
    User.all_users = [] #clear stored users
    Project.all_projects = [] #clear stored projects
    Task.all_tasks = [] #clear stored tasks

def test_models():
    with pytest.raises(ValueError):
        User("Sam", "bad-email")
#create test user, project and task
    user = User("Eddie", "eddie@email.com")
    project = Project("CLI Tool", "desc", "20-07-2026", user)
    task = Task("Implement add-task", "pending", "Eddie", project)

    assert project in user.projects and task in project.tasks #ensure project belongs to user and task belongs to project
    task.complete() 
    assert task.status == "complete" #ensure task was updated
    assert User.from_dict(user.to_dict()).projects[0].title == "CLI Tool" #ensure that user can be converted to dictionary and restored correctly

