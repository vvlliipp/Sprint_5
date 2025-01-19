from selenium.webdriver.common.by import By
class Loсators():
    LOGIN_BUTTON = By.XPATH, "//button[text() = 'Войти в аккаунт']" #кнопка "Войти в аккаунт"
    REGISTRATION_BUTTON = By.XPATH, "//a[text() = 'Зарегистрироваться']" #кнопка "Зарегистрироваться"
    NAME_FIELD = By.XPATH, "//label[text() = 'Имя']/..//input" #поле Имя в форме регистрации
    EMAIL_FIELD = By.XPATH, "//label[text() = 'Email']/..//input" #поле Email в форме регистрации
    PASSWORD_FIELD = By.NAME, "Пароль" #поле Пароль в форме регистрации
    REGISTR_BUTTON = By.XPATH, "//button[text() = 'Зарегистрироваться']" # кнопка Зарегистрироваться в форме регистрации
    SIGN_BUTTON_REGISTRATION_FORM = By.XPATH, "//button[text() = 'Войти']" #кнопка Войти в форме регистрации
    PLACE_ON_ORDER_BUTTON = By.XPATH, "//button[text() = 'Оформить заказ']" #кнопка Оформить заказ
    INVALID_PASSWORD = By.XPATH, "//p[text() = 'Некорректный пароль']" #Ошибка "Некорректный пароль"
    PERSONAL_ACCOUNT = By.XPATH, "//p[text() = 'Личный Кабинет']" #Кнопка Личный Кабинет
    TEXT_LINK_TO_LOG_IN = By.XPATH, "//a[text() = 'Войти']" #Текст-ссылка Войти
    RECOVERY_PASSWORD = By.XPATH, "//a[text() = 'Восстановить пароль']" #Текст-ссылка Восстановить пароль
    PROFILE = By.XPATH, "//a[text() = 'Профиль']" #Профиль пользователя
    CONSTRUCTOR = By.XPATH, "//p[text() = 'Конструктор']" #Кнопка Конструктор
    BURGER_BUILD_PAGE = By.XPATH, "//h1[text() = 'Соберите бургер']" #Страница сбора бургера
    LOGO_STELLAR_BURGER = By.CLASS_NAME, "AppHeader_header__logo"
    LOG_OUT = By.XPATH, "//button[text() = 'Выход']" #Кнопка Выход из профиля
    BREAD_SECTION = By.XPATH, "//span[text() = 'Булки']" #Раздел Булки
    SELECTED_SECTION = By.XPATH, "[contains(@class, 'current')]" #Выбранный раздел в Конструкторе
    SAUCES_SECTION = By.XPATH, "//span[text() = 'Соусы']" #Раздел Соусы
    FILLING_SECTION = By.XPATH, "//span[text() = 'Начинки']" #Раздел Начинки

