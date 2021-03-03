ECS 152A Programing 2

Part A

Q1:



![image-20210302232643098](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302232643098.png)

![image-20210302232651154](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302232651154.png)

Questions: 

1. Is your browser running HTTP version 1.0 or 1.1? What version of HTTP is the server running?
2. What languages (if any) does your browser indicate that it can accept to the server?
3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?
4. What is the status code returned from the server to your browser?
5. When was the HTML file that you are retrieving last modified at the server?
6. How many bytes of content are being returned to your browser?
7. By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window? If so, name one.

Answers:

	1. My browser is running **HTTP version 1.1**; the server also running **HTTP version 1.1**.
 	2. My browser accept **zh-CN**.
 	3. The IP address of my computer is **192.168.1.5**; the IP address of gaia.cs.umass.edu server is **128.119.245.12**.
 	4. The status code returned from the server to my browser is **200**.
 	5. The last modified time is **Wed, 03 Mar 2021 07:25:10 GMT**.
 	6. There are **128 bytes** being returned to my browser.
 	7. I did not see any headers within the data thar are not displayed in the packet-listing window.

Q2:

First Time:

![](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302225226473.png)

![image-20210302225152123](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302225152123.png)

Second Time:

![image-20210302225227522](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302225227522.png)



Questions:

8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?
10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET? If so, what information follows the “IF-MODIFIED-SINCE:” header?
11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.

Answers:

8. There is **No** “IF-MODIFIED-SINCE” line in the first HTTP GET.
9. **Yes, the server explicity return the contesnts fo the file.** Since we can see the full test of the file in the first response.
10. **Yes**, there is an “IF-MODIFIED-SINCE” line in the second HTTP GET. The information follows the “IF-MODIFIED-SINCE” header is a record of the time, which is **Tue, 02 Mar 2021 06:59:01 GMT**.
11. The status code returned from the server in response to the second HTTP GET is code **304**, which represents “not modified”. The server does **NOT** explicity return the contents of the file.

Q3:

![image-20210302231616161](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231616161.png)

Questions:

12. How many HTTP GET request messages did your browser send? Which packet number in the trace contains the GET message for the Bill or Rights?
13. Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?
14. What is the status code and phrase in the response?
15. How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?

Answers:

12. My browser only send **1** HTTP GET request message. The packet contains the GET message for the Bill or Rights is the packet with number **64**.
13. The packet that contians the status code and phrase associated with the response to the HTTP GET request is the packet number **68**.
14. The status code and phrase in the response is **200 OK**.
15. **3 packets** are needed to carry the single HTTp response and the text of the Bill of Rights. They are packet **68, 69, 70**.

Q4:

![image-20210302231709897](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231709897.png)

Questions:

16. How many HTTP GET request messages did your browser send? To which Internet addresses were these GET requests sent?
17. Can you tell whether your browser downloaded the two images serially, or whether they were downloaded from the two web sites in parallel? Explain.

Answers:

16. My browser send **3** HTTP Get request messages. The packet **80** sent to **128.119.245.12**; the packet **104** sent to **128.119.245.12**; the packet **127** sent to **178.79.137.164**.
17. My browser downloaded the two images **serially** since the GET requests were sent in packet NO.104 and NO.127, but the first respose was returned in packet NO.113 from the server. Thus, my browser downloaded the two images serially but not parallel.

Q5:

First Request

![image-20210302231730152](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231730152.png)

First Response

![image-20210302231742634](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231742634.png)

Second Request

![image-20210302231754353](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231754353.png)

Second Response

![image-20210302231841549](C:\Users\wzy19\AppData\Roaming\Typora\typora-user-images\image-20210302231841549.png)

Questions:

18. What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?
19. When your browser’s sends the HTTP GET message for the second time, what new field is included in the HTTP GET message?

Answers:

18. Packet NO.946 is the initial server’s response to the initial HTTP GET message from my browser. The status code and phrase is **401 Unauthorized**.
19. The new field included in the second HTTP GET message is **Authorization: Basic  d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=** , which is the password of the website.