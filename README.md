kharej:
backup ro upload kon
```
cd /etc/x-ui 
wget https://raw.githubusercontent.com/httpsMrFeri/scripts/main/update.py
nano update.py
```
replace 10.10.10.10 with your domain or iran server ip
```
python3 -m http.server
```
iran:
```
wget -Nq https://github.com/Musixal/haproxy-tunnel/raw/main/haproxy.sh && bash haproxy.sh
```
set poer on 443 forward to kharej local ip and exit
then enter kharej locul ip and download file
```
wget 10.10.144.4:8000/x-ui.db
wget https://raw.githubusercontent.com/httpsMrFeri/scripts/main/exportPorts.py
wget https://raw.githubusercontent.com/httpsMrFeri/scripts/main/setProxy.sh
cat x-ui.db > ports.txt
python3 exportPorts.py 
``` 
then remove not support port:
```
grep -E '^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5]?[0-9]{1,4})$' unique_ports.txt > valid_ports.txt
mv valid_ports.txt unique_ports.txt
sort -n unique_ports.txt | uniq > temp.txt && mv temp.txt unique_ports.txt
```
change locul ip and set kharej local ip address:
```
nano ./setProxy.sh 
```
save and exit
then:
```
chmod +x ./setProxy.sh 
./setProxy.sh
```

shopt -s dotglob && mv scripts/* . && rmdir scripts && shopt -u dotglob
