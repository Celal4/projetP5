import core

def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("position",(400,400))
    core.memory("vitesse", (1,0))

def run():
    core.cleanScreen()

    core.memory("Position", core.memory("Position") + core.memory("Vitesse"))

    #Control
    if core.getKeyPressList("z"):
        core.memory("vitesse").scale.to.length(core.memory("vitesse").length()+0.1)

    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))

    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-5))

    #Dessin Vaisseau

    vectP1 = core.memory("vitesse").rotate(90)
    vectP1.scale.to.length(10)

    P1 = core.memory("position") + vectP1

