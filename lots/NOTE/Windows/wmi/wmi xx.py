
'''
...> wmic NICConfig
...> powershell
PS ...> gwmi -Namespace root\wmi -List
    ...
    MSiSCSI_NICConfig ...
    ...


t = wmi.WMI(moniker = "//./root/wmi")
t.ExecQuery('Select * from BatteryFullChargedCapacity')
classes = sorted(t.classes)
'''

if False:
    import wmi
    t = wmi.WMI(moniker = "//./root/wmi")
    classes = sorted(t.classes)
    assert 'MSiSCSI_NICConfig' in classes
    # fail: r = t.ExecQuery('Select * from MSiSCSI_NICConfig')

# http://timgolden.me.uk/python/wmi/cookbook.html
import wmi
c = wmi.WMI ()

for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    print(interface.Description, interface.MACAddress)
    for ip_address in interface.IPAddress: print(ip_address)
    print()





