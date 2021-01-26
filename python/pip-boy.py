import keyboard
import serial
import time

ser = serial.Serial('/dev/ttyACM0')

while True:
  data = ser.readline().strip().decode()
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
    # This should be filtered on the Arduino, but I can't be bothered opening the Pip-boy just now.
    if abs(pot[command[1]] - command[2]):
      print(data);
      keyboard.write(command[1] + command[2] + ' ')
      pot[command[1]] = command[2]
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
