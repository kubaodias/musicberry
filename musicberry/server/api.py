# MusicBerry API controller functions

def process(data, app):
    print("\nHTTP request:", data)
    event = data['event']
    if event == 'play':
        app.play()
    elif event == 'pause':
        app.pause()
    elif event == 'next':
        app.next()
    elif event == 'prev':
        app.prev()
    elif event == 'up':
        app.volume_up()
    elif event == 'down':
        app.volume_down()