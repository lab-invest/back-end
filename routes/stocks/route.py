from controller.stock.StockController import StockController
from domain.entities.WalletObject import WalletList, WalletsRequest
from service.router.service import RouterService
from typing import List, Dict
import json
from fastapi import Query, Body
app = RouterService.get_router()


@app.get("/stock/", tags=["stock"])
async def actual_cotation(ticker: str):
    return StockController.get_cotation(ticker)

# @app.get("/stockList/", tags=["stock"])
# async def cotation_list():
#     return StockController.get_cotation_list()

# @app.get("/stock/prevision", tags=["stock"])
# async def stock_prevision(ticker: str):
#     return StockController.get_stock_prevision(ticker)

# @app.get("/stock/marketplace", tags=["stock"])
# async def stock_marketplace(ticker: str):
#     return StockController.get_stock_marketplace(ticker)

# @app.get("/stock/stockPage", tags=["stock"])
# async def stock_page():
#     return StockController.get_stock_page()

# @app.get("/stock/image", tags=["stock"])
# async def image(ticker: str):
#     return StockController.get_image(ticker)

# @app.get("/stock/comparison", tags=["stock"])
# async def stock_comparison(tickerList: List[str] = Query(...)):
#     return StockController.stockComparison(tickerList)

# @app.post("/stock/comparisonAside", tags=["stock"])
# async def stock_comparison_aside(tickerList:List[dict] = Body(...)):
#     return StockController.stockComparisonAside(tickerList)

# @app.post("/wallet/comparison", tags=["wallet"])
# async def wallet_comparison(walletList: WalletsRequest):
#     return StockController.walletComparison(walletList)

# @app.post("/wallet/rentability", tags=["wallet"])
# async def wallet_rent(walletList: List[dict]):
#     return StockController.walletRent(walletList)

# @app.post("/wallet/info", tags=["wallet"])
# async def wallet_rent(walletList: WalletsRequest):
#     return StockController.walletInfo(walletList)

# @app.get("/stock/findStock", tags=["stock"])
# async def find_stock(stockName: str):
#     return StockController.findStock(stockName)