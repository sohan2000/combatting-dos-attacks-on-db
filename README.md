# combatting-dos-attacks-on-db
 **CS 257 Capstone Project:** Combatting DoS Attacks on Databases
 **Team members:** Sohan Vallapureddy, Srimanth Reddy Ummenthala

**Project PPT:** [Combatting DoS Attacks on Databases PPT](https://tinyurl.com/no-dos-attacks-on-db-ppt) (Only visible to SJSU Students)

# Instructions for installation:
* Installations for Target System:
  * Download and Install VMware Workstation Player 17 for Windows from [vmware](https://www.vmware.com/go/getplayer-win)
  * Download Windows 8.1 Disc Image (ISO File)(32-bit) from [Microsoft](https://software.download.prss.microsoft.com/dbazure/Win8.1_English_x32.iso?t=f6bf589a-fe9f-4940-8ee1-a2761e9f1562&e=1702015760&h=1a0d634d546e421f438fa20bac57eee020dc6b5de71a6513642c9224148ed7e8)
  * Create a new VM for Windows 8.1 on VMware Workstation Player 17 [Installation Guide](https://youtu.be/1ugRzE7nZq4)
  * Install Python 3.10 from [Windows installer (32-bit)](https://www.python.org/ftp/python/3.10.0/python-3.10.0.exe)
  * To download [pip](https://bootstrap.pypa.io/get-pip.py), save page as 'get-pip.py'
  * Open Command Prompt as Administrator and run command to install pip: python get-pip.py
  * Installing necessary libraries using pip
    * pip install Flask Flask-Login Flask-WTF Flask-SQLAlchemy pyotp waitress scapy requests
  * Download DB.zip from the repository
  * Go to command prompt and run command: python server.py
  * This is start the Flask server on localhost:8080
  * Go to the browser and start using the UI for retrieving records from the database!
 
* Installations for Attacker System:
  * Download Kali Linux from [Kali Linux ISO 32 bit](https://www.techspot.com/downloads/downloadnow/6738/?evp=7e087af1ea8b1811d5744556949f14ef&file=8534)
  * Installation commands
    * sudo apt install python3-pip
    * sudo apt install hping3
    * sudo apt install nmap
    * sudo apt install slowloris

# Features
* Run commands on Target system (where we have installed Flask server):
 * python flask_limiter.py
 * python geo-ip.py
 * python rbac.py
 * python two-factor-authentication.py
 * python user-registration-forms.py
 * python monitoring-and-logging.py
 * python server.py

 * We have added features like Rate Limiting, Geo-IP Filtering, Role-based access control (RBAC), Two-Factor-Authentication (2FA), and Monitoring & Logging. For registering new users to DB, run user-registration-forms.py
 * To host the database on the server, run server.py

**Contributions:**
* Sohan Vallapureddy:
  * Developing DB Schema and Architecture Model
  * Developing functional UI and Flask web server
  * Simulate DoS attacks on the System
  * PPT and Report
* Srimanth Reddy Ummenthala
  * Creating UML Diagrams
  * Developing rules to mitigate DoS attacks
  * Illustrating prevention of DoS attacks
  * PPT and Report
