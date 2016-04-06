### Run: 

Linux/Mac:

    source venv/bin/activate
    fab deploy 

Windows:

    venv\Scripts\activate.bat
    fab deploy

### Install: 

To create a virtualenv and install the requirements:

Linux/Mac:

    virtualenv venv --distribute
    source venv/bin/activate
    pip install -r requirements.txt 


Windows

    virtualenv venv --distribute
    venv\Scripts\activate.bat
    easy_install http://www.voidspace.org.uk/python/pycrypto-2.6.1/pycrypto-2.6.1.win32-py2.7.exe
    pip install -r requirements.txt 
