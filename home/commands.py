import os

import home.constants as constants


def print_home_commands():
    pass


def mv_tutorials_to_dropbox():
    tutorials_path = os.path.join(constants.DOWNLOADS_DIRECTORY, 'tutorials')
    files = []

    with os.scandir(tutorials_path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry)
