import os

class SrtItem:
    # タイムライン上に置かれる字幕

    def __init__(self, original_filepath, frame, start_offset, framerate, next_start_offset):
        self.original_filepath = original_filepath
        self.frame = frame
        self.start_offset = start_offset
        self.end_offset = start_offset + frame
        self.next_start_offset = next_start_offset
        self.framerate = framerate
        self.text = self._GetOriginalText(original_filepath)
        # self.start_timecode = start_timecode
        # srtで出力する場合にはLeftOffsetとTimeに変換するやつ用意する

    def GetText(self):
        return self.text

    def _GetOriginalText(self, original_filepath):
        # これここでいいのかなあ、あくまで値を返すだけだから大丈夫でしょ
        if self.original_filepath == "":
            return ""
        textFile = os.path.splitext(original_filepath)[0] + ".txt"
        text = ""
        with open(textFile, "r", encoding="utf-8_sig") as f:
            text = f.read()
        return text

    def Dump2Clipinfo(self, clip, include_start_empty=False, include_after_empty=True):
        end_frame = self.frame

        if include_start_empty:
            end_frame += self.start_offset - (60 * 60 * self.framerate)

        if include_after_empty:
            end_frame += self.next_start_offset - self.end_offset - 1

        clip_info = {
            "mediaPoolItem": clip,
            "startFrame": 0,
            "endFrame": end_frame,
        }
        return clip_info

    def Dump2DummyClipinfo(self, clip):
        clip_info = {
            "mediaPoolItem": clip,
            "startFrame": 0,
            "endFrame": self.next_start_offset - self.end_offset - 2,
        }
        return clip_info

    def Dump2SrtInfo(self, fill_mode):

        if fill_mode:
            end_offset = self.next_start_offset
        else:
            end_offset = self.end_offset

        start_time = self._Frame2TimeString(self.start_offset)
        end_time = self._Frame2TimeString(end_offset)
  
        text = self.text

        return f"{start_time} --> {end_time}\n{text}"

    def Dump2FcpxmlInfo(self, textfile_folder_path):

        pass


    def _Frame2TimeString(self, frame):
        # 00:00:00:000 みたいなStringを返す

        # 計算方法を フレームレートを時間に変換してそこにフレームをかける方式にする
        conma = int((frame % self.framerate) * (1000 / self.framerate))
        second = int((frame / self.framerate) % 60)
        min = int((frame / self.framerate) / 60 % 60)
        hour = int((frame / self.framerate) / 60 / 60 % 60)

        time_str = '{hour:02}:{min:02}:{second:02}.{conma:03}'.format(hour=hour, min=min, second=second,conma=conma)

        return time_str
