# S3 Integration - Installing Boto

## Introduction ##
Boto is a Python library that is required in order for DIGITS to interact with S3. This is not required if DIGITS is being trained on local files but is required for retrieving files from any S3 endpoint.

## Installation ##
To set it up, clone the boto repository into your home directory using the following:

```bash
cd ~
git clone https://github.com/cloudian/boto.git
```

After that, add it to your PYTHONPATH using:

```bash
export PYTHONPATH=${PYTHONPATH}:${HOME}/boto
```

You may wish to put this line in .bashrc or .bash_profile so this variable is set by default.
