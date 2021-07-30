from selenium import webdriver
from main import find_links
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from dbconnect import Database
import time
ques_links = find_links()

def scraping():

    # querydb = """CREATE TABLE User (
    #             user_id	TEXT PRIMARY KEY,
    #             user_name TEXT,
    #             reputation_score TEXT,
    #             gold_badge	TEXT,
    #             silver_badge TEXT,
    #             bronze_badge TEXT,
    #             )"""
    # objdb = Database(querydb)
    # objdb.execute()
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    for link in ques_links:
        # chrome_options = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)

        # 1 for user table
        section = driver.find_elements_by_css_selector('.user-info')
        for sec in section:
            try:
                user_id = sec.find_element_by_css_selector('.user-details a').get_attribute('href').split("/")[4]
                print(f'user_id ={user_id}')
                username = sec.find_element_by_css_selector(' div.user-info div.user-details a').text
                print(f'name= {username}')
                reputation_score = sec.find_element_by_css_selector('.reputation-score').text
                print(f'reputation_score= {reputation_score}')
            except NoSuchElementException:
                continue

            try:
                gold_badge = int(sec.find_element_by_css_selector('.badge1+ .badgecount').text)
            except NoSuchElementException:
                gold_badge = 0
            print(f'gold batch= {gold_badge}')
            try:
                silver_badge = int(sec.find_element_by_css_selector('.badge2+ .badgecount').text)
            except NoSuchElementException:
                silver_badge = 0
            print(f'silver batch= {silver_badge}')
            try:
                bronze_badge = int(sec.find_element_by_css_selector('.badge3+ .badgecount').text)
            except NoSuchElementException:
                bronze_badge = 0
            print(f'bronze batch= {bronze_badge}')

            query = "INSERT OR IGNORE INTO User VALUES(?,?,?,?,?,?);", (user_id,
                                                                         username,
                                                                         reputation_score,
                                                                         gold_badge,
                                                                         silver_badge,
                                                                         bronze_badge)
            obj = Database(query)
            obj.execute()

        # 2 for questions table
        try:
            question_id = driver.find_element_by_css_selector('#question-header .question-hyperlink').get_attribute('href').split("/")[4]
            print(f'question id = {question_id}')
            question = driver.find_element_by_css_selector('#question-header .question-hyperlink').text
            print(f'question = {question}')
            que_votes = driver.find_element_by_css_selector('#question .ai-center').text
            print(que_votes)
            # date_created = driver.find_element_by_css_selector('time').text
            date_created = driver.find_element_by_css_selector('.owner .relativetime').text
            print(f'date_created {date_created}')
            que_views = driver.find_element_by_css_selector('.mb8~ .mb8+ .mb8').text.split(' ')[1]
            print(f'views= {que_views}')
            question_body = driver.find_element_by_css_selector('div.js-post-body').text
            print(f'question_body= {question_body}')
            active_date = driver.find_element_by_css_selector('.mb8 .s-link__inherit').text
            print(f'active_date {active_date}')
            question_link = link
            print(f'question link = {question_link}')
            time.sleep(10)
            question_user_id = driver.find_element_by_css_selector('.owner a').get_attribute('href').split('/')[4]
            print(f'question_user_id= {question_user_id}')
            try:
                answer_count = driver.find_element_by_css_selector('#answers-header .mb0').text.split(" ")[0]
                if answer_count == "":
                    raise NoSuchElementException
            except NoSuchElementException:
                answer_count = 0
            print(f'answer count= {answer_count}')
        except NoSuchElementException:
            continue
        # try:
        #     answer_count = driver.find_element_by_css_selector('#answers-header .mb0').text.split(" ")[0]
        #     if answer_count == "":
        #         raise NoSuchElementException
        # except NoSuchElementException:
        #     answer_count = 0
        # print(f'answer count= {answer_count}')
        # question_link = link
        # print(f'question link = {question_link}')
        # time.sleep(10)
        # question_user_id = driver.find_element_by_css_selector('.owner a').get_attribute('href').split('/')[4]
        # print(f'question_user_id= {question_user_id}')
        query2 = "INSERT OR IGNORE INTO Questions VALUES(?,?,?,?,?,?,?,?,?);", (question_id,
                                                                                 question_user_id,
                                                                                 question_body,
                                                                                 date_created,
                                                                                 que_votes,
                                                                                 que_views,
                                                                                 active_date,
                                                                                 answer_count,
                                                                                 question_link
                                                                                 )
        obj2 = Database(query2)
        obj2.execute()

        # # 3 answer table

        if int(answer_count) > 0:
            answer_section = driver.find_elements_by_css_selector('.answer')
            for ans_sec in answer_section:
                try:
                    answer_id = ans_sec.get_attribute('data-answerid')
                    print(f'answer id = {answer_id}')
                    ans_body = ans_sec.find_element_by_css_selector('#answers .js-post-body').text
                    print(f'answer body = {ans_body}')
                    ans_votes = ans_sec.find_element_by_css_selector('#answers .fd-column.ai-center').text
                    print(f'ans_votes = {ans_votes}')
                    ans_date_created = ans_sec.find_element_by_css_selector('#answers .user-action-time > .relativetime').text
                    print(f'date_created = {ans_date_created}')
                    ans_question_id = link.split('/')[4]
                    print(f'ans_question_id={ans_question_id}')
                    ans_accepted = ans_sec.get_attribute("itemprop")
                    if ans_accepted == "acceptedAnswer":
                        ans_accepted = 1
                        print('****accepted****')
                    else:
                        print('*****not****')
                        ans_accepted = 0
                    answer_user_section = ans_sec.find_elements_by_css_selector('.user-details ')
                    for sec in answer_user_section:
                        answer_user = sec.get_attribute('itemprop')
                        if answer_user == 'author':
                            answer_user_id = sec.find_element_by_css_selector('a').get_attribute('href').split('/')[4]
                            print(f'answer_user_section= {answer_user_id}')
                        else:
                            continue
                    print()
                except NoSuchElementException:
                    continue
                query3 = "INSERT OR IGNORE INTO Answers VALUES(?,?,?,?,?,?,?);", (answer_id,
                                                                                   answer_user_id,
                                                                                   ans_question_id,
                                                                                   ans_body,
                                                                                   ans_votes,
                                                                                   ans_date_created,
                                                                                   ans_accepted
                                                                                   )
                obj3 = Database(query3)
                obj3.execute()

        # 4 question comments table

        comment = driver.find_elements_by_css_selector('#question .js-post-comments-component')
        try:
            load_more = driver.find_element_by_css_selector('js-show-link comments-link')
            driver.execute_script("arguments[0].click();", load_more)
        except NoSuchElementException:
            pass
        for com in comment:
            data = com.find_elements_by_css_selector('li.comment')
            for d in data:
                ques_comment_id = d.get_attribute('data-comment-id')
                print(ques_comment_id)
                comment_body = d.find_element_by_class_name('comment-copy').text
                print(comment_body)
                comment_user = d.find_element_by_css_selector('.comment-user').text
                print(comment_user)
                comment_date_created = d.find_element_by_css_selector('.relativetime-clean').get_attribute('title').split(' ')[
                    0]
                print(date_created)
                ques_question_id = link.split('/')[4]
                print(f'ans_question_id={ques_question_id}')

                query4 = "INSERT OR IGNORE INTO QuestionComments VALUES(?,?,?,?,?);", (ques_comment_id,
                                                                                        ques_question_id,
                                                                                        comment_body,
                                                                                        comment_user,
                                                                                        comment_date_created
                                                                                        )
                obj4 = Database(query4)
                obj4.execute()

        # 5 for answer_comment_section

        answers = driver.find_elements_by_css_selector('#answers .answer')
        for answer in answers:
            try:
                ans = answer.find_elements_by_class_name('comment')
                for a in ans:
                    ans_answer_id = answer.get_attribute('data-answerid')
                    print(f'ans_answer_id = {ans_answer_id}')
                    ans_comment_id = a.get_attribute('id').split('-')[1]
                    print(f'answer_comment_id = {ans_comment_id}')
                    ans_comment_body = a.find_element_by_class_name('comment-copy').text
                    print(f'ans_comment_body = {ans_comment_body}')
                    ans_comment_user = a.find_element_by_css_selector('.comment-user').text
                    print(f'answer_comment_user= {ans_comment_user}')
                    answer_date_created = \
                    a.find_element_by_css_selector('.relativetime-clean').get_attribute('title').split(' ')[0]
                    print(f'date_created = {answer_date_created}')

                    query5 = "INSERT OR IGNORE INTO AnswerComments VALUES(?,?,?,?,?);", (ans_comment_id,
                                                                                          ans_answer_id,
                                                                                          ans_comment_body,
                                                                                          ans_comment_user,
                                                                                          answer_date_created
                                                                                          )
                    obj5 = Database(query5)
                    obj5.execute()
            except NoSuchElementException:
                continue



        #  6 for tags

        tags = driver.find_elements_by_css_selector('#question .ps-relative a')
        for tag in tags:
            tag_question_id = link.split('/')[4]
            print(tag_question_id)
            ta = tag.text
            print(ta)
            query6 = "INSERT OR IGNORE INTO Mapping VALUES(?,?);", (tag_question_id,
                                                                     ta)
            obj6 = Database(query6)
            obj6.execute()


# if ques_links is not None:
scraping()
