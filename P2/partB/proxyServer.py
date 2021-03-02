from socket import *
import sys
if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')

    sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)

#FIll in start.
# serHost = gethostname()
# print(serHost) 
serPort = int(sys.argv[1])
tcpSerSock.bind(('', serPort))
tcpSerSock.listen(5)
print("socket is listening")
#Fill in end.

while 1:
    # Start receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode() # Fill in 
    print("message:", message)
    # Extract the filename from the given message
    print("message split:", message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("filename:", filename)
    fileExist = "false"
    filetouse = "/" + filename
    print("file to use:", filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        for i in range(0, len(outputdata)):
            print("outputdata[i]:", outputdata[i])
            tcpCliSock.send(outputdata[i])
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            print("file not in cache")
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","", 1)
            print("hostn", hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start
                c.connect((hostn, 80))
                print("connected to", hostn)
                # Fill in end
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('r', 0)
                fileobj.write("GET "+"http://" + filename + "HTTP/1.0\n\n") 
                # Read the response into buffer
                # Fill in start
                buffer = fileobj.readlines()

                # Fill in end
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tmpFile = open("./" + filename, "wb")
                # Fill in start
                for i in range(0, len(buffer)):
                    print(buffer[i])
                    tcpCliSock.send(buffer[i])
                    tmpFile.write(buffer[i])
                # Fill in end
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start
            print("HTTP response message for file not found")
            # Fill in end
    # Close the cliend and the server sockets
    tcpCliSock.close()

# Fill in start
# tcpSerSock.close()
# Fill in end.
