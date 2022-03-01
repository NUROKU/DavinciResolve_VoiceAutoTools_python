import sys
import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog

# 参照パスにModuleフォルダ追加
sys.path.append(
    r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools"
)

from Usecase.CreateSrt2Local import CreateSrt2Local
from Usecase.PutTexts2Timeline import PutTexts2Timeline

# from Usecase.CreateFcpXML2local import CreateFcpXML2local
from Config.VoiceAutoToolConfig import VoiceAutoToolConfig


class FolderPathSelectButton(tk.Button):
    """
    元フォルダ選択ボタン
    """

    def __init__(self, root, resolve):
        super().__init__(
            root,
            text="参照",
            command=self.dirdialog_clicked,
        )
        label1 = tk.Label(text="取得元のフォルダパス設定")
        label1.grid(row=0, column=0)
        self.grid(row=1, column=0, sticky=tk.E)

        self.config = VoiceAutoToolConfig.get()
        self.IDirEntry = ttk.Entry(width=100)
        self.IDirEntry.insert(tkinter.END, self.config["folder_path"])
        self.IDirEntry.grid(row=1, column=1, sticky=tk.W)

    def dirdialog_clicked(self):
        fld = filedialog.askdirectory(initialdir=dir)
        # 区切り文字がunix系のになってるのでここで置換
        fld = fld.replace("/", "\\")
        self.IDirEntry.delete(0, tkinter.END)
        self.IDirEntry.insert(tkinter.END, fld)
        
        self.config = VoiceAutoToolConfig.get()
        self.config["folder_path"] = fld
        VoiceAutoToolConfig.set(self.config)



class PutTextsButton(tk.Button):
    """
    PutTextsボタン
    """

    def __init__(self, root, resolve):
        self.resolve = resolve
        self.config = VoiceAutoToolConfig.get()
        super().__init__(
            root,
            text="PutTexts",
            command=self.put_texts,
        )

        label1 = tk.Label(text="音声インデックス指定")
        label1.grid(row=2, column=0, sticky=tk.E)
        self.audio_index_spinbox = tkinter.Spinbox(root, from_=0, to=100, text="teet")
        self.audio_index_spinbox.grid(row=2, column=1, sticky=tk.W)

        label2 = tk.Label(text="Fill_mode指定")
        label2.grid(row=3, column=0, sticky=tk.E)
        self.check_v = tkinter.BooleanVar(value=True)
        self.fillmode_checkbutton = tkinter.Checkbutton(
            root,
            variable=self.check_v,
            text="Fill_mode",
        )
        self.fillmode_checkbutton.grid(row=3, column=1, sticky=tk.W)

        label2 = tk.Label(text="Binの名前指定")
        label2.grid(row=4, column=0, sticky=tk.E)
        self.Entry1 = ttk.Entry(width=100)
        self.Entry1.insert(tkinter.END, self.config["srt_template_bin_name"])
        # self.IDirEntry.pack(anchor=tk.W,padx=100)
        self.Entry1.grid(row=4, column=1, sticky=tk.W)
        
        label3 = tk.Label(text="FusionTemplate名指定")
        label3.grid(row=5, column=0, sticky=tk.E)
        self.Entry2 = ttk.Entry(width=100)
        self.Entry2.insert(tkinter.END, self.config["srt_template_file_name"])
        # self.IDirEntry.pack(anchor=tk.W,padx=100)
        self.Entry2.grid(row=5, column=1, sticky=tk.W)

        label4 = tk.Label(text="PutText")
        label4.grid(row=6, column=0, sticky=tk.E)
        self.grid(row=6, column=1, sticky=tk.W)

    def put_texts(self):

        # 設定値の取得
        self.config = VoiceAutoToolConfig.get()
        self.config["srt_fill_mode"] = str(self.check_v.get())
        self.config["srt_timeline_audio_index"] = str(self.audio_index_spinbox.get())
        self.config["srt_template_bin_name"] = str(self.Entry1.get())
        self.config["srt_template_file_name"] = str(self.Entry2.get())
        VoiceAutoToolConfig.set(self.config)

        putTexts2Timeline = PutTexts2Timeline()
        try:
            putTexts2Timeline.Execute(self.resolve)
            messagebox.showinfo("putTexts2Timeline", "テキストを配置しました")
        except Exception as e:
            messagebox.showerror("エラー", e)


root = tk.Tk()

root.title("VoiceAutoTool_PutTexts")
root.geometry("400x200")

b1 = FolderPathSelectButton(root, resolve)
b2 = PutTextsButton(root, resolve)

root.mainloop()
