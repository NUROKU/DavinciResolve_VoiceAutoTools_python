import datetime
import os
import time
from Domain.SrtItem import SrtItem
from VoiceAutoToolException import OutputSrtFailedException, PullSrt2MediapoolException
from VoiceAutoToolException import NoFusionTemplateException
from VoiceAutoToolException import PutSrt2TimelineException

class SrtList:

    def __init__(self, folderpath: str):
        self.srt_folderpath = folderpath
        self.srt_list = []
        self.template_fusiontext = None
        pass

    def SetTemplateFusionText(self,
                              resolve: object,
                              template_bin_name: str,
                              template_fusiontext_name: str):
        root_bin = resolve.GetProjectManager() \
            .GetCurrentProject() \
            .GetMediaPool() \
            .GetRootFolder()

        template_bin = None
        for b in root_bin.GetSubFolderList():
            if(b.GetName() == template_bin_name):
                template_bin = b
                break

        for clip in template_bin.GetClipList():
            if(clip.GetClipProperty('File Name') == template_fusiontext_name):
                self.template_fusiontext = clip
                break

        if self.template_fusiontext is None:
            raise NoFusionTemplateException()

    def AddSrtItem2List(self,
                        filename: str,
                        frame: int,
                        start_offset: int,
                        framerate: float,
                        next_start_offset: int):
        filepath = self.srt_folderpath + "\\" + filename
        srt_item = SrtItem(filepath, frame, start_offset, framerate, next_start_offset)
        self.srt_list.append(srt_item)

    def PutSrt2Timeline(self, resolve: object, fill_mode: bool = True):
        clip = self.template_fusiontext
        is_first = True
        try:
            mediapool = resolve.GetProjectManager() \
                .GetCurrentProject() \
                .GetMediaPool()

            if fill_mode:
                for srt in self.srt_list:
                    subClip = srt.Dump2Clipinfo(clip, include_start_empty=is_first, include_after_empty=True)
                    timelineitem = mediapool.AppendToTimeline([subClip])[0]
                    self._ChangeCompText(timelineitem, srt)
                    is_first = False
            else:
                for srt in self.srt_list:
                    subClip = srt.Dump2Clipinfo(clip, include_start_empty=is_first, include_after_empty=False)
                    timelineitem = mediapool.AppendToTimeline([subClip])[0]
                    self._ChangeCompText(timelineitem, srt)

                    dummy_subClip = srt.Dump2DummyClipinfo(clip)
                    dummy_timelineitem = mediapool.AppendToTimeline([dummy_subClip])[0]
                    self._ChangeCompText(dummy_timelineitem, srt, True)
                    is_first = False
        except Exception:
            raise PutSrt2TimelineException()

    def SaveForSrt(self,
                   output_folder_path: str,
                   fill_mode: bool,
                   resolve: object):

        # TODO framerate取得はutilに置いていいかも、TimelineVoiceに同じのあるし
        srt_text = ""
        srt_count = 0
        for srtitem in self.srt_list:
            srt_text += str(srt_count) + "\n"
            srt_text += srtitem.Dump2SrtInfo(fill_mode) + "\n"
            srt_text += "\n"

            srt_count = srt_count + 1

        # TODO ファイル名適当だからなんとかして
        filepath = output_folder_path + "\\" + \
            datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S') + ".srt"

        try:
            with open(filepath, mode='w', encoding="utf-8") as f:
                f.write(srt_text)

            time.sleep(1)

            mediapool = resolve.GetProjectManager() \
                .GetCurrentProject() \
                .GetMediaPool()
            root_bin = mediapool.GetRootFolder()
            mediapool.SetCurrentFolder(root_bin)
            mediapool.ImportMedia(filepath)
        except OSError:
            raise OutputSrtFailedException()
        except Exception:
            raise PullSrt2MediapoolException()

    def SaveForFcpxml(self, resolve: object, folder_path: str, template_dict: dict):
        # TODO 実装、template_dictは辞書形式でテキストの属性(フォントとかサイズとか)を想定
        pass

    def _ChangeCompText(self,
                        timelineitem: object,
                        srtitem: SrtItem,
                        is_dummy=False):
        comp = timelineitem.LoadFusionCompByName("Template")
        comp.Lock()

        if is_dummy:
            comp.Template.StyledText = ""
        else:
            comp.Template.StyledText = srtitem.GetText()

        comp.Unlock()
