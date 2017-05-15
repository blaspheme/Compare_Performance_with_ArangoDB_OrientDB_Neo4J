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
        session.run("MATCH (js:person)-[:know]-(surfer) WHERE js.no = '%s' return surfer" % getSingleInfo(id).no)
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
        client.command("select from E where out = (select @RID from persons where no='%s')" % getSingleInfo(id).no)
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk


def ArangoV():
    client = ArangoClient(protocol='http', host='localhost', port=8529, username='root', password='123456',
                          enable_logging=True)
    db = client.db('graph')
    graphPersons = db.graph('graphPersons')
    id = 1
    record=[]
    cpu=[]
    mem=[]
    disk=[]
    startTime = time.time()
    while id <= nodeNum:
        traversal_results = graphPersons.traverse(
            start_vertex='persons/'+getSingleInfo(id).no,
            strategy='bfs',
            direction='outbound',
            edge_uniqueness='global',
            vertex_uniqueness='global',
            max_depth=1
        )
        id = writeRecord(id, record, cpu, mem, disk, startTime)
    return record, cpu, mem, disk



def run():
    neoV,neoVCpu,neoVMem,neoVDisk = NeoV()
    oriV,oriVCpu,oriVMem,OriVDisk = OriV()
    araV,araVCpu,araVMem,AraVDsik = ArangoV()

    drawSingleWriteV(neoV,neoVCpu,neoVMem,neoVDisk,oriV,oriVCpu,oriVMem,OriVDisk,araV,araVCpu,araVMem,AraVDsik)

run()
