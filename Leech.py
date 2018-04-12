import subprocess
from random import Random

import click

file_name = '.leech'


# TODO: Check Wifi enabled
# TODO: Check if user is sudo
# TODO: Fix MAC generation
# TODO: Automatically agree to ICE portal Terms & Services
# TODO: Improve file checking
# TODO: Set custom MAC address
# TODO: Option to only show current IP address

def get_mac():
    return subprocess.getstatusoutput(['ifconfig en0 | grep ether'])[1] \
        .replace("ether ", "") \
        .replace("\t", "") \
        .replace(" ", "")


def set_mac(address):
    return subprocess.getstatusoutput(['ifconfig en0 ether ' + address])


def save(address):
    try:
        with open(file_name, 'x') as f:
            f.write(address)
    except FileExistsError:
        print("Cannot overwrite the MAC save file!")


def load():
    with open(file_name, 'r') as f:
        return f.readline()


def enable_wifi(is_enabled):
    status = 'on' if is_enabled else 'off'
    return subprocess.getstatusoutput(['networksetup -setairportpower en0 ' + status])


def save_file_exists():
    try:
        with open(file_name, 'r'):
            return True
    except FileNotFoundError as e:
        return False


def randomize_mac():
    address = ""
    limit = 6

    for i in range(1, limit + 1):
        address += random_hex()

        if i < limit:
            address += ":"

    return address


def random_hex():
    return Random().randrange(0, 255, 1) \
        .to_bytes(1, 'big') \
        .hex()


@click.command()
@click.option('--reset', is_flag=True, help='Reset your MAC address back before the first run of Leech.')
def leech(reset):
    if not reset:
        mac = get_mac()
        if not save_file_exists():
            save(mac)
            print("Saved your current MAC address to disk. Use the --reset option to revert to it.")

        print(f'Your current MAC address: {mac}')
        new_mac = randomize_mac()
        print(f'Setting new MAC address: {new_mac}')
        set_mac(new_mac)
        verified_mac = get_mac()

        if verified_mac == new_mac:
            print('Successfully randomized your MAC address.')
            print('Disconnecting and reconnecting your WIFI')
            enable_wifi(False)
            enable_wifi(True)
        else:
            print('Something went wrong, make sure you use are sudo and have WIFI turned on.')
            print(f'Current mac address: {verified_mac}')
    else:
        mac = load()
        set_mac(mac)
        print(f'Resetting to your original MAC address: {mac}')


if __name__ == '__main__':
    leech()
