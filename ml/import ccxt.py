import ccxt
import time
import os
class SimpleTradingBot:
    def __init__(self, api_key, secret_key, exchange, symbol, timeframe='1h'):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': secret_key,
            'enableRateLimit': True,
        })
        self.symbol = symbol
        self.timeframe = timeframe
        self.position = 0

    def get_candlesticks(self, timeframe):
        ohlcv = self.exchange.fetch_ohlcv(self.symbol, timeframe)
        return ohlcv

    def execute_trade(self, action, quantity):
        order = None
        try:
            if action == 'buy':
                order = self.exchange.create_market_buy_order(self.symbol, quantity)
            elif action == 'sell':
                order = self.exchange.create_market_sell_order(self.symbol, quantity)
        except ccxt.NetworkError as e:
            print(f"Error de red: {e}")
        except ccxt.ExchangeError as e:
            print(f"Error del exchange: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
        return order

    def simple_strategy(self):
        while True:
            try:
                # Obtener los precios en un marco de tiempo más largo (1 hora)
                hourly_candlesticks = self.get_candlesticks('1h')
                last_hourly_candle = hourly_candlesticks[-2]  # La penúltima vela en 1 hora

                # Obtener los precios en un marco de tiempo más corto (5 minutos)
                five_minute_candlesticks = self.get_candlesticks('5m')
                last_five_minute_candle = five_minute_candlesticks[-1]  # La última vela en 5 minutos

                # Estrategia: Vender si hay manipulación de la alta en 1 hora, quiebre de estructura en 5 minutos
                # y el precio supera el último bajo más alto con un descuento del 70%
                if (last_five_minute_candle['high'] > last_hourly_candle['high'] and
                        last_five_minute_candle['close'] < last_five_minute_candle['high']):
                    # Agrega tu lógica para verificar que el precio supere el último bajo más alto aquí
                    # Puedes usar una variable para almacenar el último bajo más alto y actualizarlo en cada iteración
                    # Además, verifica que el precio esté por debajo del descuento Fibonacci del 70%
                    # Ajusta según tus necesidades específicas
                    last_highest_high = max(candle['high'] for candle in five_minute_candlesticks[:-1])
                    if last_five_minute_candle['close'] < last_highest_high:
                        discount_price = last_highest_high * 0.7
                        if last_five_minute_candle['close'] > discount_price:
                            # Implementa aquí tu estrategia específica de venta
                            # Puedes agregar condiciones adicionales según tu estrategia
                            self.execute_trade('sell', 1)  # Ejemplo: vende 1 unidad

                # Implementa lógica para la estrategia de compra si es necesario

                time.sleep(300)  # Espera 5 minutos antes de volver a verificar el mercado
            except KeyboardInterrupt:
                print("Bot detenido por el usuario.")
                break

if __name__ == "__main__":
    # Reemplaza 'YOUR_API_KEY' y 'YOUR_SECRET_KEY' con las credenciales de tu cuenta en el exchange
    api_key =os.getenv[ 'YOUR_API_KEY']
    secret_key = 'YOUR_SECRET_KEY'
    
    # Define el símbolo del par de trading (por ejemplo, 'BTC/USDT')
    symbol = 'BTC/USDT'
    
    # Crea una instancia del bot
    bot = SimpleTradingBot(api_key, secret_key, 'binance', symbol)
    
    # Ejecuta la estrategia del bot
    bot.simple_strategy()

