import uvicorn
from fastapi import FastAPI, APIRouter

from sql_utils.PostgreAlchemy import UserDAL
from sql_utils.database import get_session
from sql_utils.models import UserProfile, UserCreate

app = FastAPI(title="imgomg-auth")

user_router = APIRouter()


async def _create_new_user(body: UserCreate) -> UserProfile:
    async with get_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                login=body.login,
                password=body.password,
                name=body.name,
                surname=body.surname,
                patronymic=body.patronymic,
                email=body.email,
                birthdate=body.birthdate,
                category=body.category
            )
            return UserProfile(
                user_id=user.user_id,
                login=user.login,
                email=user.email,
                name=user.name,
                surname=user.surname,
                patronymic=user.patronymic,
                birthdate=user.birthdate,
                category=user.category
            )


@user_router.post("/", response_model=UserProfile)
async def create_user(body: UserCreate):
    return await _create_new_user(body)


main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(main_api_router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
