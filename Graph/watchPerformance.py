import time
import psutil


def calcuteTimeOperate(record,cpu,mem,disk, startTime):
    endTime=time.time()
    record.append(endTime-startTime)
    cpu.append(getCPUAvg())
    mem.append(getMemUsed())
    disk.append(getFreeDisk())


def getCPUAvg():
    arr = psutil.cpu_percent(interval=1, percpu=True)
    count=0
    for i in arr:
        count+=i
    return count/len(arr)

def getMemUsed():
    mem = psutil.virtual_memory()
    return mem.used


def getFreeDisk():
    disk = psutil.disk_usage('/')
    return disk.free