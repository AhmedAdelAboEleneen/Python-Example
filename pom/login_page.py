

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_tx = page.get_by_role("textbox", name="ادخل اسم المستخدم")
        self.password_tx = page.get_by_role("textbox", name="ادخل الرمز السرى")
        self.login_bt = page.get_by_role("button", name="تسجيل الدخول")


    def login(self, username, password):
        self.email_tx.fill(username)
        self.password_tx.fill(password)
        self.login_bt.click()