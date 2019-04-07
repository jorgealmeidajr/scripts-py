import os
import sys
from datetime import date
from pathlib import Path
import shutil

import home.constants as constants


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


def cp_bashrc_to_dropbox():
    bashrc_src = Path.home() / '.bashrc'

    if bashrc_src.exists() and bashrc_src.is_file():
        today = date.today().strftime("%Y%m%d")
        new_file_name = f"{bashrc_src.stem}-{today}"

        destination = Path.home() / 'Dropbox' / 'workspace-db' / 'home-ubuntu'

        if destination.exists() and destination.is_dir():
            final_dst = destination / new_file_name
            shutil.copy(bashrc_src, final_dst)
            print('The file .bashrc was copied with success')


def cp_codenation_projects_to_dropbox():
    codenation_dir = Path.home() / 'codenation'
    dropbox_destin_dir = constants.DROPBOX_DIRECTORY / 'workspace-db' / 'home-projects' / '2019'

    if not (codenation_dir.exists() and codenation_dir.is_dir()):
        sys.exit('The required "codenation" directory does not exist')

    if not (dropbox_destin_dir.exists() and dropbox_destin_dir.is_dir()):
        sys.exit('The required dropbox directory does not exist')

    subdirectories = [d for d in codenation_dir.iterdir() if d.is_dir()]

    for parent_directory in subdirectories:
        files_to_copy = []

        for (root, dirs, files) in os.walk(parent_directory):
            if not is_directory_to_ignore(root):
                print(f'root: {root}')
                end_index = len(str(parent_directory))
                current_dir = root[end_index:]

                for file in files:
                    print(f"file: {root}{os.sep}{file}")


def is_directory_to_ignore(path_str):
    patterns_to_ignore = [
        f'{os.sep}node_modules',
        f'{os.sep}.git'
    ]

    for pattern in patterns_to_ignore:
        if path_str.find(pattern) != -1:
            return True

    return False
