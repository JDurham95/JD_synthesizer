import numpy as np
from scipy.io import wavfile

def wav_to_file(wav, wav2 = None, fname ="temp.wav",
                amplitude = .1,
                sample_rate = 44100):

    wav = np.array(wav)
    wav = np.int16(wav * amplitude *(2**15-1))

    if wav2 is not None:
        wav2 = np.array(wav2)
        wav2 = np.int16(wav2 * amplitude *(2**15-1))
        wav = np.stack([wav, wav2]).T

    wavfile.write(fname, sample_rate, wav)



