# Fingerprinting
**Analyzes encrypted web-traffic patterns to identify certain websites**

The user inputs a PCAP file. Using PCAP training files, the fingerprinter analyzes web traffic (incoming and outgoing packets, time intervals between packets, etc) and then labels and appends them to a dataframe.
A naive-bayes classifier is trained based on the training data which then offers a prediction about what website the input file belongs to.

## How to Run
Ensure that all of the pcap files are in the same directory as preprocess.py

Navigate to the same directory in terminal and then run the following (using autolab as example):

python3 fingerprinter.py test7\(autolab\).pcap 
