import re

class GenewebParser():

    def individu_parse(self, fichier):
        """
        https://github.com/MaximeChallon/AdresseParser/blob/master/AdresseParser/AdresseParser.py
        Parse la chaîne mise en paramètre et retourne un dictionnaire
        :param adresse_string: chaîne de caractères de l'adresse
        :return: dict
        """
        dict_individu = {
            "id_geneweb":
            "nom": self.get_nom(),
            "prenoms":
        }

        list_individu = []

        return dict_individu










with open ('b.txt', 'rt') as myfile:  # Open lorem.txt for reading text
    test_str = myfile.read()              # Read the entire file to a string

regex_ind = r"^[A-Z]+[A-Za-zé_ ]*\n"
regex_individu = r"(?s)(?<=^pevt )(.*?)(?=end pevt)"
regex_ind_evt = r"(?s)(?<=^#)(.*?)(?=^#)"
regex_famille = r"(?s)(?<=^fam )(.*?)(?=^end$)"
regex_notes= r"(?s)(?<=^notes )(.*?)(?=^end notes$)"

matches = re.findall(regex_individu, test_str, re.MULTILINE)

list=[]
sous_list=[]
list_of_lists = []
for m in matches:
    line=m.split()
    id=(line[0:2])
    match_evt = re.findall(regex_ind_evt, m, re.MULTILINE)
    for i in match_evt:
        sous_list.append(" @@EVENEMENT@@ "+i)
    list.append([id,sous_list])
print(list[1])













"""
for m in matches:
    line_list=m.splitlines()
    list_of_lists.append(line_list)

for ind in range(0, len(list_of_lists)):
    for lines in range(0, len(ind)):
    match_evt = re.findall(regex_ind_evt, ind, re.MULTILINE)
    print(match_evt)




    for matchNum, match in enumerate(matches, start=1):
    print(matchNum.group(0))

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
     print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""