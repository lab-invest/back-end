from controller.stock.StockController import StockController
from service.router.service import RouterService


app = RouterService.get_router()


@app.get("/stock/", tags=["stock"])
async def get_actual_cotation(ticker: str):
    return StockController.get_cotation(ticker)

@app.get("/stockList/", tags=["stock"])
async def get_cotation_list():
    return StockController.get_cotation_list()

@app.get("/stock/prevision", tags=["stock"])
async def get_stock_prevision(ticker: str):
    return StockController.get_stock_prevision(ticker)

@app.get("/stock/marketplace", tags=["stock"])
async def get_stock_marketplace(ticker: str):
    return StockController.get_stock_marketplace(ticker)

@app.get("/stock/stockPage", tags=["stock"])
async def get_stock_page():
    return StockController.get_stock_page()

@app.get("/stock/image", tags=["stock"])
async def get_image(ticker: str):
    return StockController.get_image(ticker)