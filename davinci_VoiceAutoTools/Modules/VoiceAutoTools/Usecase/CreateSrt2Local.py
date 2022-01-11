from Domain.TimelineVoiceList import TimelineVoiceList
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class CreateSrt2Local:

    def __init__(self):
        pass

    def execute(self, resolve):

        print("Start CreateSrt2Local")

        config = VoiceAutoToolConfig.get()

        timelinevoice_list = TimelineVoiceList(resolve)

        srt_list = timelinevoice_list \
            .CatchTimelineVoiceListFromVoiceIndex(config["srt_timeline_audio_index"]) \
            .Convert2SrtList(config["folder_path"])

        srt_list.SaveForSrt(config["srt_output_folder"], resolve)

        print("Done")
