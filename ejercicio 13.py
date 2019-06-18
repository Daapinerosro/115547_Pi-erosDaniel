

frase = (input('Favor ingresar una frase'))

y =frase.replace(' ','')

#juego de condicionales centrados con variable frase.replace
if y[0]:         
   print (y[0].center(100,' ')) 
   if y[1:3]:
      print (y[1:4].center(99,' '))
      if y[4:8]:
         print (y[4:9].center(99,' '))
         if y[9:15]:
            print (y[9:16].center(99,' '))
            if y[16:24]:
               print (y[16:25].center(99,' '))
               if y[25:35]:
                  print (y[25:36].center(99,' '))
                  if y[36:48]:
                     print (y[36:49].center(99,' '))  
                     if y[49:63]:
                        print (y[49:64].center(99,' '))
                        if y[64:80]:
                            print (y[64:81].center(99,' '))
                            if y[81:99]:
                                print (y[81:100].center(99,' '))
                                if y[100:]:
                                    print (y[100:].center(99,' '))



