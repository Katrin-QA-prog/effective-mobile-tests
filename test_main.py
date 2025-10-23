from pages.main_page import MainPage

def test_about(page):
    main = MainPage(page)
    main.open_page()
    main.open_about()
    main.should_see_about()

def test_services(page):
    main = MainPage(page)
    main.open_page()
    main.open_services()
    main.should_see_services()

def test_projects(page):
    main = MainPage(page)
    main.open_page()
    main.open_projects()
    main.should_see_projects()

def test_reviews(page):
    main = MainPage(page)
    main.open_page()
    main.open_reviews()
    main.should_see_reviews()

def test_contacts(page):
    main = MainPage(page)
    main.open_page()
    main.open_contacts()
    main.should_see_contacts()
