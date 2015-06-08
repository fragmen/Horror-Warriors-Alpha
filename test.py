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
    params = None
    uid = 0
    
    def testLogin(self): 
        self.params = json.dumps({"nick":"Test", "password":"test", "master":True, "estat":"en espera", "exp":0})
        headers = {"Content-type":"application/json"}
	conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/login",self.params,headers)
        resp = conn.getresponse()
	data = resp.read()
        print str(data)
        self.assertEqual(resp.status, 200) # status = 200 OK
        obj= (json.loads(data))
        obj = json.loads(obj)
        self.uid = (obj["uid"]) 
        self.params = json.dumps({"id_jugador":self.uid, "avatar":"/images/heroes/cara_guerrero.jpg", "nom":"Spopobich", "live":20, "force":30, "agility":30})
        
    def testcreateHeroe(self):
        print """Nem a veure el params"""
        print self.params
        headers = {"Content-type":"application/json"}
        conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/createHeroe",self.params,headers)
        resp = conn.getresponse()
        data = resp.read()
        print data
        self.assertEqual(resp.status, 200)
    
    def testcreateMap(self):
        params = json.dumps({"id":self.uid,"mapName":"MapaTest","col":10,"fil":10, "background":"images/maps/bosc.jpg"})
        headers = {"Content-type":"application/json"}
        conn = httplib.HTTPConnection('localhost',80, timeout=2)
        conn.request("POST","/api/createMap",params,headers)
        resp = conn.getresponse()
        data = resp.read()
        print data
        self.assertEqual(resp.status, 200)
        

        
    

if __name__ == "__main__":
	unittest.main()
        
        
        
        
        