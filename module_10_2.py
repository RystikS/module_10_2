import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.day = 0
        self.delay = 1

    def battle(self):
        while self.enemy > 0:
            time.sleep(self.delay)
            self.enemy -= self.power
            self.day += 1
            print(f'{self.name} сражается {self.day} дней(дня), осталось {self.enemy} воинов.')


    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')


