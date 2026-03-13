import streamlit as st

st.set_page_config(
    page_title="IA en la Práctica Terapéutica",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 El Impacto de la Inteligencia Artificial en la Práctica Terapéutica")

st.markdown("""
**Frase motivadora**

> La innovación en salud mental comienza cuando usamos la tecnología con ética, conocimiento y humanidad.
""")

st.sidebar.title("Contenido")

seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "Introducción",
        "Historia de la IA en Psicología",
        "¿Qué es la IA en terapia?",
        "Componentes de la IA",
        "IA en acción",
        "Fenotipificación digital",
        "Relación humano-máquina",
        "Referencias"
    ]
)

if seccion == "Introducción":

    st.header("Introducción")

    st.write("""
La salud mental se ha convertido en una prioridad global. Cada vez más personas
necesitan apoyo psicológico, pero el número de profesionales disponibles no
siempre es suficiente para cubrir esta demanda.

Ante esta situación, la tecnología ha comenzado a desempeñar un papel importante
en el apoyo a los servicios de salud mental. La inteligencia artificial permite
analizar grandes cantidades de información, ofrecer apoyo psicológico digital y
mejorar la eficiencia de los servicios clínicos.
    """)

elif seccion == "Historia de la IA en Psicología":

    st.header("Historia de la IA en Psicología")

    st.write("""
La relación entre las computadoras y la psicología comenzó en la década de 1960
con la creación de ELIZA, uno de los primeros programas capaces de simular
una conversación terapéutica.

Aunque era un sistema muy simple, demostró algo importante: las personas pueden
sentir que una máquina las entiende cuando la comunicación está bien diseñada.
    """)

elif seccion == "¿Qué es la IA en terapia?":

    st.header("¿Qué es la IA en la práctica terapéutica?")

    st.write("""
La inteligencia artificial en psicología consiste en el uso de sistemas
computacionales capaces de realizar tareas que normalmente requieren
intervención humana, como:

- Identificar síntomas
- Analizar emociones
- Apoyar decisiones clínicas
- Monitorear el estado psicológico de los pacientes
    """)

elif seccion == "Componentes de la IA":

    st.header("Componentes principales")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Aprendizaje Automático")
        st.write("""
El aprendizaje automático permite analizar grandes cantidades de datos para
identificar patrones y predecir qué tipo de intervención podría funcionar
mejor para cada paciente.
        """)

    with col2:
        st.subheader("Procesamiento de Lenguaje Natural")
        st.write("""
Permite que las computadoras comprendan y respondan al lenguaje humano,
haciendo posible la creación de chatbots terapéuticos y asistentes
virtuales.
        """)

elif seccion == "IA en acción":

    st.header("IA en acción")

    st.write("""
Diversos estudios han demostrado que herramientas basadas en inteligencia
artificial pueden ayudar a reducir síntomas de depresión y ansiedad.

Estas herramientas incluyen:

- Chatbots terapéuticos
- Sistemas de monitoreo emocional
- Plataformas digitales de intervención
    """)

    st.info("Estas tecnologías ayudan especialmente a personas que no tienen acceso fácil a atención psicológica.")

elif seccion == "Fenotipificación digital":

    st.header("Fenotipificación digital")

    st.write("""
La fenotipificación digital consiste en analizar datos generados por el uso
de dispositivos como teléfonos inteligentes para comprender el estado
emocional de una persona.

Por ejemplo:

- Patrones de sueño
- Frecuencia de movimiento
- Velocidad al escribir
- Uso de aplicaciones

Estos datos pueden ayudar a detectar cambios emocionales o posibles crisis
antes de que ocurran.
    """)

elif seccion == "Relación humano-máquina":

    st.header("Relación entre psicólogos y la IA")

    st.write("""
La inteligencia artificial no busca reemplazar al psicólogo, sino apoyar su
trabajo.

Mientras que la IA puede analizar datos rápidamente y automatizar tareas
administrativas, el terapeuta aporta:

- Empatía
- juicio clínico
- comprensión del contexto del paciente

Por ello, el futuro de la psicoterapia probablemente será un modelo
híbrido, donde humanos y tecnología trabajen juntos.
    """)

elif seccion == "Referencias":

    st.header("Referencias")

    st.write("""
Bhatt (2024)

D'Alfonso et al. (2017)

Gual-Montolio et al. (2022)

Higgins & Wilson (2025)

Milasan & Scott-Purdy (2025)

Ni & Jia (2025)

Rollwage et al. (2023)

Sadeh-Sharvit et al. (2023)

Vaidyam et al. (2019)

Yeasmin et al. (2025)
    """)
