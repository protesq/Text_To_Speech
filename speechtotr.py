from gtts import gTTS
import os

def text_to_speech(input_file, output_file, language='tr'):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read().replace('\n', ' ')
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)
        print(f"{output_file} dosyası oluşturuldu.")
    except Exception as e:
        print("Hata:", e)
if __name__ == "__main__":
    input_text_file = "metin.txt" 
    output_audio_file = "ses.mp3"  

    text_to_speech(input_text_file, output_audio_file)