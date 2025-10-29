import math
from sine_osc import SineOscillator


class SquareOscillator(SineOscillator):
    """Class for the Square Oscillator subclass, inherits from the Sine Oscillator class """
    def __init__(self, frequency = 440, phase =0, amplitude = 1,
                 sample_rate = 44100, wave_range = (-1,1),threshold =0,):
        super().__init__(frequency, phase, amplitude, sample_rate, wave_range)
        self.threshold = threshold

    def __next__(self):
        val = math.sin(self._i + self._p)
        self._i += self._step

        if val < self.threshold:
            val = self._wave_range[0]
        else:
            val = self._wave_range[1]

        return val * self._a
