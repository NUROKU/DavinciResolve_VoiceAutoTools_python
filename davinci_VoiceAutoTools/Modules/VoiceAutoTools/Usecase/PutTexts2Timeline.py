from Domain.TimelineVoiceList import TimelineVoiceList
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class PutTexts2Timeline:

    def __init__(self):
        pass

    def execute(self, resolve):

        print("Start PutTexts2Timeline")

        config = VoiceAutoToolConfig.get()
        timeline = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetCurrentTimeline()

        timelinevoice_list = TimelineVoiceList(resolve, timeline)

        srt_list = timelinevoice_list \
            .CatchTimelineVoiceListFromVoiceIndex(config["srt_timeline_audio_index"]) \
            .Convert2SrtList(config["folder_path"], config["srt_fill_mode"])

        srt_list.SetTemplateFusionText(resolve, config["srt_template_bin_name"], config["srt_template_file_name"])

        mediapool = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetMediaPool()
        srt_list.PutSrt2Timeline(timeline, mediapool)

        print("Done")
