from strategies.user_test_strategy import UserTestStrategy

class RegularUserTestStrategy(UserTestStrategy):
    username = "shiv"

    def verify_home_page_message(self):
        assert "Bem-vindo, usuário!" in self.driver.page_source