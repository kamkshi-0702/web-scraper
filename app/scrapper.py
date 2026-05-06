import time
import requests
from app.database import SessionLocal, engine
from app import models, crud
from app.schemas import UserCreate

models.Base.metadata.create_all(bind=engine)

def fetch_and_store():
    db = SessionLocal()

    url = "https://api.github.com/users"

    for page in range(1, 101):  # ✅ Reduced pages
        params = {
            "per_page": 10,
            "page": page
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Stopping at page {page} due to API limit")  # ✅ Better handling
            break

        data = response.json()

        if not data:
            break

        for user in data:
            user_obj = UserCreate(
                id=user.get("id"),
                login=user.get("login"),
                url=user.get("html_url"),
                type=user.get("type")
            )

            crud.create_user(db, user_obj)

        print(f"Page {page} processed")

        time.sleep(1)  # ✅ Prevents rate limit

    db.close()

if __name__ == "__main__":
    fetch_and_store()