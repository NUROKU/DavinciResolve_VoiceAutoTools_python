class TimelineVoiceItem:
    # タイムライン上に置かれたAudio
    # これって値オブジェクトってことになるんですかね
    def __init__(self, voiceclip: object):
        self.clip = voiceclip
        self.frame = voiceclip.GetDuration()
        self.voicepath = voiceclip.GetName()
        self.start_offset = voiceclip.GetStart()
        self.end_offset = voiceclip.GetEnd()

    def Convert2SrtItem(self):
        # TODO AudioListでいろいろやっちゃったので
        pass

    def dump(self):
        print(self.clip)
        print(self.frame)
        print(self.voicepath)
        print(self.start_offset)
        print("----")
