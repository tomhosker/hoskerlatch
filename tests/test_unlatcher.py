"""
This code tests the Unlatcher class.
"""

# Standard imports.
import shutil
from pathlib import Path

# Source imports.
from source import latch, unlatch
from source.latcher import SALT_FILENAME

###########
# TESTING #
###########

def test_unlatcher():
    """ Test that the Unlatcher can unlatch a folder latched by the Latcher. """
    # Set up.
    test_dirname = "test_folder"
    test_filename = "smeg"
    password = "password"
    path_obj_to_test_folder = Path(test_dirname)
    path_obj_to_test_folder.mkdir()
    (path_obj_to_test_folder/test_filename).touch()
    # Run latch().
    path_to_encrypted = latch(test_dirname, password)
    path_obj_to_encrypted = Path(path_to_encrypted)
    # Check latch() has done its job.
    assert path_obj_to_encrypted.exists()
    assert not path_obj_to_test_folder.exists()
    # Run unlatch().
    path_to_decrypted = unlatch(path_to_encrypted, password)
    path_obj_to_decrypted = Path(path_to_decrypted)
    # Assert.
    assert not path_obj_to_encrypted.exists()
    assert path_obj_to_decrypted.exists()
    assert (path_obj_to_decrypted/test_filename).exists()
    # Clean.
    shutil.rmtree(path_to_decrypted)
    Path(SALT_FILENAME).unlink()
