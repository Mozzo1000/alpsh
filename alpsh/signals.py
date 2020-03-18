import signal
import logging

logger = logging.getLogger(__name__)


def handle_interrupt(signumber, frame):
    logger.debug('SIGINT signal caught.')
    return signumber, frame


def register_signals():
    signal.signal(signal.SIGINT, handle_interrupt)
