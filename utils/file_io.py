import json
import os
from models.user import User
from models.project import Project
from models.task import Task

DATA_FILE = "data.json"

def load_data() -> dict:
   
    data = {"users": [], "projects": [], "tasks": []}
    
    try:
        if not os.path.exists(DATA_FILE):
            return data
            
        with open(DATA_FILE, "r") as f:
            raw_data = json.load(f)
        
        data["users"] = [User.from_dict(u) for u in raw_data.get("users", [])]
        data["projects"] = [Project.from_dict(p) for p in raw_data.get("projects", [])]
        data["tasks"] = [Task.from_dict(t) for t in raw_data.get("tasks", [])]
        
        _relink_data(data)
        
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:

        print(f"Warning: {DATA_FILE} is corrupted. Starting with empty data.")
        pass
    except Exception as e:

        print(f"Error loading data: {e}. Starting with empty data.")
        pass
        
    return data

def save_data(data: dict):
   
    try:
       
        raw_data = {
            "users": [u.to_dict() for u in data["users"]],
            "projects": [p.to_dict() for p in data["projects"]],
            "tasks": [t.to_dict() for t in data["tasks"]]
        }
        
        with open(DATA_FILE, "w") as f:
            json.dump(raw_data, f, indent=4)
            
    except IOError as e:
        print(f"Error: Could not save data to {DATA_FILE}. {e}")
        raise
    except Exception as e:
        print(f"Unexpected error saving data: {e}")
        raise

def _relink_data(data: dict):
    
    users_by_id = {u.id: u for u in data["users"]}
    projects_by_id = {p.id: p for p in data["projects"]}
    
    
    for task in data["tasks"]:
        if task.project_id in projects_by_id:
            projects_by_id[task.project_id].tasks.append(task)
    
    for project in data["projects"]:
        if project.user_id in users_by_id:
            users_by_id[project.user_id].projects.append(project)