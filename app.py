import random
import time
from html import escape

import pandas as pd
import streamlit as st

import altair as alt

st.set_page_config(
    page_title="Team Vibe Dashboard",
    page_icon="🌈",
    initial_sidebar_state="expanded",
)

# Creamos el historial una sola vez por sesión.
if "historial_vibe" not in st.session_state:
    st.session_state.historial_vibe = []

opciones_humor = [
    "😊 Alegre",
    "😌 Tranquila",
    "💪 Motivada",
    "🤩 Entusiasmada",
    "😐 Regular",
    "😴 Cansada",
    "😟 Preocupada",
    "😰 Estresada",
    "😔 Triste",
    "😤 Frustrada",
    "😕 Mal",
]

frases = [
    "Cada línea de código te enseña algo nuevo.",
    "Resolver un error también es avanzar.",
    "Las grandes ideas pueden empezar con un pequeño botón.",
    "¡Celebra lo que ya sabes hacer y sigue experimentando!",
]

st.title("🌈 Team Vibe Dashboard")
st.markdown("### ¿Cómo está el pulso del equipo hoy?")

# 1. Recogemos los datos en la barra lateral.
with st.sidebar:
    st.header("☕ Tu registro")

    with st.form("formulario_vibe"):
        nombre = st.text_input(
            "👋 ¿Cómo te llamas?",
            placeholder="Escribe tu nombre",
        ).strip()

        humor = st.selectbox(
            "💭 ¿Cómo te sientes hoy?",
            opciones_humor,
        )

        energia = st.slider(
            "⚡ ¿Cuál es tu nivel de energía?",
            min_value=0,
            max_value=10,
            value=5,
            help="0 significa «sin energía» y 10 significa «a tope».",
        )
        bebida = st.radio(
            "🫖 ¿Qué te apetece ahora?",
            ["☕ Café", "🍵 Té", "💧 Agua", "🙌 Nada por ahora"],
        ) 

        boton_registrar = st.form_submit_button("☕ Registrar mi vibe")

# 2. Guardamos el registro y mostramos la animación en la página principal.
if boton_registrar:
    if nombre:
        nuevo_registro = {
            "Nombre": nombre,
            "Humor": humor,
            "Energia": energia,
            "Bebida": bebida,
        }
        st.session_state.historial_vibe.append(nuevo_registro)

        mensajes_bebida = {
            "☕ Café": ("☕", "¡Marchando un café para"),
            "🍵 Té": ("🍵", "¡Una taza de té para"),
            "💧 Agua": ("💧", "¡Un vaso de agua para"),
            "🙌 Nada por ahora": ("🙌", "¡Vibe registrada! Gracias,"),
        }

        icono, mensaje = mensajes_bebida[bebida]

        animacion = st.empty()
        with animacion.container():
            st.markdown(
                f"""
                <div style="text-align: center; padding: 24px;">
                    <div style="font-size: 110px;">{icono}</div>
                    <h2>{mensaje} {escape(nombre)}!</h2>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.balloons()

        time.sleep(2.5)
        animacion.empty()
        st.success(random.choice(frases))
    else:
        st.sidebar.error("⚠️ Escribe tu nombre antes de registrar tu vibe.")

# 3. Mostramos el seguimiento en la página principal.
st.divider()
st.subheader("Tu seguimiento")

if st.session_state.historial_vibe:
    datos = pd.DataFrame(st.session_state.historial_vibe)
    datos.insert(0, "Registro", range(1, len(datos) + 1))
    datos = datos.rename(columns={"Energia": "Energía"})

    tarjeta_total, tarjeta_media, tarjeta_humor = st.columns(3)
    tarjeta_total.metric("Registros", len(datos))
    tarjeta_media.metric("Energía media", f"{datos['Energía'].mean():.1f} / 10")
    tarjeta_humor.metric("Último estado de ánimo", datos["Humor"].iloc[-1])

    pestana_graficos, pestana_historial = st.tabs(
        ["📊 Gráficos", "📋 Historial"]
    )

    with pestana_graficos:
        columna_linea, columna_barras = st.columns(2)

        with columna_linea:
            st.markdown("#### Energía por registro")
            st.line_chart(datos, x="Registro", y="Energía", color="#8B5CF6")

        with columna_barras:
            st.markdown("#### Frecuencia de cada estado de ánimo")

            # Contamos los registros de cada estado de ánimo.
            recuento = datos["Humor"].value_counts()
            recuento = recuento.reindex(opciones_humor, fill_value=0)
            recuento = recuento.rename_axis("Humor").reset_index(name="Registros")

            # Asignamos un color a cada estado, en orden de arcoíris.
            colores_arcoiris = [
                "#EF4444",  # Rojo
                "#F97316",  # Naranja
                "#F59E0B",  # Ámbar
                "#EAB308",  # Amarillo
                "#84CC16",  # Verde lima
                "#22C55E",  # Verde
                "#14B8A6",  # Turquesa
                "#06B6D4",  # Celeste
                "#3B82F6",  # Azul
                "#6366F1",  # Índigo
                "#A855F7",  # Violeta
            ]

            grafico_barras = alt.Chart(recuento).mark_bar().encode(
                x=alt.X("Humor:N", sort=opciones_humor, title="Estado de ánimo"),
                y=alt.Y("Registros:Q", title="Número de registros"),
                color=alt.Color(
                    "Humor:N",
                    scale=alt.Scale(
                        domain=opciones_humor,
                        range=colores_arcoiris,
                    ),
                    legend=None,
                ),
                tooltip=["Humor:N", "Registros:Q"],
            )

            st.altair_chart(grafico_barras)

            

    with pestana_historial:
        st.dataframe(datos, hide_index=True)
else:
    st.info("Añade tu primer registro para ver el resumen y los gráficos.")