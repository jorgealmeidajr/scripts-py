import os
from datetime import date
from pathlib import Path
import shutil

import home.constants as constants

from home.cp_codenation_projects_to_dropbox import copy_codenation_projects_to_dropbox
from home.git_status_workspace import print_git_status_workspace
from home.git_push_workspace import execute_git_push_workspace


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
    copy_codenation_projects_to_dropbox()


def git_status_workspace():
    print_git_status_workspace()


def git_push_workspace():
    execute_git_push_workspace()
