from locust import HttpUser, task


class QuickStarUser(HttpUser):

    def on_start(self):
        response = self.client.post(
            "/accounts/api/v1/jwt/create/",
            data={"email": "Fahimreza20200@gmail.com", "password": "Fahim2684"},
        ).json()

        self.client.headers = {"Authorization": f"Bearer {response.get('access',None)}"}

    @task
    def post_list(self):
        self.client.get("/api/v1/post/")

    @task
    def post_category(self):
        self.client.get("/api/v1/category/")
