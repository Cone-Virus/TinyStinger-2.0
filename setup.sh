mkdir storage
sudo pip3 install -r requirements.txt
mkdir src/wafw00f
git clone https://github.com/EnableSecurity/wafw00f src/wafw00f
sudo src/wafw00f/setup.py install
git clone https://github.com/devanshbatham/FavFreak src/favfreak
sudo pip3 install -r src/favfreak/requirements.txt
wget https://github.com/projectdiscovery/subfinder/releases/download/v2.4.8/subfinder_2.4.8_linux_amd64.tar.gz
mkdir src/subfinder
mv subfinder_2.4.8_linux_amd64.tar.gz src/subfinder
cd src/subfinder
tar xvzf subfinder_2.4.8_linux_amd64.tar.gz
cd ../..
