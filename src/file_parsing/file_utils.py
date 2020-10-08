"""
   File and directory utils.
"""

import os

def check_directory(dirname):
    """Check if it is a directory, then further actions on the directory"""
    if not dirname or not os.path.exists(dirname) or not os.path.isdir(dirname):
        return False
    return True


def check_filename(filename):
    """Check the file if exists before any further operations on it"""
    if not filename or not os.path.exists(filename) or not os.path.isfile(filename):
        return False
    return True


def delete_file(filename):
    """Delete filename, not checking the existence of the file."""
    try:
        os.remove(filename)
    except:
        pass

def list_directory(foldername):
    """Lists Directory, not checking the existence of the directory"""
    try:
        return os.listdir(foldername)
    except:
        pass
    
def join_path(dirname, filename):
    """join one or more paths, not checking the existence of the directory and file"""
    try:
        return os.path.join(dirname, filename)
    except:
        pass

def write_file(contents, filename, overwrite=False):
    if not overwrite and check_filename(filename):
        return False

    if contents:
        with open(filename, 'w') as f:
            f.write(contents)
    return True
