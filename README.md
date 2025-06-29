kharej:
backup ro upload kon
```
cd /etc/x-ui 
wget https://raw.githubusercontent.com/httpsMrFeri/scripts/main/update.py
nano update.py
```
replace 10.10.10.10 with your domain or iran server ip

shopt -s dotglob && mv scripts/* . && rmdir scripts && shopt -u dotglob
