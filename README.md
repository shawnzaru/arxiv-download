# arxiv-download

## process flow

Before starting download, the proper credentials need to be set up.

Download the source manifest from s3 (`arXiv_src_manifest.xml`). Rename the old manifest. (`arXiv_src_manifest_20190425`)

For each `<file>` item in the manifest, check whether the corresponding file exists in our local directory. If no then add a record in our download task. If yes then we need to check whether the manifest md5 is the same as the md5 of our local tar file. If md5's are different, we rename the old tar file and add a record in our download task for the new one. If md5's are the same, we skip processing and continue to the next `<file>` item.

We then initiate the download task (consider sending multiple sync request to s3).

## installation

### configure an awscli profile
```
aws configure --profile YOUR_PROFILE_NAME
```
and enter your aws credentials.

### create a new conda environment for our process flow
```python
# choose python=3.6 for later using Tensorflow
# don't forget the 'pip' here or else all the pip packages will be installed to the base environment
conda create -n arxiv pip python=3.6
```
### install requisite python packages
```python
# temporary
conda install numpy scipy pandas matplotlib jupyter

# awscli is the command-line utlity 'aws', boto3 is the programming interface
pip install awscli boto3
```
