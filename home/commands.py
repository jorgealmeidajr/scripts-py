import os
import shutil

import home.constants as constants


def print_home_commands():
    pass


def mv_tutorials_to_dropbox():
    tutorials_path = os.path.join(constants.DOWNLOADS_DIRECTORY, 'tutorials')
    extensions = ['.pdf']
    files = []

    with os.scandir(tutorials_path) as entries:
        for entry in entries:
            if entry.is_file():
                name, ext = os.path.splitext(entry.path)
                if ext in extensions:
                    files.append({
                        "path": entry.path,
                        "name": entry.name
                    })

    if len(files) > 0:
        print('There are files to be moved from Downloads to Dropbox')
        print('Moving files...')

        destination = os.path.join(constants.DROPBOX_DIRECTORY, 'tutorials')

        for file in files:
            shutil.move(file['path'], destination)

        print('Files moved with success!')

    else:
        print('There are not files to be moved')
