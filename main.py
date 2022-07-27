import re
import uuid


def individu_parse():
    """
    https://github.com/MaximeChallon/AdresseParser/blob/master/AdresseParser/AdresseParser.py
    Parse la chaîne mise en paramètre et retourne un dictionnaire
    :param
    :return: dict
    """
    with open('pierre.txt', 'rt') as myfile:
        fichier = myfile.read()

    regex_individu = r"(?s)(?<=^pevt )(.*?)(?=end pevt)"
    matches = re.findall(regex_individu, fichier, re.MULTILINE)
    list_individu = []

    for m in matches:
        line = m.split()
        id_g = line[0] + " " + line[1]
        dict_individu = {
            "id_geneweb": id_g,
            "id": uuid.uuid4().hex
        }
        list_individu.append(dict_individu)

    print(list_individu)


if __name__ == '__main__':
    individu_parse()
