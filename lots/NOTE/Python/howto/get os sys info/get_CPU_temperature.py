
r'''
https://stackoverflow.com/questions/3262603/accessing-cpu-temperature-in-python



########################### 1. wmi
Use the WMI module + Open Hardware Monitor + its WMI interface described here.

Sample code:

import wmi
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
        print(sensor.Name)
        print(sensor.Value)


########################### 2. dll only, not wmi
Download http://openhardwaremonitor.org/downloads/ and http://www.cputhermometer.com/ and extract OpenHardwareMonitorLib.dll and CPUThermometerLib.dll and place these in a directory.

You can then use the pythonnet module to address the .dlls and pull any stat that these programs offer. cputhermometer offers per-core CPU temps, openhardwaremonitor offers everything else. No need to use WMI which requires the program to be active in the background.

I have written a small script (python 3.6.5) to show every temperature sensor available on the system, you can of course easily modify this for other sensor types. You must run this as administrator:

import clr #package pythonnet, not clr


openhardwaremonitor_hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
cputhermometer_hwtypes = ['Mainboard','SuperIO','CPU','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
openhardwaremonitor_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']
cputhermometer_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level']


def initialize_openhardwaremonitor():
    file = 'OpenHardwareMonitorLib.dll'
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

def initialize_cputhermometer():
    file = 'CPUThermometerLib.dll'
    clr.AddReference(file)

    from CPUThermometer import Hardware
    handle = Hardware.Computer()
    handle.CPUEnabled = True
    handle.Open()
    return handle

def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)
        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)


def parse_sensor(sensor):
        if sensor.Value is not None:
            if type(sensor).__module__ == 'CPUThermometer.Hardware':
                sensortypes = cputhermometer_sensortypes
                hardwaretypes = cputhermometer_hwtypes
            elif type(sensor).__module__ == 'OpenHardwareMonitor.Hardware':
                sensortypes = openhardwaremonitor_sensortypes
                hardwaretypes = openhardwaremonitor_hwtypes
            else:
                return

            if sensor.SensorType == sensortypes.index('Temperature'):
                print(u"%s %s Temperature Sensor #%i %s - %s\u00B0C" % (hardwaretypes[sensor.Hardware.HardwareType], sensor.Hardware.Name, sensor.Index, sensor.Name, sensor.Value))

if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    fetch_stats(HardwareHandle)
    print("\nCPUMonitor:")
    CPUHandle = initialize_cputhermometer()
    fetch_stats(CPUHandle)

Here is the output on my system:

OpenHardwareMonitor:
SuperIO Nuvoton NCT6791D Temperature Sensor #0 CPU Core - 42.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #1 Temperature #1 - 35.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #2 Temperature #2 - 34.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #3 Temperature #3 - 25.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #4 Temperature #4 - 101.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #5 Temperature #5 - 16.0°C
SuperIO Nuvoton NCT6791D Temperature Sensor #6 Temperature #6 - 14.0°C
GpuNvidia NVIDIA GeForce GTX 1070 Temperature Sensor #0 GPU Core - 60.0°C
HDD ST31000528AS Temperature Sensor #0 Temperature - 37.0°C
HDD WDC WD20EARX-00PASB0 Temperature Sensor #0 Temperature - 36.0°C
HDD WDC WDS100T2B0B-00YS70 Temperature Sensor #0 Temperature - 40.0°C
HDD WDC WD80EFZX-68UW8N0 Temperature Sensor #0 Temperature - 31.0°C
HDD WDC WD30EFRX-68EUZN0 Temperature Sensor #0 Temperature - 30.0°C
HDD WDC WD80EFZX-68UW8N0 Temperature Sensor #0 Temperature - 33.0°C
HDD Crucial_CT256MX100SSD1 Temperature Sensor #0 Temperature - 40.0°C

CPUMonitor:
CPU Intel Core i7-8700K Temperature Sensor #0 CPU Core #1 - 39.0°C
CPU Intel Core i7-8700K Temperature Sensor #1 CPU Core #2 - 38.0°C
CPU Intel Core i7-8700K Temperature Sensor #2 CPU Core #3 - 37.0°C
CPU Intel Core i7-8700K Temperature Sensor #3 CPU Core #4 - 41.0°C
CPU Intel Core i7-8700K Temperature Sensor #4 CPU Core #5 - 36.0°C
CPU Intel Core i7-8700K Temperature Sensor #5 CPU Core #6 - 47.0°C

For further documentation (however you should be able to infer everything you need from the above code), refer to the https://github.com/openhardwaremonitor/openhardwaremonitor/ (or cputhermometer, on the website) source code, the functions and methods are identical when you use these with python.

I haven't tested this on any other computers, so different processor architectures may not function identically.

Ensure you run Hardware[x].Update() between taking measurements (and SubHardware[x].Update() if needed).

'''

print('run OpenHardwareMonitor.exe in background')

import wmi
def show_temperature():
    w = wmi.WMI(namespace=r"root\OpenHardwareMonitor")
    #w = wmi.WMI(namespace=r"root\cimv2\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    for sensor in temperature_infos:
        if sensor.SensorType==u'Temperature':
            print(sensor.Name)
            print(sensor.Value)

#failure
#show_temperature()



########################################################
import clr #package pythonnet, not clr


openhardwaremonitor_hwtypes = ['Mainboard','SuperIO','CPU','RAM','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
cputhermometer_hwtypes = ['Mainboard','SuperIO','CPU','GpuNvidia','GpuAti','TBalancer','Heatmaster','HDD']
openhardwaremonitor_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']
cputhermometer_sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level']


class Global:
    path_OpenHardwareMonitor = r'D:\software\drives\OpenHardwareMonitor\OpenHardwareMonitor\OpenHardwareMonitorLib.dll'
def initialize_openhardwaremonitor():
    file = Global.path_OpenHardwareMonitor
    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True
    handle.Open()
    return handle

def initialize_cputhermometer():
    file = 'CPUThermometerLib.dll'
    clr.AddReference(file)

    from CPUThermometer import Hardware
    handle = Hardware.Computer()
    handle.CPUEnabled = True
    handle.Open()
    return handle

def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)
        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)


def parse_sensor(sensor):
        if sensor.Value is not None:
            if type(sensor).__module__ == 'CPUThermometer.Hardware':
                sensortypes = cputhermometer_sensortypes
                hardwaretypes = cputhermometer_hwtypes
            elif type(sensor).__module__ == 'OpenHardwareMonitor.Hardware':
                sensortypes = openhardwaremonitor_sensortypes
                hardwaretypes = openhardwaremonitor_hwtypes
            else:
                return

            if sensor.SensorType == sensortypes.index('Temperature'):
                print(u"%s %s Temperature Sensor #%i %s - %s\u00B0C" % (hardwaretypes[sensor.Hardware.HardwareType], sensor.Hardware.Name, sensor.Index, sensor.Name, sensor.Value))

if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    fetch_stats(HardwareHandle)
    print("\nCPUMonitor:")
    CPUHandle = initialize_cputhermometer()
    fetch_stats(CPUHandle)



