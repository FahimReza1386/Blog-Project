from locust import HttpUser , task, between


class QuickStarUser(HttpUser):
    
    @task
    def post_list(self):
        self.client.get("/api/v1/post/")
    
    @task
    def post_category(self):
        self.client.get("/api/v1/category/")