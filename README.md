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


> [!WARNING] 
> Charger un fichier écrase toutes les annotations présentes !

# Commandes relatives aux annotations

Les outils développés par Valve™ sont encore bien incomplets. Aucune documentation officielle n'est disponible, mais un descriptif rapide est présenté ci-dessous.
## Création d'annotation

Les annotations sont composées d'un ou plusieurs nœuds. Alors que la plupart des annotations se limitent à un seul nœud, les annotations de grenade en utilisent trois par défaut, et vous pouvez les personnaliser pour en utiliser davantage si nécessaire.

Afin de créer une annotation, il suffit d'utiliser la commande `annotation_create` avec un ensemble de nœuds. Il existe plusieurs nœuds correspondant à différents types d'annotation créables.

> [!TIP]
> Pour rappel, si vous voulez ajouter des repères à une configuration déjà existante, pensez à la charger avec `allocation_load [config]` avant de créer les nouvelles annotations.

### Repère de grenade

Une simple annotation de grenade. La commande créera automatiquement trois nœuds en fonction de :
- Votre position actuelle et la direction à laquelle vous faites face
- Le point final de la dernière trajectoire de grenade que vous avez lancée

Pour la créer, exécuter la commande : `annotation_create grenade (type) [title]` avec comme `type` : [smoke|flash|he|fire|decoy] et pour `title` le nom de référence de la grenade à lancer.

### Spot

Crée un nœud de point de visée. Ces nœuds sont généralement utilisés pour les annotations de grenades, mais ils peuvent être utilisés pour d'autres conseils.

La commande crée le noeud en se basant sur la position actuelle du joueur :
- Position
- Direction d'orientation

Le nœud lui-même apparaîtra de couleur rougeâtre lorsque vous n'êtes pas dans la bonne position et passera à une couleur verdâtre lorsque vous vous rapprocherez de la position à partir de laquelle le nœud a été généré.

Il suffit d'exécuter la commande suivaznte : `annotation_create spot`

En dehors des grenades, ce type de nœuds peut être utilisé pour les **wallbangs**.

### Position

Place un noeud aux pieds et dans la direction du joueur. Cela peut être utile pour, par exemple, documenter les spawns.

Exécuter la commande suivante : `annotation_create position [title]` où `title` est le nom de la position que vous souhaitez donner.

### Ligne

Cette commande ne crée pas directement des lignes d'annotation, mais des points sur lesquels des lignes peuvent être dessinées.

Les nœuds de points de ligne peuvent être montés sur une surface que le joueur regarde ou flottante (la position actuelle du joueur).

Pour créer une ligne, vous devez d'abord exécuter : `annotation_create line (surface|float) new` où `(surface|float)` est l'une des options de configuration mentionnées ci-dessus sur l'endroit où le point sera monté.
Le paramètre `new` spécifie que vous créez une nouvelle ligne et que le nœud de point précédent que vous avez créé ne sera pas connecté au nœud de point nouvellement créé.

Pour dessiner une ligne, exécutez : `annotation_create line <surface|float>` et vous devriez voir la ligne nouvellement créée.

La ligne peut être connectée à d'autres points en répétant la commande ci-dessus.

### Texte

De loin la variante la plus simple, l'argument `text` de la commande `annotation_create` vous permet d'afficher une annotation textuelle dans le jeu. C'est la méthode utilisée pour les noms de positions. 

La commande prend quatre arguments : `annotation_create text [title] [desc] (float|surface) [TextFacePlayer]`.

Les arguments `title` et `desc` correspondent au titre et à la description qui devra être affiché dans le texte. Le troisième argument ne peut avoir que deux valeurs, `float` ou `surface`, et dicte le mode d'affichage du texte. Si l'on souhaite que l'annotation flotte dans les airs à une petite distance du viseur, on privilégiera `float`, ou `surface` si l'on préfère avoir un texte accolé au mur que l'on regarde. Enfin, le dernier argument, un booléen, ordonne le comportement d'orientation du texte. S'il est mis à `true`, le texte tourne pour toujours être lisible par le joueur. Sinon, il reste fixe.

> [!CAUTION] 
> Le dernier argument n'est pas pris en compte dans la commande, mais peut être édité à la main dans les fichiers *.txt.

### Enregistrement 

Pour sauvegarder les changements que vous avez réalisé sur un fichier, vous pouvez exécuter la commande `annotation_save [nomdufichier]`.

> [!TIP]
> Effectuez des enregistrement et chargement fréquemment pour ne pas perdre vos travaux !


# Architecture du repo

Au-delà des fichiers README.md et .gitgnore, le dossier est composé d'un dossier pour chaque carte, et de différents fichiers pour les types d'annotations. Ces fichiers sont listés ci-dessous : 

| Nom du fichier | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| flashes.txt    | Contient les repères pour les flashes 💥                           |
| smokes.txt     | Contient les repères pour les fumigènes 🚬                         |
| nades.txt      | Contient les repères pour les grenades explosives 💣               |
| molos.txt      | Contient les repères pour les molotovs et grenades incendiaires 🔥 |
| bangers.txt    | Contient les repères pour les travers 🧱                           |
| positions.txt  | Contient le nom des différentes positions 🗺                        |
| À venir        | ⌛                                                                  |
