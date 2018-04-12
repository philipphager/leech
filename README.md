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

## License
```
The MIT License (MIT)

Copyright (Philipp Hager) 2018
```
