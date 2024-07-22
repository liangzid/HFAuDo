"""
======================================================================
RUN ---

Downloading Operations.

    Author: Zi Liang <zi1415926.liang@connect.polyu.hk>
    Copyright © 2024, ZiLiang, all rights reserved.
    Created: 22 July 2024
======================================================================
"""


# ------------------------ Code --------------------------------------

## normal import 
import os
import sys
import json
from typing import List,Tuple,Dict
import random
from pprint import pprint as ppp
import shutil

from datasets import load_dataset

list_of_repository=[
    "Sadanto3933/commonsense_qa",
    "Sadanto3933/ai2_arc",
    ]


def download(fname):

    # first delete the cache if there is one.
    homepath=os.environ.get('HOME', '~/')
    fpth=fname.replace("/","___")
    fpth=f"{homepath}/.cache/huggingface/datasets/{fpth}"

    if os.path.exists(fpth):
        shutil.rmtree(fpth)

    # download.
    dataset=load_dataset(fname)


    if os.path.exists(fpth):
        shutil.rmtree(fpth)
    print(f"Download and Delete {fname} DONE.")


def autoDownload(als):
    for x in als:
        download(x)



if __name__=="__main__":
    autoDownload(list_of_repository)
