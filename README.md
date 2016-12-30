# get_website_html
a simple scrapy spider that gets a website url as an input, 
then visit every single page and store the html code of evety page in a html file locally
to run it you need to have python2 and scrapy installed.
to run it, open cmd-line, navigate to the project root (where the .cfg located), run this command

scrapy crawl get_html -a website_url="http://www.example.com/"

after the crawler is finished, the files will be stored in the project root dir
