import os
from pathlib import Path

def create_file_system():
    """
    Create a file system structure for a data science, machine learning, or AI project.
    """
    # Get the current directory where the script is located
    script_directory = Path(__file__).resolve().parent

    # Get project name from user input
    project_name = input("Enter your project name: ")

    # Directory structure for a typical ML/AI project
    directories = [
        project_name,
        f"{project_name}/data/raw",
        f"{project_name}/data/processed",
        f"{project_name}/data/external",
        f"{project_name}/models",
        f"{project_name}/notebooks",
        f"{project_name}/scripts",
        f"{project_name}/src/__init__.py",
        f"{project_name}/src/utils",
        f"{project_name}/src/models",
        f"{project_name}/src/preprocessing",
        f"{project_name}/src/visualization",
        f"{project_name}/config/__init__.py",
        f"{project_name}/constants/__init__.py",
        f"{project_name}/reports",
        f"{project_name}/tests",
    ]

    # Create directories and __init__.py files
    for directory in directories:
        directory_path = script_directory / directory
        directory_path.mkdir(parents=True, exist_ok=True)
        # Create __init__.py files
        if "__init__.py" in directory:
            directory_path.joinpath("__init__.py").touch()

    print(f"File system structure for {project_name} created successfully!")

if __name__ == "__main__":
    create_file_system()
