import os


class SrtItem:
    # タイムライン上に置かれる字幕

    def __init__(self, original_filename, frame, start_offset):
        self.original_filename = original_filename
        self.frame = frame
        self.start_offset = start_offset
        # self.start_timecode = start_timecode
        # srtで出力する場合にはLeftOffsetとTimeに変換するやつ用意する

    def GetOriginalText(self, folder_path):
        # これここでいいのかなあ、あくまで値を返すだけだから大丈夫でしょ
        if self.original_filename == "":
            return ""
        textFile = folder_path + "\\" + os.path.splitext(os.path.basename(self.original_filename))[0] + ".txt"
        text = ""
        with open(textFile, "r", encoding="utf-8_sig") as f:
            text = f.read()
        return text

    def Dump2Clipinfo(self, clip):
        clip_info = {
            "mediaPoolItem": clip,
            "startFrame": 0,
            "endFrame": self.frame,
        }
        return clip_info

    def _Frame2Time(self):
        
        # TODO .srt形式で出力する場合はここ実装しないと
        
        pass