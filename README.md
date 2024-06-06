# Machine Learning-Driven Network Security: IoT DDoS Attack Detection
- Description: 
- IoT enables easy access to cloud services but faces severe DDoS threats. 
- DDoS attacks disrupt IoT services by flooding networks with compromised devices.
- Motivation :
- IoT Expansion & Vulnerability:IoT expansion requires robust security against evolving DDoS threats
- Critical Data Security:With sensitive data at stake, ML ensures data integrity and user trust.
- Evolving DDoS Threats:Traditional measures fall short, necessitating adaptive machine learning for dynamic threat detection.

- Data is retrieved from different file formats as follows: 
- • README.md - contains info about captures and associated malwares.
- • .pcap - original file that has network traffic captures 
- • conn.log.labeled - .pcap file is retrieved using Zeek network analyser with proper labelling along with some additional info

-AposematIoT-23 
- • A unique dataset capturing IoT network traffic. 
- • 20 malware captures on IoT devices and 3 benign IoT devices. 
- • Real network behaviour for research and machine learning. 
- • Labels provided for analysis, including attack, C&C, DDoS, and more. 
- • A valuable resource for IoT security and malware research.

# Description of Files

- .capinfos
    - Capinfos file
- .dnstop
    - DNS top file
- mitm.out
    - Mitm proxy interception file of http and https
- .mitm.weblog
    - This is the HTTP and HTTPS web log that includes Labels. This is the preferred file for web analysis.
    - This file includes a header with the columns names. There are two new columns defined by us:
        - Column id: This number is unique for all the weblogs generated __inside__ the same TCP connection. When a TCP connection is opened and several GET/POST, etc., requests are made inside it, all of them are assigned the same Id in this file.
        - Column timestamp_end: This is the timestamp when the weblog ended. If you use this with the id column you can compute the total duration of the TCP connection that generated __all__ the weblogs. Similar to the duration of a hypothetical CONNECT request if this would have been done using a proxy.
- .passivedns
    - Passive DNS file
- .pcap
    - Original pcap file
- .rrd
    - RRD file for graphs
- .weblogng
    - WEB log of http traffic only. Generated with justsniffer
- .exe.zip
    - Original malware file
- bro
    - Folder with all the bro output files
- .biargus
    - Argus binary file. Bidirectional flows, 3600s of report time.
- .binetflow
    - Argus text file with bidirectional flows. Report time 3600 secs.
- .uniargus
    - Argus binary file. Unidirectional flows, 5s of report time.
- .uninetflow
    - Argus text file with unidirectional flows. Report time 5 secs. TAB as column separator.
