# CoWin Vaccine Checker

[![Python 3.9.5](https://img.shields.io/static/v1?label=python&message=3.9.5&color=red)](https://www.python.org/downloads/release/python-395/)
[![API Setu](https://img.shields.io/static/v1?label=API_Setu&message=1.3.0&color=red)](apisetu.gov.in/public/api/cowin#/)
[![Python 3.9.5](https://img.shields.io/static/v1?label=PyWhatKit&message=4.8&color=green)](https://pypi.org/project/pywhatkit/)
[![Python 3.9.5](https://img.shields.io/static/v1?label=chime&message=0.6&color=green)](https://pypi.org/project/chime/)<br>

### Problem statement:
Many of us have already experienced troubles while booking vaccine slots in CoWin site due to the variation in the time of updation of slots in different Health care centers. Its difficult for common individual to sit infront of computer and check for slots throghout the day.<br>
This python script will help people to overcome this issue by identifying slots when it opens and notifying the concerned person by whatsapp and audio.

### Key features:
<ul>
  <li> Uses Public API provided by <a href="https://apisetu.gov.in/public/api/cowin#/"><b>API Setu</b></a> to get the information regarding health care centers and vaccines with pincode as filter </li>
  <li> Sends request to API with the frequency mentioned by user and checks for vaccine availability at all pincodes for 18+ age group </li>
  <li> Sends automatic whatsapp message to required person using <a href="https://pypi.org/project/pywhatkit/">PyWhatKit</a> package with pre-defined text to the phone number mentioned during script running (Laptop must be connected to whatsapp web)</li>
  <li> Uses <a href="https://pypi.org/project/chime/">chime</a> package to generate sound notification in laptop when it sends the whatsapp message </li>
</ul>

### Steps to run the script:
#### 1. Clone this repository by downloading zip or by running following command in Git or terminal :
```
git clone https://github.com/yshastri66/CoWin-Vaccine-Checker.git
```
#### 2. Create a new python environment and install the requirments using requirements.txt file by executing following commands :
```
conda create -n env_name
conda activate env_name
pip install -r requirements.txt
```
#### 3. Run cowin_main.py file using following command and enter the valid inputs :
```
python3 cowin_main.py
```

<b>Snapshots of the script outputs are below: </b><br>
<div align='center'>
  <b>Code snippet running</b><br>
  <img src="https://github.com/yshastri66/CoWin-Vaccine-Checker/blob/main/images/WhatsApp%20Image%202021-06-27%20at%2010.37.07%20AM.jpeg" alt="terminal"  width="600" height="450"><br>
  <br><b>Automatic whatsapp web opening and typed text</b>
  <img src="https://github.com/yshastri66/CoWin-Vaccine-Checker/blob/main/images/WhatsApp%20Image%202021-06-27%20at%2010.37.42%20AM.jpeg" alt="terminal"  width="600" height="450"><br>
  <br><b>Automatic message sending</b><br>
  <img src="https://github.com/yshastri66/CoWin-Vaccine-Checker/blob/main/images/WhatsApp%20Image%202021-06-27%20at%2010.34.13%20AM.jpeg" alt="terminal"  width="600" height="450">
</div><br>

#### Feel free to contact me incase on any quaries :-
<h4> Yashodhara Shastri G <br>
 yashodharashastri6@gmail.com </h4>
