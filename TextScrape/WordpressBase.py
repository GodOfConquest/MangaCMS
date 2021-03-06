
import TextScrape.SiteArchiver

class WordpressScrape(TextScrape.SiteArchiver.SiteArchiver):

	# Any url containing any of the words in the `badwords` list will be ignored.
	badwords = set([
				"r-login.wordpress.com",
				"/manga/",
				"/recruitment/",
				"wpmp_switcher=mobile",
				"account/begin_password_reset",
				"/comment-page-",

				# Why do people think they need a fucking comment system?
				'/?replytocom=',
				'#comments',
				'/comments/',

				# Mask out the PDFs
				"-online-pdf-viewer/",

				# Who the fuck shares shit like this anyways?
				"?share=",
				'wp-login.php',
				'public-api.wordpress.com',
				'xmlrpc.php',

				'.gravatar.com',
				'?openidserver=1',
				'/osd.xml',
				'pixel.wp.com',


				])

	decompose = [
		{'id'    : 'header'},
		{'class' : 'widget-area'},
		{'id'    : 'footer'},
		{'class' : 'photo-meta'},
		{'id'    : 'likes-other-gravatars'},
		{'id'    : 'sidebar'},
		{'id'    : 'carousel-reblog-box'},
		{'id'    : 'infinite-footer'},
		{'id'    : 'nav-above'},
		{'id'    : 'nav-below'},
		{'id'    : 'jp-post-flair'},
		{'id'    : 'comments'},
		{'id'    : 'colophon'},
		{'id'    : 'branding'},
		{'id'    : 'primary-sidebar'},
		{'id'    : 'search-container'},
		{'id'    : 'primary-navigation'},
		{'id'    : 'site-header'},
		{'class' : 'entry-utility'},
		{'class' : 'site-header'},
		{'class' : 'header-main'},
		{'class' : 'comments-link'},
		{'class' : 'breadcrumbs'},
		{'class' : 'screen-reader-text'},
		{'class' : 'menu-toggle'},

	]

	fileDomains = ['wp.com']

	decomposeBefore = [
		{'class' : 'comments'},
		{'class' : 'wpcnt'},
		{'id'    : 'comments'},
		{'class' : 'comments-area'},
		{'id'    : 'addthis-share'},
		{'id'    : 'info-bt'},
		{'id'    : 'jp-post-flair'},
		{'class' : 'wpcnt'},
		{'class' : 'bit'},
		{'id'    : 'bit'},
		{'id'    : 'infinite-footer'},
		{'name'  : "likes-master"},
		{'id'    : "wpstats"},
	]






