echo "[+] Setting up Directory"
mkdir storage
echo "[+] Setting up wafw00f"
sudo pip3 install -r requirements.txt
mkdir src/wafw00f
git clone https://github.com/EnableSecurity/wafw00f src/wafw00f
sudo src/wafw00f/setup.py install
echo "[+] Setting up FavFreak" 
git clone https://github.com/devanshbatham/FavFreak src/favfreak
sudo pip3 install -r src/favfreak/requirements.txt
echo "[+] Setting up subfinder"
wget https://github.com/projectdiscovery/subfinder/releases/download/v2.4.8/subfinder_2.4.8_linux_amd64.tar.gz
mkdir src/subfinder
mv subfinder_2.4.8_linux_amd64.tar.gz src/subfinder
cd src/subfinder
tar xvzf subfinder_2.4.8_linux_amd64.tar.gz
cd ../..
echo "[+] Setting up gospider"
wget https://github.com/jaeles-project/gospider/releases/download/v1.1.6/gospider_v1.1.6_linux_x86_64.zip
unzip gospider_v1.1.6_linux_x86_64.zip
mv gospider_v1.1.6_linux_x86_64 gospider
mv gospider src/
rm -rf gospider_v1.1.6_linux_x86_64.zip
