from configparser import ConfigParser
from ast import literal_eval


#function for create a packet structures in input files
def createpacket(ID,filename):
    config=ConfigParser()
    config[ID]={}
    with open(filename,'a') as configfile:
        config.write(configfile)


#function to add fields to the packets
def addfields(ID,filename,field,value):
    config=ConfigParser()
    config.read(filename)
    confile=open(filename,"w")
    config.set(ID,field,value)
    config.write(confile)
    confile.close()


#main function for get inputs to store in input files
def main():
    filename=''
    print('Select the Interface: ')
    print('1 - for Interface_1')
    print('2 - fro Interface_2')
    interface=int(input('Enter your option: ').strip(' '))
    if interface==1:
        filename='inputs_interface1.ini'
        parser = ConfigParser()
        parser.read(filename)
      

    if interface==2:
        filename='inputs_interface2.ini'
        parser = ConfigParser()
        parser.read(filename)
            

    if (interface!=1 and interface!=2):
        print('Inavlid Interface')
        arg = int(input('press 1 for re-enter data:\n 2 for abort:  '))
        if arg==1:
            main()
        else:
            print('packets are succesfully added')

    packetname=input('Packet name: ').strip(' ')
    createpacket(packetname,filename)

    protocol=input('protocol(ip/tcp/udp): ').strip(' ').lower()
    addfields(packetname,filename,'protocol',protocol)

    if (protocol!='ip'):
        destport=input('Destination Port: ').strip(" ")
        addfields(packetname,filename,'destination_port',destport)
        srcport=input('Source Port: ').strip(" ")
        addfields(packetname,filename,'source_port',srcport)

    srcaddress=input('Source Address: ').strip(" ")
    addfields(packetname,filename,'source_address',srcaddress)
    destaddress=input('Destination Address: ').strip(" ")
    addfields(packetname,filename,'destination_address',destaddress)

    arg = int(input('press 1 for re-enter data:\n 2 for abort:  '))
    if arg==1:
        main()
    else:
        print('packets are succesfully added')
	
main()