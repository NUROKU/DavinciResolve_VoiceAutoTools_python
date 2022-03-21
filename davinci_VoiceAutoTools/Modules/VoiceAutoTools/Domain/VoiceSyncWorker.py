import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from Domain.VoiceMediaBin import VoiceMediaBin


class VoiceSyncWoeker:
    class VoiceSyncEventHandler(PatternMatchingEventHandler):
        def __init__(self, voice_media_bin: object):
            ignore_patterns = ["*.txt"]
            patterns = ["*.wav"]
            ignore_directories = True
            case_sensitive = True
            super().__init__(
                patterns=patterns,
                ignore_patterns=ignore_patterns,
                ignore_directories=ignore_directories,
                case_sensitive=case_sensitive,
            )
            self.voice_media_bin = voice_media_bin

        def on_created(self, event):
            # ファイル置かれた直後だと偶にバグるのでWait挟む
            time.sleep(0.5)
            filepath = event.src_path
            try:
                item = self.voice_media_bin.PullVoiceToAudioMediaBin(filepath)
                self.voice_media_bin.PutVoice2Timeline(item)
            except Exception as e:
                #どうしようかなここ
                print("エラー")

    def __init__(self, resolve, voice_outputbin: str, folder_path: str) -> None:
        self.resolve = resolve
        self.folder_path = folder_path
        self.voice_media_bin = VoiceMediaBin(resolve, voice_outputbin)
        self.event_handler = self.VoiceSyncEventHandler(self.voice_media_bin)

    def SyncerExecute(self):
        self.observer = Observer()

        self.observer.schedule(self.event_handler, self.folder_path, recursive=False)
        self.observer.start()

    def SyncerStop(self):
        self.observer.stop()
        self.observer.join()
