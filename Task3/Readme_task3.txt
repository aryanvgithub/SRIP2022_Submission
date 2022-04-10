This was my first experience working with both TensorFlow and App development.

To complete this task I have followed the example given on 
https://www.tensorflow.org/lite/examples/audio_classification/overview

For solving this task a pre-trained model "YAMnet" was taken in use.

YAMnet is a highly specialized model that can even differenciate between sounds made by
insects, birds and even differenciate between different kind of noise 
like white noise, traffic etc.

As the question required the classifiation only among Scilence, Speech and Noise,
accordingly changes were made in the "ProbabilitiesAdapter.kt" file of the given example.

Further some changes were made in the UI to meet the problem statement.
A screenshot displaying the same has been attached in the "Task3"

These changes allowed me to use the highly specialized model in a more generalized manner.

To deploy and check my work,
->Follow and clone the repository given in the above quoted example.
->Run the specifed android file in Android Studio 
->Open the "ProbabilitiesAdapter.kt" file 
->Replace the code there with the code in "Code.txt" file from Task3
->Run and Deploy the Application

The screenshot of the App interface from my phone has been attached in "Task3"

A video demonstration of implementation has also been included in the same folder.



