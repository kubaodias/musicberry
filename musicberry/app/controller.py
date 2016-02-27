# MusicBerry controller functions

def process(data, state):
    event = data['event']
    if event == 'volume':
        action = data['action']
        state.volume_up()
        print("Volume:", action)
    elif event == 'play':
        print("Play")
    elif event == 'pause':
        print("Play")
    elif event == 'next':
        state.next()
    elif event == 'prev'
        state.prev()

def volume_up():
    print("Volume UP")

def volume_down():
    print("Volume DOWN")