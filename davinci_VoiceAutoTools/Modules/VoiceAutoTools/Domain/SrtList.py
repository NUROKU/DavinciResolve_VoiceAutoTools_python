

class SrtList:

    def __init__(self, folderpath):
        self.srt_folderpath = folderpath
        self.srt_list = []
        self.template_fusiontext = None
        pass

    def SetTemplateFusionText(self, resolve, template_bin_name, template_fusiontext_name):
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

    def addSrtItem2List(self, srtitem):
        self.srt_list.append(srtitem)

    def PutSrt2Timeline(self, timeline, mediapool):
        clip = self.template_fusiontext

        for srt in self.srt_list:
            subClip = srt.Dump2Clipinfo(clip)
            timelineitem = mediapool.AppendToTimeline([subClip])[0]
            self._ChangeCompText(timelineitem, srt)
            
    def SaveForSrt(self, folder_path):
        pass
    
    
    def Convert2FCPXMLText(self, folder_path):
        pass
    
    
    def _ChangeCompText(self, timelineitem, srtitem):
        comp = timelineitem.LoadFusionCompByName("Template")
        comp.Lock()

        comp.Template.StyledText = srtitem.GetOriginalText(self.srt_folderpath)

        comp.Unlock()
