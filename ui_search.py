import time

from playwright.sync_api import Page, expect


def test_BoozAllen(page: Page):
    page.goto("https://careers.boozallen.com/jobs/search")
    assert "Jobs at Booz Allen" in page.title()
    page.get_by_role("button").get_by_text("Accept Cookies").click()
    page.get_by_placeholder("Keywords").fill("Test")
    page.get_by_placeholder("Country").fill("USA")
    page.get_by_placeholder("Clearance Type").click()
    page.locator("#li195100").get_by_text("NA").click()
    page.locator("#li3582").get_by_text("None").click()
    page.locator("#li2552552").get_by_text("Public Trust").click()
    page.get_by_placeholder("Remote Work").click()
    page.locator("#li9148446").get_by_text("Yes").click()
    page.get_by_role("button").get_by_text("Search").click()
    print("")  # Just to see prettier output
    print("_______________________________________________________")
    print("Booz Allen")
    for index in range(page.locator("//tbody/tr").count()):
        row = page.locator("//tbody/tr").nth(index)
        if row.filter(has_text="Tester").count() > 0:
            positionName = row.locator("td").nth(0).inner_text() # Get the first column text
            # whenever we have f at the beginning everything inside {} will be treated as variable and will be executed at runtime
            print(f"{positionName}")
    print("_______________________________________________________")

def test_FannieMae(page: Page):
    page.goto("https://www.fanniemae.com/careers/search-all-jobs")
    assert "Search All Jobs | Fannie Mae" in page.title()
    page.locator(".srSearchInput").fill("Test")
    page.locator("//label[@class='srFilterRemoteElementText']").click()
    page.locator("//input[@class='srSearchButton']").click()
    print("")  # Just to see prettier output
    print("_______________________________________________________")
    print("Fannie Mae")
    for index in range(page.locator("//tbody/tr").count()):
        row = page.locator("//tbody/tr").nth(index)
        if row.filter(has_text="Test").count() > 0 and row.filter(has_text="(Open to Remote)").count() > 0:
            positionName = row.inner_text()
            print(f"{positionName}")
    print("_______________________________________________________")
    time.sleep(1)


def test_AmericanRedCross(page: Page):
    page.goto("https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers")
    expect(page.locator(".css-1uwu54i")).to_contain_text("American Red Cross")
    page.locator("//button[@class='css-1iv5pxv']").get_by_text("Time Type").click()
    page.locator(".css-1ew7hmu").get_by_text("Full time").click()
    page.locator(".css-1iv5pxv").get_by_text("Remote Type").click()
    page.locator(".css-1ew7hmu").get_by_text("Fully Remote - Eastern Time Zone schedule").click()
    page.locator(".css-1ew7hmu").get_by_text("Fully Remote anywhere in the USA").click()
    page.locator(".css-1ew7hmu").get_by_text("Fully Remote Near Primary Location").click()
    page.locator(".css-wxxug7").click()
    print("")  # Just to see prettier output
    print("_______________________________________________________")
    print("American Red Cross")
    for index in range(page.locator(".css-1q2dra3").count()):
        position = page.locator(".css-19uc56f").nth(index)
        if position.filter(has_text="Quality Assurance Engineering").count() > 0:
            positionName = position.inner_text()
            print(f"{positionName}")
    print("_______________________________________________________")
    time.sleep(1)

def test_saic(page: Page):
    page.goto("https://jobs.saic.com/search/engineering-and-sciences-information-technology-software-remote/jobs?q=Software+Tester")
    expect(page.locator("//div[@class='jobs-category-section']/div/div/h1")).to_contain_text("Software Tester jobs found")
    print("")  # Just to see prettier output
    print("_______________________________________________________")
    print("SAIC")
    for index in range(page.locator("//div[@class='jobs-section__list']/div/div/div/h5").count()):
        position = page.locator("//div[@class='jobs-section__list']/div/div/div/h5/a").nth(index)
        datePosted=page.locator("//div[@class='jobs-section__list']/div/div/div[3]").nth(index)
        if position.filter(has_text="SOFTWARE TESTER").count() > 0:
            positionName = position.inner_text()
            print(f"{positionName} - {datePosted}")
    if page.locator("//div[@class='pagination']/a").get_by_text("2").is_visible():
        print("Check additional page manually!")
    print("_______________________________________________________")

    # time.sleep(7)

def test_CareFirst(page: Page):
    page.goto("https://carefirstcareers.ttcportals.com/jobs/search?q=SDET&per_page=15")
    assert "CareFirst - Careers" in page.title()
    print("_______________________________________________________")
    print("Care First")
    # print(page.locator("//div[@class='jobs-section__item']:visible").count())
    for index in range(page.locator("//div[@class='jobs-section__item']").count()):
        row = page.locator("//div[@class='jobs-section__item']/div/div/h2").nth(index)
        if row.filter(has_text="Test Engineer").count() > 0 and row.filter(has_text="Remote").count() > 0:
            positionName = row.inner_text()  # Get the first column text
            jobId = page.locator("//div[@class='jobs-section__item']/div/div[2]").nth(index).text_content()
            # jobId=jobId.split(&)
            # whenever we have f at the beginning everything inside {} will be treated as variable and will be executed at runtime
            print(f"{positionName} {jobId}")

    print("_______________________________________________________")

def test_Discover(page: Page):
    page.goto("https://jobs.discover.com/job-search/?department=Information+Technology&page=0&location=&keyword=Quality+Engineer&remoteOnly=true")
    assert "Job search | Discover Careers" in page.title()
    print (page.locator("//div[@id='job-search-results']/div").count())

    page.wait_for_selector("//div[@id='job-search-results']/div", timeout=5000)

    for index in range(page.locator("//div[@id='job-search-results']/div").count()):
        row = page.locator("//div[@id='job-search-results']/div/h3").nth(index)
        if row.filter(has_text="Engineer (Quality)").count() > 0 :
            positionName = row.inner_text()  # Get the first column text
            print(f"{positionName}")

    print("_______________________________________________________")

# def test_Humana(page: Page):
#     page.goto("https://careers.humana.com/us/en/search-results?keywords=Software%20development%20Engineer%20in%20test")
#     assert "Software development Engineer in test job openings at Humana" in page.title()
#     page.get_by_text("Technology and Digital Analytics ").click()
#     # page.locator("//*[@id='RemoteJobAccordion']/span[1]").click()
#     # page.locator("//input[@id='isRemote_phs_Yes22']").click()
#     for index in range(page.locator("//div[@class='phw-grid-1 phw-content-block phw-grid phw-grid-lg-1 phw-gap-0']/div").count()):
#         row = page.locator("//div[@class='phw-card-block phw-posn-relative _jw-card-block_1l0xa_2 phw-stroke-bottom-dark phw-g-card-bg-secondary']/div/div/div").nth(index)
#
#         text = row.inner_text()
#
#         # Print only if conditions are met
#         if "Security" in text and "Remote Job : Yes" in text:
#             print("Ololo")
#
#
#     time.sleep(6)