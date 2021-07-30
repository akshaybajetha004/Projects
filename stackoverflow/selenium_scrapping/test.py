from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://stackoverflow.com/questions/49083680/how-are-the-new-tf-contrib-summary-summaries-in-tensorflow-evaluated')
# driver.get('https://stackoverflow.com/questions/54541969/tensorflow-compile-runs-for-a-long-time')
# driver.get('https://stackoverflow.com/questions/65446949/how-to-scrape-the-comments-using-selenium-and-python')
# driver.get('https://stackoverflow.com/questions/67919822/python-pupil-apriltags-problem-with-dll-path-could-not-find-module')
# driver.get('https://stackoverflow.com/questions/50546154/documenting-class-attributes-with-type-annotations')
# driver.get('https://stackoverflow.com/questions/8619879/javascript-calculate-the-day-of-the-year-1-366')
# driver.get('https://stackoverflow.com/questions/66520329/vue-v-html-directive-does-not-run-script-src-tags')
driver.get('https://stackoverflow.com/questions/843780/store-boolean-value-in-sqlite')
# for user table
# section = driver.find_elements_by_css_selector('.user-info')
# for sec in section:
#     try:
#         user_id = sec.find_element_by_css_selector('.user-details a').get_attribute('href').split("/")[4]
#         print(user_id)
#         username = sec.find_element_by_css_selector(' div.user-info div.user-details a').text
#         print(f'name= {username}')
#         reputation_score = sec.find_element_by_css_selector('.reputation-score').text
#         print(f'reputation_score= {reputation_score}')
#     except NoSuchElementException:
#         pass
#
#     try:
#         gold_badge = int(sec.find_element_by_css_selector('.badge1+ .badgecount').text)
#     except NoSuchElementException:
#         gold_badge = 0
#     print(f'gold batch= {gold_badge}')
#     try:
#         silver_badge = int(sec.find_element_by_css_selector('.badge2+ .badgecount').text)
#     except NoSuchElementException:
#         gold_badge = 0
#     print(f'silver batch= {silver_badge}')
#     try:
#         bronze_badge = int(sec.find_element_by_css_selector('.badge3+ .badgecount').text)
#     except NoSuchElementException:
#         gold_badge = 0
#     print(f'bronze batch= {bronze_badge}')

link = 'https://stackoverflow.com/questions/54541969/tensorflow-compile-runs-for-a-long-time'
# for question table
# question_id = driver.find_element_by_css_selector('#question-header .question-hyperlink').get_attribute('href').split("/")[4]
# print(f'question id = {question_id}')
# question = driver.find_element_by_css_selector('#question-header .question-hyperlink').text
# print(question)
# que_votes = driver.find_element_by_css_selector('#question .ai-center').text
# print(que_votes)
# # date_created = driver.find_element_by_css_selector('time').text
# date_created = driver.find_element_by_css_selector('.owner .relativetime').text
# print(date_created)
# views = driver.find_element_by_css_selector('.mb8~ .mb8+ .mb8').text.split(' ')[1]
# print(views)
# question_body = driver.find_element_by_css_selector('div.js-post-body').text
# print(f'question_body= {question_body}')
# active_date = driver.find_element_by_css_selector('.mb8 .s-link__inherit').text
# print(active_date)
try:
    answer_count = driver.find_element_by_css_selector('#answers-header .mb0').text.split(" ")[0]
    if answer_count == "":
        raise NoSuchElementException
except NoSuchElementException:
    answer_count = 0
print(f'answer count= {answer_count}')
# try:
#     question_link = driver.find_element_by_css_selector('#question .js-post-body a').get_attribute('href')
# except NoSuchElementException:
#     question_link = None
# print(question_link)
# question_user_id = driver.find_element_by_css_selector('.owner a').get_attribute('href').split('/')[4]
# print(question_user_id)
# print()


# for Answers table
if int(answer_count) > 0:
    answer_section = driver.find_elements_by_css_selector('.answer')
    for ans_sec in answer_section:
        answer_id = ans_sec.get_attribute('data-answerid')
        print(f'answer id = {answer_id}')
        ans_body = ans_sec.find_element_by_css_selector('#answers .js-post-body').text
        print(f'answer body = {ans_body}')
        ans_votes = ans_sec.find_element_by_css_selector('#answers .fd-column.ai-center').text
        print(f'ans_votes = {ans_votes}')
        date_created = ans_sec.find_element_by_css_selector('#answers .user-action-time > .relativetime').text
        print(f'date_created = {date_created}')
        question_id= link.split('/')[4]
        print(f'question_id={question_id}')
        acc = ans_sec.get_attribute("itemprop")
        if acc == "acceptedAnswer":
            acc = 1
            print('****accepted****')
        else:
            acc = 0


        answer_user_section = ans_sec.find_elements_by_css_selector('.user-details ')
        for sec in answer_user_section:
            answer_user = sec.get_attribute('itemprop')
            if answer_user == 'author':
                id = sec.find_element_by_css_selector('a').get_attribute('href').split('/')[4]
                print(f'answer_user_section= {id}')
            else:
                continue
        print()

# for comments table
# comment_count = driver.find_element_by_xpath('//*[@id="question"]/div[2]/span')
# print(comment_count)
# section = driver.find_elements_by_css_selector('.js-comments-list .comments')
# try:
#     load_more = driver.find_element_by_css_selector('js-show-link comments-link')
#     driver.execute_script("arguments[0].click();", load_more)
# except NoSuchElementException:
#     pass

# for load_link in driver.find_elements_by_css_selector('#question .comments-link'):
#     try:
#         driver.execute_script("arguments[0].click();", load_link)
#     except StaleElementReferenceException:
#         continue

# driver.find_element_by_link_text("").click()
# comment = driver.find_elements_by_css_selector('#question .js-post-comments-component')
# try:
#     load_more = driver.find_element_by_css_selector('js-show-link comments-link')
#     driver.execute_script("arguments[0].click();", load_more)
# except NoSuchElementException:
#     pass
# for com in comment:
#     data = com.find_elements_by_css_selector('li.comment')
#     for d in data:
#         ques_comment_id = d.get_attribute('data-comment-id')
#         print(f'ques_comment_id= {ques_comment_id}')
#         comment_body = WebDriverWait(d, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "comment-copy"))
#         ).text
#         # comment_body = d.find_element_by_class_name('comment-copy').text
#         print(f'comment_body= {comment_body}')
#         comment_user = WebDriverWait(d, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".comment-user"))
#         ).text
#         # comment_user = d.find_element_by_css_selector('.comment-user').text
#         print(f'comment_user = {comment_user}')
#         date_created = WebDriverWait(d, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, ".relativetime-clean"))
#         ).text
#         # date_created = d.find_element_by_css_selector('.relativetime-clean').get_attribute('title').split(' ')[0]
#         print(f'date_created = {date_created}')

# # for answer comments

# answer = driver.find_element_by_css_selector('#answers .js-comment-text-and-form').text

# answers = driver.find_element_by_css_selector('#answers #answers-header h2').text
# print(answers.split(" ")[0])

# for ans in answers:
#     ans_count = answers.find_element_by_css_selector('#answers-header ').text
#     print(ans_count)

# answers = driver.find_elements_by_css_selector('#answers .answer')
# for answer in answers:
#     try:
#         ans = answer.find_elements_by_class_name('comment')
#         for a in ans:
#             answer_id = answer.get_attribute('data-answerid')
#             print(f'answer_id = {answer_id}')
#             answer_comment_id = a.get_attribute('id').split('-')[1]
#             print(f'answer_comment_id = {answer_comment_id}')
#             comment_body = a.find_element_by_class_name('comment-copy').text
#             print(f'comment_body = {comment_body}')
#             answer_comment_user = a.find_element_by_css_selector('.comment-user').text
#             print(f'answer_comment_user= {answer_comment_user}')
#             date_created = a.find_element_by_css_selector('.relativetime-clean').get_attribute('title').split(' ')[0]
#             print(f'date_created = {date_created}')
#
#     except NoSuchElementException:
#         continue
    # ans = driver.find_elements_by_css_selector('.answer')
    # for a in ans:
    #     print(a.get_attribute('data-answerid'))

# for tags
# tags = driver.find_elements_by_css_selector('#question .ps-relative a')
# for tag in tags:
#     print(tag.text)
driver.close()


# line 92 no module find error