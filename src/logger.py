from datetime import datetime
from pathlib import Path

import logger

LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOGS_DIR / f'{datetime.now().strftime("%Y- %m- %d   %H: %M: %S")}.log'
