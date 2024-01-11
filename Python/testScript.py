import time

countdown = 5

while countdown > 0:
    print('Countdown = ', countdown)
    countdown = countdown - 1
    time.sleep(1)
    raise Exception('Kill the script')
