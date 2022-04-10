# SRIP2022_Submission

<h3>Task 1:</h3>
To solve this task, I traversed through some resarch papers published on the same topic.<br><br>

One of the resarch paper deeply explained the process and how the algorithm can be implemented
by only using the Redness of each pixel in a frame.<br><br>

The reference paper has been included in the reference folder of Task1<br><br>

Implementation of this task took the following steps:<br>
->Converting the video into frames<br>
->Traverseing the frame and find the Red part of each pixel<br>
->The plot of Redness against frames had peaks in it<br>
->These peaks signifies the time at wich your heart pumps the blood<br>
->The duration between two peaks signify the time between two pulses<br>
->Accordingly the algorithmcalculates the Heart Rate<br><br>

The other details about the Task and how to deploy it are in the "Readme_task1" file under Task1 folder<br><br>

The video demonstration of Task 1 is <a href="https://drive.google.com/file/d/1LdtaNA5O-G-pwPnx2BB5Ph_-T84_PaiH/view?usp=sharing
">here</a><br><br><hr>

<h3>Task 2:</h3>
To understand the task better, I did some study and found a resarch paper publised
on a similar topic.<br><br>

The paper talked about how Accelerometer data can be used to calculate distnce travelled<br><br>

The reference paper has been included in the reference folder of Task2<br><br>

Implementation of this task took the following steps:<br>
->Taking Accelerometer data from Matlab Mobile<br>
->Convert the .csv file into .xlsx file<br>
->Calculate the total Magnitude of Accelerometer<br>
->This data can be plotted against time for reference<br>
->A peak detection algorithm was designed<br>
->A threshold/filter value was also chosen<br>
->Step Size was calculated the distance was clculated by implementing the algorithm<br>
->Average step size was calculate while walking<br>
->Number of steps were accordingly calculated.<br><br>

The other details about the Task 2 and how to deploy it are in the "Readme_task2" file under Task2 folder<br><br>

The video demonstration of Task 2 is <a href="https://drive.google.com/file/d/1885JOvdvGUh8z36CrKPAjOTxyQCx60F3/view?usp=sharing">here</a><br><br><hr>

<h3>Task 3:</h3>
This was my first experience working with both TensorFlow and App development.<br><br>

To complete this task I have followed the example given <a href="https://www.tensorflow.org/lite/examples/audio_classification/overview">here</a><br><br>

For solving this task a pre-trained model "YAMnet" was taken in use.<br><br>

YAMnet is a highly specialized model that can even differenciate between sounds made by
insects, birds and even differenciate between different different kind of noise 
like white noise, traffic etc.<br><br>

As the question required the classifiation only among Scilence, Speech and Noise,
accordingly changes were made in the "ProbabilitiesAdapter.kt" file of the given example.<br><br>

Further some changes were made in the UI to meet the problem statement.
A screenshot displaying the same has been attached in the "Task3"<br><br>

These changes allowed me to use the highly spealized model in a more generalized manner.<br><br>

The other details about the Task 3 and how to deploy it are in the "Readme_task3" file under Task3 folder<br><br>
The video demonstration of Task 3 is <a href="https://drive.google.com/file/d/1bIn-FoeXaHuOoDRmfNfFjhRWlu-Dl0E8/view?usp=sharing">here</a><br><br><hr>
