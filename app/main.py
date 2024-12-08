from app.models.transcriber import Transcriber


def main():
    print("Добро пожаловать в DanTahSpeech!")
    file_path = input("Введите путь к аудиофайлу (MP3 или WAV): ").strip()

    try:
        transcriber = Transcriber(model_name="base")
        print("Обработка аудио...")
        text = transcriber.transcribe_audio(file_path)
        print("\nРаспознанный текст:\n")
        print(text)
    except Exception as e:
        print("Произошла ошибка:", e)


if __name__ == "__main__":
    main()
