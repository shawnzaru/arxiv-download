# arxiv-download

## process flow

Before starting download, the proper credentials need to be set up.

Download the source manifest from s3 (`arXiv_src_manifest.xml`). Rename the old manifest. (`arXiv_src_manifest_20190425`)

For each `<file>` item in the manifest, check whether the corresponding file exists in our local directory. If no then add a record in our download task. If yes then we need to check whether the manifest md5 is the same as the md5 of our local tar file. If md5's are different, we rename the old tar file and add a record in our download task for the new one. If md5's are the same, we skip processing and continue to the next `<file>` item.

We then initiate the download task (consider sending multiple sync request to s3).

## installation

### create a new conda environment for our process flow
```python
# choose python=3.6 for later using Tensorflow
conda create -n arxiv pip python=3.6
```

```python
# temporary
conda install awscli
```
