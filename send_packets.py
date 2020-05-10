from configparser import ConfigParser
from ast import literal_eval
import csv
import datetime

#get input packet from interface1
parser1 = ConfigParser()
parser1.read('inputs_interface1.ini')

#get input packet from interface2
parser2= ConfigParser()
parser2.read('inputs_interface2.ini')
file1 = open("output.txt","w+") 


#Check for each packet if they have access or not through the firewall from interface 1
for packetname in parser1.sections():
    protocol=parser1.get(packetname,'protocol')
    if (protocol!='ip'):
        destport=parser1.get(packetname,'destination_port')
    destaddress=parser1.get(packetname,'destination_address')
    srcaddress=parser1.get(packetname,'source_address')
    actionlist=[]


    #read the rules of the firewall to filter the inputs
    with open('firewall_rules.txt', mode='r') as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            
            if(protocol!='ip'):
                if line_count == 0:
                    line_count += 1

                if (row['protocol']==protocol and row["sourceIP"]=='any' and row["destinationIP"]==destaddress and row['destinationPort']==destport):
                    actionlist.append(row['Action'])
                
                
                if (row['protocol']==protocol and row["sourceIP"]==srcaddress and row["destinationIP"]==destaddress and row['destinationPort']==destport):
                    actionlist.append(row['Action'])
            
                
                if (line_count>0):
                    line_count += 1

            if(protocol=='ip'):
                if (row['protocol']==protocol and row["sourceIP"]=='any' and row["destinationIP"]==destaddress):
                    actionlist.append(row['Action'])
                
                
                if (row['protocol']==protocol and row["sourceIP"]==srcaddress and row["destinationIP"]==destaddress):
                    actionlist.append(row['Action'])
            
                
                if (line_count>0):
                    line_count += 1

        #print and write the output results for each packets
        if 'accept' in  actionlist:
            
            file1.write(protocol+' packet('+packetname+') has accepted by network interface-2 of the firewall at '+str(datetime.datetime.now())+'\n')
            print(protocol+' packet('+packetname+') has accepted by network interface-1 of the firewall at '+str(datetime.datetime.now()))
        else:
            
            file1.write(protocol+' packet('+packetname+') has denied by network interface-2 of the  firewall at '+str(datetime.datetime.now())+'\n')
            print(protocol+' packet('+packetname+') has denied by network interface-1 of the  firewall at '+str(datetime.datetime.now()))


#Check for each packet if they have access or not through the firewall from interface 1           
for packetname in parser2.sections():
    protocol=parser2.get(packetname,'protocol')
    if (protocol!='ip'):
        destport=parser2.get(packetname,'destination_port')
        destaddress=parser2.get(packetname,'destination_address')
    srcaddress=parser2.get(packetname,'source_address')
    actionlist=[]


    #read the rules of the firewall to filter the inputs
    with open('firewall_rules.txt', mode='r') as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:

            if(protocol!='ip'):
                if line_count == 0:
                    line_count += 1

                if (row['protocol']==protocol and row["sourceIP"]=='any' and row["destinationIP"]==destaddress and row['destinationPort']==destport):
                    actionlist.append(row['Action'])
                
                
                if (row['protocol']==protocol and row["sourceIP"]==srcaddress and row["destinationIP"]==destaddress and row['destinationPort']==destport):
                    actionlist.append(row['Action'])
            
                
                if (line_count>0):
                    line_count += 1

            if(protocol=='ip'):
                if (row['protocol']==protocol and row["sourceIP"]=='any' and row["destinationIP"]==destaddress):
                    actionlist.append(row['Action'])
                
                
                if (row['protocol']==protocol and row["sourceIP"]==srcaddress and row["destinationIP"]==destaddress):
                    actionlist.append(row['Action'])
            
                
                if (line_count>0):
                    line_count += 1

            
            
        #print and write the output results for each packets
        if 'accept' in  actionlist:
             
            file1.write(protocol+' packet('+packetname+') has accepted by network interface-2 of the firewall at '+str(datetime.datetime.now())+'\n')
            print(protocol+' packet('+packetname+') has accepted by network interface-2 of the firewall at '+str(datetime.datetime.now()))
        else:
            
            file1.write(protocol+' packet('+packetname+') has denied by network interface-2 of the  firewall at '+str(datetime.datetime.now())+'\n')
            print(protocol+' packet('+packetname+') has denied by network interface-2 of the  firewall at '+str(datetime.datetime.now()))
                    


file1.close() 