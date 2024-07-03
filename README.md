**Speech Emotion Detection Project Report**

**Introduction**

This project aims to develop a machine learning-based system to classify emotions in speech audio files. The project involves extracting audio features, training models for gender and emotion classification, and building a graphical user interface (GUI) for ease of use.

**Background**
Emotion detection in speech is a challenging task with applications in customer service, healthcare, and entertainment. By analyzing audio features such as MFCCs, chroma, and spectral contrast, it is possible to identify the emotional state of the speaker.

**Learning Objectives**
•	Understand the principles of audio feature extraction.
•	Learn to preprocess audio data for machine learning tasks.
•	Develop classification models using scikit-learn.
•	Implement a user-friendly GUI for real-time emotion detection.

**Activities and Tasks**

1.	Data Preparation:
o	Collected and organized the TESS Toronto emotional speech set data.
o	Categorized the dataset by gender and emotions.
2.	Feature Extraction:
o	Extracted MFCCs, chroma, and spectral contrast features from audio files using librosa library.
o	Plotted and analyzed the features for both male and female voices.
3.	Model Training:
o	Prepared datasets for gender and emotion classification.
o	Trained RandomForestClassifier models for both tasks.
o	Evaluated model performance using classification reports.
4.	GUI Development:
o	Built a GUI using Tkinter for file selection, audio recording, and emotion detection.
o	Integrated the trained models into the GUI for real-time classification.

**Skills and Competencies**

•	Technical Skills:
o	Audio signal processing with librosa and pydub.
o	Machine learning model development with scikit-learn.
o	GUI development with Tkinter.

•	Analytical Skills:
o	Data preprocessing and feature extraction.
o	Model evaluation and performance tuning.

**Feedback and Evidence**

•	Model Performance:
o	Gender classification achieved high accuracy, distinguishing between male and female voices effectively.
o	Emotion classification provided reasonable accuracy across various emotional states, with detailed classification reports.

•	GUI Usability:
o	The GUI was tested for functionality, ensuring seamless file selection, recording, and emotion detection.

**Challenges and Solutions**

•	Challenge:
o	Handling different audio formats and ensuring consistent feature extraction.
Solution:
o	Standardized audio file format and sample rates using pydub and librosa.

•	Challenge:
o	Misalignment between emotion labels and model predictions due to string label handling.
Solution:
o	Converted emotion labels to numerical values during model training and prediction.

**Outcomes and Impact**

•	Technical Outcome:
o	Successfully developed a dual-classification system for gender and emotion detection in speech audio.
o	Created a user-friendly GUI for practical application and demonstration.

•	Personal and Professional Impact:
o	Enhanced understanding of audio processing and machine learning.
o	Gained practical experience in developing and deploying machine learning models.

**Conclusion**
The Speech Emotion Detection project achieved its goals of developing an accurate and efficient system for classifying emotions in speech audio. The project provided valuable insights into the complexities of audio processing and machine learning, culminating in a practical and user-friendly application. Future work could involve expanding the dataset, improving model accuracy, and exploring real-time processing capabilities.


