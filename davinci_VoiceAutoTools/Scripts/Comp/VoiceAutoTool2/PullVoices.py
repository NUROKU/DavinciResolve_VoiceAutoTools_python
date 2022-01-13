import sys
# 参照パスにModuleフォルダ追加
sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools")

from Usecase.PullVoice2MediaPool import PullVoice2MediaPool

pullVoice2MediaPool = PullVoice2MediaPool()
pullVoice2MediaPool.Execute(resolve)