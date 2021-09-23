# Dataset API
- Convert dataset or original data into STGCN input data format(Kinetic dataset format)
- The shrec 2017 dataset is currently supported, and the original data is processed after obtaining the skeleton data through mediapipe
# Usage

1. setup
- pip install -r requirements.txt

2. run command
- python shrec_hand.py
- python origindataToJson.py
- python mediapipe_gendata.py