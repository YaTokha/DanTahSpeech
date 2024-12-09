import os

from app.models.transcriber import Transcriber
from app.models.preprocess import Preprocess
from app.utils import check_file_exists, create_temp_dir, clean_up_directory
from config import TEMP_DIR, LOGGING_LEVEL, PROCESSED_DIR
import logging

# Настройка логирования
logging.basicConfig(
    level=LOGGING_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")]
)

def save_text_to_file(text, output_dir, filename):
    """
    Сохраняет текст в файл в указанной директории.
    :param text: Текст для сохранения.
    :param output_dir: Папка для сохранения файла.
    :param filename: Имя файла.
    """
    os.makedirs(output_dir, exist_ok=True)  # Создание папки, если она не существует
    file_path = os.path.join(output_dir, f"{filename}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    logging.info(f"Текст успешно сохранён в файл: {file_path}")
    return file_path


def main():
    # Приветствие
    print("Добро пожаловать в DanTahSpeech! Преобразование аудио в текст.")

    # Ввод пути к аудиофайлу
    file_path = input("Введите путь к вашему аудиофайлу (MP3, WAV, FLAC): ").strip()
    print(f"Вы указали файл: {file_path}")

    # Проверка существования файла
    if not check_file_exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    # Создание временной директории для обработки
    temp_dir = create_temp_dir(TEMP_DIR)

    # Инициализация предобработки
    preprocessor = Preprocess()
    try:
        # Шаг 1: Предобработка аудио
        print("Предобработка аудиофайла...")
        processed_audio = preprocessor.preprocess_audio(file_path, temp_dir)
        print(f"Аудиофайл после обработки сохранен по пути: {processed_audio}")
    except Exception as e:
        logging.error(f"Ошибка при предобработке: {e}")
        clean_up_directory(temp_dir)
        return

    # Инициализация транскрибера
    transcriber = Transcriber()

    try:
        # Шаг 2: Преобразование аудио в текст
        print("Начинаем распознавание речи...")
        text = transcriber.transcribe_audio(processed_audio)
        print("Распознанный текст:")
        print(text)

        # Шаг 3: Сохранение текста в файл
        filename = os.path.splitext(os.path.basename(file_path))[0]  # Имя файла без расширения
        output_path = save_text_to_file(text, PROCESSED_DIR, filename)
        print(f"Распознанный текст сохранён в файл: {output_path}")
    except Exception as e:
        logging.error(f"Ошибка при распознавании речи: {e}")
        clean_up_directory(temp_dir)
        return

    # Шаг 4: Очистка временных файлов
    clean_up_directory(temp_dir)

    # Завершение
    print("Обработка завершена. Проверьте папку processed для сохраненного текста.")


if __name__ == "__main__":
    main()
