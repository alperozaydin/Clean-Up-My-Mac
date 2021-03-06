__author__ = "Alper Ozaydin"


import os
import commands


class cleanUpMyMacHelper(object):

    total = []

    @classmethod
    def __init__(self):
        print("asd")
        user_selection = raw_input("Press 's' to sort big files, press 'd' to clean your Mac")
        if (user_selection == "S" or user_selection =="s"):
            cleanUpMyMacHelper.sortBigFolders()
        elif (user_selection == "D" or user_selection == "d"):
            cleanUpMyMacHelper.eraseSpotifyCache()
            # cleanUpMyMacHelper.eraseSafariWebKitCache()
            # cleanUpMyMacHelper.eraseDeveloperCoreSimulator()
            cleanUpMyMacHelper.eraseHomebrew()
            print(cleanUpMyMacHelper.totalErasedAmount())


    @classmethod
    def eraseHomebrew(self):
        status, output = commands.getstatusoutput("brew cleanup")

    @classmethod
    def eraseSpotifyCache(self):
        for file in os.listdir("//Users/Seric/Library/Caches/com.spotify.client"):
            if file == "Data":
                status, output = commands.getstatusoutput("du -sh /Users/Seric/Library/Caches/com.spotify.client/Data")
                status2, output2 = commands.getstatusoutput("du -s /Users/Seric/Library/Caches/com.spotify.client/Data")
                output = output.split("\t")
                output2 = output2.split("\t")
                os.system("rm -rf /Users/Seric/Library/Caches/com.spotify.client/Data")
                print("Spotify cache successfully erased! -> " + output[0])
                self.total.append((int(output2[0])/2))
                return 1
        print("There is no Spotify cache!")
        return 0

    @classmethod
    def eraseSafariWebKitCache(self):
        for file in os.listdir("/Users/Seric/Library/Caches/com.apple.Safari"):
            if file == "WebKitCache":
                status, output = commands.getstatusoutput("du -sh /Users/Seric/Library/Caches/com.apple.Safari/WebKitCache")
                status2, output2 = commands.getstatusoutput("du -s /Users/Seric/Library/Caches/com.apple.Safari/WebKitCache")
                output = output.split("\t")
                output2 = output2.split("\t")
                os.system("rm -rf /Users/Seric/Library/Caches/com.apple.Safari/WebKitCache")
                print("Safari Webkit cache successfully erased! -> " + output[0])
                self.total.append((int(output2[0])/2))
                return 1
        print("There is no Safari Webkit cache!")
        return 0


    @classmethod
    def eraseDeveloperCoreSimulator(self):
        for file in os.listdir("/Users/Seric/Library/Developer"):
            if file == "CoreSimulator":
                status, output = commands.getstatusoutput("du -sh /Users/Seric/Library/Developer/CoreSimulator")
                status2, output2 = commands.getstatusoutput("du -s /Users/Seric/Library/Developer/CoreSimulator")
                output = output.split("\t")
                output2 = output2.split("\t")
                os.system("xcrun simctl delete unavailable")
                status3, output3 = commands.getstatusoutput("du -s /Users/Seric/Library/Developer/CoreSimulator")
                output3 = output3.split("\t")
                if (int(output3[0]) - int(output2[0])) == 0:
                    print("There is no unavailable Core Simulators file!")
                    return 1
                print("Unavailable Core Simulators successfully erased! -> " + str((int(output3[0]) - int(output2[0]))))
                self.total.append(((int(output3[0]) - int(output2[0]))/2))
                return 1
        return 0

    #TODO Display files and folders more than 3 GB.
    #TODO User can change the "big folder" size to sort
    @classmethod
    def sortBigFolders(self):
        # System Library Folders
        status, output = commands.getstatusoutput("du -hs /Library/Application\ Support/* | sort -rh | head -5")
        if "No such file or directory" not in output:
            print("In /Library")
            print(output)

        status, output = commands.getstatusoutput("du -hs /Users/Seric/Library/Android/sdk/* | sort -rh | head -5")
        if "No such file or directory" not in output:
            print("In /Android")
            print(output)
            
    @classmethod
    def totalErasedAmount(self):
        return "Total -> " + str(sum(self.total)/1024) + "MB"

