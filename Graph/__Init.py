from Constant import *
from InitMySQL import *
from watchPerformance import *
from Draw import *
import pyorient
from arango import ArangoClient
import time
import json

def initOrientDB():
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect("root", "123456")
    #client.db_open("graph", "admin", "admin")
    #client.db_create("graph", pyorient.DB_TYPE_GRAPH, pyorient.STORAGE_TYPE_PLOCAL)
    client.command("create class persons extends V")
initOrientDB()

def deleOrientDB():
    client = pyorient.OrientDB("localhost", 2424)
    session_id = client.connect("root", "123456")
    client.db_open("graph", "admin", "admin")
    client.command("DELETE VERTEX persons where true")
    client.command("DELETE EDGE  where true")


#deleOrientDB()

def initAnangoDB():
    # Initialize the client for ArangoDB
    client = ArangoClient(
        protocol='http',
        host='localhost',
        port=8529,
        username='root',
        password='123456',
        enable_logging=True
    )

    graph = client.db('graph').create_graph('graphPersons')

    persons = graph.create_vertex_collection('persons')
    know = graph.create_edge_definition(
        name='know',
        from_collections=['persons'],
        to_collections=['persons']
    )

    #persons.insert({'_key': '03', 'name': 'Anna Smith'})
    #persons.insert({'_key': '04', 'name': 'xxxxx'})

    #know.insert({'_from': 'persons/03', '_to': 'persons/04'})



#initAnangoDB()

def test():
    client = ArangoClient(protocol='http',host='localhost',port=8529,username='root',password='123456',enable_logging=True)
    db = client.db('graph')
    schedule = db.graph('graphPersons')

   # persons=schedule.vertex_collection("persons")
   # persons.insert({'_key': '04', 'name': '222'})


    e = schedule.edge_collection('know')

    e.insert({
        '_from':'persons/03',
        '_to': 'persons/04'})



#test()

def deleteArangoDB():
    client = ArangoClient(
        protocol='http',
        host='localhost',
        port=8529,
        username='root',
        password='123456',
        enable_logging=True
    )
    client.db('graph').delete_collection("persons")
    client.db('graph').delete_collection("know")
    client.db('graph').delete_graph('graphPersons')

#deleteArangoDB()


def deleteNeo():
        id = 1

        driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "123456"))
        session = driver.session()

        while id <= nodeNum:
            a=[]
            a.append(getSingleInfo(id).no)
            session.run("match (n:person{no:'%s'}) detach delete n" % tuple(a))
            id+=1

#deleteNeo()