#Author:- Kushal Dhungana
import scrapy

#Class for creating spider and parsing the website
class unjobsSpider(scrapy.Spider):
    name = 'unjobs_spider'
    start_urls = ['https://unjobs.org/']
    #Function for parsing the response file
    def parse(self, response):
        JOB_SELECTOR = 'div.job'
        for unjobs in response.css(JOB_SELECTOR):
            yield {
                'Jobtitle': unjobs.css('.jtitle::text').extract(),
                'Link': unjobs.css('a ::attr(href)').extract(),
                'company': unjobs.css('::text')[1].extract(),
                'Updateddatetime': unjobs.css('time ::attr(datetime)').extract()
            }
        #This is used to extract the data from next page until there is no furtherScrapy==1.8.0 next page
        NEXT_PAGE_SELECTOR = '.nc+ .nv a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page),callback=self.parse)
