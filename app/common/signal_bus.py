from PyQt5.QtCore import QObject, pyqtSignal, QUrl


class SignalBus(QObject):
    # 字幕排布信号
    subtitle_layout_changed = pyqtSignal(str)
    # 字幕优化信号
    subtitle_optimization_changed = pyqtSignal(bool)
    # 字幕翻译信号
    subtitle_translation_changed = pyqtSignal(bool)
    # 翻译语言
    target_language_changed = pyqtSignal(str)

    # 新增视频控制相关信号
    video_play = pyqtSignal()  # 播放信号
    video_pause = pyqtSignal()  # 暂停信号
    video_stop = pyqtSignal()  # 停止信号
    video_source_changed = pyqtSignal(QUrl)  # 视频源改变信号
    video_segment_play = pyqtSignal(int, int)  # 播放片段信号，参数为开始和结束时间(ms)
    video_subtitle_added = pyqtSignal(str)  # 添加字幕文件信号

    def on_subtitle_layout_changed(self, layout: str):
        self.subtitle_layout_changed.emit(layout)

    def on_subtitle_optimization_changed(self, optimization: bool):
        if optimization:
            # 如果开启字幕优化,则关闭字幕翻译
            self.subtitle_translation_changed.emit(False)
        self.subtitle_optimization_changed.emit(optimization)

    def on_subtitle_translation_changed(self, translation: bool):
        if translation:
            # 如果开启字幕翻译,则关闭字幕优化
            self.subtitle_optimization_changed.emit(False)
        self.subtitle_translation_changed.emit(translation)

    def on_target_language_changed(self, language: str):
        self.target_language_changed.emit(language)

    # 新增视频控制相关方法
    def play_video(self):
        """触发视频播放"""
        self.video_play.emit()

    def pause_video(self):
        """触发视频暂停"""
        self.video_pause.emit()

    def stop_video(self):
        """触发视频停止"""
        self.video_stop.emit()

    def set_video_source(self, url: QUrl):
        """设置视频源
        
        Args:
            url: 视频文件的URL
        """
        self.video_source_changed.emit(url)

    def play_video_segment(self, start_time: int, end_time: int):
        """播放指定时间段的视频
        
        Args:
            start_time: 开始时间(毫秒)
            end_time: 结束时间(毫秒)
        """
        self.video_segment_play.emit(start_time, end_time)

    def add_subtitle(self, subtitle_file: str):
        """添加字幕文件
        
        Args:
            subtitle_file: 字幕文件路径
        """
        self.video_subtitle_added.emit(subtitle_file)


signalBus = SignalBus()