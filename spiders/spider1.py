import scrapy
#import the package here.

class BootStrap(scrapy.Spider): #inherit the class to access its fxn.
    name = 'boot'  #this attribute define name of your spider.
    start_urls = [
        'https://getbootstrap.com/docs/4.4/getting-started/introduction/',
        'https://getbootstrap.com/docs/4.4/getting-started/download/',
        'https://getbootstrap.com/docs/4.4/getting-started/contents/',
    ] #list of url from where we will extract oyur content.
    def parse(self, response): #this fxn. create a response object.
        splited_url = response.url.split('/')[-2]#in this variable the split list of url is stored which help us to give the file name
        #here the url of response object is splited and second last index of list is taken & store in splited_url variable
        #[-2] take second last index fom list(i.e contents)
        #if we not use [-2] it show all list ['https:', '', 'getbootstrap.com', 'docs', '4.4', 'getting-started', 'contents', ''] during creating the name of the file.
        #if we use response.url[-2 then ]the file name we get will be data-contents if we not use split then the name is took from url.
        #using split('/') https://getbootstrap.com/docs/4.4/getting-started/introduction/ the usrl is break from  / here & create the list.
        #if we donnot use split[-2] then no file is created.
        ex = response.css('code').getall()# extract code data from the site.
        file = 'data-%s.html' % splited_url #create a variable which create a file. splited_url values is passed to %s in the string.
        # we can also use file = 'data-{}.html'.format(splited_url) or file = f'data-{splited_url}.html'
        with open(file, 'wb') as f: #open our file and create its object. 'wb' write the extract content over the file.
            f.write(response.body) #here we write the html code of page in the file.
            #self.log('saved fil %s' % file)
            
#we have three link so parse method will call 3 time for different links
#open terminal & type scrapy shell "http://quotes.toscrape.com/page/1/"
#we can use select tag with css using response object...response.css('h1')=this provide the selector list of h1 tag.
# response.css('h1::text').getall() / extract() = provide the text of title tag & store as list. if we use get() then it provide string.
#we can also use xpath selector for extracting data:
#response.xpath('//h1').getall() = provide all h1 tag, very powerfull selector.

#one top level directory of scrapy package into your terminal & type scrapy crawl boot & your file will be created.
