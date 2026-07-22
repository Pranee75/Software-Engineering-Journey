# Using Different Log Levels


import logging

# Configure logger to show all levels from DEBUG upwards
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def process_data():
    # 1. DEBUG: Detailed diagnostic info (useful only during development)
    logging.debug("Starting to process data array of length 5.")

    # 2. INFO: Confirmation that things are running normally
    logging.info("Data processing completed successfully.")

    # 3. WARNING: Something unexpected happened, but the program still works
    logging.warning("Disk space is running low (under 10% remaining).")

    # 4. ERROR: A serious problem occurred; a specific function failed
    logging.error("Failed to connect to the database. Retrying...")

    # 5. CRITICAL: A severe error causing the application to crash or halt
    logging.critical("System overheating! Shutting down server immediately.")

if __name__ == "__main__":
    process_data()