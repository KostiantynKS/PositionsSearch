from playwright.sync_api import Playwright, sync_playwright

leidosPayloadData = {
    "appliedFacets": {
        "locations": ["4d3806f19fb4100117214c80588f0000"],
        "jobFamilyGroup": ["96064918a76d1023f1586f686a4d6d3c"]
    },
    "limit": 20,
    "offset": 0,
    "searchText": ""
}

def test_positions_leidos(playwright: Playwright):
    # Playwright API request context
    api_request_context = playwright.request.new_context()

    response = api_request_context.post(
        "https://leidos.wd5.myworkdayjobs.com/wday/cxs/leidos/External/jobs",
        headers={"Content-Type": "application/json"},
        data=leidosPayloadData  # Playwright uses `data=` instead of `json=`
    )

    print("Status Code:", response.status)
    data=response.json()
    for job in data["jobPostings"]:
        title = job["title"]
        if "Test" in title:
            print(title)

    # try:
    #     print("Response JSON:", response.json())
    # except Exception:
    #     print("Response Text:", response.text())


with sync_playwright() as playwright:
    test_positions_leidos(playwright)