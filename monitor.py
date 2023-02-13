import time

begin_time = time.perf_counter()
event_data = []


class KeyObj(object):
    def __init__(self):
        self.move = 1
        self.click = 2
        self.scroll = 3
        self.press = 4
        self.release = 5


Key = KeyObj()


def move(x, y):
    event_data.append([(time.perf_counter() - begin_time), [x, y], Key.move])


def click(x, y, button, pressed):
    if pressed:
        event_data.append([(time.perf_counter() - begin_time), [x, y, 0], Key.click])
    else:
        event_data.append([(time.perf_counter() - begin_time), [x, y, 1], Key.click])


def scroll(x, y, dx, dy):
    if dy < 0:
        event_data.append([(time.perf_counter() - begin_time), [x, y, 0], Key.scroll])
    else:
        event_data.append([(time.perf_counter() - begin_time), [x, y, 1], Key.scroll])


def press(key):
    try:
        if key.char == 'w':
            print(event_data)
            return False
        else:
            print(str(time.perf_counter() - begin_time) + ' al key {0} pressed'.format(key.char))
    except AttributeError:
        print(str(time.perf_counter() - begin_time) + ' special key {0} pressed'.format(
            key))


def release(key):
    print(str(time.perf_counter() - begin_time) + ' {0} released'.format(
        key))
