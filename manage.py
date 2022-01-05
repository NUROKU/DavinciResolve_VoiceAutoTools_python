import os
from distutils import dir_util

def build_sync():

    print("sync to davinci resolve")

    resolve_module_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules"
    resolve_script_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts"
    # resolve_config_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Config"

    origin_dir = os.path.dirname(__file__)

    origin_module_path = os.path.join(origin_dir, "davinci_VoiceAutoTools", "Modules") + "\\"
    origin_script_path = os.path.join(origin_dir, "davinci_VoiceAutoTools", "Scripts") + "\\"
    # origin_config_path = os.path.join(origin_dir, "davinci_VoiceAutoTools", "Config") + "\\"

    dir_util.copy_tree(origin_module_path, resolve_module_path)
    dir_util.copy_tree(origin_script_path, resolve_script_path)
    # dir_util.copy_tree(origin_config_path, resolve_config_path)

    print("done")
