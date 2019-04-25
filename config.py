import os

class ArXivConfig(object):
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  DATA_DIR = ROOT_DIR + '/data'
  DOWNLOAD_DIR = DATA_DIR + '/downloads'
  SRC_DIR = DOWNLOAD_DIR + '/src'
  PDF_DIR = DOWNLOAD_DIR + '/pdf'
  META_DATA_DIR	= DATA_DIR + '/meta-data'
  MAIN_FILE_DIR = DATA_DIR + '/main-files'
