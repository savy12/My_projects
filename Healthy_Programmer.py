from time import time
from datetime import datetime
from pygame import mixer


def music(file,stop):
   mixer.init()
   mixer.music.load(file)
   mixer.music.play()
   while True:
      inp_user = input("\t")
      if inp_user == stop:
         mixer.music.stop()
         break

def logs(msg):
   with open('my_log.txt','a') as ml:
      ml.write(f'{msg} {datetime.now()}\n')

if __name__=='__main__':
   water_time=time()
   eye_time=time()
   phy_time=time()
   water_sec=1644
   eye_sec=1800
   phy_sec=2700
   while True:
      if time()-water_time>water_sec:
         print('if you drank water type \'drank\'')
         music('water.wav','drank')
         water_time = time()
         logs('Drank water at ')
      if time()-eye_time>eye_sec:
         print('if you have washed eyes type \'eyes\'')
         music('eyes.wav','eyes')
         eye_time = time()
         logs('Washed eyes at ')
      if time()-phy_time>phy_sec:
         print('if you have done exercise type \'exc\'')
         music('physical.wav','exc')
         phy_time = time()
         logs('done exercise at ')
         

         
   




##def water():
##   for i in range(3):#27
##      mixer.init()
##      mixer.music.load("water.wav")
##      mixer.music.play()
##      inp_water = input("If you have drank water type D and any other input if you haven't:\t")
##      inp_water = inp_water.capitalize()
##      if inp_water =='D':
##         mixer.music.stop()
##         with open('water.txt','a') as w:
##            w.write(str(getdate())+'\n')
##         time.sleep(2)#1644
##         print(i)  
##      else:
##         water()
##
##
##def eyes():
##   for i in range(3):#16
##      mixer.init()
##      mixer.music.load("eyes.wav")
##      mixer.music.play()
##      inp_water = input("If you have washed your eyes and did eyes exercise type E and any other input if you haven't:\t")
##      inp_water = inp_water.capitalize()
##      if inp_water =='E':
##         mixer.music.stop()
##         with open('eyes.txt','a') as w:
##            w.write(str(getdate())+'\n')
##         time.sleep(2)#1800
##         print(i)  
##      else:
##         eyes()
##
##
##
##def physical():
##   for i in range(3):#11
##      mixer.init()
##      mixer.music.load("physical.wav")
##      mixer.music.play()
##      inp_water = input("If you completed your physical exercise type P and any other input if you haven't:\t")
##      inp_water = inp_water.capitalize()
##      if inp_water =='P':
##         mixer.music.stop()
##         with open('pysical.txt','a') as w:
##            w.write(str(getdate())+'\n')
##         time.sleep(2)#2700
##         print(i)  
##      else:
##         physical()
##
##
##physical()
##eyes()
##water()
##l = [physical(),eyes(),water()]
##l
##if __name__=='__main__':
##   p1=Process(target=eyes)
##   p2=Process(target=water)
##   p3=Process(target=physical)
##   p1.start()
##   p2.start()
##   p3.start()
##   p1.join()
##   p2.join()
##   p3.join()

##mixer.init()
##mixer.music.load("water.wav")
##mixer.music.play()
##a= 10
##time.sleep(a)
##
##mixer.music.stop()
##   
   
   

















