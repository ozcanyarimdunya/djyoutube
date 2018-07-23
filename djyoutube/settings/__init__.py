from .base import *
from .common import *

DEBUG = True

if DEBUG:
    from .dev import *
else:
    from .prod import *
