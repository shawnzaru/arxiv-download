import sys
import os.path
from lxml import etree

from config import ArXivConfig as cfg

def compare_manifest_xml(manifest_xml_cache, manifest_xml_local):
  manifest_cache = Manifest(manifest_xml_cache)
  manifest_local = Manifest(manifest_xml_local)
  #print(manifest_cache)
  #print(manifest_local)
  for tar in manifest_cache.tar_list:
    if tar.filename in manifest_local.filename2index:
      local_md5sum = manifest_local.get_md5sum_by_filename(tar.filename)
      if tar.md5sum != local_md5sum:
        print("[C] %s" % tar.filename)
    else:
      print("[A] %s" % tar.filename)


class Manifest(object):
  
  def __init__(self, xmlfile):
    self.tar_list = []
    self.filename2index = {} # for quick reference

    if not os.path.isfile(xmlfile):
      print("file %s does not exist" % xmlfile)
      sys.exit(-1)
    print("parsing manifest file %s..." % xmlfile)
    tree = etree.parse(xmlfile)
    root = tree.getroot()
    for child in root:
      if child.tag != "file": # ignore <timestamp> tag under root
        continue
      tar = TarFile()
      tar.content_md5sum = child[0].text
      tar.filename = child[1].text
      tar.first_item = child[2].text
      tar.last_item = child[3].text
      tar.md5sum = child[4].text
      tar.num_items = child[5].text
      tar.seq_num = child[6].text
      tar.size = child[7].text
      tar.timestamp = child[8].text
      tar.yymm = child[9].text
      self.tar_list.append(tar)
      self.filename2index[tar.filename] = len(self.tar_list) - 1
    print("%d pieces of tar file info parsed." % len(self.tar_list))

  def get_md5sum_by_filename(self, filename):
    # the filename is supposed to exist in the manifest
    return self.tar_list[self.filename2index[filename]].md5sum

  def __repr__(self):
    return "%d tar files from %s to %s." % (len(self.tar_list), self.tar_list[0].filename, self.tar_list[-1].filename)


class TarFile(object):

  def __init__(self):
    self.content_md5sum = None
    self.filename = None
    self.first_item = None
    self.last_item = None
    self.md5sum = None
    self.num_items = None
    self.seq_num = None
    self.size = None
    self.timestamp = None
    self.yymm = None


if __name__ == "__main__":
  #m = Manifest(cfg.SRC_MANIFEST_PATH_CACHE)
  #print(m)
  compare_manifest_xml(cfg.SRC_MANIFEST_PATH_CACHE, cfg.SRC_MANIFEST_PATH)
