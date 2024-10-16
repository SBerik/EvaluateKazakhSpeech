import IPython.display as ipd
import librosa

class Audio:
    def __init__(self, audio_path: str = '', text_path: str = ''):
        root = '/content/drive/MyDrive/Colab Notebooks/Diploma/audio'
        self.path_to_audio = root + audio_path
        self.path_to_text = text_path

    def getSound(self, play: bool = True) -> None:
        try:
            audio, sr = librosa.load(self.path_to_audio, sr=None)
            if play:
                ipd.display(ipd.Audio(audio, rate=sr, autoplay=True))
            else:
                ipd.display(ipd.Audio(audio, rate=sr))
        except Exception as e:
            print(f"Ошибка при загрузке или воспроизведении аудио: {e}")

    def readText(self) -> str:
        with open('drive/MyDrive/Colab Notebooks/Diploma/audio' + self.path_to_text, 'r') as file:
            file_contents = file.read()
        return file_contents