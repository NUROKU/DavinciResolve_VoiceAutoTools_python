import sys
import tkinter
# 参照パスにModuleフォルダ追加
sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools")

from Usecase.SyncVoices2MediaPool import SyncVoices2MediaPool



class CheckLog(tkinter.Checkbutton):
    """
    フォルダ監視ON/OFF切替チェックボタン
    """
    def __init__(self, root, resolve):
        self.var = tkinter.BooleanVar(root, value=False)

        super().__init__(
            root,
            text="VoiceSync",
            variable=self.var,
            command=self.switch_logging,
            )
        self.pack()

        self.voice_syncer = SyncVoices2MediaPool(resolve)

    def switch_logging(self):
        if self.var.get():
            self.voice_syncer.execute()
        else:
            self.voice_syncer.stop()

root = tkinter.Tk()

var_text = tkinter.StringVar(root)
c = CheckLog(root, resolve)
root.mainloop()
