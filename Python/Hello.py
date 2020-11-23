import socket
import time
import json
from Data import Data
# 绑定信息 这里绑定的数据是一个元组
# 声明协议类型为TCP协议，同时生成socket链接对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_socket.bind(("127.0.0.1", 1235))
# 定义连接地址，端口为1234
address =("127.0.0.1",3333)
udp_socket.connect(address)
# 测试数据
m = Data(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8)
# 类序列化为Json格式
a = json.dumps(m,default=lambda obj: obj.__dict__)
while True:
    # 获取需要发送的类容
    send_data = a
    # 发送数据，编码方式为UTF-8
    udp_socket.send(send_data.encode("utf-8"))
    # 延时1秒发送一次数据
    time.sleep(1)