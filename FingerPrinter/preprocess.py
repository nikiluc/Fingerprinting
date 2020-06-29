import dpkt
import pandas as pd
import os
from statistics import mean
import socket

#Source 1: https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/
#Source 2: https://dpkt.readthedocs.io/en/latest/print_packets.html

#loads data from pcap files into a dataframe
def load_data():

    #hold each row of the dataframe
    rows = []

    #for each pcap file in the directory
    for filename in os.listdir(os.getcwd()):

        if filename.endswith(".pcap"):

            f = open(filename , 'rb')

            #opens the pcap file
            pcap = dpkt.pcap.Reader(f)

            #All of the information we're trying to capture
            total_size = 0
            total_packets = 0
            outgoing_packets = 0
            incoming_packets = 0
            timestamps = []

            #for timestamp and buffer in pcap
            for (ts, buf) in pcap:

                #add the size of the buff
                total_size += len(buf)

                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data

                #get source ip addresses
                src = socket.inet_ntoa(ip.src)

                #first packet, therefore we can say that this IP address is outgoing
                if total_packets == 0:

                    outgoing = src
                    outgoing_packets += 1


                elif src == outgoing:

                    outgoing_packets += 1

                #if not outgoing then it is incoming
                else:

                    incoming_packets += 1

                #add timestamp to list
                timestamps.append(float(ts))

                total_packets += 1

            #ratio of packets
            rop = float(incoming_packets / outgoing_packets)

            #time in between packets
            intervals = []

            #gathering time between packets by subtracting time stamps
            for i in range(1, len(timestamps)):
                intervals.append(timestamps[i] - timestamps[i-1])

            #calc the average interval time
            avg_interval = mean(intervals)


            #label this row with a website name based on the filename
            category = ""

            if "auto" in filename:
                category = "autolab"
            elif "b" in filename:
                category = "bing"
            elif "canvas" in filename:
                category = "canvas"
            elif "l" in filename:
                category = "craigslist"
            elif "n" in filename:
                category = "neverssl"
            elif "t" in filename:
                category = "tor"
            elif "w" in filename:
                category = "wikipedia"

            #store all of the information
            vals = []

            vals.append(outgoing_packets)
            vals.append(incoming_packets)
            vals.append(rop)
            vals.append(total_packets)
            vals.append(avg_interval)
            vals.append(total_size)
            vals.append(category)

            #Add information to our 2D list
            rows.append(vals)

    #create dataframe
    df = pd.DataFrame(rows, columns=["Outgoing", "Incoming", "Ratio",
                                     "Total Packets", "Average Time",
                                     "Total Size", "Category" ])


    return df

#loads data from input pcap into a dataframe
def load_input(filename):

    #open and read pcap file
    f = open(filename, 'rb')
    pcap = dpkt.pcap.Reader(f)

    #All of the information we're trying to capture
    total_size = 0
    total_packets = 0
    outgoing_packets = 0
    incoming_packets = 0
    timestamps = []

    #for timestamp and buffer in pcap (same process as the previous function)
    for (ts, buf) in pcap:

        # add the size of the buff
        total_size += len(buf)

        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data

        #source ips
        src = socket.inet_ntoa(ip.src)

        #first packet being sent, therefore this is outgoing
        if total_packets == 0:

            outgoing = src
            outgoing_packets += 1


        elif src == outgoing:

            outgoing_packets += 1

        else:

            incoming_packets += 1

        #add timestamps to list
        timestamps.append(float(ts))

        total_packets += 1

    #ratio of packets
    rop = float(incoming_packets / outgoing_packets)

    #get average time of packets

    intervals = []

    for i in range(1, len(timestamps)):
        intervals.append(timestamps[i] - timestamps[i - 1])

    avg_interval = mean(intervals)

    #classify row based on filename
    category = ""

    if "auto" in filename:
        category = "autolab"
    elif "b" in filename:
        category = "bing"
    elif "canvas" in filename:
        category = "canvas"
    elif "l" in filename:
        category = "craigslist"
    elif "n" in filename:
        category = "neverssl"
    elif "t" in filename:
        category = "tor"
    elif "w" in filename:
        category = "wikipedia"


    #add all of info to list
    vals = []

    vals.append(outgoing_packets)
    vals.append(incoming_packets)
    vals.append(rop)
    vals.append(total_packets)
    vals.append(avg_interval)
    vals.append(total_size)
    vals.append(category)

    #2D list
    vals = [vals]

    #convert to dataframe
    df = pd.DataFrame(vals, columns=["Outgoing", "Incoming", "Ratio",
                                     "Total Packets", "Average Time",
                                     "Total Size", "Category"])


    return df

