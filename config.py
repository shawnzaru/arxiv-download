import os

class ArXivConfig(object):
  PROFILE_NAME = 'shawn'  # enter your profile name here is sufficient
  AWS_ACCESS_KEY_ID = None
  AWS_SECRET_ACCESS_KEY = None

  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  DATA_DIR = ROOT_DIR + '/data/'
  DOWNLOAD_DIR = DATA_DIR + 'downloads/'
  SRC_DIR = DOWNLOAD_DIR + 'src/'
  PDF_DIR = DOWNLOAD_DIR + 'pdf/'
  META_DATA_DIR = DATA_DIR + 'meta-data/'
  MAIN_FILE_DIR = DATA_DIR + 'main-files/'

  BUCKET = 'arxiv'
  SRC_PREFIX = 'src'
  PDF_PREFIX = 'pdf'
  SRC_MANIFEST_FILE = 'arXiv_src_manifest.xml'
  PDF_MANIFEST_FILE = 'arXiv_pdf_manifest.xml'

  CMD_PREFIX = 'aws s3 --profile' + ' ' + PROFILE_NAME
  CMD_PREFIX_LS = CMD_PREFIX + ' ' + 'ls --request-payer requester'
  CMD_PREFIX_CP = CMD_PREFIX + ' ' + 'cp --request-payer requester'
  CMD_PREFIX_SYNC = CMD_PREFIX + ' ' + 'sync --requester-payer requester'
  CMD_BUCKET = 's3://arxiv/'
  CMD_BUCKET_SRC = 's3://arxiv/src/'
  CMD_BUCKET_PDF = 's3://arxiv/pdf/'

  CMD_SYNC_ALL = CMD_PREFIX_SYNC + ' ' + CMD_BUCKET + ' ' + DOWNLOAD_DIR + ' --dryrun'
  CMD_SYNC_SRC = CMD_PREFIX_SYNC + ' ' + CMD_BUCKET_SRC + ' ' + SRC_DIR + ' --dryrun'
  CMD_SYNC_PDF = CMD_PREFIX_SYNC + ' ' + CMD_BUCKET_PDF + ' ' + PDF_DIR + ' --dryrun'
  CMD_LS_SRC = CMD_PREFIX_LS + ' ' + CMD_BUCKET_SRC
  CMD_LS_PDF = CMD_PREFIX_LS + ' ' + CMD_BUCKET_PDF
  CMD_DOWNLOAD_SRC_MANIFEST = CMD_PREFIX_CP + ' ' + CMD_BUCKET_SRC + SRC_MANIFEST_FILE + ' ' + SRC_DIR
  CMD_DOWNLOAD_PDF_MANIFEST = CMD_PREFIX_CP + ' ' + CMD_BUCKET_PDF + PDF_MANIFEST_FILE + ' ' + PDF_DIR

if __name__ == '__main__':
  cfg = ArXivConfig
  print("PROFILE_NAME:", cfg.PROFILE_NAME)
  print("AWS_ACCESS_KEY_ID:", cfg.AWS_ACCESS_KEY_ID)
  print("AWS_SECRET_ACCESS_KEY:", cfg.AWS_SECRET_ACCESS_KEY)
  print("ROOT_DIR:", cfg.ROOT_DIR)
  print("DATA_DIR:", cfg.DATA_DIR)
  print("DOWNLOAD_DIR:", cfg.DOWNLOAD_DIR)
  print("SRC_DIR:", cfg.SRC_DIR)
  print("PDF_DIR:", cfg.PDF_DIR)
  print("META_DATA_DIR:", cfg.META_DATA_DIR)
  print("MAIN_FILE_DIR:", cfg.MAIN_FILE_DIR)
  print("BUCKET:", cfg.BUCKET)
  print("SRC_PREFIX:", cfg.SRC_PREFIX)
  print("PDF_PREFIX:", cfg.PDF_PREFIX)
  print("SRC_MANIFEST_FILE:", cfg.SRC_MANIFEST_FILE)
  print("PDF_MANIFEST_FILE:", cfg.PDF_MANIFEST_FILE)
  print("CMD_PREFIX:", cfg.CMD_PREFIX)
  print("CMD_PREFIX_LS:", cfg.CMD_PREFIX_LS)
  print("CMD_PREFIX_CP:", cfg.CMD_PREFIX_CP)
  print("CMD_PREFIX_SYNC:", cfg.CMD_PREFIX_SYNC)
  print("CMD_BUCKET:", cfg.CMD_BUCKET)
  print("CMD_BUCKET_SRC:", cfg.CMD_BUCKET_SRC)
  print("CMD_BUCKET_PDF:", cfg.CMD_BUCKET_PDF)
  print("CMD_SYNC_ALL:", cfg.CMD_SYNC_ALL)
  print("CMD_SYNC_SRC:", cfg.CMD_SYNC_SRC)
  print("CMD_SYNC_PDF:", cfg.CMD_SYNC_PDF)
  print("CMD_LS_SRC:", cfg.CMD_LS_SRC)
  print("CMD_LS_PDF:", cfg.CMD_LS_PDF)
  print("CMD_DOWNLOAD_SRC_MANIFEST:", cfg.CMD_DOWNLOAD_SRC_MANIFEST)
  print("CMD_DOWNLOAD_PDF_MANIFEST:", cfg.CMD_DOWNLOAD_PDF_MANIFEST)
