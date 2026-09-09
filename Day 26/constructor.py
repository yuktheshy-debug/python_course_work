#cons is a special method which is going to call whenever the obj is crated


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to Instagram, {self.username}")

yukthesh = Instagram('yukthesh','1234')
king = Instagram('king','2345')
ssr = Instagram('SSR','4747')