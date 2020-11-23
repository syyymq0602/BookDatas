import numpy as np

class Data(object):
    def __init__(self,VibrationX,VibrationY,MotorDisplacementX,MotorDisplacementY,PumpDisplacementX,
    PumpDisplacementY,MotorSpeed,ZeroSpeed,PumpOutletP1,PumpOutletP2,FilterPressure1,FilterPressure2,
    FirPreBeforeSeal,SecPreBeforeSeal,ThiPreBeforeSeal,UpperBearTemperature,UpperBearBushTemperature,
    LowerThrustBearBushTemperature,UpperThrustBearBushTemperature,UpMotorAirTemperature,StatorTemperatureU,
    StatorTemperatureV,StatorTemperatureW,LowMotorAirTemperature,LowerOilTemperature,LowerBearTemperature,
    CoolerInletTemperature,CoolerOutletTemperature,InjectWaterTemperature,ControlLeakageTemperature,
    ControlLeakageFlow,LowPressureLeakageFlow,InjectWaterFlow,CoolerSecFlow,UpperBearingOilLevel,
    LowerBearingOilLevel,SealPositionMonitor,FlywheelPositionMonitor):
        self.VibrationX=VibrationX
        self.VibrationY=VibrationY
        self.MotorDisplacementX=MotorDisplacementX
        self.MotorDisplacementY=MotorDisplacementY
        self.PumpDisplacementX=PumpDisplacementX
        self.PumpDisplacementY=PumpDisplacementY
        self.MotorSpeed=MotorSpeed
        self.ZeroSpeed=ZeroSpeed
        self.PumpOutletP1=PumpOutletP1
        self.PumpOutletP2=PumpOutletP2
        self.FilterPressure1=FilterPressure1
        self.FilterPressure2=FilterPressure2
        self.FirPreBeforeSeal=FirPreBeforeSeal
        self.SecPreBeforeSeal=SecPreBeforeSeal
        self.ThiPreBeforeSeal=ThiPreBeforeSeal
        self.UpperBearTemperature=UpperBearTemperature
        self.UpperBearBushTemperature=UpperBearBushTemperature
        self.LowerThrustBearBushTemperature=LowerThrustBearBushTemperature
        self.UpperThrustBearBushTemperature=UpperThrustBearBushTemperature
        self.UpMotorAirTemperature=UpMotorAirTemperature
        self.StatorTemperatureU=StatorTemperatureU
        self.StatorTemperatureV=StatorTemperatureV
        self.StatorTemperatureW=StatorTemperatureW
        self.LowMotorAirTemperature=LowMotorAirTemperature
        self.LowerOilTemperature=LowerOilTemperature
        self.LowerBearTemperature=LowerBearTemperature
        self.CoolerInletTemperature=CoolerInletTemperature
        self.CoolerOutletTemperature=CoolerOutletTemperature
        self.InjectWaterTemperature=InjectWaterTemperature
        self.ControlLeakageTemperature=ControlLeakageTemperature
        self.ControlLeakageFlow=ControlLeakageFlow
        self.LowPressureLeakageFlow=LowPressureLeakageFlow
        self.InjectWaterFlow=InjectWaterFlow
        self.CoolerSecFlow=CoolerSecFlow
        self.UpperBearingOilLevel=UpperBearingOilLevel
        self.LowerBearingOilLevel=LowerBearingOilLevel
        self.SealPositionMonitor=SealPositionMonitor
        self.FlywheelPositionMonitor=FlywheelPositionMonitor


normal_VibrationX = np.random.normal(loc=1.493249163782827e+03,scale=0.646411050597545) # 160
normal_VibrationX = int(normal_VibrationX )
normal_VibrationY = np.random.normal(loc=5.875189801042958e+02,scale=2.745910268115703) # 001
normal_VibrationY = round(normal_VibrationY,1)
normal_MotorDisplacementX = np.random.normal(loc=0.866723880510640,scale=0.0349) # 106
normal_MotorDisplacementX = round( normal_MotorDisplacementX ,3)
normal_MotorDisplacementY = np.random.normal(loc=0.897424671010749,scale=0.081219378558145) # 107
normal_MotorDisplacementY = round(normal_MotorDisplacementY,3)
normal_PumpDisplacementX = np.random.normal(loc=59.409067024682706,scale=1.041220776194501) # 152
normal_PumpDisplacementX = round(normal_PumpDisplacementX ,1)
normal_PumpDisplacementY = np.random.normal(loc=56.565427483470806,scale=0.971338199888906) # 153
normal_PumpDisplacementY = round(normal_PumpDisplacementY,1)
normal_MotorSpeed = np.random.normal(loc=1.135426742746030e+02,scale=13.516308550230391) # 150
normal_MotorSpeed = round(normal_MotorSpeed,1)
normal_ZeroSpeed = np.random.normal(loc=1.215861853450753e+02,scale=12.089381173673026) # 151
normal_ZeroSpeed = round(normal_ZeroSpeed,1)
normal_PumpOutletP1 = np.random.normal(loc=76.498099559042190,scale=0.109909892997096 ) # 611
normal_PumpOutletP1 = round(normal_PumpOutletP1,1)
normal_PumpOutletP2 = np.random.normal(loc=70.634724135106380,scale=0.138274780519703 ) # 612
normal_PumpOutletP2 = round(normal_PumpOutletP2,1)
normal_FilterPressure1 = np.random.normal(loc=65.298817143320010,scale= 0.145158721879140) # 644
normal_FilterPressure1 = round(normal_FilterPressure1,1)
normal_FilterPressure2 = np.random.normal(loc=65.295116954664400,scale=0.140748242011379 ) # 645
normal_FilterPressure2 = round(normal_FilterPressure2,1)
normal_FirPreBeforeSeal = np.random.normal(loc= 65.862097660868930,scale=0.134016367675141 ) #613
normal_FirPreBeforeSeal = round(normal_FirPreBeforeSeal,1)
normal_SecPreBeforeSeal = np.random.normal(loc=65.520238191693420,scale=0.133912435891065 ) # 643
normal_SecPreBeforeSeal = round(normal_SecPreBeforeSeal,1)
normal_ThiPreBeforeSeal = np.random.normal(loc=67.488981609023100,scale=0.140163202319602 ) # 615
normal_ThiPreBeforeSeal = round(normal_ThiPreBeforeSeal,1)
normal_UpperBearTemperature = np.random.normal(loc=70.723262462289600,scale=117015093654033) # 616
normal_UpperBearTemperature = round(normal_UpperBearTemperature,1)
normal_UpperBearBushTemperature = np.random.normal(loc=52.212149165003520,scale= 0.161119385140606) # 653
normal_UpperBearBushTemperature = round(normal_UpperBearBushTemperature,1)
normal_LowerThrustBearBushTemperature = np.random.normal(loc= 2.767466892744297e+03,scale=6.897553533926969) #605
normal_UpperBearBushTemperature = int(normal_UpperBearBushTemperature)
normal_UpperThrustBearBushTemperature = np.random.normal(loc=0.076368560549005,scale=0.006847207762448) # 606
normal_UpperThrustBearBushTemperature = round(normal_UpperThrustBearBushTemperature,2)
normal_UpMotorAirTemperature = np.random.normal(loc=0.215686045300202,scale=0.008014714235006 ) # 650
normal_UpMotorAirTemperature = round(normal_UpMotorAirTemperature,2)
normal_StatorTemperatureU = np.random.normal(loc= 94.631692920269420,scale=1.288557338566940) # 601
normal_StatorTemperatureU = round(normal_StatorTemperatureU,2)
normal_StatorTemperatureV = np.random.normal(loc= 94.333489195720790,scale=1.192110162287749) # 602
normal_StatorTemperatureV = round(normal_StatorTemperatureV,1)
normal_StatorTemperatureW = np.random.normal(loc= 30.438213099377520,scale=3.571389144186890) # 603
normal_StatorTemperatureW = round(normal_StatorTemperatureW,2)
normal_LowMotorAirTemperature = np.random.normal(loc= 30.145695883154200,scale=3.625238773721247) # 604
normal_LowMotorAirTemperature = round(normal_LowMotorAirTemperature,2)
normal_LowerOilTemperature = np.random.normal(loc= 52.837410330893010,scale=0.462179116181627) # 605
normal_LowerOilTemperature = round(normal_LowerOilTemperature,2)
normal_LowerBearTemperature = np.random.normal(loc= 53.600203238404580,scale= 0.094762753901546) # 606 MN
normal_LowerBearTemperature = round(normal_LowerBearTemperature,2)
normal_CoolerInletTemperature = np.random.normal(loc= 3.442426939503015e+02,scale=58.084551632246280) # 606 MD
normal_CoolerInletTemperature = int(normal_CoolerInletTemperature)
normal_CoolerOutletTemperature = np.random.normal(loc=57.525176791920660,scale= 0.181475527776540 ) # 651
normal_CoolerOutletTemperature = round(normal_CoolerOutletTemperature,1)
normal_InjectWaterTemperature = np.random.normal(loc=51.704229117734826,scale= 0.210833187318344) # 652
normal_InjectWaterTemperature = round(normal_InjectWaterTemperature,1)
normal_ControlLeakageTemperature = np.random.normal(loc= 27.803655050292893,scale= 0.243213558210030) # 654
normal_ControlLeakageTemperature = round(normal_ControlLeakageTemperature,2)
normal_ControlLeakageFlow = np.random.normal(loc=32.733275656530594,scale=0.252884487328883 )# 655
normal_ControlLeakageFlow = round(normal_ControlLeakageFlow ,2)
normal_LowPressureLeakageFlow = np.random.normal(loc=25.766224580733635,scale=25.766224580733635 ) # 131
normal_LowPressureLeakageFlow = round(normal_LowPressureLeakageFlow,2)
normal_InjectWaterFlow = np.random.normal(loc=46.468423282136555,scale= 0.187880844815710) # 111
normal_InjectWaterFlow = round(normal_InjectWaterFlow,2)
normal_CoolerSecFlow = np.random.normal(loc=26.201447552688137,scale=0.126570790404492 ) # 121
normal_CoolerSecFlow = round(normal_CoolerSecFlow ,2)
normal_UpperBearingOilLevel = np.random.normal(loc=69.049546880297870,scale= 0.220317656831326) # 631
normal_UpperBearingOilLevel = round(normal_UpperBearingOilLevel,1)
normal_LowerBearingOilLevel = np.random.normal(loc=69.887459635857600,scale= 0.200911191555422) # 632
normal_LowerBearingOilLevel = round(normal_LowerBearingOilLevel,1)
normal_SealPositionMonitor = np.random.normal(loc= 55.788997581059070,scale= 0.142936412649990) # 620
normal_SealPositionMonitor = round(normal_SealPositionMonitor ,2)
normal_FlywheelPositionMonitor = np.random.normal(loc=31.263797641233833,scale=0.213894582841562 ) # 622
normal_FlywheelPositionMonitor = round(normal_FlywheelPositionMonitor,2)

normal_Data = Data(normal_VibrationX,normal_VibrationY,normal_MotorDisplacementX,normal_MotorDisplacementY,normal_PumpDisplacementX,
    normal_PumpDisplacementY,normal_MotorSpeed,normal_ZeroSpeed,normal_PumpOutletP1,normal_PumpOutletP2,normal_FilterPressure1,normal_FilterPressure2,
    normal_FirPreBeforeSeal,normal_SecPreBeforeSeal,normal_ThiPreBeforeSeal,normal_UpperBearTemperature,normal_UpperBearBushTemperature,
    normal_LowerThrustBearBushTemperature,normal_UpperThrustBearBushTemperature,normal_UpMotorAirTemperature,normal_StatorTemperatureU,
    normal_StatorTemperatureV,normal_StatorTemperatureW,normal_LowMotorAirTemperature,normal_LowerOilTemperature,normal_LowerBearTemperature,
    normal_CoolerInletTemperature,normal_CoolerOutletTemperature,normal_InjectWaterTemperature,normal_ControlLeakageTemperature,
    normal_ControlLeakageFlow,normal_LowPressureLeakageFlow,normal_InjectWaterFlow,normal_CoolerSecFlow,normal_UpperBearingOilLevel,
    normal_LowerBearingOilLevel,normal_SealPositionMonitor,normal_FlywheelPositionMonitor)