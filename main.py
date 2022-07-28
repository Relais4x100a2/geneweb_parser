import re
import uuid


def individu_parse():
    """
    https://github.com/MaximeChallon/AdresseParser/blob/master/AdresseParser/AdresseParser.py
    Parse la chaîne mise en paramètre et retourne un dictionnaire
    :param
    :return: dict
    """
    with open('b.txt', 'rt') as myfile:
        fichier = myfile.read()

    regex_individu = r"(?s)(?<=^pevt )(.*?)(?=end pevt)"
    regex_evt = r"(?s)(?<=^#)(.*?)(?=\n)"
    matches = re.findall(regex_individu, fichier, re.MULTILINE)
    list_individu = []
    list_evt_ind = []

    for m in matches:
        # on crée la liste des individus, un individu étant défini dans un dictionnaire
        line = m.split()
        id_g = line[0] + " " + line[1]
        dict_individu = {
            "id_geneweb": id_g,
            "id_ind": uuid.uuid4().hex
        }
        list_individu.append(dict_individu)
        # on crée la liste des événéments de chaque individu, chaque événément étant défini par un dictionnaire
        match_evt = re.findall(regex_evt, m, re.MULTILINE)
        for evt in match_evt:
            line = evt.split()
            dict_evt = {
                "id_evt": uuid.uuid4().hex,
                "type": line[0],
                "ind_evt": [{"ind": dict_individu, "role": "objet"}]
                #"date": line[1]
            }
            list_evt_ind.append(dict_evt)
            # il faudra modifier ind_evt en ajoutant le statut dans l'événement
        #, re.MULTILINE
        #print(m)
        #for m in matches:
            #print(m)


    print(list_evt_ind)


if __name__ == '__main__':
    individu_parse()
