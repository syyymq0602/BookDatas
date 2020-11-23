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
VibrationX = np.random.normal(loc=1.493249163782827e+03,scale=0.646411050597545) # 160
VibrationX = int(VibrationX )
fault_2_VibrationY = np.random.normal(loc=6.875189801042958e+02,scale=2.745910268115703) # 001
fault_2_VibrationY = round(fault_2_VibrationY,1)
fault_2_MotorDisplacementX = np.random.normal(loc=1.266723880510640,scale=0.0349) # 106
fault_2_MotorDisplacementX = round(fault_2_MotorDisplacementX ,3)
fault_2_MotorDisplacementY = np.random.normal(loc=1.297424671010749,scale=0.081219378558145) # 107
fault_2_MotorDisplacementY = round(fault_2_MotorDisplacementY,3)
fault_2_PumpDisplacementX = np.random.normal(loc=68.409067024682706,scale=1.041220776194501) # 152
fault_2_PumpDisplacementX = round(fault_2_PumpDisplacementX ,1)
fault_2_PumpDisplacementY = np.random.normal(loc=63.565427483470806,scale=0.971338199888906) # 153
fault_2_PumpDisplacementY = round(fault_2_PumpDisplacementY,1)
fault_2_MotorSpeed = np.random.normal(loc=1.305426742746030e+02,scale=13.516308550230391) # 150
fault_2_MotorSpeed = round(fault_2_MotorSpeed,1)
fault_2_ZeroSpeed = np.random.normal(loc=1.405861853450753e+02,scale=12.089381173673026) # 151
fault_2_ZeroSpeed = round(fault_2_ZeroSpeed,1)
fault_2_PumpOutletP1 = np.random.normal(loc=85.498099559042190,scale=0.109909892997096 ) # 611
fault_2_PumpOutletP1 = round(fault_2_PumpOutletP1,1)
fault_2_PumpOutletP2 = np.random.normal(loc=78.634724135106380,scale=0.138274780519703 ) # 612
fault_2_PumpOutletP2 = round(fault_2_PumpOutletP2,1)
fault_2_FilterPressure1 = np.random.normal(loc=72.298817143320010,scale= 0.145158721879140) # 644
fault_2_FilterPressure1 = round(fault_2_FilterPressure1,1)
fault_2_FilterPressure2 = np.random.normal(loc=72.295116954664400,scale=0.140748242011379 ) # 645
fault_2_FilterPressure2 = round(fault_2_FilterPressure2,1)
fault_2_FirPreBeforeSeal = np.random.normal(loc= 72.862097660868930,scale=0.134016367675141 ) #613
fault_2_FirPreBeforeSeal = round(fault_2_FirPreBeforeSeal,1)
fault_2_SecPreBeforeSeal = np.random.normal(loc=72.520238191693420,scale=0.133912435891065 ) # 643
fault_2_SecPreBeforeSeal = round(fault_2_SecPreBeforeSeal,1)
fault_2_ThiPreBeforeSeal = np.random.normal(loc=72.488981609023100,scale=0.140163202319602 ) # 615
fault_2_ThiPreBeforeSeal = round(fault_2_ThiPreBeforeSeal,1)
fault_2_UpperBearTemperature = np.random.normal(loc=76.723262462289600,scale=117015093654033) # 616
fault_2_UpperBearTemperature = round(fault_2_UpperBearTemperature,1)
fault_2_UpperBearBushTemperature = np.random.normal(loc=58.212149165003520,scale= 0.161119385140606) # 653
fault_2_UpperBearBushTemperature = round(fault_2_UpperBearBushTemperature,1)
fault_2_LowerThrustBearBushTemperature = np.random.normal(loc= 2.870466892744297e+03,scale=6.897553533926969) #605
fault_2_UpperBearBushTemperature = int(fault_2_UpperBearBushTemperature)
fault_2_UpperThrustBearBushTemperature = np.random.normal(loc=0.085368560549005,scale=0.006847207762448) # 606
fault_2_UpperThrustBearBushTemperature = round(fault_2_UpperThrustBearBushTemperature,2)
fault_2_UpMotorAirTemperature = np.random.normal(loc=0.265686045300202,scale=0.008014714235006 ) # 650
fault_2_UpMotorAirTemperature = round(fault_2_UpMotorAirTemperature,2)
fault_2_StatorTemperatureU = np.random.normal(loc= 101.631692920269420,scale=1.288557338566940) # 601
fault_2_StatorTemperatureU = round(fault_2_StatorTemperatureU,2)
fault_2_StatorTemperatureV = np.random.normal(loc= 101.333489195720790,scale=1.192110162287749) # 602
fault_2_StatorTemperatureV = round(fault_2_StatorTemperatureV,1)
fault_2_StatorTemperatureW = np.random.normal(loc= 36.438213099377520,scale=3.571389144186890) # 603
fault_2_StatorTemperatureW = round(fault_2_StatorTemperatureW,2)
fault_2_LowMotorAirTemperature = np.random.normal(loc= 35.145695883154200,scale=3.625238773721247) # 604
fault_2_LowMotorAirTemperature = round(fault_2_LowMotorAirTemperature,2)
fault_2_LowerOilTemperature = np.random.normal(loc= 58.837410330893010,scale=0.462179116181627) # 605
fault_2_LowerOilTemperature = round(fault_2_LowerOilTemperature,2)
fault_2_LowerBearTemperature = np.random.normal(loc= 58.600203238404580,scale= 0.094762753901546) # 606 MN
fault_2_LowerBearTemperature = round(fault_2_LowerBearTemperature,2)
fault_2_CoolerInletTemperature = np.random.normal(loc= 3.602426939503015e+02,scale=58.084551632246280) # 606 MD
fault_2_CoolerInletTemperature = int(fault_2_CoolerInletTemperature)
fault_2_CoolerOutletTemperature = np.random.normal(loc=62.525176791920660,scale= 0.181475527776540 ) # 651
fault_2_CoolerOutletTemperature = round(fault_2_CoolerOutletTemperature,1)
fault_2_InjectWaterTemperature = np.random.normal(loc=58.704229117734826,scale= 0.210833187318344) # 652
fault_2_InjectWaterTemperature = round(fault_2_InjectWaterTemperature,1)
fault_2_ControlLeakageTemperature = np.random.normal(loc= 32.803655050292893,scale= 0.243213558210030) # 654
fault_2_ControlLeakageTemperature = round(fault_2_ControlLeakageTemperature,2)
fault_2_ControlLeakageFlow = np.random.normal(loc=38.733275656530594,scale=0.252884487328883 )# 655
fault_2_ControlLeakageFlow = round(fault_2_ControlLeakageFlow ,2)
fault_2_LowPressureLeakageFlow = np.random.normal(loc=31.766224580733635,scale=25.766224580733635 ) # 131
fault_2_LowPressureLeakageFlow = round(fault_2_LowPressureLeakageFlow,2)
fault_2_InjectWaterFlow = np.random.normal(loc=52.468423282136555,scale= 0.187880844815710) # 111
fault_2_InjectWaterFlow = round(fault_2_InjectWaterFlow,2)
fault_2_CoolerSecFlow = np.random.normal(loc=29.201447552688137,scale=0.126570790404492 ) # 121
fault_2_CoolerSecFlow = round(fault_2_CoolerSecFlow ,2)
fault_2_UpperBearingOilLevel = np.random.normal(loc=75.049546880297870,scale= 0.220317656831326) # 631
fault_2_UpperBearingOilLevel = round(fault_2_UpperBearingOilLevel,1)
fault_2_LowerBearingOilLevel = np.random.normal(loc=75.887459635857600,scale= 0.200911191555422) # 632
fault_2_LowerBearingOilLevel = round(fault_2_LowerBearingOilLevel,1)
fault_2_SealPositionMonitor = np.random.normal(loc= 60.788997581059070,scale= 0.142936412649990) # 620
fault_2_SealPositionMonitor = round(fault_2_SealPositionMonitor ,2)
fault_2_FlywheelPositionMonitor = np.random.normal(loc=36.263797641233833,scale=0.213894582841562 ) # 622
fault_2_FlywheelPositionMonitor = round(fault_2_FlywheelPositionMonitor,2)

fault_2_Data = Data(VibrationX,fault_2_VibrationY,fault_2_MotorDisplacementX,fault_2_MotorDisplacementY,fault_2_PumpDisplacementX,
    fault_2_PumpDisplacementY,fault_2_MotorSpeed,fault_2_ZeroSpeed,fault_2_PumpOutletP1,fault_2_PumpOutletP2,fault_2_FilterPressure1,fault_2_FilterPressure2,
    fault_2_FirPreBeforeSeal,fault_2_SecPreBeforeSeal,fault_2_ThiPreBeforeSeal,fault_2_UpperBearTemperature,fault_2_UpperBearBushTemperature,
    fault_2_LowerThrustBearBushTemperature,fault_2_UpperThrustBearBushTemperature,fault_2_UpMotorAirTemperature,fault_2_StatorTemperatureU,
    fault_2_StatorTemperatureV,fault_2_StatorTemperatureW,fault_2_LowMotorAirTemperature,fault_2_LowerOilTemperature,fault_2_LowerBearTemperature,
    fault_2_CoolerInletTemperature,fault_2_CoolerOutletTemperature,fault_2_InjectWaterTemperature,fault_2_ControlLeakageTemperature,
    fault_2_ControlLeakageFlow,fault_2_LowPressureLeakageFlow,fault_2_InjectWaterFlow,fault_2_CoolerSecFlow,fault_2_UpperBearingOilLevel,
    fault_2_LowerBearingOilLevel,fault_2_SealPositionMonitor,fault_2_FlywheelPositionMonitor)
