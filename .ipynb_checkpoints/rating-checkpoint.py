import streamlit as st
from streamlit_option_menu import option_menu

# 1. Configuration de la page
st.set_page_config(page_title="Rating Crédit OAD", layout="wide")

# 2. Barre de navigation horizontale
# Tu peux choisir l'icône (Bootstrap icons) pour chaque page
selected = option_menu(
    menu_title=None,  # Pas de titre pour le menu
    options=["Bienvenue", "Éligibilité", "Questionnaire", "États Financiers", "Résultats"],
    icons=["house", "check2-circle", "list-task", "bar-chart", "trophy"], # Icônes gratuites
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
)

# 3. Initialisation de la mémoire (Session State)
if 'donnees' not in st.session_state:
    st.session_state['donnees'] = {
        "ca_n": 0.0, "ebitda_n": 0.0, "dette_n": 0.0,
        "score_eco": 3, "methode": "Non définie"
    }

# --- LOGIQUE DES PAGES ---

if selected == "Bienvenue":
    st.title("👋 Bienvenue sur l'OAD Rating Crédit")
    st.write("Le menu est maintenant en haut de l'écran pour plus de visibilité.")

elif selected == "Éligibilité":
    st.title("⚖️ Éligibilité & Méthode")
    secteur = st.selectbox("Secteur d'activité", ["Industrie", "Services", "Holding"])
    st.session_state['donnees']['methode'] = secteur

elif selected == "Questionnaire":
    st.title("📝 Questionnaire Économique")
    note = st.slider("Note Qualitative", 1, 5, st.session_state['donnees']['score_eco'])
    st.session_state['donnees']['score_eco'] = note

elif selected == "États Financiers":
    st.title("📊 Saisie des États Financiers")
    c1, c2 = st.columns(2)
    with c1:
        st.session_state['donnees']['ca_n'] = st.number_input("Chiffre d'Affaires", value=st.session_state['donnees']['ca_n'])
    with c2:
        st.session_state['donnees']['dette_n'] = st.number_input("Dette", value=st.session_state['donnees']['dette_n'])

elif selected == "Résultats":
    st.title("🏆 Score Final")
    st.metric("Score Économique", f"{st.session_state['donnees']['score_eco']}/5")