
import logSetup
if __name__ == "__main__":
	print("Initializing logging")
	logSetup.initLogging()

import TextScrape.SiteArchiver

import readability.readability
import bs4
import webFunctions
import urllib.error

class Scrape(TextScrape.SiteArchiver.SiteArchiver):
	tableKey = 'remonwiki'
	loggerPath = 'Main.Text.ReMonWiki.Scrape'
	pluginName = 'ReMonWikiScrape'

	wg = webFunctions.WebGetRobust(logPath=loggerPath+".Web")

	threads = 4

	feeds = [
		'http://re-monster.wikia.com/wiki/Special:RecentChanges?feed=atom'
	]


	baseUrl = [
			"http://re-monster.wikia.com/wiki/Novel",
			"http://re-monster.wikia.com/wiki/Day_1-10/Day_1",
			"http://re-monster.wikia.com/",
		]
	startUrl = baseUrl

	badwords = [
				"/viewtopic.php",
				"/memberlist.php",
				"/search.php",
				"/wp-content/plugins/",
				"/styles/prosilver/theme/",
				"/forums/",
				"/forum/",
				"/cdn-cgi/",
				"/help/",
				"?share=",
				"?popup=",
				"viewforum.php",
				"/wp-login.php",
				"/#comments",      # Ignore in-page anchor tags
				"/staff/"
				"title=Special",
				"action=edit",
				"action=history",
				"action=info",
				"title=Help:",
				"title=User_talk:",
				"&oldid=",
				"?oldid=",
				"title=Baka-Tsuki:",
				"title=Special:Book",
				"Message_Wall:",
				"Special:Search",
				"Special:Log",
				"action=purge",

				"Special:WhatLinksHere",
				"Special:Editcount",
				"Special:Chat",
				"Special:UserLogin",
				"Special:RecentChanges",
				"Special:",
				"action=edit",
				"diff=",
				"diff%3D",
				"feed=atom",
				"action=submit",
				"MediaWiki:Sandbox",
				"Special:Contributions",

				"/Template:",
				"/Thread:",
				"/Forum:",
				"/Help:",
				"/User_blog:",

				"Special:RecentChangesLinked",
				"/wiki/Sandbox",
				"Special:Forum",
				"/__load/-/",
				"__load/",
				"@comment",
				'action=purge',

				# Block user pages
				"title=User:",
				"=Talk:",
				"=talk:",
				"Special:ListUsers",

				# misc
				"viewforum.php",
				"viewtopic.php",
				"memberlist.php",
				"printable=yes",


				]

	positive_keywords = ['main_content']

	negative_keywords = ['mw-normal-catlinks',
						"printfooter",
						"mw-panel",
						'portal']




	decomposeBefore = [
		{'id'      :'disqus_thread'},
		{'id'      :'WikiaBar'},
		{'id'      :'WikiaArticleComments'},
		{'id'      :'fb-root'},
		{'id'      :'ad-skin'},
		{'id'      :'globalNavigation'},
		{'id'      :'WikiaNotifications'},
		{'id'      :'GPT_FLUSH'},
		{'id'      :'SEVENONEMEDIA_FLUSH'},
		{'id'      :'WikiaTopAds'},
		{'id'      :'PageShareContainer'},
		{'id'      :'WikiaArticleBottomAd'},

		{'class'   :'skiplinkcontainer'},
		{'class'   :'global-footer'},
		{'class'   :'home-top-right-ads'},
		{'class'   :'transparent-out'},
		{'class'   :'ChatModule'},
		{'class'   :'ad-in-content'},
		{'class'   :'ForumActivityModule'},
	]


	decompose = [
		{'id'    : 'articleCategories'},
		{'id'    : 'WikiaArticleFooter'},
		{'id'    : 'WikiaFooter'},
		{'id'    : 'WikiaRail'},
		{'id'    : 'WikiHeader'},

		{'class' : 'share-box'},
		{'class' : 'header-tally'},
		{'class' : 'wikia-menu-button'},
		{'class' : 'comments'},
		{'class' : 'printfooter'},
		{'class' : 'portal-section'},
		{'class' : 'main-page-tag-rcs'},
		# This is used for some relevant tables. Arrrgh.
		# {'class' : 'clear-right-after-ad-in-content'},

	]





def test():
	scrp = Scrape()
	scrp.crawl()
	# scrp.retreiveItemFromUrl(scrp.startUrl)
	# new = gdp.GDocExtractor.getDriveFileUrls('https://drive.google.com/folderview?id=0B-x_RxmzDHegRk5iblp4alZmSkU&usp=sharing')


if __name__ == "__main__":
	test()







