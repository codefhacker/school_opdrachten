import json

# let op ik gebruik hier """ ipv ' dit is waarschijnlijk een fout in het boek 
aStudenten = """[{"voornaam":"Floris", "achternaam":"Ruysdaal"}, {"voornaam":"julia",
"achternaam":"Gomez"}, {"voornaam":"Anusha", "achternaam":"Verberge"}]"""
data_Studenten = json.loads(aStudenten)

print(data_Studenten)

for student in data_Studenten:
    print(student["voornaam"])

# let op ik gebruik hier geen ; dat moet in c niet in python
strStudenten = "".join(aStudenten)  
i = strStudenten.find("Gomez")
print(i)

