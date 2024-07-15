## 1. 取樣率與解析度相關公式

### 甲、決定取樣框長度（時域）

取樣框長度（時域）是指我們在進行頻譜分析時，一次處理的資料點數量。這個長度會直接影響到頻率解析度。

公式：
```
頻率解析度 = 取樣率 / 取樣框長度
```

例如，如果取樣率為 1000 Hz，取樣框長度為 1000 點，則頻率解析度為 1 Hz。

Python 範例：

```python
import numpy as np

sampling_rate = 1000  # Hz
frame_length = 1000   # 點

frequency_resolution = sampling_rate / frame_length
print(f"頻率解析度：{frequency_resolution} Hz")
```

### 乙、Fmax 設定

Fmax 是可以分析的最高頻率，它與取樣率有直接關係。根據奈奎斯特定理，Fmax 不能超過取樣率的一半。然而，一些專家建議將取樣率直接除以 2.56，以獲得更保守和可靠的結果。

公式：

1. 基於奈奎斯特定理：
```
Fmax ≤ 取樣率 / 2
```

2. 基於專家建議的更保守估計：
```
Fmax ≤ 取樣率 / 2.56
```

Python 範例：

```python
sampling_rate = 1000  # Hz

# 基於奈奎斯特定理
fmax_nyquist = sampling_rate / 2

# 基於專家建議的更保守估計
fmax_conservative = sampling_rate / 2.56

print(f"基於奈奎斯特定理的最大可分析頻率（Fmax）：{fmax_nyquist} Hz")
print(f"基於專家建議的保守最大可分析頻率（Fmax）：{fmax_conservative:.2f} Hz")
```

使用更保守的 Fmax 估計可以幫助減少混疊效應（aliasing）和提高測量的可靠性。在實際應用中，您可以根據具體需求和信號特性來選擇使用哪種 Fmax 設定。例如，在需要更高安全係數的應用中，可以選擇專家建議的方法。

## 2. 頻譜轉換設定

### 甲、時域轉頻域公式

我們使用離散傅立葉轉換（DFT）將時域信號轉換為頻域。實際應用中，我們通常使用快速傅立葉轉換（FFT）算法來提高效率。

公式（DFT）：

$$X(k) = \sum_{n=0}^{N-1} x(n) e^{-j2\pi kn/N}$$

其中，$x(n)$ 是時域信號，$X(k)$ 是頻域信號，$N$ 是取樣點數。

Python 範例（使用 FFT）：

```python
import numpy as np

# 生成一個示例信號
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# 進行 FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(t), t[1] - t[0])

# 繪製結果
import matplotlib.pyplot as plt

plt.plot(freqs, np.abs(X))
plt.xlabel('頻率 (Hz)')
plt.ylabel('幅度')
plt.show()
```

### 乙、Hanning Windows 公式

Hanning 窗函數用於減少頻譜洩漏。它在信號的開始和結束處平滑地降低信號強度。

公式：

$$w(n) = 0.5 \times \left(1 - \cos\left(\frac{2\pi n}{N-1}\right)\right)$$

其中，$n$ 是取樣點的索引，$N$ 是總取樣點數。

Python 範例：

```python
import numpy as np
import matplotlib.pyplot as plt

N = 1000
n = np.arange(N)
hanning = 0.5 * (1 - np.cos(2 * np.pi * n / (N - 1)))

plt.plot(n, hanning)
plt.title('Hanning Window')
plt.xlabel('取樣點')
plt.ylabel('振幅')
plt.show()
```

### 丙、帶通濾波公式

帶通濾波器用於只保留特定頻率範圍內的信號。

我們可以使用 SciPy 庫中的 `butter` 函數來設計一個巴特沃斯帶通濾波器：

```python
from scipy import signal
import numpy as np

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y

# 範例使用
fs = 1000.0
lowcut = 20.0
highcut = 100.0

t = np.linspace(0, 1, 1000, endpoint=False)
data = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*50*t) + np.sin(2*np.pi*200*t)

filtered_data = butter_bandpass_filter(data, lowcut, highcut, fs)

plt.plot(t, data, label='原始信號')
plt.plot(t, filtered_data, label='過濾後信號')
plt.legend()
plt.show()
```

## 3. 包絡頻譜轉換

包絡頻譜轉換用於分析信號的整體形狀或趨勢。

### 甲、參數1：濾波頻段[開始、結束]

這個參數定義了我們感興趣的頻率範圍。例如，[20, 20000] 表示我們關注 20 Hz 到 20 kHz 的頻率範圍。

### 乙、參數2：轉換函式

轉換函式決定了如何從原始信號獲得包絡。常見的方法包括希爾伯特變換和峰值檢測。

以下是使用希爾伯特變換的 Python 範例：

```python
import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt

# 生成一個示例信號
t = np.linspace(0, 1, 1000)
carrier = np.cos(2 * np.pi * 50 * t)
modulator = 1 + 0.5 * np.sin(2 * np.pi * 3 * t)
signal = carrier * modulator

# 計算包絡
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)

# 繪製結果
plt.plot(t, signal, label='原始信號')
plt.plot(t, amplitude_envelope, label='包絡')
plt.legend()
plt.show()
```

## 4. 諧波計算

諧波是基頻的整數倍頻率。計算諧波通常涉及找到基頻，然後計算其整數倍的幅度。

Python 範例：

```python
import numpy as np
import matplotlib.pyplot as plt

def calculate_harmonics(signal, fs, num_harmonics=5):
    N = len(signal)
    freqs = np.fft.fftfreq(N, 1/fs)
    spectrum = np.abs(np.fft.fft(signal))
    
    fundamental_idx = np.argmax(spectrum[1:N//2]) + 1
    fundamental_freq = freqs[fundamental_idx]
    
    harmonics = []
    for i in range(1, num_harmonics + 1):
        harmonic_freq = i * fundamental_freq
        harmonic_idx = np.argmin(np.abs(freqs - harmonic_freq))
        harmonics.append((harmonic_freq, spectrum[harmonic_idx]))
    
    return harmonics

# 生成一個含有諧波的信號
t = np.linspace(0, 1, 1000, endpoint=False)
f0 = 50  # 基頻
signal = np.sin(2*np.pi*f0*t) + 0.5*np.sin(2*np.pi*2*f0*t) + 0.25*np.sin(2*np.pi*3*f0*t)

fs = 1000  # 取樣率
harmonics = calculate_harmonics(signal, fs)

for i, (freq, amp) in enumerate(harmonics, 1):
    print(f"第 {i} 諧波: 頻率 = {freq:.2f} Hz, 幅度 = {amp:.4f}")
```

## 5. 旁波計算

旁波（側帶）通常出現在調幅（AM）或調頻（FM）信號中，位於載波頻率的兩側。

Python 範例（以 AM 信號為例）：

```python
import numpy as np
import matplotlib.pyplot as plt

# 生成 AM 信號
t = np.linspace(0, 1, 10000, endpoint=False)
fc = 1000  # 載波頻率
fm = 100   # 調製頻率
m = 0.5    # 調製指數

carrier = np.cos(2 * np.pi * fc * t)
modulator = 1 + m * np.cos(2 * np.pi * fm * t)
am_signal = carrier * modulator

# 計算頻譜
spectrum = np.abs(np.fft.fft(am_signal))
freqs = np.fft.fftfreq(len(t), t[1] - t[0])

# 繪製結果
plt.plot(freqs, spectrum)
plt.xlim(0, 1500)  # 限制 x 軸範圍以便觀察
plt.xlabel('頻率 (Hz)')
plt.ylabel('幅度')
plt.title('AM 信號頻譜')
plt.show()
```

在這個例子中，您應該能看到在載波頻率 (1000 Hz) 的兩側各有一個旁波，位置在 900 Hz 和 1100 Hz。

## 6. Amplitude 計算 (OA 值) 計算

OA（Overall Amplitude）值是指信號的總體幅度，通常用均方根（RMS）值來表示。

公式：

$$OA = \sqrt{\frac{1}{N}\sum_{i=1}^{N} x_i^2}$$

其中，$x_i$ 是信號的每個取樣點，$N$ 是總取樣點數。

Python 範例：

```python
import numpy as np

def calculate_oa(signal):
    return np.sqrt(np.mean(np.square(signal)))

# 生成一個示例信號
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*20*t)

oa_value = calculate_oa(signal)
print(f"OA 值：{oa_value:.4f}")
```