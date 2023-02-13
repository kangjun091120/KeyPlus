import time

begin_time = time.perf_counter()
event_data = []


class Key(object):  # 创建Circle类
    def __init__(self, r):  # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
        self.r = r


def move(x, y):
    print([(time.perf_counter() - begin_time), (x, y)])


def click(x, y, button, pressed):
    print(str(time.perf_counter() - begin_time) + ' {0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def scroll(x, y, dx, dy):
    print(str(time.perf_counter() - begin_time) + ' Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))


def press(key):
    try:
        print(str(time.perf_counter() - begin_time) + ' al key {0} pressed'.format(
            key.char))
    except AttributeError:
        print(str(time.perf_counter() - begin_time) + ' special key {0} pressed'.format(
            key))


def release(key):
    print(str(time.perf_counter() - begin_time) + ' {0} released'.format(
        key))
