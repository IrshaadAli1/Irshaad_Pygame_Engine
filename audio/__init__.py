from .. import utils
from .pydub import AudioSegment
from .pydub.playback import _play_with_simpleaudio
import threading
import time

class Audio:
    def __init__(self, filename, fromMusic=False, isRaw=False):
        self.original = AudioSegment.from_file((utils.loadSound(filename) if not fromMusic else utils.loadMusic(filename)) if not isRaw else filename)
        self.audio = self.original
        self.play_obj = None
        self.position = 0  # in milliseconds
        self.volume = 0  # dB adjustment
        self.play_thread = None
        self.is_paused = False
        self.should_stop = False

    def set_position(self, ms):
        self.position = ms

    def get_position(self):
        return self.position

    def set_volume(self, dB):
        self.volume = dB
        self.audio = self.original + dB

    def get_volume(self):
        return self.volume

    def fade_in(self, duration=2000):
        self.audio = self.audio.fade_in(duration)

    def fade_out(self, duration=2000):
        self.audio = self.audio.fade_out(duration)

    def _play(self, start, end):
        seg = self.audio[start:end]
        self.play_obj = _play_with_simpleaudio(seg)

    def play(self, start=None, end=None):
        if start is not None:
            self.set_position(start)
        if end is None:
            end = len(self.audio)

        if self.play_thread and self.play_thread.is_alive():
            self.stop()

        self.should_stop = False
        self.play_thread = threading.Thread(target=self._play, args=(self.position, end))
        self.play_thread.start()

    def pause(self):
        if self.play_obj:
            self.position += int(self.play_obj.get_playback_position() / 44100 * 1000)
            self.play_obj.stop()
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            self.play()
            self.is_paused = False

    def stop(self):
        if self.play_obj:
            self.play_obj.stop()
        self.should_stop = True

    def speed_up(self, factor=1.25):
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * factor)
        }).set_frame_rate(self.audio.frame_rate)

    def slow_down(self, factor=0.8):
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * factor)
        }).set_frame_rate(self.audio.frame_rate)

    def pitch_up(self, semitones=1):
        factor = 2 ** (semitones / 12)
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * factor)
        }).set_frame_rate(self.original.frame_rate)

    def pitch_down(self, semitones=1):
        factor = 2 ** (-semitones / 12)
        self.audio = self.audio._spawn(self.audio.raw_data, overrides={
            "frame_rate": int(self.audio.frame_rate * factor)
        }).set_frame_rate(self.original.frame_rate)

    @classmethod
    def loadRaw(cls, path):
        return Audio(path, isRaw=True)
