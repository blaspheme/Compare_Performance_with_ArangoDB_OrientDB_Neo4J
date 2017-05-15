# Compare_Performance_with_ArangoDB_OrientDB_Neo4J
ArangoDB、Neo4j、OrientDB单机性能比较


# 环境
| 图数据库      | 版本     | 备注                      |
| --------- | ------ | ----------------------- |
| Neo4J     | 3.2    |                         |
| OrientDB  | 2.2.x  |                         |
| ArangoDB、 | 3.1.19 | 有密钥失效问题，导致无法下载成功server端 |
| Titan     | 1.0.0  | 需要集群，暂不分析               |

## OS&库信息

- OS：Ubuntu 16.04
- 虚拟机VM12
- python3驱动
  - python-arango
  - neo4j-driver
  - PyOrient
- 绘图库：MatPlotLib+Numpy
- 性能监测库：psutil


## 测试信息

- 测试所得四张图分别为
  - 数量时间图，斜率越小性能越好
  - CPU平均占用率图
  - RAM使用图
  - 硬盘剩余空间图
