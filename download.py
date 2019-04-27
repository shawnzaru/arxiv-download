import os.path
from subprocess import call
from time import time
from datetime import datetime

import config

class DownloadManager(object):

  def __init__(self):
    self.config = config.ArXivConfig

  def _list_src_objects(self):
    cmd = self.config.CMD_PREFIX_LS + self.config.CMD_BUCKET_SRC
    call(cmd, shell=True)

  def _list_pdf_objects(self):
    cmd = self.config.CMD_PREFIX_LS + self.config.CMD_BUCKET_PDF
    call(cmd, shell=True)

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
    cmd = self.config.CMD_PREFIX_CP \
        + self.config.CMD_BUCKET_SRC \
        + self.config.SRC_MANIFEST_FILE + ' ' \
        + self.config.SRC_DIR
    call(cmd, shell=True)

  def download_pdf_manifest(self):
    cmd = self.config.CMD_PREFIX_CP \
        + self.config.CMD_BUCKET_PDF \
        + self.config.PDF_MANIFEST_FILE + ' ' \
        + self.config.PDF_DIR
    call(cmd, shell=True)

if __name__ == '__main__':
  dm = DownloadManager()
  #dm._list_src_objects()
  #dm._list_pdf_objects()

  if dm.check_src_manifest_exists():
    print("src manifest exists.")
  else:
    print("src manifest does not exist. Download src manifest...")
    dm.download_src_manifest()

  if dm.check_pdf_manifest_exists():
    print("pdf manifest exists")
  else:
    print("pdf manifest does not exist. Download pdf manifest...")
    dm.download_pdf_manifest()

  print(dm._get_timestamp_suffix())
