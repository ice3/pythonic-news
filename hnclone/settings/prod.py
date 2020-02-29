import os
from hnclone.settings.base import *

debug = False
STATIC_ROOT = os.path.join(BASE_DIR, "rendered", "static")
