import re
import uuid

def individu_parse():
    """
    https://github.com/MaximeChallon/AdresseParser/blob/master/AdresseParser/AdresseParser.py
    Parse la chaîne mise en paramètre et retourne un dictionnaire
    :param adresse_string: chaîne de caractères de l'adresse
    :return: dict
    """
    with open('pierre.txt', 'rt') as myfile:
        fichier = myfile.read()

    regex_individu = r"(?s)(?<=^pevt )(.*?)(?=end pevt)"
    matches = re.findall(regex_individu, fichier, re.MULTILINE)
    list_individu = []

    for m in matches:
        line = m.split()
        id_g = line[0]+" "+line[1]
        dict_individu = {
        "id_geneweb": id_g,
        "id": uuid.uuid4().hex
    }
        list_individu.append(dict_individu)

    print(list_individu)


if __name__ == '__main__':
    individu_parse()















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