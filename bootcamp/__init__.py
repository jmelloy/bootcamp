__version__ = "2.1.1"
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)

import os
PHOTOLOGUE_APP_DIR = os.path.dirname(os.path.abspath(__file__))
