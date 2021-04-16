

#1. in ubuntu, mint and other Debian based distributions
sudo apt-get install python-numpy python-qt4 python-lxml python-six


#2. Install/Upgrade ETE using PIP
pip install --upgrade ete3


#or using EasyInstall
easy_install -U ete3

#or from the sources: Download latest version from PyPU and execute:
python setup.py install 


#3. Compile external tools - optional step, required only by ete-build and ete-evol
ete3 upgrade-external-tools
