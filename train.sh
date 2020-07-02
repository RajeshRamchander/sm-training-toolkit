aws sagemaker create-training-job --training-job-name sklearn-byoc-training-toolkit-002 \
    --algorithm-specification \
    TrainingImage=266000547366.dkr.ecr.us-east-1.amazonaws.com/sklearn-byoc-training-toolkit:latest,TrainingInputMode=File \
    --role-arn arn:aws:iam::266000547366:role/rajramch-sagemaker \
    --input-data-config '[
        {
            "ChannelName": "train",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://rajramch-sagemaker/byoc/train/input/",
                    "S3DataDistributionType": "FullyReplicated"
                }
            },
            "CompressionType": "None",
            "RecordWrapperType": "None"
        }
    ]' \
    --output-data-config S3OutputPath=s3://rajramch-sagemaker/byoc/train/model/ \
    --resource-config InstanceType=ml.m5.large,InstanceCount=1,VolumeSizeInGB=1 \
    --stopping-condition MaxRuntimeInSeconds=86400
