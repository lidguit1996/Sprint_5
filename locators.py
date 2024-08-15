from selenium.webdriver.common.by import By


class SellaBurgersLocators:
    ACCOUNT_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # кнопка "Личный Кабинет"
    REGISTRATION_LINK = (By.LINK_TEXT, "Зарегистрироваться") # кнопка "Зарегистрироваться" в окне входа

    REGISTRATION_NAME_FIELD = (By.XPATH, ".//label[contains(text(),'Имя')]/parent::div/input") # поле ввода имени в окне регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//label[contains(text(),'Email')]/parent::div/input") # поле ввода электронной почты в окне регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, ".//input[@type = 'password']") # поле ввода пароля в окне регистрации

    REGISTRATION_BUTTON = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]") # кнопка "Зарегистрироваться" в окне регистрации

    PASSWORD_ERROR = (By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]") # сообщение об ошибке, возникающее при вводе невалидного пароля при регистрации

    LOGIN_BUTTON_IN_MAIN_PAGE = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]") #кнопка "Войти в аккаунт" на главной странице

    LOGIN_EMAIL_FIELD = (By.XPATH, ".//input[@name = 'name']") # поле ввода электронной почты в окне входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//input[@name = 'Пароль']") # поле ввода почты в окне входа
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]") # поле ввода пароля в окне входа

    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]") # кнопка "Оформить заказ" в личном кабинете

    LOGIN_LINK_IN_REGISTRATION_WINDOW = (By.LINK_TEXT, "Войти")  # кнопка "Войти" в окне регистрации
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль") # кнопка "Восстановить пароль" в окне входа

    LOGIN_LINK_IN_FORGOT_PASSWORD_WINDOW = (By.LINK_TEXT, "Войти") # кнопка "Войти" в окне восстановления пароля
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]") # кнопка выхода из личного кабинета

    SAUCES_LIST = (By.XPATH, ".//h2[contains(text(), 'Соусы')]") # раздел соусы в конструкторе бургеров
    GALACTIC_SAUCE = (By.XPATH, ".//img[@alt = 'Соус традиционный галактический']") # иконка галактического соуса

    TOPPINGS_LIST = (By.XPATH, ".//h2[contains(text(), 'Начинки')]") # раздел начинок в конструкторе
    BEAF_METEOR = (By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")  # иконка выбора говяжьего метеорита

    BREAD_LIST = (By.XPATH, ".//h2[contains(text(), 'Булки')]") # раздел булок в конструкторе
    CRATER_BREAD = (By.XPATH, ".//img[@alt = 'Краторная булка N-200i']") # иконка выбора краторной булки

    GALACTIC_SAUCE_CALORIES = (By.XPATH, ".//p[contains(text(), '99')]")
    BEAF_METEOR_CALORIES = (By.XPATH, ".//p[contains(text(), '2674')]")
    CRATER_BREAD_CALORIES = (By.XPATH, ".//p[contains(text(), '420')]")





