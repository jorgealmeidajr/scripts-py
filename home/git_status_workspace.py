import sys
import subprocess
from pathlib import Path


def print_git_status_workspace():
    print("INFO: The command 'git_status_workspace' started\n")
    check_pre_conditions()

    workspace_dir = Path.home() / 'Workspace'
    dirs = [d for d in workspace_dir.iterdir() if d.is_dir()]

    for project_dir in dirs:
        cwd = str(project_dir)
        print("#" * 60)
        print("=> " + cwd)
        subprocess.call("git status", cwd=cwd, shell=True)
        print("\n")

    check_post_conditions()
    print("INFO: The command 'git_status_workspace' ended its execution")


def check_pre_conditions():
    workspace_dir = Path.home() / 'Workspace'

    if not (workspace_dir.exists() and workspace_dir.is_dir()):
        sys.exit('The required "Workspace" directory does not exist')


def check_post_conditions():
    pass
