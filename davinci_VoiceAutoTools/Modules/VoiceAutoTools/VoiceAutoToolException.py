# エラーメッセージとクラス名はそのままUIに出力される


# -------------------
# 共通
# -------------------
class ConfigGetException(Exception):
    def __init__(self):
        super().__init__("""設定情報の取得に失敗しました""")


# -------------------
# CreateSet関連
# -------------------


class CatchVoiceFromTimelineFailedException(Exception):
    def __init__(self):
        super().__init__(
            """タイムラインから音声を取得する処理で失敗しました。
タイムラインを開いている事、また音声インデックスの番号が正常であることを確認してください"""
        )


class OutputSrtFailedException(Exception):
    def __init__(self):
        super().__init__(
            """字幕ファイルの出力に失敗しました。
出力先のフォルダのパス指定が正しいか確認してください"""
        )


class PullSrt2MediapoolException(Exception):
    def __init__(self):
        super().__init__(
            """字幕ファイルをMediaPoolに引っ張ってこれませんでした。
恐らく指定された出力先に字幕ファイルが出力されているはずです"""
        )


class NoFusionTemplateException(Exception):
    def __init__(self):
        super().__init__(
            """字幕用のFusionTextが見つかりませんでした。
字幕用のFusionTextが配備されていること、またbin_nameとtext_nameが正しいかを確認してください"""
        )


class PutSrt2TimelineException(Exception):
    def __init__(self):
        super().__init__("""字幕テキストをタイムライン上に置けませんでした。""")


# -------------------
# SyncVoice関連
# -------------------


class PullVoiceFailedException(Exception):
    def __init__(self):
        super().__init__(
            """音声ファイルの取得に失敗しました。
取得元のフォルダのパス指定が正しいか確認してください"""
        )


class PutVoiceFailedException(Exception):
    def __init__(self):
        super().__init__(
            """音声ファイルをタイムラインに配置する処理に失敗しました。
タイムラインを開いているか等を確認してください"""
        )
