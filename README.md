# arxiv-download

## process flow

Before starting download, the proper credentials need to be set up.

Download the source manifest from s3 (`arXiv_src_manifest.xml`). Rename the old manifest. (`arXiv_src_manifest_20190425.xml`)

For each `<file>` item in the manifest, check whether the corresponding file exists in our local directory. If no then add a record in our download task. If yes then we need to check whether the manifest md5 is the same as the md5 of our local tar file. If md5's are different, we rename the old tar file and add a record in our download task for the new one. If md5's are the same, we skip processing and continue to the next `<file>` item.

We then initiate the download task (consider sending multiple sync request to s3).

## installation

### create a new conda environment for our process flow
```python
# choose python=3.6 for later using Tensorflow
# don't forget the 'pip' here or else all the pip packages will be installed to the base environment
conda create -n arxiv pip python=3.6
```

### switch to the newly created environment
```
conda activate arxiv
```

### install requisite python packages
```python
# temporary
# conda install numpy scipy pandas matplotlib jupyter
conda install sqlalchemy lxml

# awscli is the command-line utlity 'aws', which is crucial for our task
pip install awscli
```

### configure an awscli profile
```
aws configure --profile YOUR_PROFILE_NAME
```
and enter your aws credentials. This only needs to be configured once.

### install GNU parallel
```
sudo apt install parallel
```

### Data Structure
 arxiv_download
  - data (where the downloaded data goes, symlink this to a larger hard disk if necessary)
     - raw_data (two thousand tars with manifest)
     - meta_data (in sqlite db file)
     - (association of paper to big tar file, I think this is needed information)
 - (list of main files)
     - (extracted sentences, in text files or in DB files)
     - (more structures, e.g. syntax trees, etc)
  - scripts (where we put our scripts)
  - visualization (where we put charts or notebook scripts)
  - (there can be one or several master scripts at the top to control
 the whole data processing pipeline)
  - (formalities)
