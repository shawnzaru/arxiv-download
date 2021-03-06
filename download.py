import sys
import os
import os.path
import hashlib
from subprocess import call
from time import time
from datetime import datetime
from distutils.util import strtobool

from config import ArXivConfig as cfg
from manifest import compare_manifest_xml

class DownloadManager(object):

  def _list_src_objects(self):
    call(cfg.CMD_LS_SRC, shell=True)

  def _list_pdf_objects(self):
    call(cfg.CMD_LS_PDF, shell=True)

  def check_data_dir_exists(self):
    return os.path.exists(cfg.DATA_DIR)

  def _check_dryrun(self, cmd, dryrun):
    if dryrun:
      cmd += ' ' + '--dryrun'
    return cmd

  # 'y', 'yes', 't', 'true', 'on' and '1' evaluated to True, otherwise False
  def _yes_or_quit(self):
    ans_str = input("Are you sure you want to continue? [*no*|yes]: ")
    try:
      ans_bool = strtobool(ans_str)
    except:
      ans_bool = False
    if ans_bool == False:
      print("The program exits.")
      sys.exit(0)

  def _check_dryrun_with_prompt(self, cmd, dryrun):
    if dryrun:
      cmd += ' ' + '--dryrun'
    else:
      print("You are going to run the following resource-critical command:")
      print(cmd)
      print("Make sure you have more than 2.6TB of free space in %s." % cfg.DATA_DIR)
      print("This process may take over 24 hours. Make sure your SSH session is persistent.")
      self._yes_or_quit()
    return cmd

  def sync_all(self, dryrun=True):
    cmd = cfg.CMD_SYNC_ALL
    cmd = self._check_dryrun_with_prompt(cmd, dryrun)
    call(cmd, shell=True)

  def sync_src(self, dryrun=True):
    cmd = cfg.CMD_SYNC_SRC
    cmd = self._check_dryrun_with_prompt(cmd, dryrun)
    call(cmd, shell=True)

  def sync_pdf(self, dryrun=True):
    cmd = cfg.CMD_SYNC_PDF
    cmd = self._check_dryrun_with_prompt(cmd, dryrun)
    call(cmd, shell=True)

  def check_src_manifest_exists(self):
    return os.path.exists(cfg.SRC_MANIFEST_PATH)

  def check_pdf_manifest_exists(self):
    return os.path.exists(cfg.PDF_MANIFEST_PATH)

  def download_src_manifest(self):
    call(cfg.CMD_DOWNLOAD_SRC_MANIFEST, shell=True)

  def download_pdf_manifest(self):
    call(cfg.CMD_DOWNLOAD_PDF_MANIFEST, shell=True)

  def _download_src_manifest_cache(self):
    call(cfg.CMD_DOWNLOAD_SRC_MANIFEST_CACHE, shell=True)

  def _download_pdf_manifest_cache(self):
    call(cfg.CMD_DOWNLOAD_PDF_MANIFEST_CACHE, shell=True)

  def download_src_object(self, tar, dryrun=True):
    cmd = cfg.CMD_DOWNLOAD_SRC_OBJECT % tar
    cmd = self._check_dryrun(cmd, dryrun)
    call(cmd, shell=True)

  def download_pdf_object(self, tar, dryrun=True):
    cmd = cfg.CMD_DOWNLOAD_PDF_OBJECT % tar
    cmd = self._check_dryrun(cmd, dryrun)
    call(cmd, shell=True)

  def _get_content_md5(self, file_path):
    return hashlib.md5(open(file_path, 'rb').read()).hexdigest()

  def _check_manifest_md5(self, manifest_cache, manifest_local):
    manifest_cache_md5 = self._get_content_md5(manifest_cache)
    manifest_local_md5 = self._get_content_md5(manifest_local)
    print("cache: %s [%s]" % (manifest_cache, manifest_cache_md5))
    print("local: %s [%s]" % (manifest_local, manifest_local_md5))
    return manifest_cache_md5 == manifest_local_md5

  def check_remote_src_manifest_identical(self):
    print("Cache remote src manifest...")
    self._download_src_manifest_cache()
    return self._check_manifest_md5(cfg.SRC_MANIFEST_PATH_CACHE,
                                    cfg.SRC_MANIFEST_PATH)

  def check_remote_pdf_manifest_identical(self):
    print("Cache remote pdf manifest...")
    self._download_pdf_manifest_cache()
    return self._check_manifest_md5(cfg.PDF_MANIFEST_PATH_CACHE,
                                    cfg.PDF_MANIFEST_PATH)

  def _get_timestamp_suffix(self):
    ts = time()
    suffix = datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    return suffix

  def rename_old_src_manifest(self):
    old_name = cfg.SRC_MANIFEST_PATH
    new_name = cfg.SRC_MANIFEST_PATH + '_' + self._get_timestamp_suffix()
    os.rename(old_name, new_name)
    print("rename %s to %s" % (old_name, new_name))

  def rename_old_pdf_manifest(self):
    old_name = cfg.PDF_MANIFEST_PATH
    new_name = cfg.PDF_MANIFEST_PATH + '_' + self._get_timestamp_suffix()
    os.rename(old_name, new_name)
    print("rename %s to %s" % (old_name, new_name))


if __name__ == '__main__':
  dm = DownloadManager()
  #dm._list_src_objects()
  #dm._list_pdf_objects()

  # dryrun is defaulted to be True so that there is no real download.
  if not dm.check_data_dir_exists():
    print("Data does not exist. This is the first run.")
    dm.sync_all(dryrun=True)
    sys.exit(0)

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

  dm.download_src_object('arXiv_src_0001_001.tar', dryrun=True)
  dm.download_pdf_object('arXiv_pdf_0001_001.tar', dryrun=True)
  #dm.sync_all(dryrun=True)
  #dm.sync_src(dryrun=True)
  #dm.sync_pdf(dryrun=True)

  if dm.check_remote_src_manifest_identical():
    print("The src manifest is the newest.")
  else:
    print("The src manifest is out-dated.")
    compare_manifest_xml(cfg.SRC_MANIFEST_PATH_CACHE, cfg.SRC_MANIFEST_PATH)
    #dm.rename_old_src_manifest()

  if dm.check_remote_pdf_manifest_identical():
    print("The pdf manifest is the newest.")
  else:
    print("The pdf manifest is out-dated.")
    compare_manifest_xml(cfg.PDF_MANIFEST_PATH_CACHE, cfg.PDF_MANIFEST_PATH)
    #dm.rename_old_pdf_manifest()

