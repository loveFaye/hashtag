#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 Kimi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

##########################################################
#
# It is used for data cleanser
#
##########################################################

import pandas as pd
import re

def read_df(dir):
    """
    Read data from the file
    """
    
    df = pd.read_csv(dir)
    return df

def to_lowercase(df):
    """
    Change the character in data frame to lower case character only
    """

    for i in xrange(len(df)):
        tmp_str = re.sub(r'[\W]', ' ', df.tweet[i].lower()).split()
        tmp_str.sort()
        df.tweet[i] = tmp_str
    return df

