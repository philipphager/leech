# Leech
A simple OSX CLI tool to change your MAC address temporarily to a new random address.

## Usage
As leech uses ifconfig settings, you need to run the script with sudo:
```
sudo python Leech.py
```
On first start, it saves your current MAC address to disk and you can reset to it anytime:
```
sudo python Leech.py --reset
```
*NOTICE* After your MAC address was successfully changed, the script will also automatically turn your WIFI off/on to reconnect to the network with the new address. So keep that in mind if you have pending downloads.

## License
```
The MIT License (MIT)

Copyright (Philipp Hager) 2018
```
