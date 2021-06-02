from seleniumbase import BaseCase

class MyTestClass(BaseCase):

     # standard user 
    def test_basics(self):
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "standard_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        self.click('button[name="add-to-cart-sauce-labs-backpack"]')
        self.click('div[id="shopping_cart_container"]')
        self.click('button[name="checkout"]')
        self.type('input[name="firstName"]', "standard")
        self.type('input[name="lastName"]', "user")
        self.type('input[name="postalCode"]', "02130")
        self.click('input[name="continue"]')
        self.click('button[name="finish"]')
        self.assert_text('THANK YOU FOR YOUR ORDER')

    # locked_out_user
    def test_basics1(self):
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "locked_out_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        self.assert_text('Epic sadface: Sorry, this user has been locked out.')

    # problem_user
    def test_basics2(self):
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "problem_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        self.click('button[name="add-to-cart-sauce-labs-backpack"]')
        self.click('div[id="shopping_cart_container"]')
        self.click('button[name="checkout"]')
        self.type('input[name="firstName"]', "standard")
        self.type('input[name="lastName"]', "user")
        self.type('input[name="postalCode"]', "02130")
        self.click('input[name="continue"]')
        self.assert_text('Error: Last Name is required')

   