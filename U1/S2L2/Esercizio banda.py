#/**Scrivere un programma in Python che genera un nome per una band 
#musicale utilizzando due input forniti dall'utente: 
#la città di origine e il nome del proprio animale domestico.

#Descrizione dell'Esercizio' In questo esercizio, dovrai creare un 
#programma che esegue le seguenti operazioni: 1. 2. 3. Richiesta di Input: Il programma deve chiedere all'utente di inserire: 
#○ Il nome della città di origine.
#○ Il nome del proprio animale domestico. 
#Generazione del Nome della Band: Una volta ricevuti gli input, il programma deve combinare il nome della città e il nome dell'animale'
#'in un'unica stringa che rappresenta il nome della band.
#Output: Il programma deve stampare a video il nome generato per la band**/#



print("Escribe el nimbre de tu ciudad de origen:")
ciudad=input("")
print("Ahora escribe el nombre de tu mascota:")
mascota=input("")
nome_band = ciudad + " " + mascota
print("el nombre de la band es %s"% nome_band)