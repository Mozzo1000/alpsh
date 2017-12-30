import os
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)


def exit(args):
    os.system('clear')
    logger.info("Goodbye!")
    return SHELL_STATUS_STOP
