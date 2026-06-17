"""Project Management CLI - Final version"""
import click
from rich.console import Console
from rich.table import Table
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_data, save_data

console = Console()
DATA = load_data()

@click.group()
def cli():
    """Manage users, projects and tasks from the command line"""
    pass

@cli.command()
@click.option("--name", prompt="User name")
@click.option("--email", prompt="Email")
def add_user(name, email):
    """Add a new user"""
    try:
        user = User(name, email)
        DATA["users"].append(user)
        save_data(DATA)
        console.print(f"[green]✓ User added:[/green] {user}")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")

@cli.command()
def list_users():
    """Display all users"""
    if not DATA["users"]:
        console.print("[yellow]No users found[/yellow]")
        return
    
    table = Table(title="All Users")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email")
    table.add_column("Projects", justify="right")
    
    for user in DATA["users"]:
        table.add_row(str(user.id), user.name, user.email, str(len(user.projects)))
    console.print(table)

@cli.command()
@click.option("--title", prompt="Project title")
@click.option("--desc", prompt="Description")
@click.option("--due", prompt="Due date YYYY-MM-DD")
@click.option("--user-id", type=int, prompt="Owner user ID")
def add_project(title, desc, due, user_id):
    """Add a new project"""
    user = next((u for u in DATA["users"] if u.id == user_id), None)
    if not user:
        console.print(f"[red]Error:[/red] User ID {user_id} not found")
        return
    
    try:
        project = Project(title, desc, due, user_id)
        user.add_project(project)
        DATA["projects"].append(project)
        save_data(DATA)
        console.print(f"[green]✓ Project added:[/green] {project}")
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")

@cli.command()
@click.option("--project-id", type=int, prompt="Project ID")
@click.option("--title", prompt="Task title")
def add_task(project_id, title):
    """Add a new task"""
    project = next((p for p in DATA["projects"] if p.id == project_id), None)
    if not project:
        console.print(f"[red]Error:[/red] Project ID {project_id} not found")
        return
    
    task = Task(title, project_id)
    project.add_task(task)
    DATA["tasks"].append(task)
    save_data(DATA)
    console.print(f"[green]✓ Task added:[/green] {task}")

@cli.command()
@click.option("--project-id", type=int, default=None)
def list_tasks(project_id):
    """Display all tasks"""
    tasks = DATA["tasks"] if project_id is None else [t for t in DATA["tasks"] if t.project_id == project_id]
    
    if not tasks:
        console.print("[yellow]No tasks found[/yellow]")
        return
    
    table = Table(title="All Tasks" if project_id is None else f"Tasks for Project {project_id}")
    table.add_column("ID", style="cyan")
    table.add_column("Title")
    table.add_column("Status")
    table.add_column("Project ID", justify="right")
    
    for task in tasks:
        status_style = {"todo": "dim", "doing": "yellow", "done": "green"}[task.status]
        table.add_row(str(task.id), task.title, f"[{status_style}]{task.status}[/{status_style}]", str(task.project_id))
    console.print(table)

@cli.command()
def list_all():
    """Show everything - good for demo"""
    console.print("\n[bold blue]=== USERS ===[/bold blue]")
    list_users.callback()
    
    console.print("\n[bold blue]=== PROJECTS ===[/bold blue]")
    if DATA["projects"]:
        table = Table()
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Due")
        table.add_column("Owner ID")
        table.add_column("Status")
        for p in DATA["projects"]:
            status = "OVERDUE" if p.is_overdue else "Active"
            style = "red" if p.is_overdue else "green"
            table.add_row(str(p.id), p.title, p.due_date_str, str(p.user_id), f"[{style}]{status}[/{style}]")
        console.print(table)
    else:
        console.print("[yellow]No projects[/yellow]")
    
    console.print("\n[bold blue]=== TASKS ===[/bold blue]")
    list_tasks.callback(project_id=None)

if __name__ == "__main__":
    cli()