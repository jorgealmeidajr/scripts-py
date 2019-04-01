import argparse

import home.commands as home_commands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--command", required=True,
                    help="Command to execute")
    args = vars(ap.parse_args())

    print(f"Command to execute: {args['command']}")

    # home_commands.print_home_commands()
    if args['command'] == 'mv-tutorials-to-dropbox':
        home_commands.mv_tutorials_to_dropbox()

    elif args['command'] == 'cp-bashrc-to-dropbox':
        home_commands.cp_bashrc_to_dropbox()

    else:
        print(f"Command: {args['command']} is not supported")


if __name__ == "__main__":
    main()
