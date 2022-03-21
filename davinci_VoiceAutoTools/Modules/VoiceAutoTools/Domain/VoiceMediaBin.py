from VoiceAutoToolException import PullVoiceFailedException
from VoiceAutoToolException import PutVoiceFailedException
from pathlib import Path
import os


class VoiceMediaBin:
    def __init__(self, resolve: object, voice_outputbin: str):
        self.resolve = resolve
        self.mediapool = self._GetMediapool(resolve)
        self.bin = self._GetBin(self.mediapool, voice_outputbin)

    def PullVoiceToAudioMediaBin(self, voice_file_path: str):
        try:
            self.resolve.GetProjectManager().GetCurrentProject().GetMediaPool().SetCurrentFolder(
                self.bin
            )

            if os.path.isdir(voice_file_path):
                files = self._SortFiles(voice_file_path)
                storage = self.resolve.GetMediaStorage()
                clip_list = []
                for file in files:
                    file_path = voice_file_path + "\\" + file
                    clip = storage.AddItemListToMediaPool(file_path)
                    if clip != []:
                        clip_list.append(clip[0])

                return clip_list
            else:
                storage = self.resolve.GetMediaStorage()
                clip_list = storage.AddItemListToMediaPool(voice_file_path)
                return clip_list

        except Exception:
            raise PullVoiceFailedException()

    def PutVoice2Timeline(self, voice_mediapoolitem: object):
        try:
            timelineitem_list = self.mediapool.AppendToTimeline(voice_mediapoolitem)
            return timelineitem_list
        except Exception:
            raise PutVoiceFailedException()

    def _GetMediapool(self, resolve: object):
        mediapool = resolve.GetProjectManager().GetCurrentProject().GetMediaPool()
        return mediapool

    def _GetBin(self, mediapool: object, voice_outputbin: str):
        root_bin = mediapool.GetRootFolder()

        sub_folders = root_bin.GetSubFolderList()
        for folder in sub_folders:
            if folder.GetName() == voice_outputbin:
                return folder

        return mediapool.AddSubFolder(root_bin, voice_outputbin)

    def _SortFiles(self, folder_path: str):
        files = list(Path(folder_path).glob(r"*"))
        files.sort(key=os.path.getmtime)
        files = map(lambda x: x.name, files)
        return files
