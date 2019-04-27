import os

class ArXivConfig(object):
  PROFILE_NAME = 'shawn'  # enter your profile name here is sufficient
  AWS_ACCESS_KEY_ID = None
  AWS_SECRET_ACCESS_KEY = None

  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  DATA_DIR = ROOT_DIR + '/data'
  DOWNLOAD_DIR = DATA_DIR + '/downloads'
  SRC_DIR = DOWNLOAD_DIR + '/src/'
  PDF_DIR = DOWNLOAD_DIR + '/pdf/'
  META_DATA_DIR	= DATA_DIR + '/meta-data/'
  MAIN_FILE_DIR = DATA_DIR + '/main-files/'

  BUCKET = 'arxiv'
  SRC_PREFIX = 'src'
  PDF_PREFIX = 'pdf'
  SRC_MANIFEST_FILE = 'arXiv_src_manifest.xml'
  PDF_MANIFEST_FILE = 'arXiv_pdf_manifest.xml'

  CMD_PREFIX = 'aws s3 --profile' + ' ' + PROFILE_NAME
  CMD_PREFIX_LS = CMD_PREFIX + ' ' + 'ls --request-payer requester'
  CMD_PREFIX_CP = CMD_PREFIX + ' ' + 'cp --request-payer requester'
  CMD_PREFIX_SYNC = CMD_PREFIX + ' ' + 'sync --requester-payer requester'
  CMD_BUCKET_SRC = 's3://arxiv/src/'
  CMD_BUCKET_PDF = 's3://arxiv/pdf/'
  CMD_LS_SRC = CMD_PREFIX_LS + ' ' + CMD_BUCKET_SRC
  CMD_LS_PDF = CMD_PREFIX_LS + ' ' + CMD_BUCKET_PDF
  CMD_DOWNLOAD_SRC_MANIFEST = CMD_PREFIX_CP + ' ' + CMD_BUCKET_SRC + SRC_MANIFEST_FILE + ' ' + SRC_DIR
  CMD_DOWNLOAD_PDF_MANIFEST = CMD_PREFIX_CP + ' ' + CMD_BUCKET_PDF + PDF_MANIFEST_FILE + ' ' + PDF_DIR
