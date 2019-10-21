import threading
import speech_recognition as sr
g_Radiator = False

def update_scheduler():
    global g_Radiator
    while True:

        r = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            audio = r.listen(source, timeout=5)

            try:
                command_text = r.recognize_google(audio, language="ko-KO")
                print("Transcription: " + command_text)
                if command_text != 'OK 구글':
                    continue
            except:
                pass

        try:
            while True:
                r = sr.Recognizer()
                mic = sr.Microphone()
                with mic as source:
                    audio = r.listen(source, timeout=5)
                    command_text = r.recognize_google(audio, language="ko-KO")
                    print("Transcription: " + command_text)
                    if command_text == '가습기 켜' and g_Radiator == False:
                        print("가습기켜 명령어 인식")
                        sendData = '1'
                    else:
                        break

        except:
            pass

update_scheduler()