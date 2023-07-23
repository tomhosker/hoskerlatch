"""
This script installs any required software which cannot be installed
conveniently via SetUpTools.
"""

# Standard imports.
import subprocess
from pathlib import Path

# Local constants.
PATH_TO_INSTALL_SPECIALS_SHELL_SCRIPT = \
    Path(__file__).resolve().parent/"scripts"/"hoskerlatch-install-specials"

###################
# RUN AND WRAP UP #
###################

def run():
    """ Run this file. """
    subprocess.run(["sh", PATH_TO_INSTALL_SPECIALS_SHELL_SCRIPT], check=True)

if __name__ == "__main__":
    run()
