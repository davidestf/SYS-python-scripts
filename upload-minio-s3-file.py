#!/usr/bin/env/python
import boto3
from botocore.client import Config


s3 = boto3.resource('s3',
                    endpoint_url='http://minio.staffieri.co.uk:9000',
                    aws_access_key_id='minio',
                    aws_secret_access_key='minio123',
                    config=Config(signature_version='s3v4'),
                    region_name='uk-lon1')




##create bucket
response = s3.create_bucket(Bucket='mytestbucket',
           CreateBucketConfiguration={'LocationConstraint':'uk-lon1'})

## upload a file from local file system 
s3.Bucket('test').upload_file('/root/miniotest/miniotest.txt','miniotest.txt')

# download the object  and save it to local FS 
s3.Bucket('test').download_file('miniotest.txt', '/tmp/miniotestdownload.txt')

print ("successfull")

