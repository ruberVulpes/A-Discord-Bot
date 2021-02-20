import logging
import sys
from datetime import timedelta

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

anti_spam_wait_time = timedelta(hours=6)

from bot.bot import client
