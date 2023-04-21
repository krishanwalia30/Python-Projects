import voice as vo

while True:
     print("PLEASE TELL THE PASSWORD:")
     pas = vo.get_audio()
     if 'hello' in pas:
          vo.speak("how may i help you")
          print("TELL:")
          q = vo.get_audio()
          if 'on' in q and 'bulb' in q:
               print('THE BULB IS ONN')
               vo.speak("THE LIGHTS ARE SWITCHED ON")
          else:
               print("HELLO")
          
     else:
          print("ACCESS DENIED!!!")
          print()

     
     
