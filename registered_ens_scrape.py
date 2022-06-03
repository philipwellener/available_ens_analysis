# run with
# scrapy runspider registered_ens_scrape.py -o -:csv > registered_ens.csv 2> TRACE

from scrapy import Request
from scrapy.spiders import Spider
# from scrapy.selector import Selector

class Crypto(Spider):
    name = 'ens'
    handle_httpstatus_list = [404, 403]
    allowed_domains = ['ens.tools']

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'DOWNLOADER_CLIENT_TLS_METHOD' : 'TLSv1.2',
        'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }

    def start_requests(self):
        yield Request("https://ens.tools/domains?perPage=250&showFilters=true&expiration=registered", callback=self.parse)
        number_of_pages = 4713
        for i in range(2,number_of_pages+1):
            yield Request("https://ens.tools/domains?perPage=250&showFilters=true&expiration=registered&page={0}".format(i),callback=self.parse)
    

    def parse(self, response):
        rows = response.xpath('//tr')[1:]
        ans=[]
        for row in rows:
            item = {}
            item['domain'] = row.xpath('./td[3]/div/a[1]/text()[1]').extract()[0].strip()
            ans.append(item)

        return ans