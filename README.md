# Project_SR

## Steps for get starting

### Python 3.6 for Ubuntu 14.04 or 16.04 and build-essential
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt update
sudo apt install python3.6 python3.6-dev python3.6-venv python3.6-dbg
sudo apt install build-essential
```
*Restart the terminal*
### Addressing the project
```
git clone https://github.com/carlosaospinac/Project_SR.git
cd Project_SR/
```
### Virtual environment
```
python3.6 -m venv venv
source venv/bin/activate
```
### Install requeriments
```
pip install --upgrade pip
pip install -r requeriments.txt
```
### Run
```
python project/app.py
```
### It will get something like ...
```
...
...
2017-04-11 14:48:38,284: DEBUG: 
                 ▄▄▄▄▄
        ▀▀▀██████▄▄▄       _______________
      ▄▄▄▄▄  █████████▄  /                 \
     ▀▀▀▀█████▌ ▀▐▄ ▀▐█ |   Gotta go fast!  |
   ▀▀█████▄▄ ▀██████▄██ | _________________/
   ▀▄▄▄▄▄  ▀▀█▄▀█════█▀ |/
        ▀▀▀▄  ▀▀███ ▀       ▄▄
     ▄███▀▀██▄████████▄ ▄▀▀▀▀▀▀█▌
   ██▀▄▄▄██▀▄███▀ ▀▀████      ▄██
▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███     ▌▄▄▀
▌    ▐▀████▐███▒▒▒▒▒▐██▌
▀▄▄▄▄▀   ▀▀████▒▒▒▒▄██▀
          ▀▀█████████▀
        ▄▄██▀██████▀█
      ▄██▀     ▀▀▀  █
     ▄█             ▐▌
 ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄
▌     ▐                ▀▀▄▄▄▀
 ▀▀▄▄▀

2017-04-11 14:48:38,285: INFO: Goin' Fast @ http://0.0.0.0:8000
2017-04-11 14:48:38,422: INFO: Starting worker [19659]
```
Go to <a target="_blank">http://0.0.0.0:8000</a>
