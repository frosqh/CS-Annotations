# Des annotations ? Kézako ?

Les annotations sont un nouveau système introduit par Valve™ pour afficher des symboles sur les cartes.

Celles-ci permettent de signaler des lineups pour le stuff, mais aussi des repères pour des wallbangs ou simplement du texte.

# Comment ça s'utilise ?

## Installation du dossier d'annotations

La première étape consiste à récupérer les annotations localement.

Commencez par localiser le dossier d'accueil des annotations `steamapps\common\Counter-Strike Global Offensive\game\csgo\annotations`. Si vous ne savez pas où se trouve votre dossier d'installation de CS, vous pouvez y accéder depuis les propriétés Steam : `CS2 > Propriétés > Fichiers Intallés > Parcourir...`. Si le dossier `annotations` n'est pas présent, vous pouvez juste le créer.

Puis, deux possibilités s'offrent à vous, en fonctions des besoins :

### Clone du repo git

Si vous comptez suivre les évolutions et/ou contribuer à ce repo d'annotations, la meilleure solution est de cloner ce repo dans le dossier. 

Puisque git ne vous permet pas de cloner dans un dossier existant, renommez le dossier `annotations` en `annotation.old`. Puis, dans le répertoire parent, exécutez `git clone https://github.com/frosqh/CS-Annotations.git annotations`. Enfin, déplacez le contenu du dossier `annotation.old` dans le nouveau dossier `annotations`. Si vous souhaitez partagez vos annotations, vous pouvez effectuer ensuite un `git commit -m 'Ma contribution'`, `git push`.

### Téléchargement du dossier

Si vous ne voulez pas vous em\*\*\*\*er avec git, vous pouvez simplement télécharger le dossier [ici](https://github.com/frosqh/CS-Annotations/archive/refs/heads/main.zip) et le coller dans votre propre dossier d'annotations 

## Chargement des annotations

### Lancement d'une carte CS2

La première étape pour utiliser les annotations consiste à lancer une carte CS2 (duh).

Si vous êtes adeptes des interfaces, une fois le jeu lancé, `Jouer > Entraînement > de_???`. Vérifiez bien que les options "Échauffement infini", "Munitions Infinies" et "Caméra Grenade" sont activées. 

Si vous préférez la console, vous pouvez utiliser la commande `map de_???` suivie de : 

```
bot_kick;
mp_warmuptime 999999;
mp_warmup_start;
mp_warmup_pausetimer 1;
sv_cheats 1;
sv_infinite_ammo 1;
sv_grenade_trajectory_prac_pipreview true;
mp_maxmoney 100000;
mp_startmoney 100000;
```

### Chargement du fichier d'annotations

Une fois en jeu, il faut commencer par autoriser l'utilisation d'annotations `sv_allow_annotations true`. Une fois cela fait, on peut charger le fichier qui nous intéresse avec la commande `annotation_load [map]/[type]` où \[map\] et \[type\] sont à renseigner en fonction de vos besoins et en suivant la nomenclature rappelée [plus bas](https://github.com/frosqh/CS-Annotations?tab=readme-ov-file#architecture-du-repo).

# Commandes relatives aux annotations

Les outils développés par Valve™ sont encore bien incomplets. Aucune documentation officielle n'est disponible, mais un descriptif rapide est présenté ci-dessous.
## Création d'annotation

Afin de créer une annotation, on utilise la commande `annotation_create`. Il existe plusieurs modes correspondant à différents types d'annotation créables.

De manière générale, si vous voulez ajouter des repères à un config déjà existante, pensez à la charger avec `allocation_load [config]` avant de créer les nouvelles annotations.
### Repère de grenade

Le premier de ces modes correspond à celui qui nous intéresse le plus : les repères de grenades. 

La version la plus simple de la

### Spot

### Position

### Ligne

### Texte

De loin la variante la plus simple, l'argument `text` de la commande `annotation_create` vous permet d'afficher une annotation textuelle dans le jeu. C'est la méthode utilisée pour les noms de positions. 

La commande prend quatre arguments : `annotation_create text [title] [desc] (float|surface) [TextFacePlayer]`.

Les arguments `title` et `desc` correspondent au titre et à la description qui devra être affiché dans le texte. Le troisième argument ne peut avoir que deux valeurs, `float` ou `surface`, et dicte le mode d'affichage du texte. Si l'on souhaite que l'annotation flotte dans les airs à une petite distance du viseur, on privilégiera `float`, ou `surface` si l'on préfère avoir un texte accolé au mur que l'on regarde. Enfin, le dernier argument, un booléen, ordonne le comportement d'orientation du texte. S'il est mis à `true`, le texte tourne pour toujours être lisible par le joueur. Sinon, il reste fixe.

>[!Warning] Attention
>Le dernier argument n'est pas pris en compte dans la commande, mais peut être édité à la main dans les fichiers *.txt.




### Enregistrement 

# Architecture du repo

Au-delà des fichiers README.md et .gitgnore, le dossier est composé d'un dossier pour chaque carte, et de différents fichiers pour les types d'annotations. Ces fichiers sont listés ci-dessous : 

| Nom du fichier | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| flashes.txt    | Contient les repères pour les flashes 💥                           |
| smokes.txt     | Contient les repères pour les fumigènes 🚬                         |
| nades.txt      | Contient les repères pour les grenades explosives 💣               |
| molos.txt      | Contient les repères pour les molotovs et grenades incendiaires 🔥 |
| bangers.txt    | Contient les repères pour les travers 🧱                           |
| positions.txt  | Contient le nom des différents positions 🗺                        |
| À venir        | ⌛                                                                  |
