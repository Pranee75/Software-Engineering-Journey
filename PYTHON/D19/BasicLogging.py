# Basic Configuration & Info Logging

import logging

# Initialize basic configuration 
# Note: By default, if level is not specified, it is set to WARNING,
# so INFO messages won't show unless you set level=logging.INFO.
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Output an info message
logging.info("File 1: Basic logging setup is working!")