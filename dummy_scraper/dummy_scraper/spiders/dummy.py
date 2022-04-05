
import scrapy

class DummySpider(scrapy.Spider):
    name = 'dummy'
    allowed_domains = ['sun-ruiheng.github.io']
    start_urls = ['https://sun-ruiheng.github.io/Dummy-Page/']

    def has_no_children(self, path):
        if path.xpath('.//*'):
            return False
        return True

    def dig_further(self, path):
        if self.has_no_children(path) and not path.xpath('.//text()'):
            # if path.xpath('.//text()') and path:
            #     # If current element has no children, it is at the lowest level, and I can now take its text value.
            #     self.overall_data += path.xpath('.//text()').get()
            # else:
            #     # If element exists but has no text() attribute, it is itself a text.

            self.overall_data += ' ' + path.get()
        


    def parse(self, response):

        self.overall_data = ''

        example_div = response.xpath('//ul')
        nodes = example_div.xpath('.//child::node()')
        for x in nodes:
            print("new: \n")
            print(x)
            # self.dig_further(x)
        for x in nodes:
            self.dig_further(x)
        

        print(self.overall_data)
