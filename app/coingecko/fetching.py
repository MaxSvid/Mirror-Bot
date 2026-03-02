# https://dev.to/mfs_corp/how-i-built-a-telegram-bot-for-real-time-crypto-alerts-and-you-can-too-26io

import requests
from typing import List, Dict, Optional

class CoinGeckoAPI:
    BASE_URL = "https://api.coingecko.com/api/v3"
    url_coins ="https://api.coingecko.com/api/v3/coins/list"
    url_currency ="https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    url_price="https://api.coingecko.com/api/v3/simple/price?"

    def get_price(self, coin_id: str) -> Optional[float]:
        """Fetch current price for a cryptocurrency"""
        try:
            response = requests.get(
                f"{self.BASE_URL}/simple/price",
                params={
                    "ids": coin_id,
                    "vs_currencies": "usd"
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return data.get(coin_id, {}).get("usd")
        except Exception as e:
            print(f"Error fetching price for {coin_id}: {e}")
            return None

    def get_multiple_prices(self, coin_ids: list) -> Dict[str, float]:
        """Fetch prices for multiple cryptocurrencies at once"""
        try:
            response = requests.get(
                f"{self.BASE_URL}/simple/price",
                params={
                    "ids": ",".join(coin_ids),
                    "vs_currencies": "usd"
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            return {coin: data.get(coin, {}).get("usd", 0) for coin in coin_ids}
        except Exception as e:
            print(f"Error fetching prices: {e}")
            return {}