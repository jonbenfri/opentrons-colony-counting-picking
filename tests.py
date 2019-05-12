#! /usr/bin/python3

import unittest
from colony_roi_import import ColonyROIImportCSV


DATA_DIR = "data"

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


if __name__ == "__main__":
    unittest.main()
