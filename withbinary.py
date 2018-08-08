# reddit.py
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driverLocation = '/Users/himanshu/Coding Stuff/PYcharm file/chituuudemo/driver/chromedriver' #if windows
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841');
#options.add_argument('headless')
driver = webdriver.Chrome(driverLocation,chrome_options=options)
baseUrl = 'https://paytm.com/';
driver.get('https://paytm.com/movies/pune')
fullhtml = driver.find_element_by_xpath('//*[@id="popular-movies"]'); ##//*[@id="popular-movies"]/div[1]/ul/ul[1]/li[1]/ div/ul/li[2]/a
viewMoreHtml = fullhtml.find_element_by_xpath('./div[3]/span');
viewMoreHtml.click();
allMoviesHtml = fullhtml.find_element_by_xpath('./div[1]/ul')
OuterSize =0
try:
    while(True) :
        outerpath = './ul['+str(OuterSize+1)+']'
        #print(outerpath)
        OneLineMovie = allMoviesHtml.find_element_by_xpath(outerpath)
        try:
            InnerSize =0;
            while(True):
                innerPath = './li[' +str(InnerSize+1) + ']';
                #print(innerPath)
                OneMovie = OneLineMovie.find_element_by_xpath(innerPath);
                href =  OneMovie.find_elements_by_partial_link_text('')
                href = OneMovie.find_element_by_xpath('./a').get_attribute('href');
                print(href);
                #gettign only one link have to improve it later..
                # href2 = OneMovie.find_element_by_xpath('//a[@href]')
                # for href3 in href2 :
                #     print(href3.get_attribute('href'))
                Movietitle = OneMovie.find_element_by_xpath('./a/div[2]').text; #jjfnd
                Movietitle= Movietitle.replace('\n', '_')
                Movielanguage = OneMovie.find_element_by_xpath('./a/div[2]/span').text;
                print(Movietitle)
                print('\n');
                #print(OneMovie.get_attribute('innerHTML'))
                #print(OneMovie.get_attribute('innerHTML'))
                InnerSize = InnerSize+1;
        except NoSuchElementException:
            #print('size of inner element is : ' + str(InnerSize));
            pass
        OuterSize = OuterSize+1;
except NoSuchElementException:
    #print('size of outer element is : ' + str(OuterSize));
    pass;
# allUl = allMoviesHtml.find_element_by_xpath('./ul')
# allhref = {}
# print(html)
# size = AllMovieHtml.size;
# for i in range(1,size[0]) :
#     oneRowofMovies = AllMovieHtml.find_element_by_xpath('ul['+ i +']')
#     rowSize = oneRowofMovies.size;
#     for j in range(1,rowSize) :
#         oneMovie = oneRowofMovies.find_element_by_xpath('/li['+j+']')
#         print(oneMovie.get_attribute('innerHTML'))
#print(len)
driver.quit()
