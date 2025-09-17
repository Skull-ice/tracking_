import streamlit as st

# Injecter les scripts de tracking
st.markdown("""
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->

<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>
<!-- End Meta Pixel Code -->
""", unsafe_allow_html=True)

# Titre
st.title("Test de Tracking")

# Explications
st.write("""
Cliquez sur le bouton pour tester le tracking avec Meta Pixel et GA4 via GTM.
Vérifiez les événements dans :
- **Meta Pixel** : Facebook Pixel Helper (extension Chrome).
- **GA4** : DebugView dans Google Analytics.
- **GTM** : Mode Preview dans Google Tag Manager.
""")

# Bouton pour tester le tracking
if st.button("Tester le Tracking"):
    st.success("Événement 'test_click' envoyé !")
    st.markdown("""
    <script>
    fbq('track', 'Lead', {action: 'test_click'});
    dataLayer.push({'event': 'test_click', 'action': 'button_clicked'});
    </script>
    """, unsafe_allow_html=True)