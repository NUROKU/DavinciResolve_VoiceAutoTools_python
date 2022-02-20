import configparser
import os
from tkinter.filedialog import Directory

from VoiceAutoToolException import ConfigGetException


class VoiceAutoToolConfig:

    CONFIG_PATH = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Modules\VoiceAutoTools\Config"
    FILE_NAME = "Config.ini"
    SECTION_NAME = "VoiceAutoTools"

    @classmethod
    def get(self) -> dict:
        if not os.path.exists(self.CONFIG_PATH):
            # TODO iniファイル作る手順追加しときたい
            raise FileNotFoundError("Configファイルが存在していない可能性があります")

        config_ini = configparser.ConfigParser()
        
        try:
            config_ini.read(self.CONFIG_PATH + "\\" + self.FILE_NAME, encoding='utf-8')
        except Exception as e:
            raise ConfigGetException()
        
        dic = {}
        for key in config_ini.options(self.SECTION_NAME):
            # 雑に型変換
            dic[key] = config_ini.get(self.SECTION_NAME, key)
            if(dic[key].isdigit()):
                dic[key] = int(dic[key])
            elif(dic[key] == "True"):
                dic[key] = True
            elif(dic[key] == "False"):
                dic[key] = False

        return dic

    @classmethod
    def set(self, config_dic: Directory):
        # 単純に全パラメータ置き換えしているだけ
        config = configparser.RawConfigParser()
        config.add_section(self.SECTION_NAME)
        for k, v in config_dic.items():
            config.set(self.SECTION_NAME, k, str(v))

        with open(self.CONFIG_PATH + "\\" + self.FILE_NAME, 'w', encoding='utf-8') as file:
            config.write(file)
