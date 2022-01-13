from Domain.VoiceMediaBin import VoiceMediaBin
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class PullVoice2MediaPool:

    def __init__(self):
        pass

    def Execute(self, resolve):

        print("Start PutTexts2Timeline")

        config = VoiceAutoToolConfig.get()
        voice_mediabin = VoiceMediaBin(resolve, config["voice_outputbin"])

        voice_mediapoolitem_list = voice_mediabin.PullVoiceToAudioMediaBin(config["folder_path"])

        voice_mediabin.PutVoice2Timeline(voice_mediapoolitem_list)
        print("Done")
