from selenium import webdriver
from time import sleep as sl
from selenium.webdriver.chrome.options import Options

class crawler:
    def __init__(self):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.__drivrer=webdriver.Chrome(chrome_options=chrome_options)
        self.__information="dcard Linebot v1"

    @property
    def information(self):
        return self.__information
    
    def get_forumList(self):
        forumlist = []
        with open("forum.csv",'r',encoding='utf-8') as f:
            for line in f.readlines():
                if line == '\n':
                    continue
                forumlist.append(line)
        return forumlist
    def __close(self):
        sl(0.5)
        self.__drivrer.close()
    def crawl_specific_forum(self,name):
        forumlist=self.get_forumList()
        for i in forumlist:
            if i.split(",")[0] in name:
                link = i.split(",")[1]
                break
        else:
            self.__close()
            return "無此看板"
        self.__drivrer.get(link)
        sl(0.5)
        r_list=self.__drivrer.find_elements_by_xpath('//*[@id="__next"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div')
        xStr=""
        for artical in r_list:
            try:
                title = artical.find_element_by_xpath('./article/h2/a/span').text
                href = artical.find_element_by_xpath('./article/h2/a').get_attribute('href')
                motion =artical.find_element_by_xpath('./article/div[4]/div[1]/div/div[2]').tect
                response =artical.find_element_by_xpath('./article/div[4]/div[2]/span[2]').text
                xStr += '\n'.join([title,href,motion,response])
            except Exception as e:
                pass
        self.__close()
        return xStr
x = crawler()
x.crawl_specific_forum('dfsdaf')

