import streamlit as st

st.set_page_config(page_title="Rating Crédit OAD", layout="wide")

st.title("🏦 Outil d'Aide à la Décision : Rating Crédit")

# --- PARTIE 1 : QUESTIONNAIRE ÉCONOMIQUE ---
st.header("1. Analyse Qualitative (Questionnaire)")
with st.expander("Répondre aux questions économiques", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        q_secteur = st.selectbox(
            "Qualité du secteur d'activité",
            options=[(1, "En déclin"), (2, "Stable"), (3, "En croissance")],
            format_func=lambda x: x[1]
        )
        
    with col2:
        q_management = st.selectbox(
            "Expérience du management",
            options=[(1, "Faible (< 2 ans)"), (2, "Intermédiaire"), (3, "Expérimenté (> 5 ans)")],
            format_func=lambda x: x[1]
        )

# --- PARTIE 2 : SAISIE DES ÉTATS FINANCIERS ---
st.header("2. Analyse Quantitative (Données Financières)")

# On crée deux colonnes pour comparer Année N et Année N-1
col_n, col_n_1 = st.columns(2)

with col_n:
    st.subheader("Année N (Plus récente)")
    ca_n = st.number_input("Chiffre d'Affaires (N)", min_value=0.0, step=1000.0)
    ebitda_n = st.number_input("EBITDA (N)", step=1000.0)
    dette_n = st.number_input("Dette Financière Totale (N)", min_value=0.0, step=1000.0)

with col_n_1:
    st.subheader("Année N-1")
    ca_n_1 = st.number_input("Chiffre d'Affaires (N-1)", min_value=0.0, step=1000.0)
    ebitda_n_1 = st.number_input("EBITDA (N-1)", step=1000.0)
    dette_n_1 = st.number_input("Dette Financière Totale (N-1)", min_value=0.0, step=1000.0)

# --- PARTIE 3 : CALCULS ET RATING ---
if st.button("Calculer le Rating"):
    st.divider()
    
    # Calcul des ratios simples (Exemple : Levier financier)
    try:
        levier_n = dette_n / ebitda_n if ebitda_n != 0 else 0
        croissance_ca = ((ca_n - ca_n_1) / ca_n_1) * 100 if ca_n_1 != 0 else 0
        
        # Logique de score (Simplifiée pour l'exemple)
        score_final = (q_secteur[0] + q_management[0]) / 2
        
        # Affichage des résultats
        c1, c2, c3 = st.columns(3)
        c1.metric("Levier Financier (N)", f"{levier_n:.2f}x")
        c2.metric("Croissance CA", f"{croissance_ca:.1f}%")
        c3.metric("Score Qualitatif", f"{score_final}/3")
        
        # Affichage du Rating final
        if levier_n < 2 and score_final > 2:
            st.success("### Rating Suggéré : Excellent (A+)")
        elif levier_n < 4:
            st.warning("### Rating Suggéré : Moyen (BBB)")
        else:
            st.error("### Rating Suggéré : Risqué (C)")
            
    except Exception as e:
        st.error(f"Erreur dans le calcul : Vérifiez les données saisies.")