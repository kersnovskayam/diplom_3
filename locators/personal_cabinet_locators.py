from selenium.webdriver.common.by import By


class PersonalCabinetLocators:
    # локатор кнопки Личный Кабинет
    personal_cabinet_xpath = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    # Локатор текст-кнопки "Восстановить пароль"
    recover_password_xpath = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # локатор кнопки "Скрыть/Показать пароль"
    hide_password_xpath = (By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]")

    # Поле ввода email на экране восстановления пароля
    recovery_email_input_xpath = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # локатор кнопки восстановить
    recovery_button_xpath = (By.XPATH, "(//button[text()='Восстановить'])")

    # локатор поля email, авторизация и регистрация
    email_recovery_xpath = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # локатор поля пароль, авторизация и регистрация
    password_recovery_xpath = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

    # локатор кнопки войти
    input_button_xpath = (By.XPATH, "(//button[text()='Войти'])")

    # текст кнопка История заказов
    orders_history = (By.XPATH, "//a[contains(text(),'История заказов')]")

    number_order_in_history_orders = (By.XPATH, "//p[@class='text text_type_digits-default']")

    # локатор кнопки выход
    logout_xpath = (By.XPATH, "(//button[text()='Выход'])")
