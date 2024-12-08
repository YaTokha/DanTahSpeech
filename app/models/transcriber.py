import whisper

class Transcriber:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe_audio(self, file_path: str) -> str:
        if not file_path.endswith(('.mp3', '.wav')):
            raise ValueError("Поддерживаются только форматы MP3 и WAV.")
        result = self.model.transcribe(file_path)
        return result['text']
