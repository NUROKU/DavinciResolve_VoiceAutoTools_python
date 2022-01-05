from Domain.SrtItem import SrtItem
from Domain.SrtList import SrtList
from Domain.TimelineVoiceItem import TimelineVoiceItem

class TimelineVoiceList:
    # えんててー
    def __init__(self, resolve, timeline):
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

    def CatchTimelineVoiceListFromVoiceIndex(self, index: int):
        voiceclip_list = self.timeline.GetItemListInTrack("audio",  index)
        for voiceclip in voiceclip_list:
            self.timeline_voice_list.append(TimelineVoiceItem(voiceclip))
        return self

    def Convert2SrtList(self, voice_folderpath, fill_mode):
        srt_list = SrtList(voice_folderpath)
        if fill_mode:
            # 音声クリップのstart_offset->次の音声のstart_offsetの長さのsrtが生成される
            # TODO Timecodeが1:00:00である前提で計算、もうちょっと良い感じにしたい
            srt_len = 60 * 60 * self.framerate
            for index, voiceitem in enumerate(self.timeline_voice_list):
                if index + 1 != len(self.timeline_voice_list):
                    nextvoice_start_offset = self.timeline_voice_list[index + 1].start_offset
                    frame = nextvoice_start_offset - srt_len
                    srt_len = srt_len + frame
                    # 補正、これがあったらズレない、何故ズレないのかがわからない
                    frame = frame - 1
                    srt_list.addSrtItem2List(SrtItem(voiceitem.voicepath, frame, voiceitem.start_offset))
                else:
                    srt_list.addSrtItem2List(SrtItem(voiceitem.voicepath, voiceitem.frame - 1, voiceitem.start_offset))
        else:
            # 音声の長さに合わせたsrtが生成される
            srt_len = 60 * 60 * self.framerate
            for index, voiceitem in enumerate(self.timeline_voice_list):
                # 自分のvoiceitemの前に何も無かったらごみ字幕追加
                if voiceitem.start_offset - srt_len > 1:
                    tmpframe = voiceitem.start_offset - srt_len - 1
                    srt_len = voiceitem.start_offset
                    srt_list.addSrtItem2List(SrtItem("", tmpframe))

                # 直後にvoiceitemがあったら、直後のstartoffsetまでを字幕の長さにする。Duration信用できない
                if index + 1 != len(self.timeline_voice_list) \
                    and self.timeline_voice_list[index + 1].start_offset - voiceitem.end_offset < 1:
                    voiceitem_frame = self.timeline_voice_list[index + 1].start_offset - voiceitem.start_offset
                    srt_list.addSrtItem2List(
                        SrtItem(voiceitem.voicepath, voiceitem_frame - 1, voiceitem.start_offset))
                    srt_len = srt_len + voiceitem_frame
                else:
                    # ここでそのまま追加
                    srt_list.addSrtItem2List(SrtItem(voiceitem.voicepath, voiceitem.frame, voiceitem.start_offset))
                    srt_len = srt_len + voiceitem.frame + 1

        return srt_list