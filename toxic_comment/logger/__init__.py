import logging
from datetime import datetime
import sys

TIMESTAMP = f'{datetime.now().strftime("%Y-%m-%d_%H-%M")}'

logging.basicConfig(
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
