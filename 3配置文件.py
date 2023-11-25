import configparser
#分隔符可以是=或：
#区块sectio，section名字不允许重复
#ini，配置文件，由section、key、value组成
#ConfigParser模块操作配置文件，解析
# [DEFAULT] 一个特殊的section。其他section的option取不到值时的备用值，不是必须提供

conf = configparser.ConfigParser()
INI = './配置文件.ini'
conf.read(INI,encoding='utf-8')

value = conf['select']['url']
print(value)


