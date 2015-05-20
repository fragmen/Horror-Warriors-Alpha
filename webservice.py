__author__ = 'joaquin'
# -*- coding: utf-8 -*-

import cherrypy
import json
import pymongo
from bson.objectid import ObjectId
import datetime
import hashlib
from hashlib import md5

class HorrorWarriors:

    exposed = True
    def __init__(self):

        self.client = pymongo.MongoClient()
        self.db = self.client.hw
        self.jugadors = self.db.jugadors
        self.personatges = self.db.personatges
        self.bestiari = self.db.bestiari
        self.heroes = self.db.heroes
        self.partida = self.db.partida
        self.combat = self.db.combat
        self.terreny = self.db.terreny
        self.item = self.db.item
        self.armes = self.db.armes
        self.armadures = self.db.armadures
        self.resposta = {}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def login(self,*args,**kwargs):
        """
        Funcio que serveix per logarnos i en cas de que no existeixi el usuari, el crea.
        Accepta els parametres de nick password, que desara encriptat i el bolea de si es master o no
        """

        try:

            dades_in = cherrypy.request.json

            nick = str(dades_in["nick"])
            password = str(dades_in["password"])
            try:
                master = bool(dades_in["master"])
            except:
                master = False
            m = hashlib.md5()
            m.update(password.encode('utf-8'))
            password = m.hexdigest()

            print """Despres de agafar les dades"""

            try:
                nick_db = (self.jugadors.find_one({"nick":nick}))
                nick_db = str(nick_db["nick"])
                password_db = (self.jugadors.find_one({"password":password}))
                password_db = str(password_db["password"])
                print """Apunt de comprpbar el jugador"""

                if(nick_db == nick and password_db == password):
                    uid = self.jugadors.find_one({"nick":nick})
                    nick = self.jugadors.find_one({"nick":nick},{"nick":1})
                    self.resposta["status"]="Ok"
                    self.resposta["msg"]="S'ha trobat el jugador"
                    self.resposta["uid"] = str(uid["_id"])
                    self.resposta["nick"] = str(nick["nick"])
                    return json.dumps( self.resposta )

            except:
                print("""No s'ha trobat el jugadpr""")
                if (master==True):
                    uid = self.jugadors.save( {"password":password,"nick":nick,"estat":"en espera", "exp":0 ,"master":master})
                else:
                    uid = self.jugadors.save( {"password":password,"nick":nick,"estat":"en espera", "exp":0})
                jugador = self.jugadors.find_one( {"_id":uid} )
                # transformem el _id en string per que sigui JSON-serializable (si no, dona error)
                jugador["_id"] = str(uid)
                # retornem dades d'usuari
                self.resposta["status"]="OK"
                self.resposta["msg"]="S'ha creat el jugador exitosament"
                self.resposta["uid"] = str(jugador["_id"])
                return json.dumps(self.resposta)
        except:

            self.resposta["status"]="Error"
            self.resposta["msg"]="Les dades no son correctes"
            return json.dumps(self.resposta)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def esMaster(self,*args,**kwargs):
        """
        comprva si la id del jugador que enviem es de un Master o no, ens serveix en la plana principal
        homeLayout per filtar les opcions depenent aquest origen
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id = str(dades_in["id"])
            master = self.jugadors.find_one({"_id":ObjectId(id)})
            if(master["master"]==True):
                self.resposta["master"] = True
                return json.dumps(self.resposta)

        except:
            self.resposta["master"] = False
            return json.dumps(self.resposta)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def createMap(self,*args,**kwargs):
        """
        Desa les dades del mapa i la id del master com a relacio
        """
        self.resposta = {}
        try:

            dades_in = cherrypy.request.json

            id = str(dades_in["id"])
            mapName = str(dades_in["mapName"])
            col = int(dades_in["col"])
            fil = int(dades_in["fil"])
            background = str(dades_in["background"])

            uid = self.terreny.save({"id_master": id, "mapName": mapName, "col": col, "fil": fil, "background": background})
            self.resposta["status"] = "Ok"
            self.resposta["msg"] = "Ha guadat el mapa amb exit"
            return json.dumps(self.resposta)
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = "El mapa no ha guardat correctament"
            return json.dumps(self.resposta)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def createBeast(self, *args, **keywargs):
        """
        Desa les dades de la criatura i els seus atributs amb la id de relació amb el master
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_master = str(dades_in["id_master"])
            nom = str (dades_in["nom"])
            avatar = str(dades_in["avatar"])
            live = str(dades_in["live"])
            force = str(dades_in["force"])
            agility = str(dades_in["agility"])
            defense = str(dades_in["defense"])

            uid = self.bestiari.save({"id_master":id_master,"nom":nom,"avatar":avatar,"live":live,"force":force,"agility":agility,"defense":defense})
            self.resposta["status"] = """OK"""
            self.resposta["msg"] = """Les dades s'han guardat correctament"""
            return(json.dumps(self.resposta))

        except:
            self.resposta["status"] = ["Error"]
            self.resposta["msg"] = ["""No s'han passat les dades correctament"""]
            return json.dumps(self.resposta)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def loadBeast(self,*args, **keywargs):
        """
        carrega tot els atributs de la bestia la qual pasem la Id
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_master = str(dades_in["id_master"])
            besties = self.bestiari.find({"id_master":id_master},{"nom":1, "_id":False})
            besties_array = []

            for best in besties:
                best["nom"] = str(best["nom"])
                besties_array.append(best)

            self.resposta["status"] = "Ok"
            self.resposta["msg"] = """S'han carregat les dades"""
            self.resposta["data"] = besties_array
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """No tens encara cap mostre disponible!"""
            return(json.dumps(self.resposta))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def listBeast(self):
        """
        Carrega les dades de totes les besties del Master que li pasem la id
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_master = str(dades_in["id_master"])
            besties = self.bestiari.find({"id_master":id_master},{"_id":False})
            besties_array = []

            for best in besties:
                best["nom"] = str(best["nom"])
                besties_array.append(best)

            self.resposta["status"] = "Ok"
            self.resposta["msg"] = """S'han carregat les dades"""
            self.resposta["data"] = besties_array
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """No tens encara cap mostre disponible!"""
            return(json.dumps(self.resposta))
    
    """ Opcions del Jugador normal"""
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def createHeroe(self, *args, **keywargs):
        """
        Desa les dades del Heroi que hem introduit al formulari i el relaciona amb la id del Master
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_jugador = str(dades_in["id_jugador"])
            nom = str (dades_in["nom"])
            avatar = str(dades_in["avatar"])
            live = str(dades_in["live"])
            force = str(dades_in["force"])
            agility = str(dades_in["agility"])
 
            

            uid = self.heroes.save({"id_jugador":id_jugador,"nom":nom,"avatar":avatar,"live":live,"force":force,"agility":agility})
            self.resposta["status"] = """OK"""
            self.resposta["msg"] = """Les dades s'han guardat correctament"""
            return(json.dumps(self.resposta))

        except:
            self.resposta["status"] = ["Error"]
            self.resposta["msg"] = ["""No s'han passat les dades correctament"""]
            return json.dumps(self.resposta)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def loadHeroes(self,*args, **keywargs):
        """
        Llista tots els herois del Jugador
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_jugador = str(dades_in["id_jugador"])
            heroes = self.heroes.find({"id_jugador":id_jugador},{"nom":1})
            heroes_array = []

            for hero in heroes:
                hero["nom"] = str(hero["nom"])
                hero["_id"] = str(hero["_id"])
                heroes_array.append(hero)

            self.resposta["status"] = "Ok"
            self.resposta["msg"] = """S'han carregat les dades"""
            self.resposta["data"] = heroes_array
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """No tens encara cap Heroi disponible!"""
            return(json.dumps(self.resposta))
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def loadHeroe(self):
        """
        Llista els atributs del Heroi en questio
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_heroe = str(dades_in["id_heroe"])
            
            heroes = self.heroes.find_one({"_id":ObjectId(id_heroe)})
            heroes["_id"] = str(heroes["_id"])
            self.resposta["status"] = "OK"
            self.resposta["msg"] = "Les dades del Heroe han carregat correctament"
            self.resposta["data"] = heroes
            return(json.dumps(self.resposta))
            
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = "Les dades del Heroe no es troben"
            
            return(json.dumps(self.resposta))
        
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def listHeroes(self):
        """
        Llista tots els herois del Jugador
        """
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_jugador = str(dades_in["id_jugador"])
            heroes = self.heroes.find({"id_jugador":id_jugador})
            heroes_array = []

            for hero in heroes:
                hero["nom"] = str(hero["nom"])
                hero["id"] = str(hero["_id"])
                heroes_array.append(hero)

            self.resposta["status"] = "Ok"
            self.resposta["msg"] = """S'han carregat les dades"""
            self.resposta["data"] = heroes_array
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """No tens encara cap Heroi disponible!"""
            return(json.dumps(self.resposta))
        
    def relacionsHerois(self, id_heroe):
        """
        Busca si exiteixen relaion de partides on aquest heroi estiges subscrit, si es el cas, les elimina
        """
        self.resposta = {}
        heroi_array = []
        try:
            partida = self.partida.find({},{"herois":1})
            for party in partida:
                tmp = party
                for p in party["herois"]:
                        
                    if(str(p) != str(id_heroe)):
                        heroi_array.append(str(p))
                        id = str(tmp["_id"]);
                            
                    
                self.partida.update({"_id":ObjectId(id)},{'$set':{"herois":heroi_array}})

            return(True)
                 
        except:
                
            return(False)
            
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def dropHeroe(self):
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_heroe = str(dades_in["id_heroe"])
            if(self.relacionsHerois(id_heroe)==True):
                self.resposta["msg"] = "Els heroi s'ha borrat correctament incloint les relacions"
            else:
                self.resposta["msg"] = "Els heroi s'ha borrat correctament"
                
            self.heroes.remove({"_id":ObjectId(id_heroe)})
            self.resposta["status"] = "OK"
            
            return(json.dumps(self.resposta))
            
            
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = "No s'ha trobat el jugador a la BD de Mongo"
            return(json.dumps(self.resposta))
    
    
    
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def createParty(self):
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            
            id_jugador = str(dades_in["master_id"])
            nom = str(dades_in["nom"])
            pas = str(dades_in["pass"])
            maxper = int(dades_in["maxper"])
            idioma = str(dades_in["idioma"])
            print(id,nom,pas,maxper,idioma)
            
            master = self.jugadors.find_one({"_id":ObjectId(id_jugador)})
            self.partida.save({"id_master":id_jugador,"nom":nom, "pass":pas, "maxper":maxper,"cua":0, "idioma":idioma, "online":False})
            self.resposta["status"] = "OK"
            self.resposta["msg"] = """S'han guardat les dades d el apartida correctament"""
            return(json.dumps(self.resposta))
                
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """Aquest usuari no pot crear partida"""
            return(json.dumps(self.resposta))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def loadPartys(self,*args, **keywargs):
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            id_jugador = str(dades_in["id_jugador"])
            partys = self.partida.find({"id_master":id_jugador})
            partys_array = []

            for party in partys:
                party["nom"] = str(party["nom"])
                party["maxper"] = int(party["maxper"])
                party["online"] = str(party["online"])
                party["_id"] = str(party["_id"])
                partys_array.append(party)

            self.resposta["status"] = "Ok"
            self.resposta["msg"] = """S'han carregat les dades"""
            self.resposta["data"] = partys_array
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """No tens encara cap Partida disponible!"""
            return(json.dumps(self.resposta))
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def onlineParty(self):
        self.resposta = {}
        try:
            dades_in = cherrypy.request.json
            nom = str(dades_in["nom"])
            estat = str(dades_in["estat"])
            self.partida.find_one({"nom":nom})
            estat2 = None
            if(estat=="True"):
                estat2 = False
            if(estat == "False" ):
                estat2 = True
            self.partida.update({"nom":nom},{'$set':{"online":estat2}})
            self.resposta["status"] = "OK"
            self.resposta["msg"] = """El estat de la partida ara es %s""",(estat2)
            self.resposta["estat"] = estat2
            return json.dumps(self.resposta)
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = """El estat de la partida sense modificar"""
            self.resposta["estat"] = estat2
            return(json.dumps(self.resposta))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listParty(self):
        self.resposta = {}
        try:
            valor = True
            partides = self.partida.find({"online":True})
            partides_array = []
            for part in partides:
                part["nom"] = str(part["nom"])
                part["_id"] = str(part["_id"])
                part["online"] = str(part["online"])
                part["maxper"] = str(part["maxper"])
                part["pass"] = str(part["pass"])
                idMaster = str(part["id_master"])
                nomMaster = self.jugadors.find_one({"_id":ObjectId(idMaster)})
                nomMaster = str(nomMaster["nick"])
                print nomMaster
                part["master"] = nomMaster
                partides_array.append(part)
                    
            self.resposta["status"] = "OK"
            self.resposta["msg"] = "Les dades s'han carregat estupendament"
            self.resposta["data"] = partides_array 
            return(json.dumps(self.resposta))
        except:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = "Les dades no s'han pogut consultar"
            return(json.dumps(self.resposta))
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def joinParty(self):
        
        self.resposta = {}
        try:
          
            dades_in = cherrypy.request.json
            nom_p = str(dades_in["nom"])
            id_jugador = str(dades_in["id_jugador"])
            id_heroi = str(dades_in["id_heroi"])
            partida = self.partida.find_one({"nom":nom_p},{"_id":False})
            jugadors_array = []
            herois_array = []
            print("""DADES BEN PASADES""")
            
            if(int(partida["cua"]<int(partida["maxper"]))):
                if(partida.get("jugadors")):
                    for part in partida["jugadors"]:
                        if(str(part)==id_jugador):
                            self.resposta["status"]= "Error"
                            self.resposta["msg"] = "El jugador ja esta inscrit amb anterioritat"
                            self.resposta["data"] = partida
                            return(json.dumps(self.resposta))
                        
                        else:
                            jugadors_array.append(str(part))
                if(partida.get("herois")):            
                    for parth in partida["herois"]:
                        if(str(parth)==id_heroi):
                            self.resposta["status"]= "Error2"
                            self.resposta["msg"] = "El heroi ja esta inscrit amb anterioritat"
                            self.resposta["data"] = partida
                            return(json.dumps(self.resposta))

                        else:
                            herois_array.append(str(parth))
                
                print("""CHICA FORA!!""")
                
                partida["nom"] = str(partida["nom"])
                partida["online"] = str(partida["online"])
                partida["maxper"] = str(partida["maxper"])
                partida["pass"] = str(partida["pass"])
                idMaster = str(partida["id_master"])
                nomMaster = self.jugadors.find_one({"_id":ObjectId(idMaster)})
                nomMaster = str(nomMaster["nick"])
                    
                cua = int(partida["cua"])+1
                partida["id_master"] = nomMaster
                       
                
                jugadors_array.append(str(id_jugador))
                herois_array.append(str(id_heroi))
                partida["jugadors"] = jugadors_array
                partida["herois"] = herois_array

                    
                self.partida.update({"nom":nom_p},{'$set':{"cua":int(cua)}})
                    
                self.partida.update({"nom":nom_p},{'$set':{"jugadors":jugadors_array,"herois":herois_array}})
                   
                    
                self.resposta["status"] = "OK"
                self.resposta["msg"] = "Unit a la partida correctament"
                self.resposta["data"] = partida
                return(json.dumps(self.resposta))
            else:
                self.resposta["status"] = "Error"
                self.resposta["msg"] = "No queda lloc per la partida"
                return(json.dumps(self.resposta))
        except Exception as e:
            self.resposta["status"] = "Error"
            self.resposta["msg"] = "Error a la funcio del webservice de joinParty"
            print "ERROR desconegut: "+str(e.__class__.__name__)
            return(json.dumps(self.resposta))
    
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def viewParty(self):
        self.resposta = {}
        if(1==1):
    
            dades_in = cherrypy.request.json
            nomParty = str(dades_in["nomParty"])
            partida = self.partida.find_one({"nom":nomParty})
            partida["_id"] = str(partida["_id"])
            jugadors_array_Oj = []
            herois_array_Oj = []
            
            jugadors_array = partida["jugadors"]
            herois_array = partida["herois"]
            
            for jugador in jugadors_array:
                jugador = ObjectId(jugador)
                print jugador
                jugadors_array_Oj.append(jugador)
            
            for herois in herois_array:
                herois = ObjectId(herois)
                print herois
                herois_array_Oj.append(herois)
                
            print jugadors_array_Oj
            print herois_array_Oj
            
            self.resposta["msg"] = "S'han trobat les seguents dades"
            self.resposta["status"] = "OK"
            jugadors = self.jugadors.find({"_id":{"$in":jugadors_array_Oj}})
            herois = self.heroes.find({"_id":{"$in":herois_array_Oj}})
            herois_array = []
            jugadors_array = []
            for hero in herois:
                hero["_id"] = str(hero["_id"])
                herois_array.append(hero)
            for juga in jugadors:
                juga["_id"] = str(juga["_id"])
                jugadors_array.append(juga)
            self.resposta["herois"]=herois_array
            self.resposta["jugadors"] = jugadors_array
            return(json.dumps(self.resposta))
            
        else:
            
            print "ERROR desconegut: "
            return "ERROR desconegut: "+str(e.__class__.__name__)
        

        
application = cherrypy.Application(HorrorWarriors(), script_name=None, config=None)