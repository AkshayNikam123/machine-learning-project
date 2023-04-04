import logging
from datetime import datetime
import os



LOG_DIR="housing_logs" #all logs store in directory logs 
current_time_stamp=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"  #format for datetime


LOG_FILE_NAME=f"log_{current_time_stamp}.log"

os.makedirs(LOG_DIR,exist_ok=True) #exist ok just to run when it is available 

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)


logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',
level=logging.INFO
)



    
 