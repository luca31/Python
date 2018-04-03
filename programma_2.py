print("AVVENTURA TESTUALE")
nome = input("inserisci il tuo nome:   ")
print("era una normale giornata di primavera quando al tg si sente una tragica notizia.")
print("una bomba atomica è esplosa nel nord italia")
print("subito dopo questa notizia la gente comincia a fare le valigie e allontanarsi più possibile.")
print()
print("tu e il tuo amico avete due possibilità")
print("1) fuggire con qualcuno")
print("2) cercare riparo nella vostra cantina")
a = input()
print()


if a == "1":
	print("decidi così di chiedere un passaggio a qualcuno in fuga")
	print("una volta arrivato su una strada maggiore di rendi conto che non si può proseguire")
	print("la gente in movimento è troppa: le strade non sono più percorribili.")
	print('ora bisogna decidere se:')
	print('1) proseguire fuori strada')
	print('2) tornare a casa e rifugiaresi nella cantina')
	b = input()
	print()
	if b == "1":
		print("decidi di proseguire fuori strada.")
		print("a causa di alcuni incendi scoppiati a causa di fabbriche abbandonate")
		print("durante il tragitto perdi i sensi, inalando dei gas tossici")
	else:
		print("decidi così di tornare indietro e rifugiarti nella tua cantina.")
		print("resti li per molte settimane")
		print("le provviste scarseggiano e a causa della stanchezza perdi i sensi")
else:
	print("decidi di preparare più provviste possivili e rifugiarti in cantina")
	print("resti li per molte settimane")
	print("le provviste scarseggiano e a causa della stanchezza perdi i sensi")

print("...")
print("...")
print("...")


print("ti sei appena risvegliato")
print("in qualche modo sei riuscito a sopravvivere all'esplosione e alle conseguenze")
print("sono passati alcuni mesi dall'esplosione e le radiazioni non sembrano più un pericolo")
print('devi sciegliere se uscire allo scoperto o restare ancora nel rifugio')
print('1) resti lì')
print('2) esci allo scoperto')
c = input()
print()

if c == "1":
	print("decidi di non uscire nonostante la scarsità di risorse")
	print("passati alcuni giorni non hai altra scelta: devi abbandonare il rifugio")
else:
	print("ti appresti così ad abbandonare il rifugio")

print("una volta uscito ti rendi conto di una cosa:")
print("tu e il tuo amico siete tra gli ultimi abitanti della zona")
print("decidete così di andare in esplorazione nelle circostanze")
print("dovete decidere se andare a nord o a sud")
print("1) andate a nord")
print("2) andate a sud")
d = input()
print()

if d == "1":
	print("vi dirigete a nord, orientandovi con la luce solare")
else:
	print("vi dirigete a sud, orientandovi con la luce solare")

print("l'aria è cupa e la desolazione del paesaggio è terrorizzante")	
print("la sera è vicina e voi vi avvicinate ad una grande città abbandonata")
print("arrivati nella periferia di essa dovete sciegliere se addentrarvi in un edificio per la notte")
print("o restare allo scoperto")
print("1)restate allo scoperto")
print("2) vi addentrate in un edificio")
e = input()
print()

if e == "1":
	print("rischiosamente decidete di rimanere alle intemperie.")
	print("il tutto sembra troppo tranquillo")
	print("sentite dei passi")
	print("non sono i vostri")
else:
	print("decidete di entrare in un edificio per cercare provviste e passare la notte sotto un tetto")
	print("purtoppo l'apparenza inganna e appena cala il sole")
	print("vi accorgete di migliaia di occhi che vi fissano nel buio")
	print("(°°) (°°) (°°) (°°) (°°) (°°) (°°) (°°)")
	print("(°°) (°°) (°°) (°°) (°°) (°°) (°°) (°°)")
	print("(°°) (°°) (°°) (°°) (°°) (°°) (°°) (°°)")

print("dovete decidere se restare immoboli o scappare")
print("1) restate immobili")
print("2) scappate")
f = input()

if f == "1":
	print("tutto è fermo")
	print("il cuore batte fortissimo")
	print("l'unica cosa che si può fare è aspettare")
	print("passano dei secondi interminabili, ma dopo qualche minuto")
	if e == "1":
		print("i passi si fanno sempre più lontani e voi vi addormentate tranquilli")
	else:
		print("gli occhi spariscono e voi vi addormentete tranquilli")

else:
	print("comunciate a correre all'impazzata")
	print("dietro di voi sentite migliaia di creature che vi inseguono")
	print("dopo qualche centinaio di metri di corsa no ce la fate più")
	print("capite che è finita quando vedete tutte quelle creature venirvi incontro")
	print("vi fissate a vicenda")
	print("...")
	print("...")
	print("...")

print("FINE")
