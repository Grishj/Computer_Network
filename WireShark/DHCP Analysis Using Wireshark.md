# Using Wireshark to Demonstrate Different Packets Involved In Getting On IP Address From DHCP Server

## Filtering Packets
Filtering the DHCP packets on wireshark with ```dhcp``` flag , we can see 4 network packets i.e. ```Discover```, ```Offer```, ```Request``` and ```Acknowledge``` .

![inital](https://github.com/nilumahato/Computer-Network/assets/55197156/a49f2613-d265-44d6-ad9e-3f78a2016bbf)

## Analysing DHCP Discover Packet
Client is broadcasting discover packet for DHCP server with source IP ```0.0.0.0``` and destination IP ```255.255.255.255``` where the source IP address is 0.0.0.0, indicating that the client does not yet have an IP address and The destination IP address is 255.255.255.255, indicating that the message is a broadcast intended for all devices on the local network.

![Discover](https://github.com/nilumahato/Computer-Network/assets/55197156/48b1fe15-aef4-4af7-8f4d-55ed97179330)

Here, client is sending its mac address and host name by specifying the Parameter Request List. Along with that, its also setting ```Bootp flags``` as ```0``` meaning the response from DHCP server should be unicast with maximum response size ```576 bytes```.

## Analysing DHCP Offer Packet
As offer from DHCP server, DHCP server has sent its ip address including all requested parameters.  

![offer](https://github.com/nilumahato/Computer-Network/assets/55197156/fc495af4-1229-412b-89d6-26d8e9407cc6)

In above image we can see, DHCP server has offered ```192.168.1.79``` ip address with lease time 1 day. Additionally, we can see subnet mask, DNS server and other parameters that were in parameter request list.

## Analysing DHCP Request Packet
DHCP Request packet is sent by the client by including the IP address i.e ```192.168.1.79```. In this case its same IP that was offered by DHCP server. 
![Request](https://github.com/nilumahato/Computer-Network/assets/55197156/e69fa5de-de15-4971-a59d-75bb40f16596)

## Analysing DHCP Acknowledgement Packet
As acknowledgement of request, DHCP server has sent all the parameters that are being assigned to the client. It was last step of assignment of IP address by DHCP server to the client.
![Ack](https://github.com/nilumahato/Computer-Network/assets/55197156/22e100ff-c20e-432c-a4f4-48e426f086c3)

In this way, client is successfully assigned ```192.168.1.79``` as IP address ```192.168.1.254``` as dns server and ```255.255.255.0``` as subnet mask.