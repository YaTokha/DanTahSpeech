import unittest
from app.models.transcriber import Transcriber

class TestTranscriber(unittest.TestCase):
    def setUp(self):
        self.transcriber = Transcriber(model_name="tiny")

    def test_transcribe_audio(self):
        result = self.transcriber.transcribe_audio("data/example_audio.wav")
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

if __name__ == "__main__":
    unittest.main()
