__author__ = "Alper Ozaydin"


import os
import commands


class cleanUpMyMacHelper(object):

    total = []

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

    @classmethod
    def totalErasedAmount(self):
        return "Total -> " + str(sum(self.total)/1024) + "MB"

