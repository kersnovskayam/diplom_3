class PersonalCabinetLocators:

    # Локатор текст-кнопки "Восстановить пароль"
    recover_password_xpath = "//a[contains(text(),'Восстановить пароль')]"

    # локатор кнопки "Скрыть/Показать пароль"
    hide_password_xpath = "//*[name()='path' and contains(@d,'M12 4C14.0')]"

    # Поле ввода email на экране восстановления пароля
    recovery_email_input_xpath = "//label[text()='Email']/following-sibling::input"

    # локатор кнопки восстановить
    recovery_button_xpath = "(//button[text()='Восстановить'])"

    # локатор поля email, авторизация и регистрация
    email_recovery_xpath = "//label[text()='Email']/following-sibling::input"

    # локатор поля пароль, авторизация и регистрация
    password_recovery_xpath = "//label[text()='Пароль']/following-sibling::input"

    # локатор кнопки войти
    input_button_xpath = "(//button[text()='Войти'])"

    # текст кнопка История заказов
    orders_history = "//a[contains(text(),'История заказов')]"

    number_order_in_history_orders = "//p[@class='text text_type_digits-default']"

    # локатор кнопки выход
    logout_xpath = "(//button[text()='Выход'])"
