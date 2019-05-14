# OpenTrons Hack-A-Tron 2019 Hackathon



May 10 6PM EDT - May 11 6PM EDT

Slack workspace: https://hack-a-tron.slack.com 

[Invite link](https://hack-a-tron.slack.com/join/shared_invite/enQtNjMyMDY1Mjg1NjA0LWQyN2ZjZDU1NmM3YWNjMjQxMmNjNjM0MTdmMGVkY2ZmNmYwZTEyYmZjNWExM2JhNjM0MGI2NDgyMjJiOWQ3N2E)

Join the [#colony_counting](https://hack-a-tron.slack.com/messages/CJ94E3MFV/) channel.

## Colony Counting and Picking

### Description

**Colony counting and picking functionality for OpenTrons.**

Pre-prepped agar plates with visible colonies are loaded onto the OpenTrons deck. Colony location data is uploaded to OpenTrons. After calibration, OpenTrons picks individual colonies using pipettor for processing.

### Ideas

* Add a camera to head assembly
  * Take photo
  * Add custom instrument
  * Add `capture_image` function

* Add agar plate labware
  * Calibrate robot position
  * https://docs.opentrons.com/examples.html?highlight=vector#precision-pipetting

* Add `count_colonies` function
  * ImageJ --headless: https://imagej.nih.gov/ij/plugins/colony-counter.html
  * Run macro: ImageJ --headless -macro custom_macro.ijm
  * Returns count

* Add second camera for depth detection
  * https://docs.opencv.org/3.1.0/dd/d53/tutorial_py_depthmap.html

* Add `analyze_colonies` function
  * Returns count
  * Returns list of colonies with (x,y,z) coordinates

* Adjust agar plate labware object to include (x,y,z) coordinates of each colony
  * Intuitive interface can be something like: `plate.colonies('1')`
  * Use center of mass for each colony (e.g. move_to plate.colonies('1') will go to center of mass or centroid)

* Alternative: Take image of agar plate, each pixel is a "well" e.g. 800 x 600 image = 480000 wells

* Image Normalization
  * Perspective correction using homography with OpenCV:
    * https://docs.opencv.org/3.4.1/d9/dab/tutorial_homography.html#tutorial_homography_Demo2
    * https://stackoverflow.com/questions/41995916/opencv-straighten-an-image-with-python

### Instructions

This repository provides a way to import ImageJ regions of interest (ROI) data into python.

ImageJ outputs ROI data in a binary format. Dylan Muir provides a [Matlab script](https://github.com/DylanMuir/ReadImageJROI/blob/master/ReadImageJROI.m) to read binary ROI data to import into Matlab.

We use Octave, an open-source Matlab clone, to convert ROI data from binary to csv format for import into python.

#### Requirements

* [Octave](https://www.gnu.org/software/octave/)
* [ImageJ](https://imagej.nih.gov/ij/)
* [ImageJ Colony Counter plugin](https://imagej.nih.gov/ij/plugins/colony-counter.html)
* [OpenTrons](http://web.archive.org/web/20190514124729/https://opentrons.github.io/Hack-A-Tron/development_setup)

1. Obtain plate image
1. Run ImageJ Colony Counter on plate image (note location of ROI zip file output)
1. Edit variables in `ColonyROI2csv.m` (create `DATA_DIR` if it doesn't exist)
1. Import data into python (example):
```python
from colony_roi_import import ColonyROIImportCSV

DATA_DIR = "data"

roi_import = ColonyROIImportCSV(DATA_DIR)

colony_count = roi_import.get_colony_count()
colony_roi_data = roi_import.colony_data()
```
Colony roi data is a python dictionary:
```python
colony_data = {
	'colony_name': colony_name,
	'roi_data': roi_data,
    }
```

Where `roi_data` is a list of (x,y) pixel coordinates for the boundaries drawn around colonies by ImageJ.

### Future

* Create another python file to extend labware functionality interface, e.g. `plate.colonies('1')`
* Improve `agar_plate.py` to use colony interface
* Use a machine learning algorithm to improve performance of colony detection
