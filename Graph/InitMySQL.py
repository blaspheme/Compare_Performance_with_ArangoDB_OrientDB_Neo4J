from Constant import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from random import Random
import random

OnceNum = 100

engine = create_engine(dataSource,pool_size=5,max_overflow=5,encoding='utf-8')
DBSession = sessionmaker(bind=engine)

metadata = MetaData(engine)

persons = Table('persons', metadata,
    Column('id', Integer, primary_key=True),
    Column('no', String(20)),
    Column('name', String(20)))


relations = Table('relations',metadata,
    Column('id', Integer, primary_key=True),
    Column('no_from', String(20)),
    Column('no_to', String(20)))


metadata.create_all(engine)

def random_str(randomlength=10):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def executeSQL(sqlString,values):
    s=engine.connect()
    s.execute(sqlString % values[:-1])
    engine.connect().close()
    return ''

def getNumStr(i):
    str_value = str(i)
    if(len(str_value)!=10):
        return '0'*(10-len(str_value))+str_value
    return str_value

def insertDataToInfo():
    sqlString = 'insert into persons(no,name) values %s'
    i=0
    values=''
    while i < nodeNum:
        str_No = getNumStr(i)
        name = random_str()
        values="('%s','%s')" % (str_No , name) +','+values
        i += 1
        if(i % OnceNum == OnceNum-1):
            values = executeSQL(sqlString,values)
    if(len(values)!=0):
        executeSQL(sqlString,values)

def insertDateToRelation():
    sqlString = 'insert into relations(no_from,no_to) values %s'
    i=0
    values=''
    while i < relationNum:
        str_NoFrom=getNumStr(random.randint(0,nodeNum))
        str_NoTo=getNumStr(random.randint(0,nodeNum))
        values="('%s','%s')" % (str_NoFrom , str_NoTo) +','+values
        i += 1
        if(i % OnceNum == OnceNum-1):
            values = executeSQL(sqlString,values)
    if(len(values)!=0):
        executeSQL(sqlString,values)


def getSingleInfo(index):
    return (engine.execute('select * from persons where id = %s',str(index))).fetchall()[0]

def getSingleRelation(index):
    return (engine.execute('select * from relations where id = %s', str(index))).fetchall()[0]


insertDataToInfo()
insertDateToRelation()


