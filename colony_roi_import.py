#! /usr/bin/python3
# Import colony ROI csv data

from glob import glob
import os.path
import numpy as np

# Change working directory to data directory
DATA_DIR = "data"


class ColonyROIImportCSV(object):

    def __init__(self, data_dir=DATA_DIR):
        self.data_dir = data_dir
        os.chdir(data_dir)

        # Get list of csv files
        csv_files_list = glob("*.csv")
        self.csv_files_list = csv_files_list

    def colony_count(self):
        # Get a colony count
        colony_count = len(self.csv_files_list)
        self.colony_count = colony_count
        return self.colony_count

    def colony_data(self):
        try:
            return self.colonies
        except AttributeError:
            colonies = []

            for csv_filename in self.csv_files_list:
                colony_name = os.path.splitext(csv_filename)[0]
                roi_data = np.genfromtxt(csv_filename, delimiter=',') 

                colony_data = {
                        'colony_name': colony_name,
                        'roi_data': roi_data,
                    }
                colonies.append(colony_data)
            return colonies
