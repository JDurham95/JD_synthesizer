import math
from abc import ABC, abstractmethod
import itertools

class Oscillator(ABC):
    def __init__(self, frequency=440, phase=0,
                 sample_rate=44100,
                 amplitude=1, wave_range=(-1, 1)):
        self._frequency = frequency
        self._sample_rate = sample_rate
        self._amplitude = amplitude
        self._wave_range = wave_range
        self._phase = phase

        self._f = frequency
        self._a = amplitude
        self._p = phase
        self._step = 0

    @property
    def init_phase(self):
        return self._phase

    @property
    def init_frequency(self):
        return self._frequency

    @property
    def init_amplitude(self):
        return self._amplitude

    @property
    def frequency(self):
        return self._f

    @property
    def phase(self):
        return self._p

    @phase.setter
    def phase(self, new_phase):
        self._p = new_phase
        self._post_phase_set()

    @frequency.setter
    def frequency(self, new_frequency):
        self._f = new_frequency
        self._post_frequency_set()

    @property
    def amplitude(self):
        return self._a

    @amplitude.setter
    def amplitude(self, new_amplitude):
        self._a = new_amplitude
        self._post_amplitude_set()

    def _post_frequency_set(self):
        pass

    def _post_amplitude_set(self):
        pass

    def _post_phase_set(self):
        pass

    @staticmethod
    def squish_val(val, min_val, max_val):
        return ((val + 1) / 2) * (max_val - min_val) + min_val

    @abstractmethod
    def __next__(self):
        return None

    def __iter__(self):
        self.frequency = self._frequency
        self.amplitude = self._amplitude
        self._initialize_osc()
        return self