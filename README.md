
# CS 598: Deep Learning for Healthcare
- Instructor: Dr. Jimeng Sun
- Team Members:
	- Carmelita Valimento
	- William Su
	- Austin Harmon
  
## Final Project
Replication Paper #42: “Investigating Sleep Apnea in Children with a Specialized Multi-Modal Transformer”

## GitHub Repository Link
- Original Paper: https://github.com/healthylaife/Pediatric-Apnea-Detection
- Team 4 Repository: https://github.com/dlh-team-4/t4

## Demo Video Link
- TODO: add video link

# Prerequisites

## Installing the right dependency versions
Run the following command to install all the necessary libraries. Newer versions might also work, but it is not guaranteed.
`pip3 install -r ./requirements.txt`

## Data installation

1.  To install the data, we requested access by first taking the UIUC HIPAA training and then presenting our use case to NSRR for approval.
    
2.  Once approved, we used [nsrr-gem](https://github.com/nsrr/nsrr-gem/blob/master/README.md#prerequisites) to download the datasets we needed.
    
	a.  For the CHAT data, we executed the command:  
	    `nsrr download chat/polysomnography/edfs/baseline  `
	    We also needed the NSRR annotations for each edf file downloaded using the previous command:  
	    `nsrr download chat/polysomnography/annotations-events-nsrr/baseline`
	    
	b.  For the NCH data, we executed the command:
    

3.  Once downloaded, we took note of the dataset directory and supplied it to the directory variables found in the notebooks.

## Running the files

There's a certain order in running the notebooks:

 1. **CHAT_Preprocessor.ipynb** - takes the raw .edf and .xml files from the CHAT dataset and compresses each one into its own .npz file.
 2. **CHAT_Data_Loader.ipynb** - takes .npz files from the previous notebook and compresses them further into K number of files, representative of each fold.
 3.  **NCH_Preprocessor.ipynb** - takes the raw .edf and .xml files from the NCH dataset and compresses each one into its own .npz file.
 4. **NCH_Data_Loader.ipynb** - takes .npz files from the previous notebook and compresses them further into K number of files, representative of each fold.
 5.  **Trainer_Evaluator.ipynb** - builds the .pt model file, trains it, and evaluates its performance against a given set of metrics.

## Final Output
At the end of the training, it will create a `results` folder in the same directory with a `.txt` file of the different metrics measures during evaluation.
