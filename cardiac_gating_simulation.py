# MRI doesn’t measure the electrical heartbeat directly
# It measures motion of the heart tissue or blood

# importing libaries
import numpy as np
import matplotlib.pyplot as plt

# Creating a time axis
t = np.linspace(0, 10, 1000)

# Creating a heartbeat signal
heartbeat = np.sin(2 * np.pi * 1 * t) # to show a heartbeat pattern

# creating the heartbeat signal
moving_signal = np.sin(2 * np.pi * 1 * t + np.random.normal(0, 0.5, len(t))) # this is to add random noise
# to the heartbeat signal because in real life the heartbeat is not perfectly clean.

 # without gating
random_indices = np.random.choice(len(t), size=100, replace=False) # this picks 100 random time points like
# MRI capturing data at random times

random_samples = moving_signal[random_indices]
# this extract those random values. here MRI is sampling without timmng resulting to messy to data

# with gating
gated_indices = np.where(heartbeat > 0.9)[0] # detects heartbeat peaks that is when the heartbeat happens

gated_samples = moving_signal[gated_indices]
# takes only sample at this moment, MRI captures data only at specific cardiac phase

plt.figure(figsize=(12, 8)) # Creates a big window for plots

# plot heartbeat
plt.subplot(3,1,1)
plt.plot(t, heartbeat)
plt.title("Heartbeat Signal (Timing Reference)")

# plot heartbeat without gathing
plt.subplot(3,1,2)
plt.plot(t, moving_signal, alpha=0.5)
plt.scatter(t[random_indices], random_samples, color='red')
plt.title("Without Gating (Random Sampling → Messy)")

# plot heartbeat with gating
plt.subplot(3,1,3)
plt.plot(t, moving_signal, alpha=0.5)
plt.scatter(t[gated_indices], gated_samples, color='green')
plt.title("With Gating (Synchronized Sampling → Consistent)")

plt.tight_layout()
plt.show()




