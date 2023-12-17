# Tooling: SiLK


# Which version of SiLK is installed on the VM?
`silk_config -v`
3.19.1

# What is the size of the flows in the count records?
`rwfileinfo suspicious-flows.silk`
count-records: 11774

# What is the start time (sTime) of the sixth record in the file?
`rwcut suspicious-flows.silk --num-recs=6 `
2023/12/05T09:33:07.755

# What is the destination port of the sixth UDP record?
`rwcut suspicious-flows.silk --fields=protocol,dPort | grep -E "^ 17\|" | head -n6`
17 - UDP
Port: 49950

# What is the record value (%) of the dport 53?
`rwstats suspicious-flows.silk  --fields=dPort --count=10`
dPort|   Records|  %Records|   cumul_%|
   53|      4160| 35.332088| 35.332088|
35.332088

# What is the number of bytes transmitted by the top talker on the network?
`rwstats suspicious-flows.silk --fields=sIP --values=bytes --count=1 --top`
                                    sIP|               Bytes|    %Bytes|   cumul_%|
                        175.219.238.243|              735229| 52.048036| 52.048036|
735229

# What is the sTime value of the first DNS record going to port 53?
`rwfilter suspicious-flows.silk --dport=53 --pass=stdout | rwcut --fields=stime | head -10`
2023/12/08T04:28:44.825

# What is the IP address of the host that the C2 potentially controls? (In defanged format: 123[.]456[.]789[.]0 )
```bash
rwfilter suspicious-flows.silk --aport=53 --pass=stdout | rwstats --fields=sIP,dIP --values=records,bytes,packets --count=10
rwfilter suspicious-flows.silk --saddress=175.175.173.221 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -10
rwfilter suspicious-flows.silk --saddress=175.219.238.243 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -10

rwfilter suspicious-flows.silk --any-address=175.175.173.221 --pass=stdout | rwstats --fields=sIP,dIP --count=10
rwfilter suspicious-flows.silk --any-address=205.213.108.99 --pass=stdout | rwstats --fields=sIP,sPort,dIP,dPort,proto --count=10
```
205.213.108.99 - potential C2
175.175.173.221 - potentially infected host

175[.]175[.]173[.]221

# Which IP address is suspected to be the flood attacker? (In defanged format: 123[.]456[.]789[.]0 )
```bash
rwfilter suspicious-flows.silk --aport=80 --pass=stdout | rwstats --fields=sIP,dIP,dPort --count=10
rwfilter suspicious-flows.silk --saddress=175.215.236.223 --pass=stdout | rwcut --fields=sIP,dIP,dPort,flag,stime | head
rwfilter suspicious-flows.silk --saddress=175.215.236.223 --pass=stdout | rwstats --fields=sIP,flag,dIP --count=10
```
175[.]215[.]236[.]223

# What is the sent SYN packet's number of records?
1658
