FROM 683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-scikit-learn:0.20.0-cpu-py3

RUN pip install sagemaker-training

RUN mkdir -p /opt/ml/code/ && mkdir -p /opt/ml/output/ && mkdir -p /opt/ml/input/ && mkdir -p /opt/ml/model/
COPY train.py /opt/ml/code/train.py

ENV SAGEMAKER_PROGRAM train.py