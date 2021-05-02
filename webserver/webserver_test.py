from webserver import run_server

class DummyLed:
    def __init__(self):
        self._value = 1

    def value(self, new_value = None):
        if new_value is None:
            return self._value
        else:
            self._value = new_value


def start_test_server(port = 8080):
    led = DummyLed()
    run_server(port, led)

if __name__ == '__main__':
    start_test_server()
