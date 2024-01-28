from utils.plywright_utils import PlaywrightUtils


class HomePage(PlaywrightUtils):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    TEXT_INPUT = "//textarea[@name='q']"

    def navigate_to_home(self, test_browser_url):
        self.page.goto(test_browser_url)

    def enter_input(self):
        self.fill_input(self.TEXT_INPUT, "playwright")
        self.press_key("Enter")
        self.page.wait_for_load_state("load")
        self.page.wait_for_timeout(5000)
        print(self.page.url)
        search_results_title = self.get_page_title()
        return search_results_title

    def perform_search(self, query):
        self.page.fill(self.TEXT_INPUT, query)
        self.page.press(self.TEXT_INPUT, 'Enter')

    def click_search_result(self, result_index):
        selector = f'//h3[{result_index + 1}]'
        self.page.click(selector)

    # Add other methods as needed
