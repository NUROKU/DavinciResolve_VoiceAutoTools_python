from Domain.SrtItem import SrtItem
from Domain.SrtList import SrtList
from Domain.TimelineVoiceItem import TimelineVoiceItem

class TimelineVoiceList:

    def __init__(self, resolve: object):
        timeline = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetCurrentTimeline()
        self.resolve = resolve
        # TODO タイムラインが存在しなかったら勝手に持ってくるか作るかする機能、だれかつくって
        self.timeline = timeline
        self.timeline_voice_list = []
        self.framerate = self._GetTimelineFramerate()
        pass

    def _GetTimelineFramerate(self):
        framerate = self.resolve \
            .GetProjectManager() \
            .GetCurrentProject() \
            .GetSetting("timelineFrameRate")
        return framerate

    def CatchTimelineVoiceListFromVoiceIndex(self, index: int = 0):
        voiceclip_list = self.timeline.GetItemListInTrack("audio",  index)
        for voiceclip in voiceclip_list:
            self.timeline_voice_list.append(TimelineVoiceItem(voiceclip))
        return self

    def Convert2SrtList(self, voice_folderpath: str):
        # TODO SrtItemに余白分を合わせて作成するようにして、fillmode無しでも数変わらないようにする
        srt_list = SrtList(voice_folderpath)

        for index, voiceitem in enumerate(self.timeline_voice_list):
            if index + 1 != len(self.timeline_voice_list):
                nextvoice_start_offset = self.timeline_voice_list[index + 1].start_offset
                srt_list.AddSrtItem2List(
                    filename=voiceitem.voicepath,
                    frame=voiceitem.frame - 1,
                    start_offset=voiceitem.start_offset,
                    framerate=self.framerate,
                    next_start_offset=nextvoice_start_offset
                    )
            else:
                srt_list.AddSrtItem2List(
                    filename=voiceitem.voicepath,
                    frame=voiceitem.frame - 1,
                    start_offset=voiceitem.start_offset,
                    framerate=self.framerate,
                    next_start_offset=voiceitem.start_offset + voiceitem.frame
                    )
        return srt_list
