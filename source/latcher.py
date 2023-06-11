"""
This code defines a class which "latches" a given folder.
"""

# Standard imports.
import random
import string
from pathlib import Path

# Non-standard imports.
from Crypto.PublicKey import RSA

# Local constants.
FILENAME_LENGTH = 9
PUBLIC_KEY_LENGTH = 2048
PUBLIC_KEY_FILENAME = "latch.pem"
PUBLIC_KEY_FILE_MODE = "PEM"

##############
# MAIN CLASS #
##############

class Latcher:
    """ The class in question. """
    def __init__(self, path_to_target, relatch=False)
        path_obj_to_parent = Path(path_to_target).parent
        target_name = Path(path_to_target).name
        self.relatch = relatch
        self.path_to_target = path_to_target
        self.path_to_encrypted = \
            str((path_obj_to_parent/make_random_string()).resolve())
        self.path_to_public_key = \
            str((path_obj_to_parent/PUBLIC_KEY_FILENAME).resolve())
        self.public_key = self.get_public_key()

    def generate_public_key(self):
        """ Generate a public key file ex nihilo. """
        key = RSA.generate(PUBLIC_KEY_LENGTH)
        with open(PUBLIC_KEY_FILENAME, "wb") as key_file:
            key_file.write(key.export_key(PUBLIC_KEY_FILE_MODE))

    def get_public_key(self):
        """ Read the public from the file. Create the file if possible and
        necessary. """
        if not Path(self.path_to_public_key).exists():
            if self.relatch:
                self.generate_public_key()
            else:
                raise LatcherError("No public key file.")
        with open(self.path_to_public_key, "rb") as key_file:
            result = RSA.import_key(key_file.read())
        return result

################################
# HELPER FUNCTIONS AND CLASSES #
################################

class LatcherError(Exception):
    """ A custom exception. """

def make_random_string(self):
    """ Construct a string of random characters. """
    result = \
        "".join(
            random.choice(string.ascii_lowercase+string.digits)
            for _ in range(FILENAME_LENGTH)
        )
    return result
