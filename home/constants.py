from os import path


HOME_DIRECTORY = path.expanduser('~')

if not (path.exists(HOME_DIRECTORY) and path.isdir(HOME_DIRECTORY)):
    raise Exception('Home directory doesnt exists')

DOWNLOADS_DIRECTORY = path.join(HOME_DIRECTORY, 'Downloads')

if not (path.exists(DOWNLOADS_DIRECTORY) and path.isdir(DOWNLOADS_DIRECTORY)):
    raise Exception('Downloads directory doesnt exists')

DROPBOX_DIRECTORY = path.join(HOME_DIRECTORY, 'Dropbox')

if not (path.exists(DROPBOX_DIRECTORY) and path.isdir(DROPBOX_DIRECTORY)):
    raise Exception('Dropbox directory doesnt exists')
