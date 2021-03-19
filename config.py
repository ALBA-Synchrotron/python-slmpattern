from microscope.device_server import device
from _microscope.lights.meadowlark import HDMIslm

DEVICES = [
    device(HDMIslm, host="0.0.0.0", port=8001),
]
