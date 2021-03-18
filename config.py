from microscope.device_server import device
from _microscope.lights.meadowlark import HDMIslm

DEVICES = [
    device(HDMIslm, host="127.0.0.1", port=8001),
]
