from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    indice_sim = 0
    simMax = 0
    for i in range (0, 10):
        image_resizee = image_localisee.resize(liste_modeles[i].H, liste_modeles[i].W)
        if image_resizee.similitude(liste_modeles[i]) > simMax:
            indice_sim = i
            simMax = image_resizee.similitude(liste_modeles[i])
    return indice_sim

