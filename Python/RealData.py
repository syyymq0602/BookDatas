import numpy as np
import threading
import time
import socket
import json
from Python.Data import Data

tx = 5  # 故障初始阶段时间
ty = 15  # 故障阶段时间
# RCS001MIXQ1: 5.875
# RCS106MVXQ1: 0.8667
# RCS107MVXQ1: 0.8974
t1 = time.time()
normal_data = []
fault_1_data = []
# 绑定信息 这里绑定的数据是一个元组
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1.声明协议类型，同时生成socket链接对象
tcp_socket.bind(("127.0.0.1", 1235))
address =("127.0.0.1",1234)
tcp_socket.connect(address)


def fun_timer4():
    def fun_timer5():
        RCS001MIXQ1 = np.random.normal(loc=12.875189801042958e+02, scale=2.745910268115703)  # loc：均值， scale:标准差
        RCS001MIXQ1 = np.float(RCS001MIXQ1)

        RCS106MVXQ1 = np.random.normal(loc=1.866723880510640, scale=0.0349)
        RCS106MVXQ1 = np.float(RCS106MVXQ1)

        RCS107MVXQ1 = np.random.normal(loc=1.897424671010749, scale=0.081219378558145)
        RCS107MVXQ1 = np.float(RCS107MVXQ1)

        RCS150MMXQ1 = np.random.normal(loc=2.135426742746030e+02, scale=13.516308550230391)
        RCS150MMXQ1 = np.float(RCS150MMXQ1)

        RCS151MMXQ1 = np.random.normal(loc=2.215861853450753e+02, scale=12.089381173673026)
        RCS151MMXQ1 = np.float(RCS151MMXQ1)

        RCS152MMXQ1 = np.random.normal(loc=80.409067024682706, scale=1.041220776194501)
        RCS152MMXQ1 = np.float(RCS152MMXQ1)

        print("故障阶段数据:", "RCS001MIXQ1:", RCS001MIXQ1, " RCS106MVXQ1:", RCS106MVXQ1, " RCS107MVXQ1:", RCS107MVXQ1)
        send_data = str(RCS001MIXQ1) + str("  ") + str(RCS106MVXQ1) + str("  ") + str(RCS107MVXQ1) + str("  ") + str(
            RCS150MMXQ1) + str("  ") + str(RCS151MMXQ1) + str("  ")
        # tcp_socket.sendto(send_data.encode("utf-8"))

        global timer3

        t4 = time.time()
        timer3 = threading.Timer(1, fun_timer5)
        timer3.start()

    timer3 = threading.Timer(interval=1, function=fun_timer5)  # interval:等待时间，func:执行函数
    timer3.start()


def fun_timer2():
    def fun_timer3():
        RCS001MIXQ1 = np.random.normal(loc=8.875189801042958e+02, scale=2.745910268115703)  # loc：均值， scale:标准差
        RCS001MIXQ1 = np.float(RCS001MIXQ1)

        RCS106MVXQ1 = np.random.normal(loc=1.266723880510640, scale=0.0349)
        RCS106MVXQ1 = np.float(RCS106MVXQ1)

        RCS107MVXQ1 = np.random.normal(loc=1.297424671010749, scale=0.081219378558145)
        RCS107MVXQ1 = np.float(RCS107MVXQ1)

        RCS150MMXQ1 = np.random.normal(loc=1.535426742746030e+02, scale=13.516308550230391)
        RCS150MMXQ1 = np.float(RCS150MMXQ1)

        RCS151MMXQ1 = np.random.normal(loc=1.615861853450753e+02, scale=12.089381173673026)
        RCS151MMXQ1 = np.float(RCS151MMXQ1)

        RCS152MMXQ1 = np.random.normal(loc=65.409067024682706, scale=1.041220776194501)
        RCS152MMXQ1 = np.float(RCS152MMXQ1)

        RCS153MMXQ1 = np.random.normal(loc=56.565427483470806, scale=0.971338199888906)
        RCS153MMXQ1 = np.float(RCS153MMXQ1)

        RCS160MCXQ1 = np.random.normal(loc=1.493249163782827e+03, scale=0.646411050597545)
        RCS160MCXQ1 = np.float(RCS160MCXQ1)

        RCS601MNXQ1 = np.random.normal(loc=94.631692920269420, scale=1.288557338566940)
        RCS601MNXQ1 = np.float(RCS601MNXQ1)

        RCS602MNXQ1 = np.random.normal(loc=94.333489195720790, scale=1.192110162287749)
        RCS602MNXQ1 = np.float(RCS602MNXQ1)

        RCS603MNXQ1 = np.random.normal(loc=30.438213099377520, scale=3.571389144186890)
        RCS603MNXQ1 = np.float(RCS603MNXQ1)

        RCS604MNXQ1 = np.random.normal(loc=30.145695883154200, scale=3.625238773721247)
        RCS604MNXQ1 = np.float(RCS604MNXQ1)

        RCS605MDXQ1 = np.random.normal(loc=2.767466892744297e+03, scale=6.897553533926969)
        RCS605MDXQ1 = np.float(RCS605MDXQ1)

        RCS605MNXQ1 = np.random.normal(loc=52.837410330893010, scale=0.462179116181627)
        RCS605MNXQ1 = np.float(RCS605MNXQ1)

        RCS606MDXQ1 = np.random.normal(loc=3.442426939503015e+02, scale=58.084551632246280)
        RCS606MDXQ1 = np.float(RCS606MDXQ1)

        RCS606MNXQ1 = np.random.normal(loc=53.600203238404580, scale=0.094762753901546)
        RCS606MNXQ1 = np.float(RCS606MNXQ1)

        RCS606MPXQ1 = np.random.normal(loc=0.076368560549005, scale=0.006847207762448)
        RCS606MPXQ1 = np.float(RCS606MPXQ1)

        RCS611MTXQ1 = np.random.normal(loc=76.498099559042190, scale=0.109909892997096)
        RCS611MTXQ1 = np.float(RCS611MTXQ1)

        RCS612MTXQ1 = np.random.normal(loc=70.634724135106380, scale=0.138274780519703)
        RCS612MTXQ1 = np.float(RCS612MTXQ1)

        RCS613MTXQ1 = np.random.normal(loc=65.862097660868930, scale=0.134016367675141)
        RCS613MTXQ1 = np.float(RCS613MTXQ1)

        RCS615MTXQ1 = np.random.normal(loc=67.488981609023100, scale=0.140163202319602)
        RCS615MTXQ1 = np.float(RCS615MTXQ1)

        RCS616MTXQ1 = np.random.normal(loc=70.723262462289600, scale=117015093654033)
        RCS616MTXQ1 = np.float(RCS616MTXQ1)

        RCS620MTXQ1 = np.random.normal(loc=55.788997581059070, scale=0.142936412649990)
        RCS620MTXQ1 = np.float(RCS620MTXQ1)

        RCS622MTXQ1 = np.random.normal(loc=31.263797641233833, scale=0.213894582841562)
        RCS622MTXQ1 = np.float(RCS622MTXQ1)

        RCS631MTXQ1 = np.random.normal(loc=69.049546880297870, scale=0.220317656831326)
        RCS631MTXQ1 = np.float(RCS631MTXQ1)

        RCS632MTXQ1 = np.random.normal(loc=69.887459635857600, scale=0.200911191555422)
        RCS632MTXQ1 = np.float(RCS632MTXQ1)

        RCS643MTXQ1 = np.random.normal(loc=65.520238191693420, scale=0.133912435891065)
        RCS643MTXQ1 = np.float(RCS643MTXQ1)

        RCS644MTXQ1 = np.random.normal(loc=65.298817143320010, scale=0.145158721879140)
        RCS644MTXQ1 = np.float(RCS644MTXQ1)

        RCS645MTXQ1 = np.random.normal(loc=65.295116954664400, scale=0.140748242011379)
        RCS645MTXQ1 = np.float(RCS645MTXQ1)

        RCS650MPXQ1 = np.random.normal(loc=0.215686045300202, scale=0.008014714235006)
        RCS650MPXQ1 = np.float(RCS650MPXQ1)

        RCS651MTXQ1 = np.random.normal(loc=57.525176791920660, scale=0.181475527776540)
        RCS651MTXQ1 = np.float(RCS651MTXQ1)

        RCS652MTXQ1 = np.random.normal(loc=51.704229117734826, scale=0.210833187318344)
        RCS652MTXQ1 = np.float(RCS652MTXQ1)

        RCS653MTXQ1 = np.random.normal(loc=52.212149165003520, scale=0.161119385140606)
        RCS653MTXQ1 = np.float(RCS653MTXQ1)

        RCS654MTXQ1 = np.random.normal(loc=27.803655050292893, scale=0.243213558210030)
        RCS654MTXQ1 = np.float(RCS654MTXQ1)

        RCS655MTXQ1 = np.random.normal(loc=32.733275656530594, scale=0.252884487328883)
        RCS655MTXQ1 = np.float(RCS655MTXQ1)

        WCC111MDXQ1 = np.random.normal(loc=46.468423282136555, scale=0.187880844815710)
        WCC111MDXQ1 = np.float(WCC111MDXQ1)

        WCC121MDXQ1 = np.random.normal(loc=26.201447552688137, scale=0.126570790404492)
        WCC121MDXQ1 = np.float(WCC121MDXQ1)

        WCC131MDXQ1 = np.random.normal(loc=25.766224580733635, scale=25.766224580733635)
        WCC131MDXQ1 = np.float(WCC131MDXQ1)

        print("故障初级阶段数据:", "RCS001MIXQ1:", RCS001MIXQ1, " RCS106MVXQ1:", RCS106MVXQ1, " RCS107MVXQ1:", RCS107MVXQ1,
              " RCS150MMXQ1:", RCS150MMXQ1, " RCS151MMXQ1:", RCS151MMXQ1)
        print("             ", "RCS152MMXQ1:", RCS152MMXQ1, " RCS153MMXQ1:", RCS153MMXQ1, " RCS160MCXQ1:", RCS160MCXQ1,
              " RCS601MNXQ1:", RCS601MNXQ1, " RCS602MNXQ1:", RCS602MNXQ1)
        print("             ", "RCS603MNXQ1:", RCS603MNXQ1, " RCS604MNXQ1:", RCS604MNXQ1, " RCS605MDXQ1:", RCS605MDXQ1,
              " RCS605MNXQ1:", RCS605MNXQ1, " RCS606MDXQ1:", RCS606MDXQ1)
        print("             ", "RCS606MNXQ1:", RCS606MNXQ1, " RCS606MPXQ1:", RCS606MPXQ1, " RCS611MTXQ1:", RCS611MTXQ1,
              " RCS612MTXQ1:", RCS612MTXQ1, " RCS613MTXQ1:", RCS613MTXQ1)
        print("             ", "RCS615MTXQ1:", RCS615MTXQ1, " RCS616MTXQ1:", RCS616MTXQ1, " RCS620MTXQ1:", RCS620MTXQ1,
              " RCS622MTXQ1:", RCS622MTXQ1)
        print("             ", "CS631MTXQ1:", RCS631MTXQ1, "RCS632MTXQ1:", RCS632MTXQ1, " RCS643MTXQ1:", RCS643MTXQ1,
              " RCS644MTXQ1:", RCS644MTXQ1, " RCS645MTXQ1:", RCS645MTXQ1)
        print("             ", "RCS650MPXQ1:", RCS650MPXQ1, "RCS651MTXQ1:", RCS651MTXQ1, " RCS652MTXQ1:", RCS652MTXQ1,
              " RCS653MTXQ1:", RCS653MTXQ1, " RCS654MTXQ1:", RCS654MTXQ1)
        print("             ", "WCC111MDXQ1:", WCC111MDXQ1, " WCC121MDXQ1:", WCC121MDXQ1, " WCC131MDXQ1:", WCC131MDXQ1,
              " RCS655MTXQ1:", RCS655MTXQ1)

        send_data = str(RCS001MIXQ1) + str("  ") + str(RCS106MVXQ1) + str("  ") + str(RCS107MVXQ1) + str("  ") + str(
            RCS150MMXQ1) + str("  ") + str(RCS151MMXQ1) + str("  ")
        # tcp_socket.sendto(send_data.encode("utf-8"))

        #         RCS152MMXQ1,
        #         RCS153MMXQ1,RCS160MCXQ1,RCS601MNXQ1,RCS602MNXQ1,
        #         RCS603MNXQ1,RCS604MNXQ1,RCS605MDXQ1,RCS605MNXQ1,RCS606MDXQ1,RCS606MNXQ1,RCS606MPXQ1,RCS611MTXQ1,RCS612MTXQ1,RCS613MTXQ1,RCS615MTXQ1,RCS616MTXQ1,RCS620MTXQ1,RCS622MTXQ1,
        #         RCS631MTXQ1,,RCS632MTXQ1,RCS643MTXQ1,RCS644MTXQ1,RCS645MTXQ1,RCS650MPXQ1,RCS651MTXQ1,RCS652MTXQ1,RCS653MTXQ1,RCS654MTXQ1,WCC111MDXQ1,,WCC121MDXQ1,,WCC131MDXQ1,RCS655MTXQ1])

        global timer2

        t3 = time.time()
        timer2 = threading.Timer(1, fun_timer3)
        if t1 + ty < t3:
            timer2.cancel()
            fun_timer4()
        else:
            timer2.start()

    timer2 = threading.Timer(interval=1, function=fun_timer3)  # interval:等待时间，func:执行函数
    timer2.start()


def fun_timer():
    RCS001MIXQ1 = np.random.normal(loc=5.875189801042958e+02, scale=2.745910268115703)  # loc：均值， scale:标准差
    RCS001MIXQ1 = np.float(RCS001MIXQ1)

    RCS106MVXQ1 = np.random.normal(loc=0.866723880510640, scale=0.0349)
    RCS106MVXQ1 = np.float(RCS106MVXQ1)

    RCS107MVXQ1 = np.random.normal(loc=0.897424671010749, scale=0.081219378558145)
    RCS107MVXQ1 = np.float(RCS107MVXQ1)

    RCS150MMXQ1 = np.random.normal(loc=1.135426742746030e+02, scale=13.516308550230391)
    RCS150MMXQ1 = np.float(RCS150MMXQ1)

    RCS151MMXQ1 = np.random.normal(loc=1.215861853450753e+02, scale=12.089381173673026)
    RCS151MMXQ1 = np.float(RCS151MMXQ1)

    RCS152MMXQ1 = np.random.normal(loc=59.409067024682706, scale=1.041220776194501)
    RCS152MMXQ1 = np.float(RCS152MMXQ1)

    RCS153MMXQ1 = np.random.normal(loc=56.565427483470806, scale=0.971338199888906)
    RCS153MMXQ1 = np.float(RCS153MMXQ1)

    RCS160MCXQ1 = np.random.normal(loc=1.493249163782827e+03, scale=0.646411050597545)
    RCS160MCXQ1 = np.float(RCS160MCXQ1)

    RCS601MNXQ1 = np.random.normal(loc=94.631692920269420, scale=1.288557338566940)
    RCS601MNXQ1 = np.float(RCS601MNXQ1)

    RCS602MNXQ1 = np.random.normal(loc=94.333489195720790, scale=1.192110162287749)
    RCS602MNXQ1 = np.float(RCS602MNXQ1)

    RCS603MNXQ1 = np.random.normal(loc=30.438213099377520, scale=3.571389144186890)
    RCS603MNXQ1 = np.float(RCS603MNXQ1)

    RCS604MNXQ1 = np.random.normal(loc=30.145695883154200, scale=3.625238773721247)
    RCS604MNXQ1 = np.float(RCS604MNXQ1)

    RCS605MDXQ1 = np.random.normal(loc=2.767466892744297e+03, scale=6.897553533926969)
    RCS605MDXQ1 = np.float(RCS605MDXQ1)

    RCS605MNXQ1 = np.random.normal(loc=52.837410330893010, scale=0.462179116181627)
    RCS605MNXQ1 = np.float(RCS605MNXQ1)

    RCS606MDXQ1 = np.random.normal(loc=3.442426939503015e+02, scale=58.084551632246280)
    RCS606MDXQ1 = np.float(RCS606MDXQ1)

    RCS606MNXQ1 = np.random.normal(loc=53.600203238404580, scale=0.094762753901546)
    RCS606MNXQ1 = np.float(RCS606MNXQ1)

    RCS606MPXQ1 = np.random.normal(loc=0.076368560549005, scale=0.006847207762448)
    RCS606MPXQ1 = np.float(RCS606MPXQ1)

    RCS611MTXQ1 = np.random.normal(loc=76.498099559042190, scale=0.109909892997096)
    RCS611MTXQ1 = np.float(RCS611MTXQ1)

    RCS612MTXQ1 = np.random.normal(loc=70.634724135106380, scale=0.138274780519703)
    RCS612MTXQ1 = np.float(RCS612MTXQ1,1)

    RCS613MTXQ1 = np.random.normal(loc=65.862097660868930, scale=0.134016367675141)
    RCS613MTXQ1 = np.float(RCS613MTXQ1)

    RCS615MTXQ1 = np.random.normal(loc=67.488981609023100, scale=0.140163202319602)
    RCS615MTXQ1 = np.float(RCS615MTXQ1)

    RCS616MTXQ1 = np.random.normal(loc=70.723262462289600, scale=117015093654033)
    RCS616MTXQ1 = np.float(RCS616MTXQ1)

    RCS620MTXQ1 = np.random.normal(loc=55.788997581059070, scale=0.142936412649990)
    RCS620MTXQ1 = np.float(RCS620MTXQ1)

    RCS622MTXQ1 = np.random.normal(loc=31.263797641233833, scale=0.213894582841562)
    RCS622MTXQ1 = np.float(RCS622MTXQ1)

    RCS631MTXQ1 = np.random.normal(loc=69.049546880297870, scale=0.220317656831326)
    RCS631MTXQ1 = np.float(RCS631MTXQ1)

    RCS632MTXQ1 = np.random.normal(loc=69.887459635857600, scale=0.200911191555422)
    RCS632MTXQ1 = np.float(RCS632MTXQ1)

    RCS643MTXQ1 = np.random.normal(loc=65.520238191693420, scale=0.133912435891065)
    RCS643MTXQ1 = np.float(RCS643MTXQ1)

    RCS644MTXQ1 = np.random.normal(loc=65.298817143320010, scale=0.145158721879140)
    RCS644MTXQ1 = np.float(RCS644MTXQ1)

    RCS645MTXQ1 = np.random.normal(loc=65.295116954664400, scale=0.140748242011379)
    RCS645MTXQ1 = np.float(RCS645MTXQ1)

    RCS650MPXQ1 = np.random.normal(loc=0.215686045300202, scale=0.008014714235006)
    RCS650MPXQ1 = np.float(RCS650MPXQ1)

    RCS651MTXQ1 = np.random.normal(loc=57.525176791920660, scale=0.181475527776540)
    RCS651MTXQ1 = np.float(RCS651MTXQ1)

    RCS652MTXQ1 = np.random.normal(loc=51.704229117734826, scale=0.210833187318344)
    RCS652MTXQ1 = np.float(RCS652MTXQ1)

    RCS653MTXQ1 = np.random.normal(loc=52.212149165003520, scale=0.161119385140606)
    RCS653MTXQ1 = np.float(RCS653MTXQ1)

    RCS654MTXQ1 = np.random.normal(loc=27.803655050292893, scale=0.243213558210030)
    RCS654MTXQ1 = np.float(RCS654MTXQ1)

    RCS655MTXQ1 = np.random.normal(loc=32.733275656530594, scale=0.252884487328883)
    RCS655MTXQ1 = np.float(RCS655MTXQ1)

    WCC111MDXQ1 = np.random.normal(loc=46.468423282136555, scale=0.187880844815710)
    WCC111MDXQ1 = np.float(WCC111MDXQ1)

    WCC121MDXQ1 = np.random.normal(loc=26.201447552688137, scale=0.126570790404492)
    WCC121MDXQ1 = np.float(WCC121MDXQ1)

    WCC131MDXQ1 = np.random.normal(loc=25.766224580733635, scale=25.766224580733635)
    WCC131MDXQ1 = np.float(WCC131MDXQ1)

    PrintData = Data(RCS001MIXQ1, RCS106MVXQ1, RCS107MVXQ1, RCS150MMXQ1, RCS151MMXQ1, RCS152MMXQ1,RCS153MMXQ1,
                     RCS160MCXQ1, RCS601MNXQ1, RCS602MNXQ1, RCS603MNXQ1, RCS604MNXQ1, RCS605MDXQ1,RCS605MNXQ1,
                     RCS606MDXQ1, RCS606MNXQ1, RCS606MPXQ1, RCS611MTXQ1, RCS612MTXQ1, RCS613MTXQ1, RCS615MTXQ1,
                     RCS616MTXQ1,RCS620MTXQ1, RCS622MTXQ1, RCS631MTXQ1, RCS632MTXQ1, RCS643MTXQ1, RCS644MTXQ1,
                     RCS645MTXQ1,RCS650MPXQ1,RCS651MTXQ1, RCS652MTXQ1, RCS653MTXQ1, RCS654MTXQ1, WCC111MDXQ1,
                     WCC121MDXQ1, WCC131MDXQ1,RCS655MTXQ1)


    print("正常阶段数据:", "RCS001MIXQ1:", RCS001MIXQ1, " RCS106MVXQ1:", RCS106MVXQ1, " RCS107MVXQ1:", RCS107MVXQ1,
          " RCS150MMXQ1:", RCS150MMXQ1, " RCS151MMXQ1:", RCS151MMXQ1)
    print("             ", "RCS152MMXQ1:", RCS152MMXQ1, " RCS153MMXQ1:", RCS153MMXQ1, " RCS160MCXQ1:", RCS160MCXQ1,
          " RCS601MNXQ1:", RCS601MNXQ1, " RCS602MNXQ1:", RCS602MNXQ1)
    print("             ", "RCS603MNXQ1:", RCS603MNXQ1, " RCS604MNXQ1:", RCS604MNXQ1, " RCS605MDXQ1:", RCS605MDXQ1,
          " RCS605MNXQ1:", RCS605MNXQ1, " RCS606MDXQ1:", RCS606MDXQ1)
    print("             ", "RCS606MNXQ1:", RCS606MNXQ1, " RCS606MPXQ1:", RCS606MPXQ1, " RCS611MTXQ1:", RCS611MTXQ1,
          " RCS612MTXQ1:", RCS612MTXQ1, " RCS613MTXQ1:", RCS613MTXQ1)
    print("             ", "RCS615MTXQ1:", RCS615MTXQ1, " RCS616MTXQ1:", RCS616MTXQ1, " RCS620MTXQ1:", RCS620MTXQ1,
          " RCS622MTXQ1:", RCS622MTXQ1)
    print("             ", "CS631MTXQ1:", RCS631MTXQ1, "RCS632MTXQ1:", RCS632MTXQ1, " RCS643MTXQ1:", RCS643MTXQ1,
          " RCS644MTXQ1:", RCS644MTXQ1, " RCS645MTXQ1:", RCS645MTXQ1)
    print("             ", "RCS650MPXQ1:", RCS650MPXQ1, "RCS651MTXQ1:", RCS651MTXQ1, " RCS652MTXQ1:", RCS652MTXQ1,
          " RCS653MTXQ1:", RCS653MTXQ1, " RCS654MTXQ1:", RCS654MTXQ1)
    print("             ", "WCC111MDXQ1:", WCC111MDXQ1, " WCC121MDXQ1:", WCC121MDXQ1, " WCC131MDXQ1:", WCC131MDXQ1,
          " RCS655MTXQ1:", RCS655MTXQ1)

    send_data = str(RCS001MIXQ1) + str("  ") + str(RCS106MVXQ1) + str("  ") + str(RCS107MVXQ1) + str("  ") + str(
        RCS150MMXQ1) + str("  ") + str(RCS151MMXQ1) + str("  ")
    sendData = json.dumps(PrintData,skipkeys=True,default=lambda obj: obj.__dict__)
    tcp_socket.send(sendData.encode("utf-8"))

    #     normal_data.append([RCS001MIXQ1,RCS106MVXQ1,RCS107MVXQ1,RCS150MMXQ1,RCS151MMXQ1,RCS152MMXQ1,RCS153MMXQ1,RCS160MCXQ1,RCS601MNXQ1,RCS602MNXQ1,
    #     RCS603MNXQ1,RCS604MNXQ1,RCS605MDXQ1,RCS605MNXQ1,RCS606MDXQ1,RCS606MNXQ1,RCS606MPXQ1,RCS611MTXQ1,RCS612MTXQ1,RCS613MTXQ1,RCS615MTXQ1,RCS616MTXQ1,RCS620MTXQ1,RCS622MTXQ1,
    #     RCS631MTXQ1,,RCS632MTXQ1,RCS643MTXQ1,RCS644MTXQ1,RCS645MTXQ1,RCS650MPXQ1,RCS651MTXQ1,RCS652MTXQ1,RCS653MTXQ1,RCS654MTXQ1,WCC111MDXQ1,,WCC121MDXQ1,,WCC131MDXQ1,RCS655MTXQ1])

    global timer

    t2 = time.time()
    if t1 + tx < t2:
        timer.cancel()
        fun_timer2()
    else:
        timer = threading.Timer(1, fun_timer)
        timer.start()


timer = threading.Timer(interval=1, function=fun_timer)  # interval:等待时间，func:执行函数
timer.start()
# timer3.cancel()
