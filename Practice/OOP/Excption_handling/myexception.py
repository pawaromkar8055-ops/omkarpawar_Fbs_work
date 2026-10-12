class Myexception(Exception):
    def __init__(self, *args):
        self.age=args
        print("I am in Con Of")
        Myexception
    def __str__(self):
        return f"Bhai age proper Enter ka de "
            