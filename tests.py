#! /usr/bin/python3

import unittest

import os.path

from scipy import misc
import matplotlib.pyplot as plt

from colony_roi_import import ColonyROIImportCSV



DATA_DIR = "data"
IMAGE_DIR = "photos"
IMAGE_FILENAME = "600px-E.coliAgarpicture.jpg"
ROI_IMAGE_FILENAME = "600px-E.coliAgarpicture-ROI.jpg"

class TestColonyROIImportCSV(unittest.TestCase):

    def test_colony_count(self):
        roi_import = ColonyROIImportCSV(data_dir=DATA_DIR)
        colony_count = roi_import.get_colony_count()

        roi_data = roi_import.colony_data()

        self.assertEqual(colony_count, 16)
        self.assertEqual(len(roi_data), 16)

    def test_center_of_mass(self):
        roi_import = ColonyROIImportCSV(data_dir=DATA_DIR)
        colony_count = roi_import.get_colony_count()

        colony_roi_data = roi_import.colony_data()
        print(roi_import.center_of_mass(1))

    def test_colony_import_visual(self):
        """
        Draw ROI on original image
        """
        roi_import = ColonyROIImportCSV(data_dir=DATA_DIR)
        colony_count = roi_import.get_colony_count()

        colony_roi_data = roi_import.colony_data()


        f=misc.imread(os.path.join(IMAGE_DIR, IMAGE_FILENAME))
        plt.imshow(f)
        for i in range(colony_count):
            plt.scatter(*roi_import.center_of_mass(i))
            colony_i_roi_data =  colony_roi_data[i]['roi_data']
            l = len(colony_i_roi_data)
            for j in range(l):
                plt.scatter(*colony_i_roi_data[j], s=1)

        plt.show()


if __name__ == "__main__":
    unittest.main()
