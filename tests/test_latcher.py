"""
This code tests the Latcher class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from source import latch
from source.latcher import SALT_FILENAME

###########
# TESTING #
###########

def test_latcher():
    """ Test that the Latcher class can encrypt a given folder. """
    # Set up.
    test_dirname = "test_folder"
    test_filename = "smeg"
    password = "password"
    path_obj_to_test_folder = Path(test_dirname)
    path_obj_to_test_folder.mkdir()
    (path_obj_to_test_folder/test_filename).touch()
    # Run.
    path_to_encrypted = latch(test_dirname, password)
    path_obj_to_encrypted = Path(path_to_encrypted)
    # Assert.
    assert path_obj_to_encrypted.exists()
    assert not path_obj_to_test_folder.exists()
    # Clean.
    path_obj_to_encrypted.unlink()
    Path(SALT_FILENAME).unlink()
