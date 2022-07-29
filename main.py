import re
import uuid
import io

# Pour nettoyer le code, regarder
# https://github.com/MaximeChallon/AdresseParser/blob/master/AdresseParser/AdresseParser.py


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
        line = m.split()
        id_g = line[0] + " " + line[1]
        dict_individu = {
            "id_geneweb": id_g,
            "id_ind": uuid.uuid4().hex
        }
        list_individu.append(dict_individu)

        # On crée la liste des événéments de chaque individu, chaque événément étant défini par un dictionnaire
        match_evt = re.findall(regex_evt, m, re.MULTILINE)
        for evt in match_evt:
            line = evt.split()
            dict_evt = {
                "id_evt": uuid.uuid4().hex,
                "type": line[0],
                "date": line[1],
                "ind_evt": [{"ind": dict_individu, "role": "objet"}]
            }
            list_evt_ind.append(dict_evt)
            # on récupère les infos (note/wit) relatives aux événements des individus
            # pour cela on récupère les lignes de chaque evt.
            lines = evt.split("\n")

            liste=[]
            for i in lines:
                lines_note = i.startswith("note ")
                #lines_note_vide = i.startswith(" ",5,7)
                if lines_note is True:
                    x=i.replace("note ","")
                    liste.append(x)
            new_list = [x for x in liste if x != '']
            print(new_list)

                # On récupère les témoins.
                # Il faudra modifier ind_evt en ajoutant le statut dans l'événement, via une deuxieme boucle.
                #lines_wit = i.startswith("wit")
                #if lines_wit is True:
                    #print(i)


if __name__ == '__main__':
    individu_parse()

