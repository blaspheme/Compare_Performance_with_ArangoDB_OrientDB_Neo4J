from Constant import *
from InitMySQL import *
from watchPerformance import *
from Draw import *
import pyorient
from arango import ArangoClient
import time
import json

def writeRecord(id, record,cpu,mem,disk, startTime):
    if id % recordPer == 0:
        calcuteTimeOperate(record,cpu,mem,disk, startTime)
    id += 1
    return id # no return the id while can't change


def NeoV():
    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "123456"))
    session = driver.session()
    startTime=time.time()
    while id <= nodeNum:
        session.run("CREATE (a:person {no: '%s', name: '%s'})" % getPersonTuple(getSingleInfo(id)))
        id = writeRecord(id, record,cpu,mem,disk, startTime)
    return record,cpu,mem,disk


def OriV():
    client = pyorient.OrientDB("localhost", 2424)
    client.connect("root", "123456")
    client.db_open("graph", "admin", "admin")

    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    startTime = time.time()
    while id <= nodeNum:
        client.command("insert into persons(no,name) values ('%s','%s')" % getPersonTuple(getSingleInfo(id)))
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk


def ArangoV():
    client = ArangoClient(protocol='http', host='localhost', port=8529, username='root', password='123456',
                          enable_logging=True)
    db = client.db('graph')
    graphPersons = db.graph('graphPersons')
    persons = graphPersons.vertex_collection("persons")
    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    startTime = time.time()
    while id <= nodeNum:
        persons.insert(json.loads(json.dumps({'_key': '%s', 'name': '%s'})% getPersonTuple(getSingleInfo(id))))
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk


def NeoE():
    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "123456"))
    session = driver.session()
    startTime=time.time()
    while id <= relationNum:
        session.run(
            "create (p1:person {no:'%s'}),(p2:person {no:'%s'}) ,(p1)-[:know]->(p2) return p1,p2" % getRelationTuple(
                getSingleRelation(id)))
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk

def OriE():
    client = pyorient.OrientDB("localhost", 2424)
    client.connect("root", "123456")
    client.db_open("graph", "admin", "admin")

    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    startTime = time.time()
    while id <= relationNum:
        try:
            client.command("create edge from (select from persons where no='%s') to (select from persons where no='%s')" % getRelationTuple(getSingleRelation(id)))
        except:
            id = writeRecord(id, record, cpu, mem, disk, startTime)
            continue
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk


def ArangoE():
    client = ArangoClient(protocol='http', host='localhost', port=8529, username='root', password='123456',
                          enable_logging=True)
    db = client.db('graph')
    graphPersons = db.graph('graphPersons')
    e = graphPersons.edge_collection('know')

    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    startTime = time.time()
    while id <= relationNum:
        try:
            e.insert(json.loads(json.dumps({'_from': 'persons/'+'%s','_to': 'persons/'+'%s'})% getRelationTuple(getSingleRelation(id))))
        except:
            id = writeRecord(id, record, cpu, mem, disk, startTime)
            continue
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk


def run():
    neoV,neoVCpu,neoVMem,neoVDisk = NeoV()
    oriV,oriVCpu,oriVMem,OriVDisk = OriV()
    araV,araVCpu,araVMem,AraVDsik = ArangoV()

    neoE,neoECpu,neoEMem,neoEDisk=NeoE()
    oriE,oriECpu,oriEMem,oriEDisk=OriE()
    araE,araECpu,araEMem,araEDisk = ArangoE()

    drawSingleWriteV(neoV,neoVCpu,neoVMem,neoVDisk,oriV,oriVCpu,oriVMem,OriVDisk,araV,araVCpu,araVMem,AraVDsik)
    drawSingleWriteE(neoE,neoECpu,neoEMem,neoEDisk,oriE,oriECpu,oriEMem,oriEDisk,araE,araECpu,araEMem,araEDisk)

run()
