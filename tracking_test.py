import streamlit as st
import streamlit.components.v1 as components

# Injecter GTM dans le "head" (le plus haut possible)
components.html("""
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-57BGF9ZN');</script>
<!-- End Google Tag Manager -->
""", height=0)

# Injecter noscript dans le "body"
components.html("""
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-57BGF9ZN"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
""", height=0)

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
    components.html("""
    <script>
    dataLayer.push({'event': 'test_click', 'action': 'button_clicked'});
    </script>
    """, height=0)
