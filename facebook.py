def fb_all_posts(list_of_home_page_urls, username, password, num_posts):
    from datetime import datetime
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    # getting rid of chrome problems
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2
    })
    # Using Chrome to access web
    driver = webdriver.Chrome(options=option, executable_path=r'D:\chromedriver.exe')
    
    # Open the website
    driver.get('https://www.facebook.com/login/')

    ## logging in
    # attempting to input email 
    driver.find_element(By.ID, ("email")).send_keys(username)
    sleep(5)
    # attempting to input password
    driver.find_element(By.ID, ("pass")).send_keys(password)
    sleep(5)

    driver.minimize_window()
    # setting up post list
    posts = []

    for website in list_of_home_page_urls:
        # getting posts page
        website = website.split('.com')[1]
        website = "https://www.facebook.com/pg{}posts/?ref=page_internal".format(website)
        driver.get(website)
        page = driver.find_element_by_xpath('//*[@id="seo_h1_tag"]/a/span').text
        # getting the data for each post
        for _ in range(2, num_posts):
            temp = {}        
            temp['page'] = page
            # formatting where each post is
            post = "//*[@class='_1xnd']/div[{}]".format(_)

            # getting the link for the post
            link = driver.find_element_by_xpath(post + '//*[@data-testid="story-subtitle"]/span/span/a').get_attribute('href')
            temp['link'] = link
            # gets the date 
            date = driver.find_element_by_xpath(post + '//abbr').get_attribute('TITLE')
            # reformats the date into my liking
            date = datetime.strptime(date, "%A, %B %d, %Y at %I:%M %p")
            temp['datetime_obj'] = date
            temp['date'] = date.strftime("%B %d, %Y at %I:%M %p")

            # attempts to get text content
            try:
                temp['text_content'] = driver.find_element_by_xpath(post + '//*[@data-testid="post_message"]').text
            except:
                temp['text_content'] = 'None'


            # adding the post to posts
            posts.append(temp)
    return posts
        