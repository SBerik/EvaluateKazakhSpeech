import os
import matplotlib.pyplot as plt

# Нужно указать полное место файла
def renameFile(old_name: str, new_name: str) -> bool:
    if not os.path.exists(old_name):
        print(f"Файл '{old_name}' не существует.")
        return False
    if os.path.exists(new_name):
        print(f"Файл '{new_name}' уже существует. Выберите другое имя.")
        return
    os.rename(old_name, new_name)
    print(f'Файл успешно переименован с {old_name} на {new_name}')
    return True

# renameFile("drive/MyDrive/Colab Notebooks/hello-91045.mp3", 'drive/MyDrive/Colab Notebooks/hello-word.mp3')

def plotG(time, y, title = ''):
    plt.figure(figsize=(10, 4))
    plt.plot(time, y, color='b')
    plt.title(f'{title}')
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')
    plt.grid(True)
    plt.show()


def signalsToSpeech(signals, name: str) -> str:
    root = '/content/drive/MyDrive/Colab Notebooks/Diploma/audio'
    output_file_flac = root + name
    sf.write(output_file_flac, signals, sr, format='flac')
    return name