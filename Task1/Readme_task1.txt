To solve this task, i traversed through some resarch papers published on the same topic.

One of the resarch paper deeply explained the process and how the algorithm can be implemented
by only using the Redness of each pixel in a frame.

The reference paper has been included in the reference folder of Task1

Implementation of this task took the following steps:
->Converting the video into frames
->Traverseing the frame and find the Red part of each pixel
->The plot of Redness against frames had peaks in it
->These peaks signifies the time at wich your heart pumps the blood
->The duration between two peaks signify the time between two pulses
->Accordingly the algorithmcalculates the Heart Rate

The output graph was plotted in Matlab for reference and is included in the Task1 folder.

Pre-requisites to run the code on local machine:
1. Install pillow for python
2. Install opencv for python
3. Install scipy for python
4. Install numpy for python
5. Install tkinter for python

Copy all the files and folders under "Task1" in a single directory for ease of use

For best results with this algorith record the finger video on 30FPS settings.

The code trims the video uploaded into a 10 secend video and then save it frame by frame
into 300 different frames

These frames are then read by the alogorithm and accordingly the results are processed.

The "Temp" folder here is used to store the trimmed video and the frames.

The test videos ued were shot on Vivo V15 Pro on 30FPS 
and the algorithm was designed for the same

You can changes the file paths in the code accordingly as mentioned and run the code for results.

A video demonstration of implementation has also been included in the same folder.