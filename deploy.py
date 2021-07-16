# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:33:09 2021

@author: Joshh
"""

import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "WGEKHiHFU0I1ep4ySxp2-hhqNqBF0bwNu3eTfl_Xcert"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": ['Temp','D.O. (mg/l)','PH','CONDUCTIVITY (mhos/cm)','B.O.D. (mg/l)','NITRATENAN N+ NITRITENANN (mg/l)','TOTAL COLIFORM (MPN/100ml)Mean'],
                    "values": [[2014,5.7,6.8,203,6.9,0.2,24]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/f04ea5b0-fc93-4bf0-88ba-d4c7edf05fe7/predictions?version=2021-07-13', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
