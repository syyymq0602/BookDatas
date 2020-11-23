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
fault_1_VibrationY = np.random.normal(loc=6.275189801042958e+02,scale=2.745910268115703) # 001
fault_1_VibrationY = round(fault_1_VibrationY,1)
fault_1_MotorDisplacementX = np.random.normal(loc=1.066723880510640,scale=0.0349) # 106
fault_1_MotorDisplacementX = round(fault_1_MotorDisplacementX ,3)
fault_1_MotorDisplacementY = np.random.normal(loc=1.097424671010749,scale=0.081219378558145) # 107
fault_1_MotorDisplacementY = round(fault_1_MotorDisplacementY,3)
fault_1_PumpDisplacementX = np.random.normal(loc=62.409067024682706,scale=1.041220776194501) # 152
fault_1_PumpDisplacementX = round(fault_1_PumpDisplacementX ,1)
fault_1_PumpDisplacementY = np.random.normal(loc=60.565427483470806,scale=0.971338199888906) # 153
fault_1_PumpDisplacementY = round(fault_1_PumpDisplacementY,1)
fault_1_MotorSpeed = np.random.normal(loc=1.205426742746030e+02,scale=13.516308550230391) # 150
fault_1_MotorSpeed = round(fault_1_MotorSpeed,1)
fault_1_ZeroSpeed = np.random.normal(loc=1.315861853450753e+02,scale=12.089381173673026) # 151
fault_1_ZeroSpeed = round(fault_1_ZeroSpeed,1)
fault_1_PumpOutletP1 = np.random.normal(loc=80.498099559042190,scale=0.109909892997096 ) # 611
fault_1_PumpOutletP1 = round(fault_1_PumpOutletP1,1)
fault_1_PumpOutletP2 = np.random.normal(loc=75.634724135106380,scale=0.138274780519703 ) # 612
fault_1_PumpOutletP2 = round(fault_1_PumpOutletP2,1)
fault_1_FilterPressure1 = np.random.normal(loc=68.298817143320010,scale= 0.145158721879140) # 644
fault_1_FilterPressure1 = round(fault_1_FilterPressure1,1)
fault_1_FilterPressure2 = np.random.normal(loc=69.295116954664400,scale=0.140748242011379 ) # 645
fault_1_FilterPressure2 = round(fault_1_FilterPressure2,1)
fault_1_FirPreBeforeSeal = np.random.normal(loc= 69.862097660868930,scale=0.134016367675141 ) #613
fault_1_FirPreBeforeSeal = round(fault_1_FirPreBeforeSeal,1)
fault_1_SecPreBeforeSeal = np.random.normal(loc=69.520238191693420,scale=0.133912435891065 ) # 643
fault_1_SecPreBeforeSeal = round(fault_1_SecPreBeforeSeal,1)
fault_1_ThiPreBeforeSeal = np.random.normal(loc=70.488981609023100,scale=0.140163202319602 ) # 615
fault_1_ThiPreBeforeSeal = round(fault_1_ThiPreBeforeSeal,1)
fault_1_UpperBearTemperature = np.random.normal(loc=73.723262462289600,scale=117015093654033) # 616
fault_1_UpperBearTemperature = round(fault_1_UpperBearTemperature,1)
fault_1_UpperBearBushTemperature = np.random.normal(loc=55.212149165003520,scale= 0.161119385140606) # 653
fault_1_UpperBearBushTemperature = round(fault_1_UpperBearBushTemperature,1)
fault_1_LowerThrustBearBushTemperature = np.random.normal(loc= 2.770466892744297e+03,scale=6.897553533926969) #605
fault_1_UpperBearBushTemperature = int(fault_1_UpperBearBushTemperature)
fault_1_UpperThrustBearBushTemperature = np.random.normal(loc=0.080368560549005,scale=0.006847207762448) # 606
fault_1_UpperThrustBearBushTemperature = round(fault_1_UpperThrustBearBushTemperature,2)
fault_1_UpMotorAirTemperature = np.random.normal(loc=0.235686045300202,scale=0.008014714235006 ) # 650
fault_1_UpMotorAirTemperature = round(fault_1_UpMotorAirTemperature,2)
fault_1_StatorTemperatureU = np.random.normal(loc= 97.631692920269420,scale=1.288557338566940) # 601
fault_1_StatorTemperatureU = round(fault_1_StatorTemperatureU,2)
fault_1_StatorTemperatureV = np.random.normal(loc= 97.333489195720790,scale=1.192110162287749) # 602
fault_1_StatorTemperatureV = round(fault_1_StatorTemperatureV,1)
fault_1_StatorTemperatureW = np.random.normal(loc= 32.438213099377520,scale=3.571389144186890) # 603
fault_1_StatorTemperatureW = round(fault_1_StatorTemperatureW,2)
fault_1_LowMotorAirTemperature = np.random.normal(loc= 32.145695883154200,scale=3.625238773721247) # 604
fault_1_LowMotorAirTemperature = round(fault_1_LowMotorAirTemperature,2)
fault_1_LowerOilTemperature = np.random.normal(loc= 55.837410330893010,scale=0.462179116181627) # 605
fault_1_LowerOilTemperature = round(fault_1_LowerOilTemperature,2)
fault_1_LowerBearTemperature = np.random.normal(loc= 55.600203238404580,scale= 0.094762753901546) # 606 MN
fault_1_LowerBearTemperature = round(fault_1_LowerBearTemperature,2)
fault_1_CoolerInletTemperature = np.random.normal(loc= 3.502426939503015e+02,scale=58.084551632246280) # 606 MD
fault_1_CoolerInletTemperature = int(fault_1_CoolerInletTemperature)
fault_1_CoolerOutletTemperature = np.random.normal(loc=59.525176791920660,scale= 0.181475527776540 ) # 651
fault_1_CoolerOutletTemperature = round(fault_1_CoolerOutletTemperature,1)
fault_1_InjectWaterTemperature = np.random.normal(loc=53.704229117734826,scale= 0.210833187318344) # 652
fault_1_InjectWaterTemperature = round(fault_1_InjectWaterTemperature,1)
fault_1_ControlLeakageTemperature = np.random.normal(loc= 29.803655050292893,scale= 0.243213558210030) # 654
fault_1_ControlLeakageTemperature = round(fault_1_ControlLeakageTemperature,2)
fault_1_ControlLeakageFlow = np.random.normal(loc=35.733275656530594,scale=0.252884487328883 )# 655
fault_1_ControlLeakageFlow = round(fault_1_ControlLeakageFlow ,2)
fault_1_LowPressureLeakageFlow = np.random.normal(loc=27.766224580733635,scale=25.766224580733635 ) # 131
fault_1_LowPressureLeakageFlow = round(fault_1_LowPressureLeakageFlow,2)
fault_1_InjectWaterFlow = np.random.normal(loc=48.468423282136555,scale= 0.187880844815710) # 111
fault_1_InjectWaterFlow = round(fault_1_InjectWaterFlow,2)
fault_1_CoolerSecFlow = np.random.normal(loc=27.201447552688137,scale=0.126570790404492 ) # 121
fault_1_CoolerSecFlow = round(fault_1_CoolerSecFlow ,2)
fault_1_UpperBearingOilLevel = np.random.normal(loc=73.049546880297870,scale= 0.220317656831326) # 631
fault_1_UpperBearingOilLevel = round(fault_1_UpperBearingOilLevel,1)
fault_1_LowerBearingOilLevel = np.random.normal(loc=72.887459635857600,scale= 0.200911191555422) # 632
fault_1_LowerBearingOilLevel = round(fault_1_LowerBearingOilLevel,1)
fault_1_SealPositionMonitor = np.random.normal(loc= 57.788997581059070,scale= 0.142936412649990) # 620
fault_1_SealPositionMonitor = round(fault_1_SealPositionMonitor ,2)
fault_1_FlywheelPositionMonitor = np.random.normal(loc=33.263797641233833,scale=0.213894582841562 ) # 622
fault_1_FlywheelPositionMonitor = round(fault_1_FlywheelPositionMonitor,2)

fault_1_Data = Data(VibrationX,fault_1_VibrationY,fault_1_MotorDisplacementX,fault_1_MotorDisplacementY,fault_1_PumpDisplacementX,
    fault_1_PumpDisplacementY,fault_1_MotorSpeed,fault_1_ZeroSpeed,fault_1_PumpOutletP1,fault_1_PumpOutletP2,fault_1_FilterPressure1,fault_1_FilterPressure2,
    fault_1_FirPreBeforeSeal,fault_1_SecPreBeforeSeal,fault_1_ThiPreBeforeSeal,fault_1_UpperBearTemperature,fault_1_UpperBearBushTemperature,
    fault_1_LowerThrustBearBushTemperature,fault_1_UpperThrustBearBushTemperature,fault_1_UpMotorAirTemperature,fault_1_StatorTemperatureU,
    fault_1_StatorTemperatureV,fault_1_StatorTemperatureW,fault_1_LowMotorAirTemperature,fault_1_LowerOilTemperature,fault_1_LowerBearTemperature,
    fault_1_CoolerInletTemperature,fault_1_CoolerOutletTemperature,fault_1_InjectWaterTemperature,fault_1_ControlLeakageTemperature,
    fault_1_ControlLeakageFlow,fault_1_LowPressureLeakageFlow,fault_1_InjectWaterFlow,fault_1_CoolerSecFlow,fault_1_UpperBearingOilLevel,
    fault_1_LowerBearingOilLevel,fault_1_SealPositionMonitor,fault_1_FlywheelPositionMonitor)
