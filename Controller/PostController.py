from ..Service.PostService import PostService


class PostController:

    @staticmethod
    def get_posts():
        return PostService().get_posts()

    @staticmethod
    def create_post(post):
        PostService().create_post(post)
