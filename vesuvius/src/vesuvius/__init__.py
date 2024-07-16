import os
import sys
import site

from .volume import Volume, Cube
from .volume_2 import Volume2
from .paths.utils import update_list
from .paths.utils import list_files as list

__all__ = ["Volume", "Volume2", "Cube", "list"]

def check_agreement():
    install_path = site.getsitepackages()[-1]
    agreement_file_path = os.path.join(install_path, 'vesuvius', 'setup', 'agreement.txt')

    # Get the name of the currently running script
    current_script = os.path.abspath(sys.argv[0])

    # Check if the current script is not the setup script
    if not os.path.exists(agreement_file_path):
        if "accept_terms" not in current_script:
            raise ImportError("You must accept the terms and conditions before using this package. Run `vesuvius.accept_terms`.")
    else:   
        with open(agreement_file_path, 'r') as file:
            content = file.read().strip()
            if content != 'yes':
                raise ImportError("The agreement file is corrupted or incorrect. Please run `vesuvius.accept_terms` again.")

# Check agreement on import
check_agreement()

# Update list of files on import
try:
    update_list("https://registeredusers:only@dl.ash2txt.org/other/dev/")
except:
    print("Could not update the remote file paths.")