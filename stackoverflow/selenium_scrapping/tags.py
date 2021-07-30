from selenium import webdriver

proxy = "202.142.174.10:8080"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://stackoverflow.com/tags?page=1&tab=popular')

# total_pages = driver.find_element_by_css_selector(".s-pagination--item__clear+ .js-pagination-item").text
# print(total_pages)
# tags = driver.find_elements_by_css_selector(".post-tag")
# for tag in tags:
#     print(tag.text)
#     print()

total_pages = driver.find_element_by_css_selector(".s-pagination--item__clear+ .js-pagination-item").text
openfile = open('all_tags.txt', 'w')
for page in range(1, int(total_pages)):
    driver.get(f'https://stackoverflow.com/tags?page={page}&tab=popular')
    tags = driver.find_elements_by_css_selector(".post-tag")
    for tag in tags:
        print(tag.text)
        openfile.write(tag.text)
        openfile.write(',')
        print()


openfile.close()
