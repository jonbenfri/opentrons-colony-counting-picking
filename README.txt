Colony Counting and Picking
===========================

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
  * `plate.colonies('1')`


=====
Image Normalization

Use Homography Matrix with OpenCV:
	https://stackoverflow.com/questions/41995916/opencv-straighten-an-image-with-python

====
Get data from ImageJ Colony Counting plugin into octave:
* Modified ReadImageJROI.m from:
  * https://github.com/DylanMuir/ReadImageJROI/blob/master/ReadImageJROI.m

* Run ImageJ on plate image, close ImageJ
* Regions of Interest (ROI) zip file is generated
* Run octave-cli (example):
  * [csvROIs] = ReadImageJROI("photos/600px-E.coliAgarpicture.jpg-RoiSet.zip");
* Example: Access coordinates of ROI curve for first colony in list
  * csvROIs(1){1}.mnCoordinates
  * Save to file: csvwrite("data.csv", csvROIs(1){1}.mnCoordinates)
