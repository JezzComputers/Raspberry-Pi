# Overclocking Raspberry Pi 4B and 5B

This guide provides instructions on how to overclock your Raspberry Pi 4B and 5B models for improved performance. Please note that overclocking may void your warranty and can potentially damage your device if not done carefully.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Raspberry Pi 4B Overclocking](#raspberry-pi-4b-overclocking)
- [Raspberry Pi 5B Overclocking](#raspberry-pi-5b-overclocking)
- [Monitoring and Stability](#monitoring-and-stability)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- A Raspberry Pi 4B or 5B
- Adequate cooling solution (heatsink, fan, or both)
- Latest Raspberry Pi OS installed
- Basic knowledge of terminal commands

## Raspberry Pi 4B Overclocking

1. Open the config file:

```bash
sudo nano /boot/firmware/config.txt
```

2. Add the following lines at the end of the file:

```
over_voltage=6
arm_freq=2000
gpu_freq=700
```

3. Save and exit the file (Ctrl+X, then Y, then Enter).

4. Reboot your Raspberry Pi:

```bash
sudo reboot
```

## Raspberry Pi 5B Overclocking

1. Open the config file:

```bash
sudo nano /boot/firmware/config.txt
```

2. Add the following lines at the end of the file:

```
over_voltage_delta=50000
arm_freq=3000
gpu_freq=1000
```

3. Save and exit the file (Ctrl+X, then Y, then Enter).

4. Reboot your Raspberry Pi:

```bash
sudo reboot
```

## Monitoring and Stability

To monitor your Raspberry Pi's performance and ensure stability:

1. Install stress-testing tools:

```bash
sudo apt-get install sysbench
```

2. Monitor CPU clock speed:

```bash
watch -n 1 vcgencmd measure_clock arm
```

3. Run a stress test:

```bash
sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run
```

4. Monitor temperature:

```bash
vcgencmd measure_temp
```

## Troubleshooting

If you experience stability issues:

1. Gradually reduce the `arm_freq` and `gpu_freq` values.
2. Increase cooling if temperatures exceed 80°C.
3. If overclocking fails, try setting `force_turbo=1` in config.txt.
4. For Pi 4B, you can try setting `arm_freq_min` to a higher value (e.g., 1000) to maintain a minimum clock speed.
