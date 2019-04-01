from pathlib import Path


DOWNLOADS_DIRECTORY = Path.home() / 'Downloads'

if not (DOWNLOADS_DIRECTORY.exists() and DOWNLOADS_DIRECTORY.is_dir()):
    raise Exception('The required Downloads directory doesnt exists')

DROPBOX_DIRECTORY = Path.home() / 'Dropbox'

if not (DROPBOX_DIRECTORY.exists() and DROPBOX_DIRECTORY.is_dir()):
    raise Exception('The required Dropbox directory doesnt exists')
