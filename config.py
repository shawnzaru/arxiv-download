import os

class ArXivConfig(object):
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  DATA_DIR = ROOT_DIR + '/data'
  DOWNLOAD_DIR = DATA_DIR + '/downloads'
  SRC_DIR = DOWNLOAD_DIR + '/src'
  PDF_DIR = DOWNLOAD_DIR + '/pdf'
  META_DATA_DIR	= DATA_DIR + '/meta-data'
  MAIN_FILE_DIR = DATA_DIR + '/main-files'

  AWS_ACCESS_KEY_ID = None
  AWS_SECRET_ACCESS_KEY = None
  PROFILE_NAME = 'shawn'  # enter your profile name here is sufficient

  BUCKET = 'arxiv'
  SRC_PREFIX = 'src'
  PDF_PREFIX = 'pdf'
  SRC_MANIFEST_FILE = 'arXiv_src_manifest.xml'
  PDF_MANIFEST_FILE = 'arXiv_pdf_manifest.xml'
