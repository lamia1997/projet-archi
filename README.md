# projet-archi
Objectif du projet : L'objectif principal du projet est la classification de text issus d'article de Wikipedia en differentes categories, avec plusieurs degrés de complexité (Plus de details dans le lien vers le dataset) <br />
Data récuperés de Kaggle :https://www.kaggle.com/datasets/danofer/dbpedia-classes?select=DBPEDIA_train.csv  <br />
On commence par lancer l'image docker : docker-compose up -d <br />
Nous avons entrainé nos modeles en avance dans notre notebook project qui est en meme temps un laboratoire pour tester des fonctionalités ainsi 
que le lieu ou on sauvegarde nos pipelines de preprocessing. <br />
Pour visualiser les resultats du consumer il faut tout d'abord load les modeles et les pipelines de preprocessing puis mettre fin 
à la session spark courante puis relancer une nouvelle session, lancer le producer en local puis la cellule du consumer. <br />
Le streaming des données affiche pour chaque donnée de test envoyée, 
la prediction dpnnée par le modele ainsi que le label pour chaque niveau et chaque preprocessing differents et stocke en meme temps dans des dataframe le couple prediction/label. <br />
Vu le nombre elevé de données dans notre test set, on arrete le consumer manuellement. <br />
Pour la visualisation, nous avons instancié des objets de type MulticlassMetrics à partir des dataframe sauvegardé puis on affiche une figure qui nous donne la precision des differents modeles. <br />
Autre visualisation mais peu interessante est la matrice de confusion pour les modeles à 7 classes, meme si elle n'est pas parlante, la vue de la diagonale nous permet de savoir si les modeles sont efficaces. 



⚠️ : PC performant obligatoire.
