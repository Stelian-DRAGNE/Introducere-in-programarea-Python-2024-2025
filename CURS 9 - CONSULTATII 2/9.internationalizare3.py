

tari  = ["ro", "en", "de", "ar", "it", "hu", "es", "pt", "gr", "fr", "is",]
vorbe = ["Salut !", "Hello !", "Hallo !","Marhaba", "Ciao !", "Szia", "Ola !", "Ola !", "Kalimera", "Bonjour !", "Shalom !"]

tari_vorbe = {}

for i in range(len(tari)):
    tari_vorbe[tari[i]] = vorbe[i]

print(tari_vorbe)