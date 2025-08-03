"""
url:
"""

import logging
import os
from datetime import datetime

# Properly format timestamp for filename (remove illegal characters like colons)
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create a logs folder and the full path to the log file
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Create directory if it doesn't exist
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    level=logging.INFO
)

# Example usage
logging.info("Logging system initialized successfully.")




