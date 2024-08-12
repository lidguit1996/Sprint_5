from selenium.webdriver.common.by import By


class SellaBurgersLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # кнопка "Личный Кабинет"
    REGISTRATION_LINK = (By.LINK_TEXT, "Зарегистрироваться") # кнопка "Зарегистрироваться" в окне входа

    REGISTRATION_NAME_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input") # поле ввода имени в окне регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input") # поле ввода электронной почты в окне регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]/div/div/input") # поле ввода пароля в окне регистрации

    REGISTRATION_BUTTON = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка "Зарегистрироваться" в окне регистрации

    PASSWORD_ERROR = (By.XPATH, ".//p[@class = 'input__error text_type_main-default']") # сообщение об ошибке, возникающее при вводе невалидного пароля при регистрации

    LOGIN_BUTTON_IN_MAIN_PAGE = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") #кнопка "Войти в аккаунт" на главной странице

    LOGIN_EMAIL_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']") # поле ввода электронной почты в окне входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']") # поле ввода почты в окне входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # поле ввода пароля в окне входа

    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # кнопка "Оформить заказ" в личном кабинете

    LOGIN_LINK_IN_REGISTRATION_WINDOW = (By.LINK_TEXT, "Войти")  # кнопка "Войти" в окне регистрации
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль") # кнопка "Восстановить пароль" в окне входа

    LOGIN_LINK_IN_FORGOT_PASSWORD_WINDOW = (By.LINK_TEXT, "Войти") # кнопка "Войти" в окне восстановления пароля
    LOGAUT_BUTTON = (By.XPATH, ".//button[@class = 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']") # кнопка выхода из личного кабинета

    SAUCES_LIST = (By.XPATH, ".//h2[2][@class = 'text text_type_main-medium mb-6 mt-10']") # раздел соусы в конструкторе бургеров
    GALACTIC_SAUCE = (By.XPATH, ".//img[@alt = 'Соус традиционный галактический']") # иконка галактического соуса

    TOPPINGS_LIST = (By.XPATH, ".//h2[3][@class = 'text text_type_main-medium mb-6 mt-10']") # раздел начинок в конструкторе
    BEAF_METEOR = (By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")  # иконка выбора говяжьего метеорита

    BREAD_LIST = (By.XPATH, ".//h2[1][@class = 'text text_type_main-medium mb-6 mt-10']") # раздел булок в конструкторе
    CRATER_BREAD = (By.XPATH, ".//img[@alt = 'Краторная булка N-200i']") # иконка выбора краторной булки





