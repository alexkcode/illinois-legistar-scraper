import scrapy
from urllib import urlencode

class CookCountySpider(scrapy.Spider):
  name = "cook-county.legistar"

  def start_requests(self):
    return scrapy.Request(url='https://cook-county.legistar.com/Calendar.aspx', 
                          callback=self.parse)

  def create_meeting_request(self, id, guid):
    params = {
      "id": id,
      "guid": guid,
      "options": "info"
    }

    ajax_template = "https://cook-county.legistar.com/MeetingDetail.aspx?" + urlencode(params)

    return scrapy.Request(url=ajax_template, callback=self.parse)
  
  def parse(self, response):
    response_data = scrapy.Selector(text=response.body)

    
