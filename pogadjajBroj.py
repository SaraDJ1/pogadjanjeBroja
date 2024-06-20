import random
zamisljenBroj  = random.randint (0, 20)
brojPokusaja = 5
while brojPokusaja > 0:
    mojePogadjanje = int(input("pogadjaj :"))
    if(mojePogadjanje == zamisljenBroj):
        print("Legendarno! Kraj igre")
        break
    else:
        brojPokusaja = brojPokusaja - 1
        print("Jaooooo! Imas jos",brojPokusaja,"Pokusaja")
        
    if(brojPokusaja == 0):
        print("Kraj igre, kompjuter je zamislio broj : ", zamisljenBroj)
   
