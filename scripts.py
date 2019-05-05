import argparse

import home.commands as home_commands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--command", required=True, help="Command to execute")
    args = vars(ap.parse_args())

    print(f"Command to execute: {args['command']}")

    if args['command'] == 'mv-tutorials-to-dropbox':
        home_commands.mv_tutorials_to_dropbox()

    elif args['command'] == 'cp-bashrc-to-dropbox':
        home_commands.cp_bashrc_to_dropbox()

    elif args['command'] == 'cp-codenation-projects-to-dropbox':
        home_commands.cp_codenation_projects_to_dropbox()

    elif args['command'] == 'git-status-workspace':
        home_commands.git_status_workspace()

    else:
        print(f"Command: {args['command']} is not supported")


if __name__ == "__main__":
    main()
