ECS152A-Programming_Assignment#1

Part1: Wireshark - IP

Answers:

1. ![image-20210124171856607](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124171856607.png)

   The IP address of my computer is 192.168.1.3.

![image-20210124172204357](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124172204357.png)

​		Within the IP packet header, the value in the upper layer protocol field is **ICMP(1)**

 3. ![image-20210124172500722](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124172500722.png)

    There are **20 bytes** in the IP header, and the total length of the datagram is **56 bytes**, thus, as the total length is 56 bytes and the header is 20 bytes, the number of payload bytes is calculated by 56 - 20 = 36 bytes, so the number of payload bytes is **36 bytes**.

	4.  

    ![image-20210124174050942](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174050942.png)

    As the Wireshark shows the fragment offset is 0, and also there is not set for more fragments, so this IP datagram has not been fragmented.

	5.  

    ![image-20210124174532204](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174532204.png)

    ![image-20210124174546019](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174546019.png)

    ![image-20210124174607082](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174607082.png)

    ![image-20210124174707375](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174707375.png)

![image-20210124174718530](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124174718530.png)

​	By comparing different records, the fields that always change are: **Identification**, **Time to Live**, and **Header Checksum**.

​	6. 

​	The Version, header length, source IP, destination IP, differentiated services, upper layer protocol stay constant.

​	The version, header length, source IP, destination IP, and differentiated services must stay constant.

​	The identification, time to live, and header checksum must changed.

​	Reason:

	- Version: as the computer is using IPv4 for all packets, the version should always stay constant, and it must stay constant or it might cause error on transiting packets.
	- Header length: as all the packets are ICMP packets, they are following the same formatting rule, thus there should share the same header length as the ICMP request. Thus the header length field must stay constant.
	- Source IP: since all the packets were sent from my computer, the Source IP field should always stay constant.
	- Destination IP: since all the packets were send to the gaia.cs.umass.edu, the destination IP should always stay constant.
	- Differentiated services: as all the packets are ICMP packets, they share the same services, so this field should stay constant.
	- Upper layer protocol: as all the packets are ICMP format, they share the same format, so the upper layer protocol field should stay constant.
	- Identification: since each packets are different, and they should have something to identify they are different, they should have different ID, so the identification field should be different.
	- Time to live: each packets may live different time in the traceroute, so this field should be different
	- Header checksum: since the header in each packets may be different, so the header checksum should also be different for each packets.

7.  

   ![image-20210124180052393](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124180052393.png)

   The pattern of the identification field shows the specific id number for a packet

8.  

   ![image-20210124180910089](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124180910089.png)

   Value in Identification field: 0x0210(528)

   Value in time to live field: 63

9.  

   ![image-20210124181036959](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124181036959.png)

![image-20210124181050056](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124181050056.png)

​	For the identification field, the value always changes to identify different packets. 

​	For the time to live field, since the TTL for the first hop router keep does not change, so the value in this field keep the same and will not change.



​	10. 

​	![image-20210124182314437](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124182314437.png)

​	Yes, this packet has been fragmented to more than 1 datagram.

11.  

    ![image-20210124183033254](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124183033254.png)

    The Flags fields shows the packet has been fragmented to more datagrams as there is a 1 in the ‘More fragments’ field. Since the fragment offset is 0, it indicates that the current datagram is the first fragment, with the length of 1500 bytes.

12. ![image-20210124183050201](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124183050201.png)

    In the above graph, as we can find the Fragment offset is 1480, we can tell that this datagram is not the first fragment. Since the ‘More fragment’ field under the Flags is 0, there is no more fragments.

13.  By comparing the above two graves in 11&12, the fields changed between the first and second fragment are: Flags, Fragment offset, header checksum, and total length.

14.  

    ![image-20210124183802240](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124183802240.png)

    ![image-20210124183847040](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124183847040.png)

    There are 3 fragments were created from the original datagram after set the packet size in *pingplotter* to be 3500.

15.  

    First Fragment:

    ![image-20210124183802240](file://C:/Users/wzy19/AppData/Roaming/Typora/typora-user-images/image-20210124183802240.png?lastModify=1611542359)

    Second Fragment:

    ![image-20210124183959695](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124183959695.png)

    Third Fragment:

    ![image-20210124184016992](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210124184016992.png)

    By comparing the above three graphs, fields changed among the fragments are: Flags, Header checksum, total length. and fragment offset.