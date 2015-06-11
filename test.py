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

    
    def login(self):
        params = json.dumps({"nick":"Test", "password":"test", "master":True, "estat":"en espera", "exp":0})
        headers = {"Content-type":"application/json"}
	conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/login",params,headers)
        resp = conn.getresponse()
        return resp
	
        
    def testLogin(self): 
        resp = self.login()
        data = resp.read()
        print str(data)
        self.assertEqual(resp.status, 200) # status = 200 OK
        
        
    def testcreateHeroe(self):
        resp = self.login()
        data = resp.read()
        obj= (json.loads(data))
        obj = json.loads(obj)
        uid = (obj["uid"]) 
        params = json.dumps({"id_jugador":uid, "avatar":"/images/heroes/cara_guerrero.jpg", "nom":"Spopobich", "live":20, "force":30, "agility":30})
        headers = {"Content-type":"application/json"}
        conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/createHeroe",params,headers)
        resp = conn.getresponse()
        data = resp.read()
        print data
        self.assertEqual(resp.status, 200)
    
    def testcreateMap(self):
        resp = self.login()
        data = resp.read()
        obj= (json.loads(data))
        obj = json.loads(obj)
        uid = (obj["uid"])
        params = json.dumps({"id":uid,"mapName":"MapaTest","col":10,"fil":10, "background":"images/maps/bosc.jpg"})
        headers = {"Content-type":"application/json"}
        conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/createMap",params,headers)
        resp = conn.getresponse()
        data = resp.read()
        print data
        self.assertEqual(resp.status, 200) 
    

if __name__ == "__main__":
	unittest.main()
        
        
        
        
        