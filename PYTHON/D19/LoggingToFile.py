# Logging to a File (Instead of Console)

import logging

# Configure logging to write into a file instead of the console
logging.basicConfig(
    filename='app.log',
    filemode='w',  # 'w' overwrites the file each time you run; use 'a' to append
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Application started. This message goes directly into 'app.log'.")

try:
    # Intentionally trigger an error
    result = 10 / 0
except ZeroDivisionError:
    # exc_info=True automatically appends the full Python traceback to the log file
    logging.error("An unhandled exception occurred during calculation.", exc_info=True)

logging.info("Application shutting down.")

print("Logs have been successfully written to 'app.log'. Check your project folder!")