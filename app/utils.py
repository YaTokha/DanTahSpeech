import os
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

def check_file_exists(file_path: str) -> bool:

    if not os.path.exists(file_path):
        logging.error(f"Файл {file_path} не найден.")
        return False
    return True

def create_temp_dir(base_dir: str = "temp/") -> str:

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    temp_dir = os.path.join(base_dir, f"session_{timestamp}")
    os.makedirs(temp_dir, exist_ok=True)
    logging.info(f"Создана временная директория: {temp_dir}")
    return temp_dir

def clean_up_directory(dir_path: str):

    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(dir_path)
        logging.info(f"Удалена временная директория: {dir_path}")
    else:
        logging.warning(f"Директория {dir_path} не найдена. Удаление не требуется.")

def format_duration(seconds: float) -> str:

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"
