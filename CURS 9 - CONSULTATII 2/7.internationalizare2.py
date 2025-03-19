
tari  = ["ro", "en", "de", "ar", "it", "hu", "es", "pt", "gr", "fr", "is",]
vorbe = ["Salut !", "Hello !", "Hallo !","Marhaba", "Ciao !", "Szia", "Ola !", "Ola !", "Kalimera", "Bonjour !", "Shalom !"]


while True:
    lang = input("Introduceti limba dorita:\n")
    
    index = tari.index(lang)
    print("index = ", index)
    
    print(vorbe[index])