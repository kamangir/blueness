from blueness import NAME, VERSION, DESCRIPTION, ICON
from blueness.argparse.version import main

success, message = main(NAME, VERSION, DESCRIPTION, ICON)
if not success:
    print(message)
