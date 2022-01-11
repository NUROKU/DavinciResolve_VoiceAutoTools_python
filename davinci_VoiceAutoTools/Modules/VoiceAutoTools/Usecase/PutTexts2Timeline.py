from Domain.TimelineVoiceList import TimelineVoiceList
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class PutTexts2Timeline:

    def __init__(self):
        pass

    def execute(self, resolve):

        print("Start PutTexts2Timeline")

        config = VoiceAutoToolConfig.get()

        timelinevoice_list = TimelineVoiceList(resolve)

        srt_list = timelinevoice_list \
            .CatchTimelineVoiceListFromVoiceIndex(config["srt_timeline_audio_index"]) \
            .Convert2SrtList(config["folder_path"])

        srt_list.SetTemplateFusionText(resolve, config["srt_template_bin_name"], config["srt_template_file_name"])


        srt_list.PutSrt2Timeline(resolve, config["srt_fill_mode"])

        print("Done")
