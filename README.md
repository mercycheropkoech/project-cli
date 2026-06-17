#  Project CLI 

A simple Command-Line Interface (CLI) project management tool built in Python. It allows users to manage users, projects, and tasks with persistent JSON storage.


## Features

- Add users with email validation  
- Create and manage projects  
- Add tasks linked to projects  
- View users, projects, and tasks  
- Track overdue projects  
- Persistent storage using `data.json`  
- Clean terminal UI using `rich`  
- ⚡ Fast CLI powered by `click`


## 🛠 Tech Stack

- Python 3  
- Click (CLI framework)  
- Rich (terminal formatting)  
- Python-dateutil (date handling)  
- JSON (data storage)



## Project Structure

project-cli/
├── main.py
├── data.json
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── utils/
│   ├── __init__.py
│   └── file_io.py
│
├── tests/
│   ├── test_user.py
│   └── test_project.py
│
└── venv/



## Installation

### 1. Clone the repository
git clone https://github.com/mercycheropkoech/project-cli.git
cd project-cli

# Author
Mercy cherop