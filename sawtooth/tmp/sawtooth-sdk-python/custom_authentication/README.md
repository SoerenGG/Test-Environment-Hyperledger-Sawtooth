Use the Clients and Handlers: (setup of sawtooth network has to be already done)  
1: install by changing in this directory and run: "pyhton3 setup.py install"  
2: open new terminal and connect to validator: "custom-authentication-tp-python --connect tcp://validator:4004"  
3: open new terminal and create keys: "sawtooth keygen" and stay here  
accumulator-manager-client cmd is = "accumulator-manager"  
user-client gets called through accmulator-manager-client  
4: initialize new Accumulator with a servicename, the accumulator value has to be 9 (eg "mercedes")  
"accumulator-manager initialize mercedes 9"  
5: add a user to the accumulator by specifying the service the user wants to be added to and give a username (eg user1)  
"acaccumulator-manager user-client-add user1 mercedes  
json files are created during this process:  
"mercedes.json" would be the tailsfile for the "mercedes" Accumulator  
"user1.json" would be the file for the "user1"  
