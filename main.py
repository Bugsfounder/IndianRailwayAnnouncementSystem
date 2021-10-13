import os
from gtts.tts import Speed
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


# pip install pyaudio
# pip install pydub
# pip install pandas
# pip install gTTS

def textToSpeech(text, filename):
    myText = str(text)
    language = "hi"
    myObj = gTTS(text=myText, lang=language, slow=False)
    myObj.save(filename)


# THIS FUNCTION WILL RETURNS PYDUBS AUDIO SEGMENT
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)

    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3("railway.mp3")

    # HINDI ANNOUNCEMENT
    # 1. GENERATE KRIPYA DHYAN DIJIE
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format='mp3')

    # 2. IS FROM CITY

    # 3. GENERATE SE CHAL KAR
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format='mp3')

    # 4. IS VIA CITY

    # 5. GENERATE KE RASTE
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format='mp3')

    # 6. IS TO CITY

    # 7. GENERATE KO JAANE WALI GAARI SANKHYA
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format='mp3')

    # 8. IS TRAIN NUMBER AND NAME

    # 9. GENERATE KUCHH HI SAMAI MAI PLATEFORM SANKHYA
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format='mp3')

    # 10. IS PLATEFORM NUMBER

    # 11. GENERATE PAR AA RAHI HAI
    start = 109000
    finish = 112500
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format='mp3')

    # ENGLISH ANNOUNCEMENT
    # 1. MAY I HAVE YOUR ATTENSION PLEASE TRAIN NUMBER
    start = 19000
    finish = 24000
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format='mp3')

    # 2. TRAIN NUMBER

    # 3. FROM CITY

    # 4. GENERATE FROM
    start = 30000
    finish = 31000
    audioProcessed = audio[start:finish]
    audioProcessed.export("4_english.mp3", format='mp3')

    # 5. TO CITY

    # 6. GENERATE TO
    start = 31600
    finish = 32800
    audioProcessed = audio[start:finish]
    audioProcessed.export("6_english.mp3", format='mp3')

    # 7. VIA CITY

    # 8. GENERATE VIA
    start = 33800
    finish = 34800
    audioProcessed = audio[start:finish]
    audioProcessed.export("8_english.mp3", format='mp3')
    # 9. GENERATE IS ARRIVING SORTED ON PLATFORM NUMBER
    start = 36300
    finish = 40300
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format='mp3')
    # 10 PLATFORM NUMBER


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    # print(df)
    for index, item in df.iterrows():
        # 2. GENERATE FROM CITY
        textToSpeech(item['from'], "2_hindi.mp3")

        # 4. GENERATE VIA CITY
        textToSpeech(item['via'], "4_hindi.mp3")

        # 6. GENERATE TO CITY
        textToSpeech(item['to'], "6_hindi.mp3")

        # 8. GENERATE TRAIN NUMBER AND NAME
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], "8_hindi.mp3")

        # 10. GENERATE PLATEFORM NUMBER
        textToSpeech(item['platform'], "10_hindi.mp3")

        # ENGLISH ANNOUNCEMENT

        # 2. TRAIN NUMBER
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], "2_english.mp3")
        # 3. FROM CITY
        textToSpeech(item['from'], "3_english.mp3")

        # 5. TO CITY
        textToSpeech(item['to'], "5_english.mp3")

        # 7. VIA CITY
        textToSpeech(item['via'], "7_english.mp3")

        # 10 PLATFORM NUMBER
        textToSpeech(item['platform'], "10_english.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(
            f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

        audiosEnglish = [f"{i}_english.mp3" for i in range(1, 11)]
        announcementEnglish = mergeAudios(audiosEnglish)

        announcementEnglish.export(
            f"announcementEnglish_{item['train_no']}_{index+1}.mp3", format='mp3')


def fullAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        fromCity = item['from']
        viaCity = item['via']
        toCity = item['to']
        trainNameNumber = item['train_no'] + " " + item['train_name']
        platform = item['platform']

        announcement = f"kripya dhyaan dijie {fromCity} se chal kar {viaCity} ke raste {toCity} jaane wali gaari sankhya {trainNameNumber} kuchh hee samae me platform sankhya {platform} par aa rahi hai"

        announcementEnglish = f"may i have your attension please Train number {trainNameNumber} from {fromCity} to {toCity} via {viaCity} is arriving sorted on platform number {platform}"

        textToSpeech(announcement, f"fullAnnouncement_{index+1}.mp3")

        textToSpeech(announcementEnglish,
                     f"fullAnnouncementEnglish_{index+1}.mp3")


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_hindi.xlsx")
    fullAnnouncement("announce_hindi.xlsx")
    generateAnnouncement("announce_english.xlsx")
