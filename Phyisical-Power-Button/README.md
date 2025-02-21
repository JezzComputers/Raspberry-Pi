# Phyisical-Power-Button
## Installation

Open the Raspberry Pi terminal
Enter the following command to clone the repo:
```bash
git clone https://github.com/JezzComputers/Raspberry-Pi.git
```
CD to the 'Phyisical-Power-Button' to access all the scripts
Optional: Edit line 9/10 in listen-for-shutdown.py to your preferred pin
Run the setup script:
```bash
./Raspberry-Pi/Phyisical-Power-Button/install
```

## Uninstallation

If you need to uninstall the power button script for any reason:
Run the uninstall script:
```bash
./Raspberry-Pi/Phyisical-Power-Button/uninstall
```

## Hardware

At a minimum, you'll need a [Toggle Switch](https://www.amazon.com/Gebildet-Stainless-Momentary-Normally-Waterproof/dp/B088CW8JYR?th=1), some jumper wires, and a soldering iron.

Connect the power button to Pin 5 (GPIO 3/SCL) and Pin 6 (GND) as shown in this diagram:
Also if your button has LEDs connect those pins to power and ground.

![Connection Diagram](https://raw.githubusercontent.com/JezzComputers/Raspberry-Pi/main/Phyisical-Power-Button/pinout.png)

For the GND connection you can use [any other ground pin you want](https://pinout.xyz/).
