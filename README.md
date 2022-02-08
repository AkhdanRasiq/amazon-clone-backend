# Amazon Backend Cloned Version - | LINUX / WSL |

This repository containing clone version of Amazon for Education purpose only!

## MAIN TECH STACK

1. Pyhton3.8 - Linux
2. Django - Rest Framework
3. MySQL

<br />

# QUICK ACCESS

FRONTEND : Under Construction!

BACKEND  : Under Construction!

# Repository List

1. AkhdanRasiq/amazon-clone (Frontend) : [Link](https://github.com/AkhdanRasiq/amazon-clone)
2. AkhdanRasiq/amazon-clone-backend (Backend) : [Link](https://github.com/AkhdanRasiq/amazon-clone-backend)

<br />

# Getting Started

## For Windows User

You need WSL(Windows Subsystem for Linux) for running the server. Go to **Control Panel > Programs > Programs and Features > Turn Windows features on or off** and check **Windows Subsystem for Linux**.

## Dependencies

The List of all Require Dependencies are in requirements.txt at the root of project, run this command to install all of it ```pip install -r requirements.txt``` in new python environment.

***IF YOU GET ERROR WHEN INSTALLING [ mysqlclient ] FOLLOW BELOW STEP:***

### WINDOWS

[DOWNLOAD mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)

Then Run

```
pip install {downloadedFile.whl}
```

### LINUX
```
sudo apt-get install python3.8-dev default-libmysqlclient-dev build-essential
```

# Command List

### START SERVER
```
python manage.py runserver
```

### CREATE SUPER USER
```
python manage.py createsuperuser
```

### UPDATE DATA FOR MIGRATION
```
python manage.py makemigrations
```

### MIGRATE DATA TO DATABASE
```
python manage.py migrate
```
