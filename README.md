# Des annotations ? Kézako ?

Les annotations sont un nouveau système introduit par Valve pour afficher des symboles sur les cartes.

Celles-ci permettent de signaler des lineups pour le stuff, mais aussi des repères pour des wallbangs ou simplement du texte.

# Comment ça s'utilise ?

## Installation du dossier d'annotations

La première étape consiste à récupérer les annotations localement.

Commencez par localiser le dossier d'acceuil des annotations `steamapps\common\Counter-Strike Global Offensive\game\csgo\annotations`. Si vous ne savez pas où se trouve votre dossier d'installation de CS, vous pouvez y accéder depuis les propriétés Steam : `CS2 > Propriétés > Fichiers Intallés > Parcourir...`.

Puis, deux possibilités s'offrent à vous, en fonctions des besoins :

### Clone du repo git

Si vous comptez suivre les évolutions et/ou contribuer à ce repo d'annotations, la meilleure solution est de cloner ce repo dans le dossier. 

Puisque git ne vous permet pas de cloner dans un dossier existant, renommez le dossier `annotations` en `annotation.old`. Puis, dans le répertoire parent, exécutez `git clone https://github.com/frosqh/CS-Annotations.git annotations`. Enfin, déplacez le contenu du dossier `annotation.old` dans le nouveau dossier `annotations`. Si vous souhaitez partagez vos annotations, vous pouvez effectuer ensuite un `git commit -m 'Ma contribution'`, `git push`.

### Téléchargement du dossier

Si vous ne voulez pas vous em\*\*\*\*er avec git, vous pouvez simplement télécharger le dossier et le coller dans votre propre dossier d'annotations : 