# Creating a dataset using data from S3 endpoint

Table of Contents
=================
* [Introduction](#introduction)
* [Loading Data into S3](#loading-data-into-s3)
* [Creating a Dataset](#creating-a-dataset)

## Introduction

DIGITS may also be trained on data stored at an S3 endpoint. This can be useful for cases in which data has been stored on a different node and the user does not want to have to manually migrate the data over to the node running DIGITS.

## Loading Data into S3

As an example, we will use the dataset provided by running
```sh
python -m digits.download_data mnist ~/mnist
```

We have provided a Python script "upload_s3_data.py" that can be used to upload these files into a configured S3 endpoint. This script and its accompanying configuration file "upload_config.cfg" is located at digits/digits/tools.

```sh
[S3 Config]
endpoint = http://your-s3-endpoint.com:80
accesskey = 0123456789abcde
secretkey = PrIclctP80KrMi6+UPO9ZYNrkg6ByFeFRR6484qL
bucket = digits
prefix = mnist
```

Below is a brief description of each field:

**endpoint** - This specifies the URL of the endpoint where the S3 data will be stored.

**accesskey** - The access key which will be used to authenticate your access to the endpoint.

**secretkey** - The secret key which will be used to authenticate your access to the endpoint.

**bucket** - The name of the bucket where this data should be stored. If it does not exist, it will be created by the script.

**prefix** - The prefix which will be prepended to all of the key names. This will be used later during the creation of the dataset.

Once that file has been configured appropriately, it may be run using:

```sh
python upload_mnist.py ~/mnist
```

Be patient as this upload process will take quite a bit of time to complete, depending heavily on network speed and the computing resources of the S3 endpoint.


## Creating a Dataset

Next, to get the data from S3, go to S3 tab.

![Create Dataset](create-dataset.png)

