import random

pierre = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ciseaux = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
i = 0
jeu = [pierre,papier,ciseaux]
while i < 3:
    mon_choix = int(input("Qu'est-ce que tu choisis ? Tape 0 pour pierre, 1 pour papier, 2 pour ciseaux.\n"))
    print(jeu[mon_choix])

    choix_ordinateur = random.randint(0,2)
    print("Le choix de l'ordinateur est:")
    print(jeu[choix_ordinateur])



    if(mon_choix <0 or mon_choix >= 3):
        print("Votre choix n'est pas valide, vous avez perdu !")
    elif mon_choix == 0 and choix_ordinateur == 2:
        print("Vous avez gagné !")
    elif mon_choix == 1 and choix_ordinateur == 0:
        print("Vous avez perdu !")
    elif choix_ordinateur == 0 and mon_choix == 2:
      print("Vous avez perdu !")
    elif choix_ordinateur > mon_choix:
      print("Vous avez perdu !")
    elif mon_choix > choix_ordinateur:
      print("Vous avez gagné !")
    elif choix_ordinateur == mon_choix:
      print("Match nul !")
    i = i+1

