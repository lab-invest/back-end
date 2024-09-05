from controller.stock.StockController import StockController
from service.router.service import RouterService


app = RouterService.get_router()


@app.get("/stock/", tags=["stock"])
async def get_actual_cotation(ticker: str):
    return StockController.get_cotation(ticker)

@app.get("/stockList/", tags=["stock"])
async def get_cotation_list(tickers: list):
    return StockController.get_cotation_list(tickers)