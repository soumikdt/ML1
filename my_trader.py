from typing import List, Dict
import json
import jsonpickle

Time = int
Symbol = str
Product = str
Position = int
UserId = str
ObservationValue = int


class Listing:
    def __init__(self, symbol: Symbol, product: Product, denomination: Product):
        self.symbol = symbol
        self.product = product
        self.denomination = denomination


class ConversionObservation:
    def __init__(self, bidPrice: float, askPrice: float, transportFees: float, exportTariff: float,
                 importTariff: float, sugarPrice: float, sunlightIndex: float, humidity: float):
        self.bidPrice = bidPrice
        self.askPrice = askPrice
        self.transportFees = transportFees
        self.exportTariff = exportTariff
        self.importTariff = importTariff
        self.sugarPrice = sugarPrice
        self.sunlightIndex = sunlightIndex
        self.humidity = humidity


class Observation:
    def __init__(self, plainValueObservations: Dict[Product, ObservationValue],
                 conversionObservations: Dict[Product, ConversionObservation]) -> None:
        self.plainValueObservations = plainValueObservations
        self.conversionObservations = conversionObservations

    def __str__(self) -> str:
        return "(plainValueObservations: " + jsonpickle.encode(self.plainValueObservations) + ", conversionObservations: " + jsonpickle.encode(self.conversionObservations) + ")"


class Order:
    def __init__(self, symbol: Symbol, price: int, quantity: int) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"({self.symbol}, {self.price}, {self.quantity})"

    def __repr__(self) -> str:
        return f"({self.symbol}, {self.price}, {self.quantity})"


class OrderDepth:
    def __init__(self):
        self.buy_orders: Dict[int, int] = {}
        self.sell_orders: Dict[int, int] = {}


class Trade:
    def __init__(self, symbol: Symbol, price: int, quantity: int, buyer: UserId = None,
                 seller: UserId = None, timestamp: int = 0) -> None:
        self.symbol = symbol
        self.price: int = price
        self.quantity: int = quantity
        self.buyer = buyer
        self.seller = seller
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"({self.symbol}, {self.buyer} << {self.seller}, {self.price}, {self.quantity}, {self.timestamp})"

    def __repr__(self) -> str:
        return f"({self.symbol}, {self.buyer} << {self.seller}, {self.price}, {self.quantity}, {self.timestamp})"


class TradingState:
    def __init__(self,
                 traderData: str,
                 timestamp: Time,
                 listings: Dict[Symbol, Listing],
                 order_depths: Dict[Symbol, OrderDepth],
                 own_trades: Dict[Symbol, List[Trade]],
                 market_trades: Dict[Symbol, List[Trade]],
                 position: Dict[Product, Position],
                 observations: Observation):
        self.traderData = traderData
        self.timestamp = timestamp
        self.listings = listings
        self.order_depths = order_depths
        self.own_trades = own_trades
        self.market_trades = market_trades
        self.position = position
        self.observations = observations

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


class ProsperityEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class Trader:
    def estimate_fair_value(self, product: Product, state: TradingState) -> float:
        # Try to estimate fair value using conversion observations if available.
        conv_obs = state.observations.conversionObservations.get(product)
        if conv_obs:
            # Compute an initial fair value as the average of bid and ask prices.
            fair_value = (conv_obs.bidPrice + conv_obs.askPrice) / 2.0
            # Adjust by considering additional fees and tariffs.
            fair_value += conv_obs.transportFees + conv_obs.exportTariff - conv_obs.importTariff
            print('fallback2')
            return fair_value
        # Otherwise, use a plain value observation if available.
        elif product in state.observations.plainValueObservations:
            print('fallback2')
            return state.observations.plainValueObservations[product]
        # Fall back to a default fair value.
        print('fallback')
        return 10000

    def run(self, state: TradingState):
        result = {}
        for product in state.order_depths:
            current_position = state.position.get(product, 0)
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []

            sell_size = -current_position - 20
            buy_size = -current_position + 20

            if product == 'AMETHYSTS':
                # Market making strategy: fixed spread around a fixed fair value
                fair_value = self.estimate_fair_value(product, state)
                spread = 2
                buy_order = Order(product, fair_value - spread, buy_size)
                sell_order = Order(product, fair_value + spread, sell_size)
                orders.extend([buy_order, sell_order])

            elif product == 'STARFRUIT':
                # Adaptive market making strategy using mid-price
                best_ask = min(order_depth.sell_orders.keys()) if order_depth.sell_orders else None
                best_bid = max(order_depth.buy_orders.keys()) if order_depth.buy_orders else None

                if best_ask is not None and best_bid is not None:
                    mid_price = (best_ask + best_bid) // 2
                    spread = 2
                    buy_order = Order(product, mid_price - spread, buy_size)
                    sell_order = Order(product, mid_price + spread, sell_size)
                    orders.extend([buy_order, sell_order])

            result[product] = orders

        traderData = "Updated"
        conversions = 1
        return result, conversions, traderData
