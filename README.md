# Assignment_2_repo
Repository for GEOG5003M assignment 2 files
## Contents
1. Data_out.txt: Text file containing output data from the program
2. LICENCE: File containing information regarding the licencing of the contents associated with this project
3. Lidar.txt: Text file containing the input lidar data
4. Radar.txt: Text file containing the input radar data
5. single_iceberg_model.py: Python file containing the model associated with this project
### What is the software?
The software takes in two data files containing information about an area, detecting icebergs and identifying 
if they are appropriate for towing. The lidar file shows the height of a pixel and the radar file shows if a 
pixel is ice or water. The radar file is used to determine where pixels are ice within the area. 
Equivalent heights are then pulled from the lidar files before a series of calculations are performed to 
determine the iceberg size, volume, mass and towability. This is all controlled by the user within a GUI which
shows the input datasets in a graphical format and the model results.
#### How can the software be run?
The GUI contains a series of buttons that show the input datasets, run the program, show the results and 
close the GUI. Upon closing of the GUI the program will finish. The results button is restricted to only 
be enabled after the program is run and to only be clicked once before being disabled again.
##### What are the expected outputs?
This model has two expected outputs. First, the results are written to the GUI upon user command. 
Second, the results are written out to a datafile.
