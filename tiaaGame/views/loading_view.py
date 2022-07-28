"""
Loading screen
"""
import arcade
from tiaaGame.draw_bar import draw_bar
from tiaaGame.load_game_map import load_maps
from tiaaGame.views.car_dealership_view import CarDealershipView
from tiaaGame.views.game_view import GameView
from tiaaGame.views.inventory_view import InventoryView
from tiaaGame.views.main_menu_view import MainMenuView
from tiaaGame.views.settings_view import SettingsView
from tiaaGame.views.marketplace_view import MarketPlaceView
from tiaaGame.views.car_dealership_view import CarDealershipView
from tiaaGame.views.start_menu_view import StartMenuView
from tiaaGame.views.character_presentation_view import CharacterPresentation
from tiaaGame.views.real_estate_view import RealEstateView
from tiaaGame.views.player_finances_view import PlayerFinancesView
from tiaaGame.views.stock1_view import StockOne
from tiaaGame.views.stock2_view import StockTwo
from tiaaGame.views.stock3_view import StockThree
from tiaaGame.views.fourthreeb import fourthreeb
from tiaaGame.views.ira import ira
from tiaaGame.views.annuity import annuity
# For minigame.
from tiaaGame.views.minigame_view_character_select import CharacterSelectView
from tiaaGame.views.bank_view import BankView
from tiaaGame.views.stocks_view import StocksView
from tiaaGame.views.retirement_view import RetireView

# Workview 
from tiaaGame.views.minigame_work_view import WorkView


from tiaaGame import constants


class LoadingView(arcade.View):
    def __init__(self):
        super().__init__()
        self.started = False
        self.progress = 0
        self.map_list = None
        arcade.set_background_color(constants.DARK_BLUE)
        self.background = arcade.load_texture("././resources/views/logo.png")

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.window.width/2, self.window.height/2 +30 , 500, 500, self.background)
        self.started = True
        draw_bar(
            current_amount=self.progress,
            max_amount=100,
            center_x=self.window.width / 2,
            center_y=30,
            width=self.window.width,
            height=20,
            color_a=constants.LIGHTER_BLUE,
            color_b=constants.LIGHT_BLUE,
        )
        arcade.draw_text(
            "Loading...",
            self.window.width / 2,
            self.window.height / 2 - 260,
            arcade.color.WHITE,
            constants.DEFAULT_FONT_SIZE,
            font_name= constants.DEFAULT_FONT,
            anchor_x="center",
            anchor_y="center",
            align="center",
            width=self.window.width,
        )

    def setup(self):
        pass

    def on_update(self, delta_time: float):
        # Dictionary to hold all our maps
        if self.started:
            done, self.progress, self.map_list = load_maps()
            if done:
                self.window.views["game"] = GameView(self.map_list)
                self.window.views["game"].setup()
                self.window.views["inventory"] = InventoryView()
                self.window.views["inventory"].setup()
                self.window.views["main_menu"] = MainMenuView()
                self.window.views["marketplace"] = MarketPlaceView()
                self.window.views["car_dealership"] = CarDealershipView()
                self.window.views["settings"] = SettingsView()
                self.window.views["settings"].setup()
                self.window.views["start_menu"] = StartMenuView()
                self.window.views["character_presentation"] = CharacterPresentation()
                self.window.views["real_estate"] = RealEstateView()
                self.window.views['bank'] = BankView()
                self.window.views['stock'] = StocksView()
                self.window.views['retirement'] = RetireView()
                self.window.views["platformer"] = CharacterSelectView()
                self.window.views["player_finances"] = PlayerFinancesView()
                self.window.views["stock_one"] = StockOne()
                self.window.views["stock_two"] = StockTwo()
                self.window.views["stock_three"] = StockThree()
                self.window.views["403b"] = fourthreeb()
                self.window.views["ira"] = ira()
                self.window.views["annuity"] = annuity()
                self.window.views["workview"] = WorkView()
                self.window.show_view(self.window.views["start_menu"])
