import json

# let op ik gebruik hier """ ipv ' dit is waarschijnlijk een fout in het boek 
aStudenten = """[{"voornaam":"Floris", "achternaam":"Ruysdaal", "eerstestudiejaar":"2019", "vakken":"Natuurkunde, Scheikunde"}, {"voornaam":"julia",
"achternaam":"Gomez", "vakken":"nederlands"}, {"voornaam":"Anusha", "achternaam":"Verberge" , "vakken":"russisch, chinees"}]"""
data_Studenten = json.loads(aStudenten)

print(data_Studenten)

for student in data_Studenten:
    print(student["voornaam"])

# let op ik gebruik hier geen ; dat moet in c niet in python

voornaam = str(input("typ uw voornaam "))
strStudenten = "".join(aStudenten)  
i = strStudenten.find(voornaam)
print(i)

if len(voornaam) <= 4:
    print("deze student bestaat niet helaas ")
elif int(i) == -1:
    print("deze student bestaat niet helaas ")





