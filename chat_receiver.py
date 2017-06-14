import socket
import argparse
import time
import sys


def receiverSetup(args):
  receiverPort = args.receiverPort
  serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
  serverSocket.bind(('', receiverPort))
  currentTime = time.strftime("%H:%M:%S", time.localtime())

  print "The server is ready to receive on port " + str(receiverPort) + "."

  while True:
    data, addr = serverSocket.recvfrom(1024) # buffer size is 1024 bytes
    print addr[0] + ' (' + currentTime + '): ', data
    if(data == "y"):
      sys.exit()

  serverSocket.close()

def main():
    #initiate parser object to parse command-line arguments
    parser = argparse.ArgumentParser() 
    #grab port number from command line, set as destinatination port number, default as 8080 if not specified
    #help flag will show brief description of argument when using argument --help
    parser.add_argument('--port=####', dest= 'receiverPort', default = 8080, type = int, action='store', help='Accepts port number')
    args = parser.parse_args()

    #if serverPort is used, add the serverPort argument
    if args.receiverPort:
        receiverSetup(args)

if __name__ == "__main__":
    main()  