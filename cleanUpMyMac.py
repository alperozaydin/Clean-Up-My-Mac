__author__ = "Alper Ozaydin"


from cleanUpMyMacHelper import cleanUpMyMacHelper


class cleanUpMyMac(object):

	cleanUpMyMacHelper.eraseSpotifyCache()
	cleanUpMyMacHelper.eraseSafariWebKitCache()
	cleanUpMyMacHelper.eraseDeveloperCoreSimulator()
	print(cleanUpMyMacHelper.totalErasedAmount())

