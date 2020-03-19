import os
import sys
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)


def reload(args):
    logger.debug('Reloading shell')
    os.execv(sys.executable, ['python'] + sys.argv)
    return SHELL_STATUS_STOP
