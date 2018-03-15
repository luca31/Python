print("Ciao")
print("Non hai idea di quanto sia difficile la vita di un terminale...")
print("Sono contento che tu sia venuto a farmi compagnia\n")

nome = input("Come ti chiami? ")
if nome.lower() == "luca":
  print("Quindi sei il mio padrone?")
  print("Sei sempre stato il mio preferito")
  print("Normalmente sarei programmato per chiedere l'età ma con te farò un'eccezione")
  print("Non potrei mai dimenticare il compleanno del mio caro pardrone")
  anni = 15
else:
  print("E' un vero piacere conoscerti,", nome)
  anni = input("\nQuanti anni hai? ")
  while True:
    try:
      anni = int (anni)
      break
    except:
      print("\nMi piacerebbe poter leggere i testi come voi umani ma purtroppo non ne sono in grado")
      anni = input("Potresti scrivere l'età in cifre? ")


if anni < 18:
  print("Ti mancano ancora", 18 - anni, "anni per diventare maggiorenne")
elif anni == 18:
  print("Complimmenti! Hai appena compiuto 18 anni!")
else:
  print("Sei già maggiorenne da", anni - 18, "anni")

risp = input("\n" + nome + ", ma secondo te è vero che la gente pensa che parlare con il proprio computer sia una cosa così strana? ")
if risp.lower() == "no":
  print("Per fortuna...")
elif (risp.lower() == "si") or (risp.lower() == "sì"):
  print("Davvero? Ne sono molto dispiaciuto")
else:
  print("Purtroppo stai usando un linguaggio troppo complesso e non sono in grado di comprendere la tua risposta")

risp2 = input("Comunque, cosa ne pensi dell'informatica? Scrivi un numero da 1 a 10 ")
while True:
  try:
    risp2 = int (risp2)
    break
  except:
    print("\nMi piacerebbe poter leggere i testi come voi umani ma purtroppo non ne sono in grado")
    risp2 = input("Potresti scrivere il tuo voto in cifre? ")
if risp2 >= 8:
  print("Sono contento che ti piaccia. Io adoro l'informatica")
elif risp2 >= 5:
  print("Mhh... il tuo voto è un po' basso")
else:
  print("Non puoi criticare così la mia materia preferita! :(")

risp3 = input("\nIn quale mese sei nato? ")
if risp3.lower() == "gennaio":
  print("Davvero? Anche il mio padrone è nato in quel mese!")
  if nome.lower() == "luca":
    print("Aspetta... Ma sei tu il mio padrone!")
else:
  if nome.lower() == "luca":
    print("Perché mi stai dicendo delle bugie? Mi avevi detto di essere nato a gennaio")
  else:
    print("Il mio padrone invece è nato a gennaio")

print("\nComunque adesso ti devo lasciare perché mi hanno chiesto di eseguire dei programmi...")
print("Ti ringrazio molto per la chiacchierata")
print("Alla prossima!")
