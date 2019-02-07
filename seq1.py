from Bio import Entrez
from Bio import SeqIO

Entrez.email = "asenchukova@gmail.com"


handle = Entrez.esearch(db="genome", term="Homo sapiens")
record = Entrez.read(handle)
record["IdList"]
orgID = []
orgID = record["IdList"]
print(orgID)

handle = Entrez.elink(dbfrom="genome", id=orgID[1], db="protein")
record = Entrez.read(handle)
for link in record[0]["LinkSetDb"][0]["Link"]:
	print(link["Id"])

proteinID = []
proteinID = link["Id"]
print(proteinID)

handle = Entrez.efetch(db="protein", id=link["Id"],
                       rettype="gb",
                       retmode="text")

print(handle.read())
