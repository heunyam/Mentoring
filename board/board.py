# CLI 기반 게시판 프로그램을 개발하세요.
# 모든 '게시글'은 '제목'과 '내용'으로 이루어집니다.
# '글 추가'와 '글 목록', '글 삭제' 기능을 구현하면 됩니다.
from dataclasses import dataclass, field


@dataclass
class Post:
    title: field(default_factory=str)
    content: field(default_factory=str)


class Board:

    def __init__(self):
        self.num = 0
        self.posts = []

    def post(self, title, content):
        self.num += 1

        post = Post(title, content)
        self.posts.append(post)

    def show_posts(self):
        for i, post in enumerate(self.posts):
            print(
                f"({i+1}) {post.title} | {post.content}"
            )

    def delete_post(self, post_id):
        if post_id <= self.num:
            del self.posts[post_id - 1]

            self.num -= 1

            return 1
        else:
            return 0


if __name__ == '__main__':
    board = Board()

    while True:
        category = input("글 추가(1) 글 목록(2) 글 삭제(3) 종료(E)> ")

        if category == '1':
            title = input("제목 > ")
            content = input("내용 > ")
            board.post(title, content)

        elif category == '2':
            board.show_posts()

        elif category == '3':
            board.show_posts()
            post_id = input("삭제 할 글의 번호 > ")

            if board.delete_post(int(post_id)):
                print("Deleted successfully")
            else:
                print("No such post")

        elif category == 'E' or category == 'e':
            break

        else:
            print(f"({category}) is not valid")
