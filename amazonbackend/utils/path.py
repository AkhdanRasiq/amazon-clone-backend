import os
from pathlib import Path

SITE_ROOT          = os.path.realpath(os.path.dirname(__file__))
pathRootProject    = os.path.join(Path(SITE_ROOT).parent)
pathConfig         = os.path.join(pathRootProject, 'config', 'config.json')
