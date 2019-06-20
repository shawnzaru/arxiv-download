import os
import sys

from config import ArXivConfig as cfg

f = open("cmd-untar.txt", "w")

for root, dirs, files in os.walk(cfg.SRC_DIR):
  for name in files:
    if name[-4:] == '.tar':
      cmd = os.path.join(root, name)
      cmd = "tar xf " + cmd + " -C " + cfg.UNTAR_DIR
      f.write(cmd + "\n")

f.close()

