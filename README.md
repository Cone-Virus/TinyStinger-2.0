# TinyStinger V2.0
- Version 2.0?

There is an earlier rendition of the tinystinger so I decided to make it python based and a sqlite3 DB

- What is it?

A small Bug Bounty scanner that I have been working on to not only make doing bug bounties easier but to help other small bug bounty enthuasiasts.
- Keep in mind

I am not an expert coder so there will probably be a ton of bugs and if something bad happens to your system I am not liable. But nothing should just a quick disclaimer.

## Setup 
- Before first use do the following:
```
chmod +x setup.sh
./setup.sh
```
## Usage
```
python3 TinyStinger.py
```
!!!Only works on Linux!!!
## Features
- HTTP/HTTPS Validation
- Favicon Recon
- WAF Detection
- Built-in DB Shell
- Subdomain Enumeration
- Spidering
- A GUI
## TODO
- Make a better readme
- Make GUI Look Nice
- Robots.txt enumeration
## Credits/Tools Used
- [favfreak](https://github.com/devanshbatham/FavFreak)
- [wafw00f](https://github.com/EnableSecurity/wafw00f)
- [subfinder](https://github.com/projectdiscovery/subfinder)
- [gospider](https://github.com/jaeles-project/gospider)
- [QT Designer](https://www.qt.io/)
