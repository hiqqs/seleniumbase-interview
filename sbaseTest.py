from seleniumbase import BaseCase

class MyTestClass(BaseCase):

     # standard user 
    def test_standardUser(self):

        ## Login to Swag Labs with standard_user Credentials 
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "standard_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        
        # Verify that the "Sauce Labs Backpack" is present in the inventory
        item_name = "Sauce Labs Backpack"
        self.assert_text(item_name)
        item_price = self.get_text("div.inventory_item_price")

        ## add to card the Sauce Labs Backpack
        self.click('button[name="add-to-cart-sauce-labs-backpack"]')

         # Verify the cart
        self.click("#shopping_cart_container")
        self.assert_element('span:contains("Your Cart")')
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_exact_text("1", "div.cart_quantity")
        self.assert_exact_text("REMOVE", "button.cart_button")
        self.assert_element("button#continue-shopping")

        # Checkout and adding informattion
        self.click('button[name="checkout"]')
        self.type('input[name="firstName"]', "standard")
        self.type('input[name="lastName"]', "user")
        self.type('input[name="postalCode"]', "02130")

        # Verify checkout
        self.click("input#continue")
        self.assert_element('span:contains("Checkout: Overview")')
        self.assert_element("button#cancel")
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_text(item_price, "div.inventory_item_price")
        self.assert_exact_text("1", "div.cart_quantity")

        # Finish Checkout
        self.click('button[name="finish"]')
        self.assert_text('THANK YOU FOR YOUR ORDER')

    # locked_out_user
    def test_lockedUser(self):
        ## Login to Swag Labs with locked_out_user Credentials
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "locked_out_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        
        ## Verify that the error comes out while login 
        self.assert_text('Epic sadface: Sorry, this user has been locked out.')

    # problem_user
    def test_problemUser(self):

        ## Login to Swag Labs with problem_user Credentials 
        self.open("https://www.saucedemo.com/")
        self.type('input[name="user-name"]', "problem_user")
        self.type('input[name="password"]', "secret_sauce")
        self.click('input[name="login-button"]')
        
        # Verify that the "Sauce Labs Backpack" appears on the page
        item_name = "Sauce Labs Backpack"
        self.assert_text(item_name)
        item_price = self.get_text("div.inventory_item_price")

        ## add to card the Sauce Labs Backpack
        self.click('button[name="add-to-cart-sauce-labs-backpack"]')

         # Verify the cart
        self.click("#shopping_cart_container")
        self.assert_element('span:contains("Your Cart")')
        self.assert_text(item_name, "div.inventory_item_name")
        self.assert_exact_text("1", "div.cart_quantity")
        self.assert_exact_text("REMOVE", "button.cart_button")
        self.assert_element("button#continue-shopping")

        # Checkout and adding informattion
        self.click('button[name="checkout"]')
        self.type('input[name="firstName"]', "problem")
        self.type('input[name="lastName"]', "user")
        self.type('input[name="postalCode"]', "02130")

        # Verify the problem with the page
        self.click('input[name="continue"]')
        self.assert_text('Error: Last Name is required')

   