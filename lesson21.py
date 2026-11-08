import requests

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        return None

    response.raise_for_status()
    return response.json()

for user_id in [1, 2, 999]:
    user = get_user(user_id)

    if user is None:
        print(F"მომხმარებელი {user_id} ვერ მოიძებნა")
    else:
        print(f"{user['name']} | {user['email']} | {user['address']['city']}")



def crud_tour():
    new_post = {"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1}
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post,
        timeout=10
    )
    response.raise_for_status()
    created = response.json()
    print(f"CREATE: {response.status_code}, id={created['id']}")

    post_id = created["id"]
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    read_response = requests.get(url, timeout=10)
    print(f"READ {post_id}: {read_response.status_code}")

    full_post = {
        "id": 1,
        "title": "სრულად შეცვლილი",
        "body": "ახალი ტექსტი",
        "userId": 1
    }
    put_response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1", json=full_post, timeout=10)
    put_response.raise_for_status()
    updated = put_response.json()
    print(f"UPDATE (PUT): {put_response.status_code}, title={updated['title']}")

    changes = {"title": "ნაწილობრივ შეცვლილი"}
    patch_response = requests.patch("https://jsonplaceholder.typicode.com/posts/1",
                                    json=changes, timeout=10)
    patch_response.raise_for_status()
    patched = patch_response.json()
    print(f"UPDATE (PATCH): {patch_response.status_code}, title={patched['title']}")

    delete_response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1",timeout=10)
    delete_response.raise_for_status()
    deleted = delete_response.json()
    print(f"DELETE: {delete_response.status_code}, {deleted}")


crud_tour()







