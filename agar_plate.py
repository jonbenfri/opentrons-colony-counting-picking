#! /usr/bin/python3

# Create and calibrate labware
# 1. Create pipette
# 2. Create labware to interact with

from opentrons import labware, instruments

# Declare pipette
try:
    p300 = instruments.P300_Single(mount='right')
except:
    pass

# Declare labware
plate_name = '75mm_agar_plate'
if plate_name not in labware.list():
    custom_plate = labware.create(
            plate_name,
            grid = (1, 1), # single agar plate
            spacing=(1, 1), # Are these values important for 1x1?
            diameter=(50), # diameter of agar plate
            depth=10, # random value
            volume=200) # random value

try:
    plate = labware.load(plate_name, '3')
except:
    pass

# Do a test transfer
p300.transfer(10, plate.wells('A1'), plate.wells('A1'))

# Import colony location data
