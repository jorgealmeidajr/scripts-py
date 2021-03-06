import os
import sys
from datetime import date
from pathlib import Path
import shutil

import home.constants as constants
from common.files import PatternsToIgnore


def copy_codenation_projects_to_dropbox():
    codenation_dir = Path.home() / 'codenation'
    dropbox_destin_dir = constants.DROPBOX_DIRECTORY / 'workspace-db' / 'home-projects' / '2019'

    if not (codenation_dir.exists() and codenation_dir.is_dir()):
        sys.exit('The required "codenation" directory does not exist')

    if not (dropbox_destin_dir.exists() and dropbox_destin_dir.is_dir()):
        sys.exit('The required "dropbox" directory does not exist')

    patterns_to_ignore = PatternsToIgnore()
    subdirectories = [d for d in codenation_dir.iterdir() if d.is_dir()]

    for parent_directory in subdirectories:
        path_end_name = parent_directory.parts[-1]
        today = date.today().strftime("%Y%m%d")
        destin_name = f"{path_end_name}-{today}"

        destin_final = dropbox_destin_dir / destin_name
        destin_final_path = Path(destin_final)
        if not destin_final_path.exists():
            destin_final_path.mkdir()

        files_to_copy = []
        end_index = len(str(parent_directory))

        for (root, dirs, files) in os.walk(parent_directory):
            if not patterns_to_ignore.is_path_to_ignore(root):
                print(root)
                current_dir = root[end_index:]

                for file in files:
                    file_name = Path(file).name
                    file_to_copy = {}

                    if current_dir == '':
                        file_to_copy = {
                            "origin": Path(f"{root}{os.sep}{file}"),
                            "destin": Path(f"{destin_final}{os.sep}{current_dir}{file_name}")
                        }
                    else:
                        file_to_copy = {
                            "origin": Path(f"{root}{os.sep}{file}"),
                            "destin": Path(f"{destin_final}{current_dir}{os.sep}{file_name}")
                        }

                        destin_path = Path(f"{destin_final}{current_dir}")
                        if not destin_path.exists():
                            destin_path.mkdir()

                    files_to_copy.append(file_to_copy)

        for file in files_to_copy:
            origin_path = file["origin"]
            destin_path = file["destin"]

            shutil.copy(str(origin_path), str(destin_path))

            if not (origin_path.exists() or destin_path.exists()):
                sys.exit('The origin and destin file must exist')

            if origin_path.stat().st_size != destin_path.stat().st_size:
                sys.exit('The origin and destin file must have the same size')

    print("The command 'cp-codenation-projects-to-dropbox' ended its execution")
