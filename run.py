from app.models.transcriber import Transcriber
from app.models.preprocess import Preprocess
from app.utils import check_file_exists, create_temp_dir, clean_up_directory
from config import TEMP_DIR, LOGGING_LEVEL
import logging

logging.basicConfig(
    level=LOGGING_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")]
)

def main():
    print("Добро пожаловать в DanTahSpeech! Преобразование аудио в текст.")
    file_path = input("Введите путь к вашему аудиофайлу: ").strip()
    print(f"Вы указали файл: {file_path}")

    if not check_file_exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    print("Файл найден. Начинается предобработка...")

    temp_dir = create_temp_dir(TEMP_DIR)

    preprocessor = Preprocess()
    try:
        print("Предобработка аудиофайла...")
        processed_audio = preprocessor.preprocess_audio(file_path, temp_dir)
        print(f"Аудиофайл после обработки сохранен по пути: {processed_audio}")
    except Exception as e:
        logging.error(f"Ошибка при предобработке: {e}")
        clean_up_directory(temp_dir)
        return

    transcriber = Transcriber()

    try:
        print("Начинаем распознавание речи...")
        text = transcriber.transcribe_audio(processed_audio)
        print("Распознанный текст:")
        print(text)
    except Exception as e:
        logging.error(f"Ошибка при распознавании речи: {e}")
        clean_up_directory(temp_dir)
        return

    clean_up_directory(temp_dir)

    print("Обработка завершена.")

if __name__ == "__main__":
    main()
