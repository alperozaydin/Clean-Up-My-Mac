# Alper Ozaydin
# El Capitan 10.11.6
# CleanUpMyMac

from cleanUpMyMacHelper import cleanUpMyMacHelper


class cleanUpMyMac(object):

	cleanUpMyMacHelper.eraseSpotifyCache()
	cleanUpMyMacHelper.eraseSafariWebKitCache()
	print(cleanUpMyMacHelper.totalErasedAmount())

