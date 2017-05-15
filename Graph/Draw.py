from Constant import *
from pylab import *


def drawSingleWriteV(neoV,neoVCpu,neoVMem,neoVDisk,oriV,oriVCpu,oriVMem,OriVDisk,araV,araVCpu,araVMem,AraVDsik):
    subplot(2, 2, 1)

    plot(nodeArray, neoV, color='blue', label='Neo4J')
    plot(nodeArray, oriV, color='black', label='OrientDB')
    plot(nodeArray, araV, color='red', label='ArangoDB')

    subplot(2, 2, 2)
    plot(nodeArray, neoVCpu, color='blue', label='Neo4J')
    plot(nodeArray, oriVCpu, color='black', label='OrientDB')
    plot(nodeArray, araVCpu, color='red', label='ArangoDB')

    subplot(2, 2, 3)
    plot(nodeArray, neoVMem, color='blue', label='Neo4J')
    plot(nodeArray, oriVMem, color='black', label='OrientDB')
    plot(nodeArray, araVMem, color='red', label='ArangoDB')

    subplot(2, 2, 4)
    plot(nodeArray, neoVDisk, color='blue', label='Neo4J')
    plot(nodeArray, OriVDisk, color='black', label='OrientDB')
    plot(nodeArray, AraVDsik, color='red', label='ArangoDB')

    legend(loc='upper left')
    show()

def drawSingleWriteE(neoE,neoECpu,neoEMem,neoEDisk,oriE,oriECpu,oriEMem,oriEDisk,araE,araECpu,araEMem,araEDisk):
    subplot(2, 2, 1)
    plot(relationArray, neoE, color='blue', label='Neo4J')
    plot(relationArray, oriE, color='black', label='OrientDB')
    plot(relationArray, araE, color='red', label='ArangoDB')

    subplot(2, 2, 2)
    plot(relationArray, neoECpu, color='blue', label='Neo4J')
    plot(relationArray, oriECpu, color='black', label='OrientDB')
    plot(relationArray, araECpu, color='red', label='ArangoDB')



    subplot(2, 2, 3)
    plot(relationArray, neoEMem, color='blue', label='Neo4J')
    plot(relationArray, oriEMem, color='black', label='OrientDB')
    plot(relationArray, araEMem, color='red', label='ArangoDB')


    subplot(2, 2, 4)
    plot(relationArray, neoEDisk, color='blue', label='Neo4J')
    plot(relationArray, oriEDisk, color='black', label='OrientDB')
    plot(relationArray, araEDisk, color='red', label='ArangoDB')

    legend(loc='upper left')
    show()

