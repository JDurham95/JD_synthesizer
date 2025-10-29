import math
from saw_osc import SawOscillator

class TriangleOscillator(SawOscillator):
    """Defines the Triangle Oscillator subclass, inherits from the Saw Oscillator class """

    def __next__(self):
        div = (self._i + self._p) / self._period
        val = 2 * (div - math.floor(div +0.5))
        val = (abs(val)- 0.5) * 2
        self._i += + 1
        if self._wave_range != (-1,1):
            val = self.squish_val(val, *self._wave_range)

        return val * self._a
