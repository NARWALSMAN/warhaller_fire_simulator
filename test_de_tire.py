#import
import random
import annex_func
#import

############################### action_tir_1_arme sous fonction ##############################################
def lancer_de_touche(ct_touche,nbtire_touche):
	"""
	cette fonction test si combien de tir une arme reussit/ get de touche
	entrée:
		ct_touche: int -> ct du tire
		nbtire_touche: int ->nombre de tire 
	sortie:
		nbtouche_tir: int -> nombre de touche infliger au finale
	"""
	nbtouche_tir = 0
	
	for i in range(nbtire_touche):
		dice = random.randint(1,6)
		if dice >= ct_touche:
			nbtouche_tir = nbtouche_tir + 1

	return nbtouche_tir

	############################### lancer_de_blessure #####################################################
def tab_endurance_force(e_tab,f_tab):
	"""
	fonction qui calcule la valeur a dépasser pour les jet de blessure en fonction de la force et l'endurance
	entree:
		e_tab: int -> endurance pour le test
		f_tab: int -> force pour le test
	sortie:
		taux_reussite: int -> valeur a dépasser resultat du test
	"""
	taux_reussite = 0

	if e_tab >= 2*f_tab:
		taux_reussite = 6
	elif e_tab <= 2*f_tab:
		taux_reussite = 2
	elif e_tab > f_tab:
		taux_reussite = 5
	elif e_tab < f_tab:
		taux_reussite = 3
	else:
		taux_reussite = 4

	return taux_reussite
	############################### lancer_de_blessure #####################################################

def lancer_de_blessure(nbtouche_blessure,f_blessure,e_blessure):
	"""
	cette fonction test si combien de blessure une arme reussit/ get de blessure
	entrée:
		nbtouche_blessure: int -> nombre de test a faire
		f_blessure: int -> force de l'arme
		e_blessure: int -> endurance de la cible
	sortie:
		nbblessure_blessure: int -> nombre de blessure infliger au finale

	"""
	nbblessure_blessure = 0

	for i in range(nbtouche_blessure):
		dice = random.randint(1,6)
		if dice >= tab_endurance_force(e,f):
			nbblessure_blessure = nbblessure_blessure + 1

	return nbblessure_blessure

#################### lancer_de_sauvgarde #####################################
def tab_pa_sauvgarde(pa_svg,svg_svg):
	"""
	fonction qui calcule la valeur de sauvgarde en fonction de la pa
	entree:
		pa_svg: int -> pa de l'arme utiliser
		svg_svg: int ->  valeur de sauvgarde 
	sortie:
		svg_finale: int -> valur finale de la sauvgarde
	"""
	svg_finale = svg_svg+pa_svg
	if svg_finale > 6:
		svg_finale = -1
	return svg_finale
#################### lancer_de_sauvgarde #####################################	
def lancer_de_sauvgarde(nbblessure_svg,pa_svg,svg_svg):
	"""
	cette fonction test si combien de pv une arme inflige/ get de sauvgarde
	entrée:
		nbblessure_svg: int -> nombre de test a faire
		pa_svg: int -> pa de l'arme
		svg_svg: int -> valeur de sauvgarde
	sortie:
		nbpv_svg: int -> nombre de pv infliger au finale

	"""
	nbpv_svg = 0
	svg = tab_pa_sauvgarde(pa_svg,svg_svg)
	if svg != -1:							#test si le defenseur a le droit a des sauvgarde
		for i in range(nbblessure_svg):
			dice = random.randint(1,6)
			if dice < svg:
				nbpv_svg = nbpv_svg + 1
	else:
		nbpv_svg = nbblessure

	return nbpv_svg
############################### action_tir_1_arme sous fonction ##############################################

def action_tir_1_arme (ct,f,pa,e,svg):
	"""
	fonction qui simule le tir d'une arme sur une unité ennemies
	entrée:
		ct: int -> valeur de tire 
		f: int -> force de l'arme
		pa: int -> penetration d'armure
		e: int -> endurance de la cible
		svg: int -> sauvgarde
	sortie:
		nbpv: int -> nb pv perdu
	"""

	nbtouche=lancer_de_touche(ct,nbtire)
	nbblessure=lancer_de_blessure(nbtouche,f,e)
	nbpv=lancer_de_sauvgarde(nbblessure,pa,svg)
	
	return nbpv

def action_tir (nb_tireur,ct,f,pa,e,svg,nb_pv_def,nb_defenseur,reste):
	"""
	simulation de tire pour une unité entière 
	entree:
		nb_tireur: int -> nombe de figurine qui vont tirer
		ct: int -> valeur de tire 
		f: int -> force de l'arme
		pa: int -> penetration d'armure
		e: int -> endurance de la cible
		svg: int -> sauvgarde
		nb_defenseur: int -> nombre de defenseur existant
	sortie:
		nb_defenseur: int -> nb defenseur restant 
		reste: int -> nb touche qu'il reste apres le combat
	"""

	nbtouche_reussite = 0
	terminer = False

	for i in range(nb_tireur):
		nbtouche_reussite = nbtouche_reussite + action_tir_1_arme(ct,f,pa,e,svg)
	while terminer == False :
		if nbtouche_reussite >= nb_pv_def:
			nbtouche_reussite = nbtouche_reussite-nb_pv_def
			nb_defenseur = nb_defenseur-1
		if nb_defenseur == 0 or nbtouche_reussite < nb_pv_def:
			terminer = True
	if nbtouche_reussite > 0:
		reste = reste + nbtouche_reussite

	#test de reste
	if nb_defenseur > 0:
		test = True
		while test:
			if reste > nb_pv_def:
				nb_defenseur = nb_defenseur-1
				reste = reste - nb_pv_def
			
			if reste < nb_pv_def or nb_defenseur < 1:
				test = False

	return nb_defenseur,reste

def test_de_tire_fonc ():
	"""
	cette fonction fait le test de tire du logiciel
	entrée:
		rien
	sortie:
		rien
	"""
	reste=0
	nb_unit,e,svg,nb_pv_def,nb_defenseur = recup_defensseur()
	for i in range(nb_unit):
		nb_tireur,ct,f,pa=recup_attaquant(i)
		nb_defenseur,reste=action_tir(nb_tireur,ct,f,pa,e,svg,nb_pv_def,nb_defenseur,reste)
	resultat_du_test(nb_defenseur,reste)