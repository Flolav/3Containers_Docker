import pandas as pd  # Importe la bibliothèque pandas pour la manipulation de données.
import streamlit as st  # Importe la bibliothèque Streamlit pour la création d'interfaces web.
from models import predict_similarity  # Importe la fonction de prédiction de similarité du fichier models.py.
from data.data import add_sentences_to_hash, get_past_inputs  # Importe des fonctions du fichier data.py pour gérer les données.

# Configure la page Streamlit avec un titre spécifique.
st.set_page_config(page_title="Sentence Similarity")

# Ajoute un titre à l'application web.
st.title("Sentence Similarity Checker")

# Ajoute une description ou un sous-titre sous forme de texte markdown.
st.markdown("""
This application uses NLP techniques to compute the similarity between two sentences. 
Enter two sentences to see how similar they are.
""")

# Crée deux champs de saisie de texte pour les phrases à comparer.
txt1 = st.text_input("Enter Sentence 1")
txt2 = st.text_input("Enter Sentence 2")

# Crée un bouton pour lancer la prédiction de similarité.
predict_btn = st.button("Predict Similarity")

# Bloc conditionnel qui s'exécute lorsque l'utilisateur clique sur le bouton de prédiction.
if predict_btn:
    if txt1 and txt2:  # Vérifie que les deux phrases ont été saisies.
        similarity = predict_similarity(txt1, txt2)  # Appelle la fonction de prédiction de similarité.
        st.success(f"Similarity: {round(similarity, 2)}")  # Affiche le score de similarité arrondi à deux décimales.
        add_sentences_to_hash(txt1, txt2, similarity)  # Ajoute les phrases et leur score de similarité dans une base de données ou une structure de données.
    else:
        st.error("Please enter both sentences to get a similarity score.")  # Affiche un message d'erreur si les deux phrases ne sont pas saisies.

# Crée une case à cocher pour afficher ou non les requêtes précédentes.
show_prev_queries = st.checkbox("Previous Queries")

# Bloc conditionnel qui s'exécute si l'utilisateur choisit d'afficher les requêtes précédentes.
if show_prev_queries:
    query_list = get_past_inputs()  # Récupère la liste des entrées précédentes.
    query_df = pd.DataFrame(query_list)  # Convertit la liste en DataFrame pandas pour l'affichage.
    
    st.write("Previous Queries and their Similarities")  # Ajoute un titre pour la section des requêtes précédentes.
    st.write(query_df)  # Affiche le DataFrame des requêtes précédentes et leurs scores de similarité.
