from sqlalchemy.ext.asyncio import AsyncSession

from sql_utils.models import User  # Здесь models - модуль с определением моделей базы данных


class UserDAL:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self,
                          user_id: str,
                          login: str,
                          password: str,
                          name: str,
                          surname: str,
                          patronymic: str,
                          email: str,
                          birthdate: str,
                          category: int
                          ) -> User:
        new_user = User(
            user_id=user_id,
            login=login,
            password=password,
            name=name,
            surname=surname,
            patronymic=patronymic,
            email=email,
            birthdate=birthdate,
            category=category
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user


#
# class UserRepository:
#     def __init__(self, db: Session = get_session()):
#         self.db = db
#
#     def get_user(self, user_id: int) -> User:
#         user = self.db.query(User).filter(User.id == user_id).first()
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")
#         return user
#
#     def create_user(self, user_data: dict) -> User:
#         user = User(**user_data)
#         self.db.add(user)
#         self.db.commit()
#         self.db.refresh(user)
#         return user
#
#     def update_user(self, user_id: int, user_data: dict) -> User:
#         user = self.get_user(user_id)
#         for key, value in user_data.items():
#             setattr(user, key, value)
#         self.db.commit()
#         self.db.refresh(user)
#         return user
#
#     def delete_user(self, user_id: int) -> None:
#         user = self.get_user(user_id)
#         self.db.delete(user)
#         self.db.commit()
