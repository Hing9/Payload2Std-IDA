from __future__ import print_function
import sys
import os
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-p", "--idaport", type=str, help="port that ida debugger binary use")
    parser.add_argument("-sp", "--pluginport", type=str, help="port that payload2std plugin use")
    #parser.add_argument("-m32", action="store_true", help="use 32bit debugger")
    parser.add_argument("-b", "--binary", type=str, help="which binary to use")

    args = parser.parse_args()

    binaryName = args.binary
    if binaryName == None:
        binaryName = "linux_server64"
    

    if not os.path.isfile(binaryName):
        print('Error: "{}" binary not found.'.format(binaryName))
        print("You should copy one from IDA installation directory.")
        exit(-1)

    
    idaport = args.idaport
    if idaport == None:
        idaport = 23946
    
    pluginport = args.pluginport
    if pluginport == None:
        pluginport = idaport + 1