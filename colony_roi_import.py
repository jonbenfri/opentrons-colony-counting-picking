#! /usr/bin/python3
# Import colony ROI csv data

from glob import glob
import os.path
import numpy as np

# Change working directory to data directory
DATA_DIR = "data"
START_DIR = os.getcwd()


class ColonyROIImportCSV(object):

    def __init__(self, data_dir=DATA_DIR):
        self.data_dir = data_dir
        os.chdir(data_dir)

        # Get list of csv files
        csv_files_list = glob("*.csv")
        self.csv_files_list = csv_files_list

        # Go back to starting directory
        os.chdir(START_DIR)

    def get_colony_count(self):
        try:
            return self.colony_count
        except AttributeError:
            # Get a colony count
            colony_count = len(self.csv_files_list)
            self.colony_count = colony_count
            return self.colony_count

    def colony_data(self):
        try:
            return self.colonies
        except AttributeError:
            colonies = []

            os.chdir(self.data_dir)
            for csv_filename in self.csv_files_list:
                colony_name = os.path.splitext(csv_filename)[0]
                roi_data = np.genfromtxt(csv_filename, delimiter=',') 

                colony_data = {
                        'colony_name': colony_name,
                        'roi_data': roi_data,
                    }
                colonies.append(colony_data)

            os.chdir(START_DIR)
            self.colonies = colonies
            return colonies

    def center_of_mass(self, colony_num=0):
        """
        Returns (x,y) coordinate of specified colony center of mass
        """

        try:
            self.colonies
        except AttributeError:
            print("Run `ColonyROIImportCSV.colony_data` first to import data.")

        N = self.get_colony_count()
        if colony_num not in range(N):
            raise ValueError("Pick a colony number from 0 to " + str(N))

        x_ = 0
        y_ = 0

        colony_roi = self.colonies[colony_num]
        roi_data = colony_roi['roi_data']
        roi_pixel_count = len(roi_data)

        for coord in roi_data:
            x_ = x_ + coord[0]
            y_ = y_ + coord[1]

        x_ = x_/roi_pixel_count
        y_ = y_/roi_pixel_count

        return x_, y_
