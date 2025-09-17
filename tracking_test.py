import streamlit as st

# Injecter le code GTM dans le "head" (le plus haut possible)
st.markdown("""
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TGJR5K24');</script>
<!-- End Google Tag Manager -->
""", unsafe_allow_html=True)

# Injecter le code GTM noscript juste après (simule début du body)
st.markdown("""
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TGJR5K24"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
""", unsafe_allow_html=True)

# Titre
st.title("Test de Tracking GTM")

# Explications
st.write("""
Cliquez sur le bouton pour tester un événement tracké via GTM.
Vérifiez les événements dans :
- **GTM Preview** : Mode Preview dans Google Tag Manager.
- **GA4** : DebugView dans Google Analytics (si configuré dans GTM).
- **Meta Pixel** : Facebook Pixel Helper (si configuré dans GTM).
""")

# Bouton pour tester le tracking
if st.button("Tester le Tracking"):
    st.success("Événement 'test_click' envoyé !")
    st.markdown("""
    <script>
    dataLayer.push({'event': 'test_click', 'action': 'button_clicked'});
    </script>
    """, unsafe_allow_html=True)
