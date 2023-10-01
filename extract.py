import tarfile

# Extract the .tar.gz archive
with tarfile.open('massive_dataset.tar.gz', 'r:gz') as tar:
    tar.extractall()