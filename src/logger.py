import logging 
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # this create the file format 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # this put the files in the log folder 
os.makedirs(logs_path,exist_ok=True) # this appends the files in that folder 

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level = logging.INFO,
)
