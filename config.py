import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")
PROCESSED_DIR = os.path.join(BASE_DIR, "processed")
DATA_DIR = os.path.join(BASE_DIR, "data")

MODEL_NAME = "base"

SUPPORTED_FORMATS = [".mp3", ".wav", ".flac"]

NOISE_REDUCTION = True
MAX_AUDIO_DURATION = 3600

LOGGING_LEVEL = "INFO"

LOGGING_HANDLERS = [
    "logging.StreamHandler()",
    "logging.FileHandler('app.log')"
]

FFMPEG_PATH = "/usr/bin/ffmpeg"

DEBUG = True
