from Domain.VoiceSyncWorker import VoiceSyncWoeker
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class SyncVoices2MediaPool:

    def __init__(self, resolve):
        self.resolve = resolve

    def Execute(self):
        config = VoiceAutoToolConfig.get()
        self.voice_syncer = VoiceSyncWoeker(self.resolve, config["voice_outputbin"], config["folder_path"])
        self.voice_syncer.SyncerExecute()
        print("Execute Sync")

    def Stop(self):
        self.voice_syncer.SyncerStop()
        print("Stop Sync")
