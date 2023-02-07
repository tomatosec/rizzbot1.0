# rizzbot1.0

~For educational and research purposes only~ ;)

Unlimited rizz! These scripts allow you to completley automate your liking and messaging on Tinder. Thanks to the GPT-3 API, every message is unique. Additional capabilities will be made in future realeases. 

reference material: 
https://www.youtube.com/watch?v=lckdQ6jZ8tg&ab_channel=InternetMadeCoder
https://github.com/tuomaskivioja/tinderBot

REQUIREMENTS: 

1. Install Selenium 
   On Windows go to powershell and run: pip install selenium

2. Downlaod Chrome Driver 
    https://sites.google.com/chromium.org/driver/?pli=1
    unzip the file. I recommend moving it to the C:\Windows directory

3. A Tinder account linked with Facebook 

4. An OpenAI account 
    link here: https://platform.openai.com/account/api-keys


Instructions: 

1. Go to the file 'Tinderlogin.py'. Enter your Facebook credentials 

2. Go to automessager.py and enter your API key 

3. Run and enjoy the rizz

Further automation: 

To run these scripts automatically on a Windows Machine: 

1. Navigate to Task Scheduler

2. Create a new task 

3.Check the following in General: Run whether user is logged in or not. Run with highest privledges 

4. Important and confusing part for Task scheduler: 

run  python -c "import sys; print (sys.executable)" 

whatever path you get put that in the "Program/Scipt" Line 

then put the FULL PATH of the python script in the add arguments line. 


Now your rizz should be fully automated! Have fun :D

-SpicyLatke 2/7/23 




