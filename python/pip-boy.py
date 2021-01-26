import keyboard
import serial
import time

ser = serial.Serial('/dev/ttyACM0')

#recorded = keyboard.record(until='esc')
#print(recorded)


while True:
  #time.sleep(1)
  #keyboard.press_and_release("up")

  
  data = ser.readline().strip()
  print(data)
  command = data.split(' ')
  
  if command[0] == 'rot':
    if command[1] == '1':
      print('UP')
      keyboard.press_and_release("up")
    elif command[1] == '-1':
      print('DOWN')
      keyboard.press_and_release("down")
    else:
      print('Unknown rot command "' + data  + '"');
  elif command[0] == 'pot':
    print('POT');
    # TODO figure out how to send pot values as kb input
  elif command[0][:1] == 'B':
    if command[0][1:] == '11':
      print('STATUS')
      keyboard.press_and_release("s")
    elif command[0][1:] == '12':
      keyboard.press_and_release("m")
      print('AUTOMAPS')
    elif command[0][1:] == '4':
      keyboard.press_and_release("r")
      print('ARCHIVES')
    elif command[0][1:] == '5':
      keyboard.press_and_release("c")
      print('CLOSE')
    elif command[0][1:] == '8':
      keyboard.press_and_release("enter")
      print('ENTER')
  else:
    print('Unknown command "' + data + '"');
  


'''
B8

B8

B11

B12

B4

B5
'''
