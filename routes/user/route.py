from controller.user.UserController import UserController
from service.router.service import RouterService
from domain.entities.User import User
from domain.entities.Stock import Stock


app = RouterService.get_router()

@app.post("/user/", tags=["user"])
async def sign_in(user: User):
    return UserController.register_user(user)

@app.put("/user/", tags=["user"])
async def update_user(email: str, field: str, value: str | int):
    return UserController.update_user_field(email, field, value)

@app.delete("/user/", tags=["user"])
async def delete_user(email: str):
    return UserController.delete_user(email)

@app.get("/user/", tags=["user"])
async def get_user(email: str):
    return UserController.get_user(email)

@app.get("/user/balance", tags=["user"])
async def get_balance(email: str):
    return UserController.get_balance(email)

@app.patch("/stock/buy", tags=["stocks"])
async def buy_stock(email: str, stock: Stock):
    return UserController.buy_stock(email, stock)