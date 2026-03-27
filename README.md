# Fetal & Adult Cardiac Gating Simulation

This Python project simulates **cardiac gating in MRI** using a simplified heartbeat signal and moving heart motion.

## Problem
MRI scans of moving organs like the heart often produce **motion artifacts**, making images blurry.
Gating is used to **synchronize image acquisition with the cardiac cycle**, reducing these artifacts.

## Method
- Generate a **heartbeat signal** (timing reference)
- Simulate **moving heart signal** with random variations
- Compare **random sampling** vs **gated sampling** (using threshold for peak detection)
- Visualize results with **matplotlib**

## Usage
1. Open `cardiac_gating_simulation.py` in PyCharm
2. Run the script → three plots will appear:
   - Heartbeat signal
   - Moving signal with random sampling
   - Moving signal with gated sampling

## Insights
- The **heartbeat signal triggers MRI acquisition** at the correct phase of the cardiac cycle
- Gating ensures **consistent images** even if the heart rate fluctuates
- Demonstrates principles behind **Doppler ultrasound synchronized MRI** used in fetal and adult cardiac imaging