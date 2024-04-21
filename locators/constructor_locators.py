from selenium.webdriver.common.by import By

class ConstructorLocators:
    # локатор кнопки "Конструктор"
    constructor_xpath = (By.XPATH, "(//p[text()='Конструктор'])")

    # локатор ингридиента "Флюоресцентная булка R2-D3"
    fluorescent_bun = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    # Локатор конструкторв
    constructor_create_burger_locators_xpath = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")

    # Локатор кнопки "закрыть" в модальном окне заказа
    close_button_xpath = (By.XPATH, "(//*[name()='svg'])[25]")

    # Локатор ингридиента в конструкторе
    constructor_create_order_locators_xpath = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']")

    # Локатор цены заказа в конструкторе
    price_burger_constructor = (By.XPATH, "//p[@class='text text_type_digits-medium mr-3']")

    # Локатор кнопки "Оформить заказ"
    create_order_xpath = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")

    # Локатор успешного заказа
    successfully_order_text_xpath = (By.XPATH, "(//p[text()='Ваш заказ начали готовить'])")

    # Локатор текста ингридиента
    fluorescent_bun_text_xpath = (By.XPATH, "(// p[text() = 'Флюоресцентная булка R2-D3'])")

    # Локатор кнопки номера заказа
    count_order_xpath = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'Modal_modal__title__2L34m')]")

    # Локатор кнопки закрыть заказа
    close_order_button_xpath = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']")
