from neo4j.v1 import GraphDatabase, basic_auth

nodeNum = 10000
relationNum = 100000

recordPer = 100 # when nodeNum or relationNum % recordPer ==0 ,then record the operate time of record

nodeArray=range(int(nodeNum))[::int(recordPer)]
relationArray=range(int(relationNum))[::int(recordPer)]


# MySQL
dataSource='mysql+pymysql://root:123456@127.0.0.1:3306/graph'




def getPersonTuple(result):
    person=[]
    person.append(result.no)
    person.append(result.name)
    return tuple(person)

def getRelationTuple(result):
    relation=[]
    relation.append(result.no_from)
    relation.append(result.no_to)
    return tuple(relation)