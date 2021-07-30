from selenium import webdriver

question_links = []


def find_links():
    # proxy = "102.164.252.175:8080"
    tag = input("Enter tag ")
    pages = 1
    # while(True):
    #     print('''1. for 15 questions per page
    # 2. for 30 questions per page
    # 3. for 50 questions per page\n''')
    #     choice = input()
    # pagesize = int(input("Enter pagesize "))
    # chrome_options.add_argument('--proxy-server=%s' % proxy)
    # driver.get(f'https://stackoverflow.com/questions/tagged/{tag}?tab=unanswered&page={page}&pagesize=15')

    file1 = open("all_tags.txt", "r")
    readfile = file1.read()
    if tag in readfile:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)
        # for scrapping all the searched tag link
        # question_links = []
        for page in range(1, pages + 1):
            driver.get(f'https://stackoverflow.com/questions/tagged/{tag}?tab=unanswered&page={page}&pagesize=15')

            links = driver.find_elements_by_css_selector('#questions .question-hyperlink')
            for link in links:
                # all_links.append(link)
                question_links.append(link.get_attribute('href'))
        print(question_links)
        print(len(question_links))
        driver.close()
        return question_links
    else:
        print(f'Tag {tag} Not Found')



