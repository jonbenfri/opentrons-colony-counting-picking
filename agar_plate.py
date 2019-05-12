#! /usr/bin/python3

# Create and calibrate labware
# 1. Create pipette
# 2. Create labware to interact with

from opentrons import labware, instruments
from colony_roi_import import ColonyROIImportCSV

DATA_DIR = "data"
PLATE_SLOT = 1


######################
# Colony Data Import #
######################

# Import colony location data
roi_import = ColonyROIImportCSV(data_dir=DATA_DIR)
roi_data = roi_import.colony_data()


###############
# Robot Setup #
###############

# Declare pipette
try:
    p300 = instruments.P300_Single(mount='right')
except:
    pass


# Declare agar_plate labware
# Strategy 1: Align plate(s) to grid or do 1x1 well plate,
#    use vector in move_to relative to center of dish
# Strategy 2: Each pixel is a well


# Strategy 1:
plate_name = '50mm_agar_plate'
if plate_name not in labware.list():
    custom_plate = labware.create(
            plate_name,
            grid = (1, 1), # single agar plate
            spacing=(1, 1), # Are these values important for 1x1?
            diameter=(50), # diameter of agar plate
            depth=10, # random value
            volume=200) # random value

# Load labware
try:
    plate = labware.load(plate_name, PLATE_SLOT)
except:
    pass

# Do a test transfer
p300.transfer(10, plate.wells('A1'), plate.wells('A1'))

# TODO:
# create `colony` method to access plate colonies,
# e.g. `plate.colonies('1')` will go to center of mass
