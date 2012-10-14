routes_in = (
             (r'.*:/sitemap.xml', r'/init/default/sitemap'),
             (r'.*:/robots.txt', r'/init/default/robots')
)


routes_onerror = [(r'*/404', r'/init/default/index')] #Change to 404 page
