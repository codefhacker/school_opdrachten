import json

studentBestaatNiet = 0
# let op ik gebruik hier """ ipv ' omdat ik het zo makkelijker te lezen vind maar ieder heeft zijn eigen keuze 
aStudenten = """[{"voornaam":"Floris", "achternaam":"Ruysdaal", "eerstestudiejaar":"2019", "vakken":"Natuurkunde, Scheikunde"}, {"voornaam":"julia",
"achternaam":"Gomez", "vakken":"nederlands"}, {"voornaam":"Anusha", "achternaam":"Verberge" , "vakken":"russisch, chinees"}]"""
data_Studenten = json.loads(aStudenten)

studentNaam = input("wat is uw naam ?:  ")

for x in data_Studenten:
    studentBestaatNiet +=1
    
    if x["voornaam"] == studentNaam:
        try: 
            print("Voornaam:", x["voornaam"])
            print("Achternaam:", x["achternaam"])
            print("Eerstestudiejaar:", x["eerstestudiejaar"])
            print("Vakken:", x["vakken"])
            
        except:
            print("Vakken:", x["vakken"])
        
        break

    if studentBestaatNiet == len(data_Studenten):
        print(studentNaam, "komt niet in de lijst voor.")
    




