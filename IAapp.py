import streamlit as st

st.set_page_config(
    page_title="IA en la Práctica Terapéutica",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 El Impacto de la Inteligencia Artificial en la Práctica Terapéutica")

st.markdown("> La innovación en salud mental comienza cuando usamos la tecnología con ética, conocimiento y humanidad.")

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

# INTRODUCCIÓN
if seccion == "Introducción":

    st.header("Introducción")

    st.write("""
La salud mental ha dejado de ser un tema del que se habla en voz baja para convertirse
en una prioridad para todos. Cada vez más personas necesitan apoyo psicológico, pero
no siempre hay suficientes profesionales disponibles para atender esta demanda.

Ante esta situación, la tecnología ha comenzado a desempeñar un papel importante en
el apoyo a los servicios de salud mental. La inteligencia artificial permite analizar
grandes cantidades de información, ofrecer apoyo psicológico digital y mejorar la
eficiencia de los servicios clínicos.
    """)

# HISTORIA
elif seccion == "Historia de la IA en Psicología":

    st.header("De los primeros robots a la inteligencia actual")

    st.write("""
La relación entre las computadoras y la psicología no es algo nuevo. En los años 60
se creó ELIZA, uno de los primeros programas capaces de simular una conversación
terapéutica.

Aunque era un sistema sencillo, demostró algo sorprendente: las personas pueden
sentir que una máquina las entiende si la comunicación está bien diseñada.

Actualmente la inteligencia artificial ha evolucionado y se utiliza como una
herramienta que puede apoyar tratamientos basados en evidencia científica,
especialmente en terapias como la terapia cognitivo-conductual.
    """)

# DEFINICIÓN
elif seccion == "¿Qué es la IA en terapia?":

    st.header("¿Qué es exactamente la IA cuando hablamos de terapia?")

    st.write("""
La inteligencia artificial en psicología consiste en el uso de programas
capaces de realizar tareas que normalmente realizaría un profesional humano.

Entre estas tareas se encuentran:

- Identificar problemas emocionales
- Analizar patrones de comportamiento
- Apoyar decisiones clínicas
- Monitorear el estado psicológico de los pacientes
    """)

# COMPONENTES
elif seccion == "Componentes de la IA":

    st.header("Componentes principales de la IA en psicología")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Aprendizaje Automático")
        st.write("""
Permite analizar grandes cantidades de datos para identificar patrones
y predecir qué tipo de intervención puede funcionar mejor para cada paciente.
        """)

    with col2:
        st.subheader("Procesamiento de Lenguaje Natural")
        st.write("""
Permite que las computadoras comprendan el lenguaje humano,
interpretando palabras, tono y estructura del mensaje para
responder de forma coherente.
        """)

# IA EN ACCIÓN
elif seccion == "IA en acción":

    st.header("La IA en acción: evidencia científica")

    st.write("""
Diversos estudios han demostrado que herramientas basadas en inteligencia
artificial pueden reducir síntomas de depresión y ansiedad.

Estas tecnologías incluyen:

- Chatbots terapéuticos
- Plataformas digitales de intervención
- Sistemas de monitoreo emocional
    """)

# FENOTIPO DIGITAL
elif seccion == "Fenotipificación digital":

    st.header("Fenotipificación digital")

    st.write("""
La fenotipificación digital consiste en analizar datos generados por el uso
de dispositivos como teléfonos inteligentes para comprender el estado
emocional de una persona.

Por ejemplo:

- Patrones de sueño
- Nivel de actividad física
- Velocidad al escribir
- Uso de aplicaciones

Estos datos pueden ayudar a detectar cambios emocionales o posibles crisis
antes de que ocurran.
    """)

# RELACIÓN HUMANO-MÁQUINA
elif seccion == "Relación humano-máquina":

    st.header("¿Sustitución o colaboración?")

    st.write("""
La inteligencia artificial no busca reemplazar al psicólogo, sino apoyar
su trabajo.

Mientras la IA puede analizar datos y automatizar tareas administrativas,
el terapeuta aporta:

- Empatía
- juicio clínico
- comprensión del contexto del paciente

Por ello, el futuro de la psicoterapia probablemente será un modelo
híbrido donde humanos y tecnología trabajen juntos.
    """)

# REFERENCIAS
elif seccion == "Referencias":

    st.header("Referencias y resumen de los artículos")

    st.subheader("Bhatt (2024)")
    st.write("""
Analiza el papel de la inteligencia artificial dentro de la psicoterapia digital.
Explica cómo tecnologías como aprendizaje automático y chatbots pueden apoyar
procesos terapéuticos mediante monitoreo de síntomas y personalización de
intervenciones. También señala desafíos éticos relacionados con privacidad y
la necesidad de mantener el juicio clínico humano.
    """)

    st.subheader("D'Alfonso et al. (2017)")
    st.write("""
Explora la plataforma MOST, diseñada para apoyar la salud mental de jóvenes
con depresión y psicosis. El sistema combina una red social segura con recursos
terapéuticos y apoyo profesional para ampliar el acceso a intervenciones
psicológicas.
    """)

    st.subheader("Gual-Montolio et al. (2022)")
    st.write("""
Analiza el uso de herramientas de inteligencia artificial como apoyo
complementario en intervenciones psicológicas, destacando su capacidad
para analizar datos clínicos y mejorar la personalización del tratamiento.
    """)

    st.subheader("Higgins & Wilson (2025)")
    st.write("""
Examina cómo la inteligencia artificial puede integrarse con soluciones
organizacionales para enfrentar la escasez de profesionales en salud mental,
apoyando tareas como triage automatizado y documentación clínica.
    """)

    st.subheader("Milasan & Scott-Purdy (2025)")
    st.write("""
Analiza el papel emergente de la inteligencia artificial en la práctica de
enfermería en salud mental, destacando su potencial para mejorar evaluación,
monitoreo clínico y toma de decisiones.
    """)

    st.subheader("Ni & Jia (2025)")
    st.write("""
Presenta una revisión de intervenciones digitales basadas en IA utilizadas
para detección temprana, apoyo psicológico, monitoreo de síntomas y
prevención de recaídas en salud mental.
    """)

    st.subheader("Rollwage et al. (2023)")
    st.write("""
Describe cómo la IA conversacional puede mejorar evaluaciones de salud mental
y aumentar la eficiencia clínica dentro de servicios de psicoterapia.
    """)

    st.subheader("Sadeh-Sharvit et al. (2023)")
    st.write("""
Estudio que evalúa una plataforma de IA utilizada como apoyo en terapia
cognitivo-conductual, mostrando mejoras en síntomas de depresión y ansiedad
y reducción del tiempo dedicado a notas clínicas.
    """)

    st.subheader("Vaidyam et al. (2019)")
    st.write("""
Revisión sobre el uso de chatbots en salud mental para psicoeducación,
monitoreo de síntomas y apoyo emocional.
    """)

    st.subheader("Yeasmin et al. (2025)")
    st.write("""
Examina avances recientes en inteligencia artificial aplicada al diagnóstico,
terapia y bienestar emocional, destacando tanto su potencial como los
desafíos éticos y técnicos.
    """)
