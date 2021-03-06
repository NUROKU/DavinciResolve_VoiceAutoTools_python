import sys
import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox

# 参照パスにModuleフォルダ追加
sys.path.append(
    r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools"
)

from Usecase.SyncVoices2MediaPool import SyncVoices2MediaPool
from Usecase.PullVoice2MediaPool import PullVoice2MediaPool
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class FolderPathSelectButton(tk.Button):
    """
    Sync元フォルダ選択ボタン
    """

    def __init__(self, root, resolve):
        super().__init__(
            root,
            text="参照",
            command=self.dirdialog_clicked,
        )
        self.pack(anchor=tk.W)

        self.config = VoiceAutoToolConfig.get()
        self.IDirEntry = ttk.Entry(width=100)
        self.IDirEntry.insert(tkinter.END, self.config["folder_path"])
        self.IDirEntry.pack(anchor=tk.W)
        
        self.voice_syncer = SyncVoices2MediaPool(resolve)
        self.voice_syncer.Execute()

    def dirdialog_clicked(self):
        fld = filedialog.askdirectory(initialdir=dir)
        # 区切り文字がunix系のになってるのでここで置換
        fld = fld.replace("/", "\\")
        self.IDirEntry.delete(0, tkinter.END)
        self.IDirEntry.insert(tkinter.END, fld)
        self.config = VoiceAutoToolConfig.get()

        self.config["folder_path"] = fld
        VoiceAutoToolConfig.set(self.config)
        
        self.voice_syncer.Stop()
        self.voice_syncer.Execute()

class PullButton(tk.Button):
    """
    一括Pullボタン
    """

    def __init__(self, root, resolve):
        self.resolve = resolve
        super().__init__(
            root,
            text="全てをPull",
            command=self.pullbutton_clicked,
        )
        self.pack(anchor=tk.W)

    def pullbutton_clicked(self):
        pullVoice2MediaPool = PullVoice2MediaPool()
        try:
            pullVoice2MediaPool.Execute(self.resolve)
            messagebox.showinfo("SyncVoice", "ボイスのPullが完了しました。")
        except Exception as e:
            messagebox.showerror("エラー", e)


root = tk.Tk()

# 初期設定
# 上から[フォルダパス、SyncMode_ONボタンと全部Pullボタン]
root.title("VoiceAutoTool_VoiceSyncer")
root.geometry("400x200")

label1 = tk.Label(text="Sync元のフォルダパス設定")
label1.pack(anchor=tk.W)

b1 = FolderPathSelectButton(root, resolve)
b2 = PullButton(root, resolve)
root.mainloop()
