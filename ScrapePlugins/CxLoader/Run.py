

from ScrapePlugins.CxLoader.cxFeedLoader import CxFeedLoader
from ScrapePlugins.CxLoader.cxContentLoader import CxContentLoader

import ScrapePlugins.RunBase

import time

import runStatus


class Runner(ScrapePlugins.RunBase.ScraperBase):
	loggerPath = "Main.Manga.Cx.Run"

	pluginName = "CxLoader"


	def _go(self):

		self.log.info("Checking CXC feeds for updates")
		fl = CxFeedLoader()
		fl.go()
		fl.closeDB()

		time.sleep(3)
		#print "wat", cl

		if not runStatus.run:
			return

		cl = CxContentLoader()

		if not runStatus.run:
			return

		todo = cl.retreiveTodoLinksFromDB()

		if not runStatus.run:
			return

		cl.processTodoLinks(todo)
		cl.closeDB()
