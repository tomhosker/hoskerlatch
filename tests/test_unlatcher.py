"""
This code tests the Unlatcher class.
"""

# Standard imports.
import shutil
from pathlib import Path

# Source imports.
from source.latcher import Latcher
from source.unlatcher import Unlatcher

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
    # Run latcher obj.
    latcher = Latcher(test_dirname, relatch=True)
    latcher.latch(password)
    path_obj_to_encrypted = Path(latcher.path_to_encrypted)
    # Check latcher obj has done its job.
    assert path_obj_to_encrypted.exists()
    assert not path_obj_to_test_folder.exists()
    # Run unlatcher obj.
    unlatcher = Unlatcher(latcher.path_to_encrypted, relatch=True)
    unlatcher.unlatch(password)
    path_obj_to_decrypted = Path(unlatcher.path_to_decrypted)
    # Assert.
    assert not path_obj_to_encrypted.exists()
    assert path_obj_to_decrypted.exists()
    assert (path_obj_to_decrypted/test_filename).exists()
    # Clean.
    shutil.rmtree(unlatcher.path_to_decrypted)
