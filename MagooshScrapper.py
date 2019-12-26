# reddit.py
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,WebDriverException;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By

driverLocation = '/Users/himanshu/git/PaytmMovieScrapper/driver/chromedriver' #if windows
options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841');
#options.add_argument('headless')
driver = webdriver.Chrome(driverLocation,chrome_options=options)
baseUrl = 'https://gre.magoosh.com/login';
driver.get('https://gre.magoosh.com/login')

# login into the website

# //*[@id="session_login"]
#//*[@id="session_password"]

# step 1 login to the page
loginPage_username = driver.find_element_by_xpath('//*[@id="session_login"]');
loginPage_username.send_keys('december@greprep.33mail.com');
loginPage_password = driver.find_element_by_xpath('//*[@id="session_password"]');
loginPage_password.send_keys('magoosh@december')
loginbutton = driver.find_element_by_xpath('//*[@id="session_submit_action"]');
loginbutton.click();
# step 2 open all the question module
#/html/body/div[2]/div/div/div[2]/div[2]/div[2]/a
j = 30;
def startScrap(i):
    try:

        Practise_verbal = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/a');
        Practise_verbal.click();

        while(i<361) :
            i+=1;
            driver.implicitly_wait(2)
            #mark input
            crntUrl = driver.current_url
            QuestionNumber = crntUrl.split('/')[4]+".png";
            QuestionNumber = str(i)+"_"+QuestionNumber
            print(QuestionNumber);
            driver.save_screenshot('question_'+QuestionNumber)
            #//*[@id="answer_parts_val_input"]/div

            ##/*[@id="new_answer"]/div[4]/div/div/div[1]
            ##/html/body/div[1]/form/div[4]/div/div/div[1]
            #//*[@id="answer_parts_val_input"]/div
            #//*[@id="answer_parts_val_input"]/div/label[1]

            ##step 1 choose the option -- may have error in passagetype and others
            try:
                listele = driver.find_elements_by_xpath('//*[@id="answer_parts_val_input"]/div/label[1]')
                for list in listele :
                    list.click();

                if listele.__len__() == 0 :
                    clickOption = driver.find_element_by_xpath('html/body/div[1]/form/div[3]/div[1]/div/div/p[1]/label[1]/span/');
                    clickOption.click();
            except Exception :
                driver.save_screenshot('Error_'+QuestionNumber)
                print('Choosee option Manually..... you have ten second')
                driver.implicitly_wait(10);



            ##//*[@id="new_answer"]/div[4]/div[1]/button

            ## step 2 : click submit button

            try :

                try :
                    clickSubmit = driver.find_element_by_xpath('html/body/div[1]/form/div[5]/div[1]/button');
                    clickSubmit.click();
                except NoSuchElementException:
                    try:
                        clickSubmit = driver.find_element_by_xpath('html/body/div[1]/form/div[4]/div[1]/button');
                        clickSubmit.click();
                    except NoSuchElementException :
                        clickSubmit = driver.find_element_by_xpath('html/body/div[1]/form/div[3]/div[1]/div/div/p[1]/label[1]/span/');
                        clickSubmit.click();



                #        /html/body/div[1]/form/div[3]/div[1]/div/div/p[1]/label[1]

                driver.save_screenshot("Answer_"+QuestionNumber)
            except Exception :
                driver.save_screenshot('Error_'+QuestionNumber)
                print('Choosee Submit Button Manually..... you have ten second')
                driver.implicitly_wait(10);


            ## here specific error are mentioned so that loop won't start all over and get corrupted
            try :
                try :
                    clickNext = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div[1]/div[2]');
                    clickNext.click();
                except NoSuchElementException:
                    clickNext = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[4]/div[1]/div[2]');
                    clickNext.click();
            except NoSuchElementException :
                driver.save_screenshot('Error_'+QuestionNumber)
                print('Click Next Button Manually..... you have ten second')
                driver.implicitly_wait(10);





    except Exception:
        print('Still some Error-occurred, moving to start')
        driver.get('https://gre.magoosh.com/dashboard')
        startScrap(i);
startScrap(j);









# clickAnswer = driver.find_element_by_xpath('');
# clickAnswer.click();


#click submit
#//*[@id="new_answer"]/div[5]/div[1]/button




#next question
#//*[@id="edit_answer_330320073"]/div[5]/div[1]/div[2]/a


# fullhtml = driver.find_element_by_xpath('//*[@id="popular-movies"]'); ##//*[@id="popular-movies"]/div[1]/ul/ul[1]/li[1]/ div/ul/li[2]/a
# viewMoreHtml = fullhtml.find_element_by_xpath('./div[3]/span');
# viewMoreHtml.click();
# allMoviesHtml = fullhtml.find_element_by_xpath('./div[1]/ul')
# OuterSize =0
# try:
#     while(True) :
#         outerpath = './ul['+str(OuterSize+1)+']'
#         #print(outerpath)
#         OneLineMovie = allMoviesHtml.find_element_by_xpath(outerpath)
#         try:
#             InnerSize =0;
#             while(True):
#                 innerPath = './li[' +str(InnerSize+1) + ']';
#                 #print(innerPath)
#                 OneMovie = OneLineMovie.find_element_by_xpath(innerPath);
#                 href =  OneMovie.find_elements_by_partial_link_text('')
#                 href = OneMovie.find_element_by_xpath('./a').get_attribute('href');
#                 print(href);
#                 #gettign only one link have to improve it later..
#                 # href2 = OneMovie.find_element_by_xpath('//a[@href]')
#                 # for href3 in href2 :
#                 #     print(href3.get_attribute('href'))
#                 Movietitle = OneMovie.find_element_by_xpath('./a/div[2]').text; #jjfnd
#                 Movietitle= Movietitle.replace('\n', '_')
#                 Movielanguage = OneMovie.find_element_by_xpath('./a/div[2]/span').text;
#                 print(Movietitle)
#                 print('\n');
#                 #print(OneMovie.get_attribute('innerHTML'))
#                 #print(OneMovie.get_attribute('innerHTML'))
#                 InnerSize = InnerSize+1;
#         except NoSuchElementException:
#             #print('size of inner element is : ' + str(InnerSize));
#             pass
#         OuterSize = OuterSize+1;
# except NoSuchElementException:
#     #print('size of outer element is : ' + str(OuterSize));
#     pass;
# # allUl = allMoviesHtml.find_element_by_xpath('./ul')
# # allhref = {}
# # print(html)
# # size = AllMovieHtml.size;
# # for i in range(1,size[0]) :
# #     oneRowofMovies = AllMovieHtml.find_element_by_xpath('ul['+ i +']')
# #     rowSize = oneRowofMovies.size;
# #     for j in range(1,rowSize) :
# #         oneMovie = oneRowofMovies.find_element_by_xpath('/li['+j+']')
# #         print(oneMovie.get_attribute('innerHTML'))
# #print(len)
