import configparser
import os


def read_config(name):
    # 创建 ConfigParser 对象
    config = configparser.RawConfigParser()
    # 读取配置文件
    config.read(file_path(name))
    return config

def file_path(name):
    # 获取当前文件所在的根路径
    root_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root_dir, name)
    return file_path


def intercept(func):
    def wrapper(*args, **kwargs):
        # print('拦截方法:', func.__name__)
        res = func(*args, **kwargs)
        result = []
        for r in res:
            if r == '.DS_Store':
                continue
            result.append(r)
        return result

    return wrapper

@intercept
def read_dir(dir):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path = root_dir + '/resource/' + NAMESPACE
    return os.listdir(path + '/' + dir)


def read_file(filename, encoding='utf-8'):
    lines = []
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path = root_dir + '/resource/' + NAMESPACE
    if not os.path.exists(path+'/'+filename):
        print(filename+' file not exist')
        return []
    with open(path+'/'+filename, 'r', encoding=encoding) as file:
        for line in file:
            lines.append(line.replace("\n",""))
    return lines

# 以覆盖的方式写入
def write_file(prefix, filename, lines, encoding='utf-8'):
    print('写入文件:', filename)
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path = root_dir + '/resource/' + NAMESPACE +'/output/'
    # 防止路径不存在
    if not os.path.exists(path):
        os.makedirs(path)
    dir_file_path = path + '/' + prefix+filename
    if not os.path.exists(dir_file_path):
        open(dir_file_path, 'w').close()
    with open(dir_file_path, 'w', encoding=encoding) as f:
        for m in lines:
            f.write(m+'\n')

NAMESPACE = read_config('appconf.ini')['mod']['namespace']
print('namespace='+NAMESPACE)