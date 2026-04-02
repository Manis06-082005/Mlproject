import os
import logging 
from datetime import datetime
log_dir='logs'
file_name=f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
log_dir_path=os.path.join(os.getcwd(), log_dir)
os.makedirs(log_dir_path, exist_ok=True)
log_file_path=os.path.join(log_dir_path,file_name)
logging.basicConfig(
    filename=log_file_path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


