# Pour bien commencer

## La balise HTML
Elle déclare le type de document. Dans la balise ouvrante, on peut ajouter la langue utilisée pour le texte. Cela aide, par exemple pour que le navigateur traduise la page en une autre langue de façon automatique:
```HTML
</!DOCTYPE html>
<html lang="languageId-RegionId">
</html>
```
Pour le français, en France, on a:
```HTTML
<html lang="fr-FR">
</html>

```
Si on est en Belgique, on peut alors mettre "fr-BE", ou en chine: "zh-CN".

## Le header
Pour bien commencer, il faut inclure les ressources "générales". CAD le VP (pour être responsive), auteur(s), description de la page et mot-clefs pour le référencement, les polices d'écriture (de Google) et le fichier CSS commun.
```HTML
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="author" content="@N1coc4colA, @Archimosse">
		<meta name="description" content="Application pour contacts en ligne">
		<meta name="keywords" content="Contacts, DB, Py, HTML, CSS">
		<title>Contacts</title>
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Oxygen&display=swap" rel="stylesheet">
		<link rel="stylesheet" href="styles.css">
	</head>
````

On peut y ajouter les balises suivantes pour la **favicon** ainsi que le **titre** de la page:
```HTML
<link rel="icon" href="https://th.bing.com/th/id/R.087584d26e16365c5a3686bfdd6b9c42?rik=PCuLx1mFpdPCiQ&riu=http%3a%2f%2fwww.newdesignfile.com%2fpostpic%2f2009%2f08%2fcontact-icon_179510.png&ehk=vSIGfep7%2bkYO0S4w9DnT4Bb9QFlN1xxrH6Xg3oK3o18%3d&risl=&pid=ImgRaw&r=0">
<title>Contacts</title>

```

## Le body
Pour les règles de styles dépendantes du contenu, on utilise un script ECMA afin d'ajouter des classes sur ce que l'on veut. Cependant, pour s'assurer que les scripts de nos pages s'exécutent quand tout le contenu est bien chargé, on plage les **balises de scripts à la fin de notre balise body** comme cela:
```HTML
	<body>
		<script src="styling.js"></script>
	</body>
```

# Composants

## Structure visuelle
Visuellement, on a:
Le fond -> La boîte de dialogue -> le contenu: [titre, contenu, contrôles]
Les balises correspondantes sont:
body    -> div                  -> [div, div, div]
Les classes correspondantes sont:
Aucune  -> container            -> [title, content, controls]

## Classes implémentées

### Titre de fenêtre
La classe est **title** et s'intègre dans la balise ayant comme classe **container**

### Le contenu
La classe est **content** et s'intègre dans la balise ayant comme classe **container**

### Entrée
C'est une **div** qui contient, par exemple, dans un formulaire "Mot de passe:" suivi d'une entrée (input) pour entrer ce même mot de passe.
La classe à utiliser est **Entry**.

### Titre d'entrée
Est destiné à la balise **label** de formulaires.
Dans une **div** ayant comme classe **Entry** où l'on doit entrer un mot de passe, on peut mettre un **label** ayant comme classe **Entry-Title** et texte "Mot de passe:".

### Boutons radio
Les boutons **radio** des formulaires ne s'intègrent pas toujours bien. Pour cela, au lieu de simplement mettre un **input** de type "radio", on met le code HTML ci-dessous (qui marche tout aussi bien):
```HTML
	<label class="radio radio-before" for="mobile">
		<span class="radio__input">
			<input type="radio" name="type" id="mobile" value="mobile" checked>
			<span class="radio__control"></span>
		</span>
		<span class="radio__label">Mobile</span>
	</label>

```
Les valeurs des attributs for, name, id, value 

### Contrôles
Pour mettre des contrôles en bas de la mise en page pour le dialogue, on et une div de classe **controls**

#### Contrôles droits
Cette zone doit servir uniquement au bouton "Annuler", "Retour", ou tout autre action soit négative, dangereuse ou pouvant entraîner une perte de données.
C'est une **div** de class **right-controls**, à mettre dans la div de classe **controls**.

#### Contrôles gauches
Dédié aux boutons aux effets **positifs** comme ajouter une donnée. Ou "Annuler" dans le cas où l'on veut suprimmer une donnée.
C'est une **div** de classe **left-controls**.

#### Contrôles du centre
Zone servant aux autres boutons, par exemple pour un bouton "Aide", ou "Renvoyer". La classe de la div doit être **center-controls**.

### Boutons de contrôle
Il y a 3 types de boutons de contrôle. Le basique, le positif et négatif.
Ils sont souvent des éléments de type **a**, **button** ou **input**. Cependant, les **input** lors du survol ont un petit bug d'interface sur WebKit, ou uniquement sur Microsoft Edge.

#### Bouton
Elément de classe **button**. Sers pour n'importe quel bouton, par exemple un bouton "Aide".

#### Bouton Retour, ou Annuler (négatif)
Elément de classe **button-back**.

#### Bouton Suivant, ou Appliquer (positif)
Elément de classe **button-next**

## Et en HTML?
En HTML, tout cela donne la forme suivante:
```HTML
</!DOCTYPE html>
<html lang="fr-FR">
	<head>
		<meta charset="utf-8">
		<title>Contacts</title>
		<link rel="icon" href="https://th.bing.com/th/id/R.087584d26e16365c5a3686bfdd6b9c42?rik=PCuLx1mFpdPCiQ&riu=http%3a%2f%2fwww.newdesignfile.com%2fpostpic%2f2009%2f08%2fcontact-icon_179510.png&ehk=vSIGfep7%2bkYO0S4w9DnT4Bb9QFlN1xxrH6Xg3oK3o18%3d&risl=&pid=ImgRaw&r=0">
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
		<link href="https://fonts.googleapis.com/css2?family=Oxygen&display=swap" rel="stylesheet">
		<link rel="stylesheet" href="styles.css">
	</head>
	<body>
		<form action="Ajouter un contact" method="get" class="form-example">
			<div class="container">
				<div class="title">Créer un nouveau contact</div>
				<div class="content">
					<div class="Entry">
						<label class="Entry-Title" for="name">Nom du contact</label>
						</br>
						<input type="text" name="name" id="name" placeholder="Asap Arnash" required>
					</div>
				</div>
				<div class="controls">
					<div class="left-controls">
						<!-- Utiliser une balise input ou anchor donnera le même rendu visuel. Autant utiliser une anchor vu qu'on ne passe auncune donnée. -->
						<a href="javascript:history.back()" class="button-back">Annuler</a>
					</div>
					<div class="center-layout">
					</div>
					<div class="right-controls">
						<button class="button-back" type="submit">Ajouter</button>
					</div>
				</div>
			</div>
		</form>
		<script src="styling.js"></script>
	</body>
</html>
```
Il faut noter, pour le bouton "Annuler", **l'utilisation du javascript**. La commande permet de faire un **retour à la page précédente** de l'historique de navigation.
