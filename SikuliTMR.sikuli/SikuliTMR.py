import shutil
import os

ssDir = "C:\Users\Agung\Desktop\SS"

memu_region = Region(484,0,433,727)


def OnLostConnection(event): #!!!
    print "TMRLOG: Connection lost"
    click("1479106222739.png")
    
onAppear("1479105203116.png", OnLostConnection)
observe(background=True) 


for n in range(999):
    click("1478443813669.png")
    wait("1478884257413.png",30)
    click("1478884257413.png")
    wait("1478443830872.png",30)
    click("1478443830872.png")
    wait("1478443885988.png",30)
    click("1478443885988.png") 
    wait("1478443931001.png",180)        
    click("1478443954460.png")
    wait("1478884604112.png",FOREVER)
    click("1478884604112.png")
    wait("1478444140693.png", 15)
    wait(2)
    img = capture(memu_region)
    shutil.move(img, os.path.join(ssDir, time.strftime("%Y-%m-%d %H-%M-%S") + ".png"))
    click("1478444140693.png")
    wait(10)
    click("1478896876714.png")

    wait(10)
    if(exists("1479106741623.png")):
        click("1479106741623.png")    
    
    wait("1478443813669.png", FOREVER)
