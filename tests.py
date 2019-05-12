#! /usr/bin/python3

import unittest
from colony_roi_import import ColonyROIImportCSV


DATA_DIR = "data"

class TestColonyROIImportCSV(unittest.TestCase):

    def test_colony_count(self):
        roi_import = ColonyROIImportCSV(data_dir=DATA_DIR)
        colony_count = roi_import.colony_count()

        roi_data = roi_import.colony_data()

        self.assertEqual(colony_count, 16)
        self.assertEqual(len(roi_data), 16)

if __name__ == "__main__":
    unittest.main()
