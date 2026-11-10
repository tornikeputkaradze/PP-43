import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


for user_id in (1, 2, 999):
    user = get_user(user_id)
    if user is None:
        print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
    else:
        print(f"{user['name']} │ {user['email']} │ {user['address']['city']}")

def crud_tour():
    new_post = {"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    new_id = response.json()["id"]
    print(f"CREATE: {response.status_code}, id={new_id}")

    response = requests.get(f"{BASE_URL}/posts/{new_id}")
    print(f"READ {new_id}: {response.status_code}")

    full_post = {"id": 1, "title": "სრულად შეცვლილი", "body": "ტექსტი", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=full_post)
    print(f"UPDATE (PUT): {response.status_code}, title={response.json()['title']}")

    response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "ნაწილობრივ შეცვლილი"})
    print(f"UPDATE (PATCH): {response.status_code}, title={response.json()['title']}")

    response = requests.delete(f"{BASE_URL}/posts/1")
    print(f"DELETE: {response.status_code}, {response.json()}")


crud_tour()