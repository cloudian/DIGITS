#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from s3_walker import S3Walker

endpoint = 'http://s3-tokyo.s3.cloudian.jp:80'
accesskey = '206ed442e8f43e105d4b'
secretkey = 'uzozrfZJPZvq3/k28hZLfMz0FCHvCze0rRzsIPC9'
bucket = 'digits'
path_prefix = 'mnist/'

# mnist
# - train
# -- 0 ... 9
# --- XXX.png
try:
    mnist_folder = sys.argv[1]
except:
    print('mnist folder should be passed')
    sys.exit(1)

walker = S3Walker(endpoint, accesskey, secretkey)
walker.connect()
mnist_train_folder = os.path.join(mnist_folder, 'train')
digits = os.listdir(mnist_train_folder)
for digit in digits:
    digit_folder = os.path.join(mnist_train_folder, digit)
    if os.path.isfile(digit_folder):
        continue
    files = os.listdir(digit_folder)
    for f in files:
        if not f.endswith('.png'):
            continue
        file = os.path.join(digit_folder, f)
        key = path_prefix + file[file.index('train'):]
        walker.put(bucket, key, file)
        print('uploaded ' + file + ' ==> ' + key)