# MusicBerry API controller functions

def process(data, app):
    print("\nHTTP request:", data)
    event = data['event']
    if event == 'volume':
        app.volume_up()
    elif event == 'play':
        app.play()
    elif event == 'pause':
        app.pause()
    elif event == 'next':
        app.next()
    elif event == 'prev':
        app.prev()