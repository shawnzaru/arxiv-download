import os.path
import hashlib
from subprocess import call
from time import time
from datetime import datetime

import config

class DownloadManager(object):

  def __init__(self):
    self.config = config.ArXivConfig

  def _list_src_objects(self):
    call(self.config.CMD_LS_SRC, shell=True)

  def _list_pdf_objects(self):
    call(self.config.CMD_LS_PDF, shell=True)

  def _check_dryrun(self, cmd, dryrun):
    if dryrun:
      cmd += ' ' + '--dryrun'
    return cmd

  def sync_all(self, dryrun=True):
    print(self._check_dryrun(self.config.CMD_SYNC_ALL, dryrun))

  def sync_src(self, dryrun=True):
    print(self._check_dryrun(self.config.CMD_SYNC_SRC, dryrun))

  def sync_pdf(self, dryrun=True):
    print(self._check_dryrun(self.config.CMD_SYNC_PDF, dryrun))

  def check_src_manifest_exists(self):
    manifest_path = self.config.SRC_DIR + self.config.SRC_MANIFEST_FILE
    return os.path.exists(manifest_path)

  def check_pdf_manifest_exists(self):
    manifest_path = self.config.PDF_DIR + self.config.PDF_MANIFEST_FILE
    return os.path.exists(manifest_path)

  def _get_content_md5(self, file_path):
    return hashlib.md5(open(file_path, 'rb').read()).hexdigest()

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
    call(self.config.CMD_DOWNLOAD_SRC_MANIFEST, shell=True)

  def download_pdf_manifest(self):
    call(self.config.CMD_DOWNLOAD_PDF_MANIFEST, shell=True)

  def download_src_object(self, tar, dryrun=True):
    cmd = self.config.CMD_DOWNLOAD_SRC_OBJECT % tar
    cmd = self._check_dryrun(cmd, dryrun)
    call(cmd, shell=True)

  def download_pdf_object(self, tar, dryrun=True):
    cmd = self.config.CMD_DOWNLOAD_PDF_OBJECT % tar
    cmd = self._check_dryrun(cmd, dryrun)
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
    print("pdf manifest exists.")
  else:
    print("pdf manifest does not exist. Download pdf manifest...")
    dm.download_pdf_manifest()

  print(dm._get_timestamp_suffix())
  print(dm._get_content_md5(dm.config.SRC_DIR + dm.config.SRC_MANIFEST_FILE))

  dm.download_src_object('arXiv_src_0001_001.tar')
  dm.download_pdf_object('arXiv_pdf_0001_001.tar')
  dm.sync_all()
  dm.sync_src()
  dm.sync_pdf()
