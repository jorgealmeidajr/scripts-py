import sys
import subprocess
from pathlib import Path


# TODO: this script freezes, and don't execute
def execute_git_push_workspace():
    print("INFO: The command 'git_push_workspace' started\n")
    check_pre_conditions()

    workspace_dir = Path.home() / 'Workspace'
    dirs = [d for d in workspace_dir.iterdir() if d.is_dir()]

    try:
        for project_dir in dirs:
            cwd = str(project_dir)
            print("#" * 60)
            print("PROJECT => " + cwd)
            subprocess.call("git push origin master", cwd=cwd, shell=True)
            print("\n")
    except:
        print("The exception: ", sys.exc_info()[0], "occured.")

    check_post_conditions()
    print("INFO: The command 'git_push_workspace' ended its execution")


def check_pre_conditions():
    workspace_dir = Path.home() / 'Workspace'

    if not (workspace_dir.exists() and workspace_dir.is_dir()):
        sys.exit('The required "Workspace" directory does not exist')


def check_post_conditions():
    pass
