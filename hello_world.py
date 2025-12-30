import numpy as np
import matplotlib.pyplot as plt

# 1. SIMULATE THE REAL WORLD (Mechatronics)
# Imagine a robot arm moving in a smooth sine wave
time = np.linspace(0, 10, 100)
true_movement = np.sin(time)

# 2. ADD NOISE (The Problem)
# Sensors are imperfect. Let's add random static (Gaussian noise)
noise = np.random.normal(0, 0.2, 100)
sensor_data = true_movement + noise

# 3. APPLY THE MATH (Applied Science)
# We use a "Convolution" to calculate a Moving Average.
# This creates a "sliding window" that averages every 5 data points together.
kernel_size = 5
kernel = np.ones(kernel_size) / kernel_size
smoothed_data = np.convolve(sensor_data, kernel, mode='same')

# 4. VISUALIZE THE RESULT
plt.figure(figsize=(10, 5))
plt.plot(time, sensor_data, label='Noisy Sensor (Raw)', color='red', alpha=0.5)
plt.plot(time, smoothed_data, label='Smoothed (Algorithm)', color='blue', linewidth=2)
plt.legend()
plt.title("Applied Science: Cleaning Sensor Data with Math")
plt.show()

    
    