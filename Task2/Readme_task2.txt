To understand the task better, I did some study and found a resarch paper published
on a similar topic.

The paper talked about how Accelerometer data can be used to calculate distance travelled

The reference paper has been included in the reference folder of Task2

Implementation of this task took the following steps:
->Taking Accelerometer data from Matlab Mobile
->Convert the .csv file into .xlsx file
->Calculate the total Magnitude of Accelerometer
->This data can be plotted against time for reference
->A peak detection algorithm was designed
->A threshold/filter value was also chosen
->Step Size was calculated the distance was calculated by implementing the algorithm
->Average step size was calculate while walking
->Number of steps were accordingly calculated.

*The filter threshold for my dataset was taken 12.78
*My average step size was 80cm

The graph was also plotted in Matlab for reference and is included in the Task2 Folder.

Pre-requisites to run the code on local machine:
1. Install openpyxl for python
2. Install pandas for python

The data from accelerometer collected by using MATLAB Mobile is in .csv format

It is first converted into .xlsx and then further interpreted.

The "Temp" folder in the directory is used to save this file in .xlsx format

You can changes the file paths in the code accordingly as mentioned and run the code for results.

The accelerometer data in .csv format has also been included in the Task2 folder.

A video demonstration of implementation has also been included in the same folder.
