from selenium.webdriver.common.by import By


class ListOrderLocators:
    # локатор кнопки "Лента Заказов"
    list_order_xpath = (By.XPATH, "(//p[text()='Лента Заказов'])")

    # локатор текста "Состав"
    compound_in_modal_window_xpath = (By.XPATH, "//p[text()='Cостав']")

    # Локатор текста номера заказа
    orders_in_work_xpath = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li")

    # Локатор заказа в списке заказов
    order_in_list_xpath = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")

    # Локатор количества "Выполнено за все время"
    count_all_orders_xpath = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[1]")

    # Локатор количества "Выполнено за сегодня"
    count_today_orders_xpath = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ')])[2]")
