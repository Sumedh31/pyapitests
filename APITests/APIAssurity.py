'''
Created on 01-Apr-2019

@author: Sumedh.Tambe
'''
import unittest
from Lib.Logger import Logger
import requests
from requests.models import Response

class APIAssurity(unittest.TestCase):
    def setUp(self):
        self.ApiUrl='https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false' 
        self.Log_Level='info'       
        self.Log=Logger(self.Log_Level)
        self.StatusCode=requests.get(self.ApiUrl).status_code
        
        try:
            if(self.StatusCode!='200'):
                self.Response=requests.get(self.ApiUrl)
                self.JsonData=self.Response.json()
                
        except Response.raise_for_status():
                self.Log.Info("Issues in cousnuming API")
                self.Log.Error(self.StatusCode)
     
    def test_FirstAcceptanceCriteriaForName(self):        
        self.Log.Info("Checking name from json response")
        self.AcceptanceCriteria='Carbon credits'
        self.assertEqual(self.JsonData['Name'], self.AcceptanceCriteria)
     
     
    def test_SecondAcceptanceCriteriaForIsCanReListTrue(self):
        self.Log.Info("Checking if CanReList returns true in json response")
        self.AcceptanceCriteria=True        
        self.assertEqual(self.JsonData['CanRelist'], self.AcceptanceCriteria)
    
    def test_ThirdAcceptanceCriteriaForCheckDescriptionContent(self):
        self.Log.Info("Checking the description in Promotions element that has Name as Gallery and description as 2x larger image")
        self.AcceptanceCriteria='2x larger image'
        self.PassedTest=False
        if (self.AcceptanceCriteria in self.JsonData['Promotions'][1]['Description']):
            self.Log.Info("Acceptance criteria '%s' is Present in the json response '%s'"%(self.AcceptanceCriteria,self.JsonData['Promotions'][1]['Description']))
            self.PassedTest=True
        self.assertTrue(self.PassedTest,'Test Case Failed')
        
        
            
        
        
        






