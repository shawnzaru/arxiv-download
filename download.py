import boto3
import config

# create session, resource and paginator
session = boto3.session.Session(profile_name=config.ArXivConfig.PROFILE_NAME)
client = session.client('s3')
paginator = client.get_paginator('list_objects_v2')

page_iterator = paginator.paginate(Bucket='arxiv', Prefix='src', RequestPayer='requester')

for page in page_iterator:
  for content in page['Contents']:
    print(content['Key'])
