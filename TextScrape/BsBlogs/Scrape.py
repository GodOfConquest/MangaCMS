
import logSetup
if __name__ == "__main__":
	print("Initializing logging")
	logSetup.initLogging()

import TextScrape.BlogspotBase

import webFunctions


class Scrape(TextScrape.BlogspotBase.BlogspotScrape):
	tableKey = 'bs'
	loggerPath = 'Main.Text.Bs.Scrape'
	pluginName = 'BsScrape'

	wg = webFunctions.WebGetRobust(logPath=loggerPath+".Web")

	threads = 6

	baseUrl = [

		'http://a0132.blogspot.ca',
		'http://ahoujicha.blogspot.ca',
		'http://aquarilasscenario.blogspot.com',
		'http://arzengi.blogspot.com',
		'http://cetranslation.blogspot.ca',
		'http://cetranslation.blogspot.com',
		'http://cetranslation.blogspot.sg',
		'http://ecwebnovel.blogspot.ca',
		'http://hereticlnt.blogspot.ca',
		'http://hereticlnt.blogspot.com',
		'http://hikuosan.blogspot.com',
		'http://imoutoliciouslnt.blogspot.ca',
		'http://imoutoliciouslnt.blogspot.com.au',
		'http://jawztranslations.blogspot.ca',
		'http://jawztranslations.blogspot.com',
		'http://kaezartranslations.blogspot.com',
		'http://kurotsuki-novel.blogspot.ca',
		'http://kurotsuki-novel.blogspot.com',
		'http://nakulas.blogspot.com',
		'http://noitl.blogspot.com',
		'http://panofitrans.blogspot.com',
		'http://royalroadweed.blogspot.co.il',
		'http://skythewood.blogspot.com',
		'http://skythewood.blogspot.sg',
		'http://sousetsuka.blogspot.ca',
		'http://swordandgame.blogspot.ca',
		'http://swordandgame.blogspot.it',
		'http://the-last-skull.blogspot.com',
		'http://thenakedsol.blogspot.com',
		'http://thenakedsol.blogspot.com.au',
		'http://thezombieknight.blogspot.co.uk',
		'http://untuned-strings.blogspot.ca',
		'http://untuned-strings.blogspot.com',
		'http://xcrossj.blogspot.com.au',
		'http://xhawk77x.blogspot.com',
		'https://sousetsuka.blogspot.com',
		'http://mahoukoukoku.blogspot.com.au',
		'http://istlovesu.blogspot.com',
		'http://azureskytls.blogspot.com.au',
		'http://tu-shu-guan.blogspot.com',



	]

	feeds = [item+"/feeds/posts/default" for item in baseUrl]

	startUrl = [
		'https://drive.google.com/folderview?id=0B8UYgI2TD_nmMjE2ZnFodjZ1Y3c&usp=drive_web',
		'https://docs.google.com/document/d/1LKdA3x0k3I3Hbemmp5tc_xu0IMGyhwjV7y6UV5bUhXU',
		'http://imoutoliciouslnt.blogspot.ca/p/projects.html',
		'http://cetranslation.blogspot.com/p/projects.html',

		] + baseUrl


	tld = set(['com', 'ca', 'fr', 'sg', 'it'])

	# Any url containing any of the words in the `badwords` list will be ignored.
	badwords = [

				"-online-pdf-viewer/",
				".yahoo.com",
				"/comment-page-",
				"/manga/",
				"/recruitment/",
				"?share=",
				"_wpnonce=",
				"account/begin_password_reset",
				"facebook.com",
				"like_comment=",
				"mailto:",
				"plus.google.com",
				"showComment=",
				"twitter.com",
				"wpmp_switcher=mobile",
				'#comment-form',
				'#comments',
				'.googleusercontent.com',
				'/?replytocom=',
				'/comments/default',
				'/feeds/',
				'/search/',
				'/search/label/',
				'/search?',
				'p.opt.fimserve.com',
				'showComment=',
				'the-imouto-petter.html',
				'tinypic.com',
				'updated-max',
				'/page/page/',

				# I don't know why the scrape is walking over to taptaptap content, but it's fucking annoying.
				'www.taptaptaptaptap.net',
				]

	decomposeBefore = [

		{'class' : 'comments'},
		{'class' : 'comments-area'},
		{'class' : 'post-share-buttons'},
		{'class' : 'wpcnt'},
		{'id'    : 'addthis-share'},
		{'id'    : 'comments'},
		{'id'    : 'info-bt'},
		{'id'    : 'jp-post-flair'},

	]

	decompose = [

		{'class'  : 'authorpost'},
		{'class'  : 'bit'},
		{'class'  : 'blog-feeds'},
		{'class'  : 'blog-pager'},
		{'class'  : 'btop'},
		{'class'  : 'column-left-outer'},
		{'class'  : 'column-right-outer'},
		{'class'  : 'comments'},
		{'class'  : 'date-header'},
		{'class'  : 'entry-utility'},
		{'class'  : 'footer'},
		{'class'  : 'footer-outer'},
		{'class'  : 'header-outer'},
		{'class'  : 'headerbg'},
		{'class'  : 'komensamping'},
		{'class'  : 'menucodenirvana'},
		{'class'  : 'menujohanes'},
		{'class'  : 'navbar'},
		{'class'  : 'photo-meta'},
		{'class'  : 'post-feeds'},
		{'class'  : 'post-footer'},
		{'class'  : 'quickedit'},
		{'class'  : 'sidebar'},
		{'class'  : 'sidebar-wrapper'},
		{'class'  : 'tabs-outer'},
		{'class'  : 'widget-area'},
		{'class'  : 'widget-container'},
		{'class'  : 'widget-content'},
		{'class'  : 'wpcnt'},
		{'class'  : 'wpcom-follow-bubbles'},
		{'id'     : 'addthis-share'},
		{'id'     : 'bit'},
		{'id'     : 'carousel-reblog-box'},
		{'id'     : 'comments'},
		{'id'     : 'credit'},
		{'id'     : 'credit-wrapper'},
		{'id'     : 'footer'},
		{'id'     : 'header'},
		{'id'     : 'headerimg'},
		{'id'     : 'infinite-footer'},
		{'id'     : 'jp-post-flair'},
		{'id'     : 'likes-other-gravatars'},
		{'id'     : 'nav-above'},
		{'id'     : 'nav-below'},
		{'id'     : 'postFooterGadgets'},
		{'id'     : 'sidebar'},
		{'id'     : 'sidebar-wrapper'},
		{'id'     : 'sidebar-wrapper1'}, # Yes, two `sidebar-wrapper` ids. Gah.
		{'id'     : 'site-navigation'},


	]

	stripTitle = [
		"Untuned Translation Blog:",
		'| Sousetsuka',
		'Skythewood translations:',
		"Translations From Outer Space:",
		"Translation Treasure Box:",
		'Imoutolicious Light Novel Translations:',
		"EC Webnovel:",
		'C.E. Light Novel Translations:',

	]


	# Grab all images, ignoring host domain
	allImages = True


	# def checkDomain(self, url):
	# 	return False

	# def crawl(self):
	# 	print('wat')


	# 	print(self.checkDomain('https://gekkahimethetranslation.wordpress.com/volume-2/chapter-2-little-one-eyed-princess/chapter-2-7/'))
	# 	print(self.checkDomain('https://gekkahimethetranslation.wordpress.com/volume-2/chapter-2-little-one-eyed-princess/chapter-2-11/'))

def test():

	# Scrape.buildScannedDomainSet()
	scrp = Scrape()
	scrp.crawl()
	# scrp.retreiveItemFromUrl(scrp.startUrl)


if __name__ == "__main__":
	test()




