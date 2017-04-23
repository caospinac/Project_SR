# Project_SR

## Steps for get starting

### Python 3.6 for Ubuntu 14.04 or 16.04, build-essential and Git
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt update
sudo apt install python3.6 python3.6-dev python3.6-venv python3.6-dbg
sudo apt install build-essential git
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
### PostgreSQL
```
sudo apt install postgresql postgresql-client postgresql-contrib
sudo apt install libpq-dev
sudo -u postgres psql postgres
```
#### Configure password
In the postgres CLI...
```
\password postgres
\q
```
#### Install pgAdmin III
```
sudo apt install pgadmin3
```
*In Postgres, the database must exist before mapping o run the project*
<hr>

In the virtual environment...
```
pip install --upgrade pip
pip install -r requirements.txt
```
### Run
```
python agronify/app.py
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
Go to http://0.0.0.0:8000
