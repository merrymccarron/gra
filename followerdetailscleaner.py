# -*- coding: utf-8 -*-

import os
import sys
import pandas as pd

df = pd.read_csv('sociallandmarkstofix/nycgovfollowerdetails.csv', header=False, index_col = 0)

# print df.head(2)

df['Locatio'] = df['geo_enabled']
df['Geo_Enable'] = df['screen_name']
df['Screen_Nam'] = df['location']

df.to_csv('sociallandmarkstofix/a_nycgovfollowerdetails.csv', columns=['UserID', 'Locatio', 'Screen_Nam', 'name', 'Geo_Enable'])


dfa = pd.read_csv('sociallandmarkstofix/a_nycgovfollowerdetails.csv', header=False, index_col = 0)

# print df.head(2)

dfa['location'] = dfa['Locatio']
dfa['geo_enabled'] = dfa['Geo_Enable']
dfa['screen_name'] = dfa['Screen_Nam']

dfa.to_csv('sociallandmarkstofix/nycgovfollowerdetails.csv', columns=['UserID', 'location', 'screen_name', 'name', 'geo_enabled'])
