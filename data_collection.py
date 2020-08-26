# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 18:44:54 2020

@author: ibrahim
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/ibrahim/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 15)
df

