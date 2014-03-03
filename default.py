import os
import sys
import xbmcaddon
import xbmcgui
import xbmc

__addon__ = xbmcaddon.Addon('screensaver.template')
__scriptname__ = __addon__.getAddonInfo('name')
__path__ = __addon__.getAddonInfo('path')
__media__ = os.path.join(__path__,'resources','skins','default','media')

class Screensaver(xbmcgui.WindowXMLDialog):
	class ExitMonitor(xbmc.Monitor):
		def __init__(self, exit):
			self.exit = exit

		def onScreensaverDeactivated(self):
			self.exit()

	def onInit(self):
		self.monitor = self.ExitMonitor(self.exit)

	def exit(self):
		self.close()

if __name__ == '__main__':
	screensaver = Screensaver(
		'default.xml',
		__path__,
		'default',
		)
	screensaver.doModal()
	del screensaver
	sys.modules.clear()

