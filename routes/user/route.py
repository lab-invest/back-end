from fastapi import Header

from controller.user.UserController import UserController
from service.router.service import RouterService
from domain.entities.User import User


app = RouterService.get_router()

@app.post("/user/", tags=["user"])
async def sign_in(user: User):
    return UserController.register_user(user)

@app.put("/user/", tags=["user"])
async def update_user(cpf: str, field: str, value: str | int):
    return UserController.update_user_field(cpf, field, value)

@app.delete("/user/", tags=["user"])
async def delete_user(cpf: str):
    return UserController.delete_user(cpf)

@app.get("/user/", tags=["user"])
async def get_user(cpf: str):
    return UserController.get_user(cpf)