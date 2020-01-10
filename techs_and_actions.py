# This file aims to create the technology tree,
# and the functions (read: actions) that are unlocked
# with each action.

# This file is going to be less object-oriented
# than the other ones. Woo-hoo!

# This dictionary has the techs as keys,
# what inherits from them as values.

techDict = {
	'hunting':       ['burden', 'husbandry'],
	'gathering':     ['farming', 'scavenging'],
	'fishing':       ['sailing', 'camping'],
	'combat':        ['swordsmanship', 'defense'],

	'burden':        ['', ''],
	'husbandry':     ['', '']
	'farming':       ['', '']
	'scavenging':    ['', '']
	'sailing':       ['', '']
	'camping':       ['', '']
	'swordsmanship': ['', '']
	'defense':       ['', '']
}

techInheritanceDict = {}

# 'Filling up' techInheritanceDict
for tech in techDict.keys():
	for inheritedTech in techDict[tech]:
		techInheritanceDict[inheritedTech] = tech

# To make sure no doubling up took place
def check_tech_dict():

	valueTechs = []

	for tech in techDict.keys():
		if techDict.keys().count(tech) != 1:
			raise ValueError('Sorry, {} has two entries.').format(tech)
		if techDict[tech] in valueTechs:
			raise ValueError('Sorry, {} inherits from two techs: {} and {}.').format(techDict[tech], tech, valueTechs.get(techDict[techs]))