"""
ce fichier permet de lister toutes les uniter utiliser
"""
#defensseur:
#e,svg,nb_pv_def,nb_defenseur
#attaquant:
#nb_de_tire,nb_tireur,ct,f,pa

def FW(attack):
	"""
	FIRE WARRIOR
	"""
	if attack:
		return 3,4,1,10
	else:
		return 1,10,3,5,0

def MARINES(attack):
	"""
	SPACE MARINES
	"""
	if attack:
		return 3,4,1,10
	else:
		return 1,10,3,5,0

def CULTIST(attack):
	"""
	CULTIST
	"""
	if attack:
		return 3,4,1,10
	else:
		return 1,10,3,5,0

def HAMMERHEAD(attack):
	"""
	HAMMERHEAD
	"""
	if attack:
		return 3,4,1,10
	else:
		return 1,10,3,5,0


