The program accepts two command line arguments
X: Number of hosts per switch
Y: Number of switches

- Each switch is connected to its next switch
- Odd numbered hosts are added to subnet 10.0.1.x/24
- Odd numbered hosts are added to subnet 10.0.2.x/24
- Bandwidth of odd numbered hosts is 1 Mb
- Bandwidth of odd numbered hosts is 2 Mb
- Subnet Mask is 24 bits

Example:
	s1 --> s2 --> s3 --> s4

So, lets try one Example

	1) Lets create a network with x = 2, y = 4; 
		i.e 2 hosts are connected to each switch

	2) Hence hosts: 1, 3, 5, 7 will be connected to subnet 10.0.1.x/24
		with Bandwidth of 1 Mb

	3) Hence hosts: 2, 4, 6, 8 will be connected to subnet 10.0.2.x/24
		with Bandwidth of 2 Mb

	4) Lets have a look at details of network
