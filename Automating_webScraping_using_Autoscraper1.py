from autoscraper import AutoScraper

url = 'https://www.skillshare.com/profile/Emma-Gannon/9502115'

#we can add one or multiple candidate here
# you can also put urls here to retrieve urls.

wanted_list = ['Emma Gannon','emmagannon.co.uk/']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)

result1 = scraper.get_result_similar('https://github.com/Tusharroul?tab=repositories', grouped=True)
print(result1)

scraper.set_rule_aliases({'rule_ymkf' : 'Type', 'rule_7vq5' : 'Title'})
scraper.keep_rules(['rule_ymkf', 'rule_7vq5'])
scraper.save('github-repository-search')

scraper.load('github-repository-search')

#if I want to get the similar result from other website then
result2 = scraper.get_result_similar("https://github.com/abhi1thakur?tab=repositories", group_by_alias=True)

print(result2)