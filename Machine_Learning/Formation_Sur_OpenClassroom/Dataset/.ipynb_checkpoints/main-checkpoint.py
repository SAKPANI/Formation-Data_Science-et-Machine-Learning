import pandas as pd
import streamlit as st

# 1. Titre du site web (généré automatiquement)
st.title("🩸TALK-AI Togo : Gestion des Stocks de Sang")

# 2. Menu de sélection de l'hôpital
hopital = st.selectbox(
    "Sélectionnez l'établissement sanitaire :",
    ["CHU Sylvanus Olympio", "CHU Campus", "CHR Kara", "CHR Dapaong"],
)

# 3. Affichage d'indicateurs visuels sous forme de cartes
col1, col2, col3 = st.columns(3)
col1.metric(label="Stock Actuel (Poches O-)", value="12 poches", delta="-5 cette semaine")
col2.metric(label="Précipitations (Pluie)", value="48 mm", delta="+12 mm (Risque Paludisme)")
col3.metric(label="Jours de stock restants", value="3.5 Jours", delta_color="inverse")

# 4. Message d'alerte automatique
st.error(
    f"⚠️ **ALERTE ROUGE sur le {hopital}** : Risque de rupture imminente sur le groupe O- dans 3 jours !"
)