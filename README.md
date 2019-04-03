# Leech
A simple OSX CLI tool to change your MAC address temporarily to a new random address.

## Installation
You can install leech via pip from [pypi](https://pypi.org/project/leech/). It requires a python version >= 3.6.
```
pip3 install leech
```

## Usage
As leech uses ifconfig settings, you need to run the script with sudo. Calling leech will create a new random MAC address and configure your OSX to use it:
```
sudo leech
```
On first start, leech saves your current MAC address to disk and you can reset to it anytime:
```
sudo leech --reset
```
**NOTICE** After your MAC address was successfully changed, the script will also automatically turn your WIFI off/on to reconnect to the network with the new address. So keep that in mind if you have pending downloads.

## License
```
The MIT License (MIT)

Copyright (Philipp Hager) 2019
```
