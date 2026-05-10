# Simulation Stochastique d'Évolution Métabolique

## 1. Contexte du Projet

En cherchant à optimiser ma nutrition pour la prise de masse musculaire et la récupération sportive, je me suis heurté à un problème d'imprévisibilité. La dépense énergétique quotidienne fluctue énormément, particulièrement en alternant des jours de repos avec des entraînements intenses très différents (séances de musculation lourdes vs entraînements cardio intenses de lutte). 
Plutôt que de tracker les calories au jour le jour de manière anxiogène, j'ai modélisé ce phénomène physiologique sur un trimestre (90 jours) en combinant analyse fonctionnelle et théorie des probabilités.

## 2. Modélisation Mathématique

### La Théorie (Équation Différentielle)
La variation de la masse corporelle au fil du temps est modélisée par une EDO du premier ordre liant l'apport et la dépense :
$y'(t) = c \cdot (E_{in}(t) - E_{out}(t))$

* $y(t)$ : La masse corporelle (kg) au jour $t$.
* $c$ : Constante de conversion énergétique ($c = 1/7700$).
* $E_{in}$ : Apport calorique quotidien (ciblé à 2800 kcal).
* $E_{out}$ : Dépense énergétique quotidienne.

### La Réalité (Simulation de Monte-Carlo)
Pour absorber le "bruit" des différents types d'entraînements, la dépense $E_{out}(t)$ n'est pas fixe, mais modélisée comme une variable aléatoire suivant une loi normale :
$E_{out}(t) \sim \mathcal{N}(2500, 300^2)$

Le programme utilise une méthode de Monte-Carlo pour simuler 100 trajectoires de poids indépendantes, dégageant ainsi une moyenne asymptotique et un intervalle de confiance réaliste.

## 3. Implémentation Technique

Le script est développé en Python :
* **`numpy` :** Génération vectorisée des variables aléatoires (lois normales) et intégration numérique de l'équation différentielle.
* **`matplotlib` :** Rendu graphique superposant les 100 scénarios probabilistes (cône de variance) et la trajectoire moyenne pour une lisibilité immédiate du modèle.

## 4. Exécution

```bash
# Création et activation de l'environnement virtuel
python -m venv .venv
.\.venv\Scripts\activate

# Installation des dépendances
pip install numpy matplotlib

# Lancement de la simulation et génération du graphique
python montecarlo.py