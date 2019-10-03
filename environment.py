from ai import NN
import cbpro
import numpy as np
import time
from random import random, randint

agent = NN()

class TradingEnvironment:
    def __init__(self, data, starting_money = 30000):
        # INITIALIZE ALL NEEDED VARIABLES
        
        self.data = data
        self.starting_money = starting_money
        self.iterations = len(self.data)
        self.possible_actions = np.arange(3)
        self.funds = starting_money
        self.owned = None
        self.price = None
        
    def iterate(self, trade_action):
        
        # CALL TRADE FUNCTION AND ITERATE TO THE NEXT DAYS STOCK PRICE
        
        
    
    def trade(self, trade_action):
        
        # MAKE THE TRADE WITH THE HIGHEST Q-VALUE
        
        # sell all owned stocks
        if trade_action == 0:
            self.funds += self.price * self.owned
            self.owned = 0
        # buy stocks with all funds
        if trade_action == 2:
            enough_money = True
            while enough_money:
                if self.funds > self.price:
                    self.owned += 1
                    self.funds -= self.price
                else:
                    enough_money = False
            
            
            

