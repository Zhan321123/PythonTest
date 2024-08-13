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
freq = 440.0  # 频率 (Hz)，例如 A4
duration = 1.0  # 持续时间 (秒)
sample_rate = 44100  # 采样率 (Hz)

# 生成纯音波形
waveform = generate_sine_wave(freq, duration, sample_rate)

# 播放纯音
play_audio(waveform, sample_rate)
