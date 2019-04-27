import boto3
import os.path
from time import time
from datetime import datetime

import config

class DownloadManager(object):

  def __init__(self):
    self.config = config.ArXivConfig
    self.session = boto3.session.Session(
        aws_access_key_id=self.config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=self.config.AWS_SECRET_ACCESS_KEY,
        profile_name = self.config.PROFILE_NAME)
    self.client = self.session.client('s3')

  def _list_objects(self, prefix):
    paginator = self.client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(
        Bucket = self.config.BUCKET,
        Prefix = prefix,
        RequestPayer = 'requester')
    for page in page_iterator:
      for content in page['Contents']:
        print(content['Key'])

  def _list_src_objects(self):
    self._list_objects(self.config.SRC_PREFIX)

  def _list_pdf_objects(self):
    self._list_objects(self.config.PDF_PREFIX)

  def check_src_manifest_exists(self):
    manifest_path = self.config.SRC_DIR + self.config.SRC_MANIFEST_FILE
    return os.path.exists(manifest_path)

  def check_pdf_manifest_exists(self):
    manifest_path = self.config.PDF_DIR + self.config.PDF_MANIFEST_FILE
    return os.path.exists(manifest_path)

  def check_src_manifest_md5_identical(self):
    pass

  def check_pdf_manifest_md5_identical(self):
    pass

  def _get_timestamp_suffix(self):
    ts = time()
    suffix = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    return suffix

  def rename_old_src_manifest(self):
    pass

  def rename_old_pdf_manifest(self):
    pass

  def download_src_manifest(self):
    pass

  def download_pdf_manifest(self):
    pass

if __name__ == '__main__':
  dm = DownloadManager()
  #dm._list_src_objects()
  #dm._list_pdf_objects()

  if dm.check_src_manifest_exists():
    print("src manifest exists")
  else:
    print("src manifest does not exist")

  if dm.check_pdf_manifest_exists():
    print("pdf manifest exists")
  else:
    print("pdf manifest does not exist")

  print(dm._get_timestamp_suffix())
