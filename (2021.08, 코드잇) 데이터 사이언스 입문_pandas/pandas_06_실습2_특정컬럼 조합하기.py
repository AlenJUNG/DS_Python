# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np
import pandas as pd

sam_df = pd.read_table('data/samsong.txt', sep=',')

hyun_df = pd.read_table('data/hyundee.txt', sep=',')

sam_df

hyun_df

sam_cul = sam_df.loc[:, '문화생활비']

hyun_cul = hyun_df.loc[:, '문화생활비']

day_sam = sam_df.loc[:, '요일']

ans_df = {"day" : day_sam, 
          "samsong" : sam_cul,
          "hyundee" : hyun_cul
         }

pd.DataFrame(ans_df)


