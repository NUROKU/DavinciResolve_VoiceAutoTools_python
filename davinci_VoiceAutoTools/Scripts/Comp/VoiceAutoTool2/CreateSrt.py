import sys
# 参照パスにModuleフォルダ追加
sys.path.append(r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools")

from Usecase.CreateSrt2Local import CreateSrt2Local

createSrt2Local = CreateSrt2Local()
createSrt2Local.Execute(resolve)