import re
import uuid


def individu_parse():
    """
    Parse la chaîne mise en paramètre et retourne un dictionnaire
    :param
    :return: dict
    """
    with open('pierre.txt', 'rt') as myfile:
        fichier = myfile.read()

    # Listes vides destinées à recevoir l'ensemle des informations parsées.
    list_individu = []
    list_evt_ind = []
    list_evt_ind_note = []

    # ***REGEX***
    # regex pour les individus
    regex_individu = r"(?s)(?<=^pevt )(.*?)(?=end pevt)"
    # regex pour les événements
    # fin de la regex (?=^#) pour inclure les notes liées à l'événement
    regex_evt = r"(?s)(?<=^#)(.*?)(?=^#)"

    # On récupère toutes les concordances avec la regex pour les individus
    matches = re.findall(regex_individu, fichier, re.MULTILINE)

    for m in matches:
        # on crée la liste des individus, un individu étant défini dans un dictionnaire
        dict_individu = {}
        line = m.split()
        id_g = line[0] + " " + line[1]
        dict_individu["id_geneweb"] = id_g
        dict_individu["id_ind"] = uuid.uuid4().hex
        list_individu.append(dict_individu)

        # On crée la liste des événéments de chaque individu, chaque événément étant défini par un dictionnaire
        match_evt = re.findall(regex_evt, m, re.MULTILINE)
        for evt in match_evt:
            dict_evt = {}
            line = evt.split()
            dict_evt["id_evt"] = uuid.uuid4().hex
            dict_evt["type"] = line[0]
            if line[1]:
                dict_evt["date"] = line[1]
            else:
                dict_evt["date"] = None
            dict_evt["ind_evt"] = [{"ind": dict_individu, "role": "objet"}]
            list_evt_ind.append(dict_evt)

            # on récupère les infos (note/wit) relatives aux événements des individus
            # pour cela on récupère les lignes de chaque evt.
            lines = evt.split("\n")
            liste = []

            for i in lines:
                lines_note = i.startswith("note ")
                if lines_note is True:
                    x = i.replace("note ", '')
                    if x != '':
                        liste.append(x)

            if liste:
                dict_note = {'related_to_evt_id': dict_evt["id_evt"], 'note': liste}
                list_evt_ind_note.append(dict_note)

                # On récupère les sources.

                # On récupère les témoins.
                # Il faudra modifier ind_evt en ajoutant le statut dans l'événement, via une deuxieme boucle.
                # lines_wit = i.startswith("wit")
                # if lines_wit is True:
                # print(i)

    # print(list_individu)
    # print(list_evt_ind)
    print(list_evt_ind_note)


if __name__ == '__main__':
    individu_parse()
