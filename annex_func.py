#import
#import
def ecrit_defensseur(e,svg,nb_pv_def,nb_defenseur):
    """
    cette fonction ecrit tout les inforùations pour les test sur les défensseur
    entrée:
            nb_unit 		= int ->  nombre d'uniter a faire tirer
            e 				= int ->  endurance de la cible
            svg				= int ->  sauvgarde
            nb_pv_def		= int ->  nombre de pv d'un défensseur
            nb_defenseur	= int ->  nombre de defenseur existant
    sortie:
            rien
    """
    print("le nombre de defensseur: "+str(e))
    print("la sauvgarde des defensseur: "+str(svg))
    print("le nombre de pv des defensseur: "+str(nb_pv_def))
    print("l'endurance du defenseur': "+str(nb_defenseur))

def ecrit_attaquant(nb_de_tire,nb_tireur,ct,f,pa):
	"""
	cette fonction ecrit tout les inforùations pour les test sur les attaquant
	entrée:
		nb_de_tire		= int -> nombre de tire par arme
		nb_tireur 		= int -> nombe de figurine qui vont tirer
		ct 				= int -> valeur de tire
		f 				= int -> force de l'arme
		pa				= int -> penetration d'armure 
	sortie:
		rien
	"""
	print("le nombre de tire par arme: "+str(nb_de_tire))
	print("le nombre de tireur: "+str(nb_tireur))
	print("la ct du tireur: "+str(ct))
	print("la force de l'arme: "+str(f))
	print("la PA (penetration armor de l'arme: "+str(pa))
def recup_defensseur():
	"""
	cette fonction récupère tout les inforùations pour les test sur les défensseur
	entrée:
		rien
	sortie:
		e 				= int ->  endurance de la cible
		svg				= int ->  sauvgarde
		nb_pv_def		= int ->  nombre de pv d'un défensseur
		nb_defenseur	= int ->  nombre de defenseur existant
	"""
	e_annex = int(input("Entrez l'endurance de l'uniter: "))
	svg_annex = int(input("Entrez la sauvgarde des figurines: "))
	nb_pv_def_annex = int(input("Entrez le nombre de pointde bie (pv) des défensseur: "))
	nb_defenseur_annex = int(input("Entrez le nombre de défensseur: "))
	return e_annex,svg_annex,nb_pv_def_annex,nb_defenseur_annex

def recup_attaquant(index):
	"""
	cette fonction récupère tout les inforùations pour les test sur les attaquant
	entrée:
		index			= int -> index de quel uniter choisir 
	sortie:
		nb_de_tire		= int -> nombre de tir par arme
		nb_tireur 		= int -> nombe de figurine qui vont tirer
		ct 				= int -> valeur de tire
		f 				= int -> force de l'arme
		pa				= int -> penetration d'armure
	"""
	print("crrer votre uniter qui vas tirer")
	print("index "+str(index))
	nb_de_tire = int(input("Entrez le nombre de tire par arme: "))
	nb_tireur_annex = int(input("Entrez le nombre de tireur dans l'uniter: "))
	ct_annex = int(input("Entrez la ct du tireur: "))
	f_annex = int(input("Entrez la force de l'arme: "))
	pa_annex = int(input("Entrez la PA (penetration armor) de l'arme: "))
	return nb_de_tire,nb_tireur_annex,ct_annex,f_annex,pa_annex

def recup_utilitaire():
	"""
	cette fonction récupère tout les inforùations pour les test (version utilitaire)
	entrée:
		rien
	sortie:
		nb_unit 		= int -> nombre d'uniter qui attaque
	"""
	nb_unit_annex = int(input("Entrez le nombre d'uniter a tirer: "))
	return nb_unit_annex

def resultat_du_test(nb_defenseur_fini,reste_fini):
	"""
	cette fonction entre les donnée du resultat du test de tire
	entrée:
		nb_defensseur_fini	= int -> nombre de defensseur encore vivant
		reste_fini			= int -> nombre de dé restant 
	sortie:
		rien
	"""
	print("il reste un total de: "+str(nb_defenseur_fini)+" défensseur encore vivant.")
	print("il reste "+str(reste_fini)+" dé")
