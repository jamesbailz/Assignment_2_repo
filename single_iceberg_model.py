# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:20:04 2021

This model is run from a GUI in which there is a run program button.
Also appearing on the GUI are 'data inputs', 'show results' and 
'close window' buttons. 
Data inputs shows the two input files in a graphical format.
Show results shows the calculation results, only after the program is run.
Close window closes the window and ends the program.
When you run the code, a message will appear 

"""
print ("Program Starting")
#Import statements
import tkinter
import requests
import matplotlib
matplotlib.use ('TkAgg')
import matplotlib.pyplot as plt
import csv
import time

"""
Stage 1: Initialise GUI main window
"""
root = tkinter.Tk ()
root.wm_title ("Iceberg-towing Model")

"""
Stage 2: Download data from Web to files
"""
#Download timing start
start_download = time.time ()

print ("Downloading Web data to files")
#Downloading data and writing to files function
def download (url):
    """
    Downloads web data and writes it to a file

    Parameters
    ----------
    url : String
        Web address used as the data source.

    Returns
    -------
    None.

    """
    path, url = url
    r = requests.get (url, stream = True)
    content = r.text
    #print (content)
    with open (path + '.txt', 'w') as f:
        f.write (content)
#List of url web data
urls = [('Lidar', 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.lidar'),
        ('Radar', 'https://www.geog.leeds.ac.uk/courses/computing/study/core-python-odl2/assessment2/white1.radar')]
#Call download function
for x in urls:
    download (x)

"""
Stage 3: Reading csv data into lists
"""
print ("Reading csv data")
#Reading csv into lidar
lidar = []
with open ('Lidar.txt', newline = '') as f1:
    reader = csv.reader (f1, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        #print (row)
        rowlist_L = []
        for value in row:
            #print (value)
            rowlist_L.append (int (value))
        lidar.append (rowlist_L)
#for row in lidar:
    #print ("length of row:", len (row))
    #List contains empty rows
#Remove empty rows
lidar_clean = [x for x in lidar if x != []]
#print ("lidar2 length =", len(lidar_clean))
# for row in lidar_clean:
#     print ("length of row:", len (row))
#Data familiaristation
# print (lidar_clean)
# print (type(lidar_clean))
# print ("Lidar length = ", len(lidar_clean))
#Reading csv into radar
radar = []
with open ('Radar.txt', newline = '') as f2:
    reader2 = csv.reader (f2, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader2:
        #print (row)
        rowlist_R = []
        for value in row:
            #print (value)
            rowlist_R.append (int (value))
        radar.append (rowlist_R)
#for row in radar:
    #print ("length of row:", len (row))
    #list contains empty rows
#remove empty rows
radar_clean = [x for x in radar if x != []]
#for row in radar_clean:
    #print ("length of row:", len (row))
#Data familiarisation
# print (radar_clean)
# print (type(radar_clean))
# print ("Radar length = ", len(radar_clean))

#Download and list creation timing
end_download = time.time ()
download_time = (end_download - start_download)
print ("Download to reading in time: " + str(download_time))

# """
# Displaying lidar and radar data
# """
# #Code based on https://www.kite.com/python/answers/how-to-show-two-figures-at-once-in-matplotlib-in-python
# #Define axes
# plt.ylim = (0, 300)
# plt.xlim = (0, 300)
# #Lidar plot
# lidar_plot = plt.figure (1)
# #Assign title
# plt.title ('Lidar data')
# plt.imshow (lidar_clean)
# #Radar plot
# radar_plot = plt.figure (2)
# #Assign title
# plt.title ('Radar data')
# plt.imshow (radar_clean)
# #Show plots
# plt.show ()
#Commented code above has been moved into the GUI so removed here

"""
Stage 4: Finding ice areas and pulling their heights
"""
#Calculation timing
start_calculation = time.time ()
#Data familiarisation
# print (radar_clean [145][150])
# print (radar_clean [145])
# print (lidar_clean [145][150])
# print (lidar_clean [145])
print ("Locating ice and pulling heights")
#Pulling heights from lidar data
def pull_heights ():
    """
    Pulls height values from the lidar data from ice locations within the 
    radar data, appending the heights to an ice list

    Returns
    -------
    None.

    """
    global ice
    ice = []
    for i in range (len (radar_clean)):
        for j in range (len (radar_clean)):
            radar_clean [i][j] = lidar_clean [i][j]
            #print (radar_clean [i][j])
            if (radar_clean [i][j]) > 100:
                #print (radar_clean [i][j])
                ice.append (lidar_clean [i][j])
#print (ice)
#print (len (ice))
print ("Ice located and heights pulled")

"""
Stage 5: Calculating ice mass
"""
print ("Determining iceberg size")
#Pull heights
def calculations ():
    pull_heights ()
    ice_size = (len(ice))
    #print ("ice size:", ice_size)
    #Calculating ice volume above sea level
    print ("Calculating ice mass")
    #Convert ice values from cm to m
    ice_m = ((sum (ice)) * 0.1)
    #print (ice_m)
    #Calculating ice volume above surface
    global ice_volume_positive
    ice_volume_positive = (ice_size * ice_m)
    #print (ice_volume_positive)
    #Calculating sub-surface ice volume
    global ice_volume_subsurface
    ice_volume_subsurface = ice_volume_positive * 10
    #print (ice_volume_subsurface)
    #Calculating total ice volume
    global ice_volume
    ice_volume = ice_volume_positive + ice_volume_subsurface
    #print (ice_volume)
    #Calculating ice mass
    global ice_mass
    ice_mass = 900 * ice_volume
    #print (ice_mass)
    print ("Ice mass calculated")
    run = tkinter.Label\
        (text= ("Running Program" + "\n"))
    run.pack ()
    results_btn ['state'] = 'normal'

# """
# Stage 6: Calculating towability
# """
# print ("Calculating towability")
# def towability ():
#     """
#     Determines the towability of the iceberg

#     Returns
#     -------
#     None.

#     """
#     if ice_mass > 36000000:
#         print ("Iceberg cannot be towed")
#     else:
#         print ("Iceberg can be towed")
# print ("Towability calculated")
#Commented towability code above moved into GUI so removed here
#Calculation timing
end_calculation = time.time ()
calculation_time = (end_calculation - start_calculation)
print ("Calculation time: ", calculation_time)

# """
# Stage 6: Writing data out to a file
# """
# with open ("Data_out.txt", 'w') as FO:
#     FO.write ("Above surface volume: " + str(ice_volume_positive) + '\n')
#     FO.write ("Subsurface volume: " + str(ice_volume_subsurface) + '\n')
#     FO.write ("Total ice volume: " + str(ice_volume) + '\n')
#     FO.write ("Total mass: " + str(ice_mass) + '\n')
    
"""
Stage 6: Initialise and populate GUI
"""
#Label code based on https://www.python-course.eu/tkinter_text_widget.php
#Create GUI description
description = tkinter.Label\
    (text="This GUI runs the Iceberg Towability Model and shows its inputs and results"\
      + '\n')
description.pack ()

#Create user defined run
# menu_bar = tkinter.Menu (root)
# root.config (menu = menu_bar)
# model_menu = tkinter.Menu (menu_bar)
# menu_bar.add_cascade (label= "Model", menu= model_menu)
# model_menu.add_command (label= "Run Model", command= calculations)
run_btn = tkinter.Button (root, text= 'Run Program', command = calculations)
run_btn.pack (side= 'top', fill= 'both')

#Show input data graphs
def show_graphs ():
    plt.ylim = (0, 300)
    plt.xlim = (0, 300)
    #Set up lidar plot to figure 1
    lidar_plot = plt.figure (1)
    #Assign title
    plt.title ('Lidar data')
    #Assign data
    plt.imshow (lidar_clean)
    #Set up radar plot to figure 2
    radar_plot = plt.figure (2)
    #Assign title
    plt.title ('Radar data')
    #Assign data
    plt.imshow (radar_clean)
    #Show plots
    plt.show ()
    
#Display the results
def show_results ():
    """
    Generates the program results, calculates towability
    and disables the results button post-execution

    Returns
    -------
    None.

    """
    #Total volume
    vol = tkinter.Label\
        (text= ("Total volume: " + str (ice_volume) + " m\u00b2"))
    vol.pack ()
    #Total mass
    mass = tkinter.Label\
        (text= ("Total mass: " + str (ice_mass) + " kg"))
    mass.pack ()
    #Towability
    print ("Calculating towability")
    if ice_mass > 36000000:
        tow = tkinter.Label (text = "Iceberg cannot be towed")
    else:
        tow = tkinter.Label (text = "Iceberg can be towed")
    print ("Towability calculated")
    tow.pack ()
    #Disable button after 1 click
    #Code based on https://www.youtube.com/watch?v=QfTo3rK3e48
    results_btn ['state'] = 'disabled'
    
#Close window
def quit (event=None):
    """
    Quits and closes the GUI to end the program at a time of the user's choice

    Parameters
    ----------
    event : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """
    root.destroy ()
    
#Create and pack buttons
quit_btn = tkinter.Button (root, text= 'Close Window', command = quit)
quit_btn.pack (side='bottom', fill= 'both')
results_btn = tkinter.Button (root, text= 'Show Results', \
                              command = show_results, state= "disabled")
results_btn.pack (side='bottom', fill= 'both')
graph_btn = tkinter.Button (root, text= 'Data inputs', command = show_graphs)
graph_btn.pack (side= 'bottom', fill= 'both')
#Activate window
root.mainloop ()

"""
Stage 7: Writing data out to a file
"""
with open ("Data_out.txt", 'w') as FO:
    FO.write ("Above surface volume: " + str(ice_volume_positive) + '\n')
    FO.write ("Subsurface volume: " + str(ice_volume_subsurface) + '\n')
    FO.write ("Total ice volume: " + str(ice_volume) + '\n')
    FO.write ("Total mass: " + str(ice_mass) + '\n')

#Finish program
print ("Program Ended")
print ("Thank you for running the program")