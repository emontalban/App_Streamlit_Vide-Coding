import random
import time
from html import escape

import streamlit as st

st.title("🚀 ¡Mi primera app!")
st.write("Si ves esto, eres oficialmente una desarrolladora.")

# Creamos el historial una sola vez por sesión.
if "historial_vibe" not in st.session_state:
    st.session_state.historial_vibe = []

frases = [
    "Cada línea de código te enseña algo nuevo.",
    "Resolver un error también es avanzar.",
    "Las grandes ideas pueden empezar con un pequeño botón.",
    "¡Celebra lo que ya sabes hacer y sigue experimentando!",
]

nombre = st.text_input("¿Cómo te llamas?").strip()
humor = st.selectbox("¿Cómo te sientes hoy?", ["😊 Bien", "😐 Regular", "😔 Mal"])
energia = st.slider("¿Cuánta energía tienes?", 1, 10, 5)

boton_registrar = st.button("☕ Registrar mi vibe")

if boton_registrar:
    if nombre:
        nuevo_registro = {
            "Nombre": nombre,
            "Humor": humor,
            "Energia": energia,
        }
        st.session_state.historial_vibe.append(nuevo_registro)

        # Guardamos la frase para mostrarla después de refrescar la app.
        st.session_state.frase_vibe = random.choice(frases)

        # Mostramos el café en un espacio temporal.
        placeholder = st.empty()
        with placeholder.container():
            st.markdown(
                f"""
                <div style="text-align: center; padding: 50px;">
                    <div style="font-size: 150px; line-height: 1;">☕</div>
                    <h2 style="color: #6F4E37;">
                        ¡Marchando una dosis de energía para {escape(nombre)}!
                    </h2>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.balloons()

        time.sleep(2.5)
        placeholder.empty()
        st.rerun()
    else:
        st.error("⚠️ Por favor, escribe tu nombre antes de registrar tu vibe.")

# Tras el refresco, recuperamos la frase y la mostramos una vez.
frase = st.session_state.pop("frase_vibe", None)
if frase:
    st.success(frase)

st.subheader("Historial de vibes")
if st.session_state.historial_vibe:
    st.table(st.session_state.historial_vibe)