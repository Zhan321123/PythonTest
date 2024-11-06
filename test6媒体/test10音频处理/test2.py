import numpy as np
import sounddevice as sd

def generate_sine_wave(freq, duration, sample_rate):
    """
    生成一个纯音的波形。

    :param freq: 音频频率 (Hz)
    :param duration: 持续时间 (秒)
    :param sample_rate: 采样率 (Hz)
    :return: 生成的音频波形
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return x

def play_audio(waveform, sample_rate):
    """
    播放音频波形。

    :param waveform: 音频波形
    :param sample_rate: 采样率 (Hz)
    """
    sd.play(waveform, sample_rate)
    sd.wait()  # 等待播放完成

# 参数设置
duration = 1.0  # 持续时间 (秒)
sample_rate = 44100  # 采样率 (Hz)

# 钢琴键盘上每个键的频率
def piano_key_frequencies():
    base_freq = 440.0  # A4 的频率
    frequencies = []
    for k in range(88):  # 88个键
        freq = base_freq * (2 ** ((k - 49) / 12))
        frequencies.append(freq)
    return frequencies

# 生成并播放每个键的音波
frequencies = piano_key_frequencies()
for freq in frequencies:
    print(f"Playing frequency: {freq:.2f} Hz")
    waveform = generate_sine_wave(freq, duration, sample_rate)
    play_audio(waveform, sample_rate)
