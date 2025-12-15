import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

print("✅ Tous les modules sont importés avec succès !")

# Chargement des données depuis le fichier CSV
data = pd.read_csv("Book.csv", sep=";", header=None, names=["vitesse", "danger"])

sns.boxplot(x="danger", y="vitesse", data=data)
plt.title("Exemple graphique : vitesse selon danger")
plt.show()
