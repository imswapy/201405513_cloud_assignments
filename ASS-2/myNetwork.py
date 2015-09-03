#!/usr/bin/python
import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink

class SingleSwitchTopo(Topo):
    # x: Number of hosts per switch
    # y: Number of switches
    def build(self, x=2, y=4):
        cnt = 1
        switchList= []
        for s in range(y):
            switch = self.addSwitch('s%s' % (s+1))
            switchList.append(switch)
            for h in range(x):
                if ((cnt%2)==1):
                    #Add odd numbered hosts to subnet 10.0.1.x
                    host = self.addHost('h'+str(cnt), ip="10.0.1.%s/24"%cnt)
                    self.addLink(host, switch, bw=1)
                else:
                    #Add even numbered hosts to subnet 10.0.2.x
                    host = self.addHost('h'+str(cnt), ip="10.0.2.%s/24"%cnt)
                    self.addLink(host, switch, bw=2)
                cnt = cnt+1
            if s > 0:
                self.addLink(switchList[s-1], switchList[s])

def simpleTest(x, y):
    "Create and test a simple network"
    topo = SingleSwitchTopo(x=x, y=y)
    net = Mininet(topo, host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            raise IndexError
        x=int(sys.argv[1])
        y=int(sys.argv[2])
        # Tell mininet to print useful information
        setLogLevel('info')
        simpleTest(x, y)
    except IndexError:
        print "Invalid No of Arguments"
