#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="joaquin"
__date__ ="$11-may-2015 19:55:16$"

import unittest
import httplib
import urllib
import json

class TestsInterns(unittest.TestCase):
    """
    def setUp(self):
        pass
    def tearDown(self):
        pass
    """
    def testLogin(self): 
        params = json.dumps({"nick":"Test", "password":"test", "master":True, "estat":"en espera", "exp":0})
        headers = {"Content-type":"application/json"}
	conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/login",params,headers)
        resp = conn.getresponse()
	data = resp.read()
        print data
        self.assertEqual(resp.status, 200) # status = 200 OK
        print data



if __name__ == "__main__":
	unittest.main()
        
        
        
        
        