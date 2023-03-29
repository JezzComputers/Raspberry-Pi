# Phyisical-Power-Button
## Installation

1. Open the Raspberry Pi terminal
1. Enter this command to clone the repo: `git clone https://github.com/Howchoo/pi-power-button.git`
1. Optional: Edit line 9/10 in listen-for-shutdown.py to your preferred pin
1. Run the setup script: `./pi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script in order to use GPIO3 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`

## Hardware

At a minimum, you'll need a [normally-open (NO) power button](https://www.amazon.com/weideer-MomentaryPush-Waterproof-Mounting-M-12-POWER-T-R-X/dp/B095S6VTHS/ref=sr_1_14?crid=3VULKU8TYQ92A&keywords=momentary%2Bpush%2Bbutton%2Bwith%2Bwires&qid=1680087678&sprefix=momentery%2Bpush%2Bbutton%2Bwith%2Bwires%2Caps%2C509&sr=8-14&th=1), some jumper wires, and a soldering iron.

Connect the power button to Pin 5 (GPIO 3/SCL) and Pin 6 (GND) as shown in this diagram:
Also if your button has LEDs connect those pins to power and ground.

![Connection Diagram](https://raw.githubusercontent.com/Howchoo/pi-power-button/master/diagrams/pinout.png)

For the GND connection you can use [any other ground pin you want](https://pinout.xyz/).
