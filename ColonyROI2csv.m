% Octave script to convert ImageJ ROI dataset from binary to JSON format
% Note: Octave uses 1-indexing (indices are from 1 to N)

ROI_SET_DIR = 'photos';
ROI_FILE = '600px-E.coliAgarpicture.jpg-RoiSet.zip';
DATA_DIR = 'data';

% `ReadImageJROI.m` function file is assumed to be in working directory

[csvROIs] = ReadImageJROI([ROI_SET_DIR filesep() ROI_FILE]);

for (i = csvROIs)
    colony_str = char(i(1){1}.strName);
    csvwrite([DATA_DIR "/" colony_str ".csv"], i(1){1}.mnCoordinates);
end;
