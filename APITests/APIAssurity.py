'''
Created on 01-Apr-2019

@author: Sumedh.Tambe
'''
import unittest
import Lib.Logger
import json
import requests
from requests.models import Response

class APIAssurity(unittest.TestCase):
    def setUp(self):
        self.ApiUrl='https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false' 
        self.Log_Level='info'       
        self.Log=Lib.Logger.Logger(self.Log_Level)
        self.StatusCode=requests.get(self.ApiUrl).status_code
        
        try:
            if(self.StatusCode!='200'):
                self.Response=requests.get(self.ApiUrl)
                self.JsonData=self.Response.json()
                
        except Response.raise_for_status():
                self.Log.Info("Issues in cousnuming API")
                self.Log.Error(self.StatusCode)
     
    def test_Name(self):        
        self.Log.Info("Checking name from json response")
        self.AcceptanceCriteria='Carbon credits'
        self.assertEqual(self.JsonData['Name'], self.AcceptanceCriteria)
    
    
    def test_IsCanReListTrue(self):
        self.Log.Info("Checking if CanReList returns true in json response")
        self.AcceptanceCriteria=True        
        self.assertEqual(self.JsonData['CanRelist'], self.AcceptanceCriteria)
    
            
            
        
        
        






