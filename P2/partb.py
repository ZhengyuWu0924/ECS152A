# Import necessary packages
# All methods from the socket package have been imported as 
# an example
from socket import *
#refer to project2B_proxyServer.pdf
#refer to https://realpython.com/python-sockets/

# Optional: take ip address and port as command line arguments or 
# hardcode them in your program, you have various options: localhost,
# custom ip address or ip address of your machine, the latter lets you
# access your server from other devices in the same network

# harcode my own ipaddress and the port

ip_addr = "192.168.0.100" #my ip address
port = 65432

# Create a server socket, bind it to a port and start listening
# use AF_INET for address family and SOCK_STREAM for protocol
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((ip_addr, port))
# Optional but recommended: Print out statements at every significant 
# step of your program, for example: print out the ip address and port
# once you bind the socket
print("socket binded to {}:{}".format(ip_addr, port))

# put the socket into listening mode
tcpSerSock.listen(5)
print("socket is listening")

while True:
    print('Ready to serve...')
    # Establish connection with client
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    # Receive requests (HTTP GET) from the client
    print(message)

    # Extract the required information from the client request:
    # eg. webpage and file names
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)

    try:
        # Check whether the required files exist in the cache
        # if yes,load the file and send a response back to the client
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        for data in outputdata:
            tcpCliSock.send(data)
        print('Read file from cache')

    # Error handling for file not found in cache
    except IOError:
        # Since the required files were not found in cache,
        # create a socket on the proxy server to send the request
        # to the actual webserver
        if fileExist == "false": 
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1).split('/')[1]
            print("This is the host", hostn)    
        try:
            # Connect your client socket to the webserver at port 80
            hostIP = 80
            c.connect((hostn, hostIP))
            print("connected to", hostn, hostIP)

            try:
                # send request to the webserver
                c.send(message)
                # recieve response from the webserver
                cmessage = c.recv(1024)
                print("Received response from webserver")
                tcpCliSock.send(cmessage)
                # relay response back to the client
                print("relayed")
                # Create a new file in the cache for the requested file
                # and save the response for any future requests from the client
                fileobj = c.makefile('r', 0)               
                fileobj.write("GET   "+"http://"   +   filename   +   " HTTP/1.0\n\n")  
                tmpFile = open("./" + filename, "wb")
                for cdata in cmessage:
                    tmpFile.writelines(cdata)
                tmpFile.close()
            except:
                print("Request to the webserver failed")

            # Close the client socket
            tcpCliSock.close()
        except:
           # Unable to connect to the webserver
           print("Unable to connect to the webserver")
tcpSerSock.close()