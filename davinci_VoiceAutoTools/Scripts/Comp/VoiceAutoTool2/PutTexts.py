import sys
# 参照パスにModuleフォルダ追加
sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools")

from Usecase.PutTexts2Timeline import PutTexts2Timeline

putTexts2Timeline = PutTexts2Timeline()
putTexts2Timeline.execute(resolve)