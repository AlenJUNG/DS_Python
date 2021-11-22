def square(x,y):
    return x * y

class Bread:
    # 클래스 변수 class variable shared by all instances
    num = 0
    def __init__(self):
        # 인스턴스 변수 instance variable unique to each instance
        self.source = "팥앙금"
        self.shape = "붕어"
        Bread.num += 1

    # 인스턴스 메소드
    def intro(self):
        return f'{self.source} 이 들어간 {self.shape}빵이에요!!'