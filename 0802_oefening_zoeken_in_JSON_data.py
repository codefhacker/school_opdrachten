# script_0802_zoeken_in_JSON_data
import json

aStudenten='[{"voornaam":"Floris", "achternaam":"Ruysdaal", "eerstestudiejaar":"2019", "vakken":"Natuurkund, Scheikunde"}, {"voornaam":"Julia", "achternaam":"Gomez", "vakken":"Nederlands"}, {"voornaam":"Anusha", "achternaam":"Verberge", "vakken":"Russisch, Chinees"}]'

data_Studenten = json.loads(aStudenten)

print(data_Studenten)

for student in data_Studenten:
    print(student["voornaam"])
    
strStudenten = "".join(aStudenten);
i = strStudenten.find("Gomez");
print(i)