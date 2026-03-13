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
La salud mental ha dejado de ser un tema del que se habla en voz baja para convertirse en una prioridad para todos. Sin embargo, hoy nos enfrentamos a un gran problema: cada vez más personas necesitan apoyo psicológico, pero no hay suficientes psicólogos o expertos preparados para atender a tanta gente al mismo tiempo.

En este escenario, la tecnología ha dado un paso al frente para ayudar a que nadie se quede sin la atención que necesita. La integración de la tecnología en este ámbito se basa en la necesidad de cerrar la brecha entre la gran cantidad de personas que buscan ayuda y la falta de especialistas disponibles para atenderlos.
    """)

# HISTORIA
elif seccion == "Historia de la IA en Psicología":

    st.header("De los primeros robots a la inteligencia actual")

    st.write("""
La relación entre las computadoras y la psicología no es algo nuevo. Los primeros pasos se dieron en los años 60 con la creación de ELIZA, el primer programa de chat que intentaba imitar a un terapeuta.

Aunque era muy sencillo, ELIZA demostró algo sorprendente: los seres humanos pueden sentir que una máquina los entiende y los acompaña si la comunicación está bien diseñada.

Hoy en día la inteligencia artificial ha evolucionado mucho. Ya no es solo un medio para enviar mensajes, sino una herramienta que puede apoyar tratamientos basados en estudios científicos, especialmente dentro de enfoques como la terapia cognitivo-conductual.
    """)

# DEFINICIÓN
elif seccion == "¿Qué es la IA en terapia?":

    st.header("¿Qué es exactamente la IA cuando hablamos de terapia?")

    st.write("""
Podemos entender la inteligencia artificial en psicología como el uso de programas inteligentes capaces de realizar tareas que normalmente haría un humano.

Por ejemplo:

- Identificar qué le sucede a una persona
- Analizar emociones
- Planear estrategias de intervención
- Monitorear el estado psicológico día a día
    """)

# COMPONENTES
elif seccion == "Componentes de la IA":

    st.header("Componentes principales de la inteligencia artificial")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Aprendizaje Automático")
        st.write("""
Es la capacidad que tienen los sistemas para analizar enormes cantidades de datos y detectar patrones. Gracias a esto, la IA puede sugerir qué tipo de tratamiento podría funcionar mejor para cada paciente.
        """)

    with col2:
        st.subheader("Procesamiento de Lenguaje Natural")
        st.write("""
Es lo que permite que las computadoras comprendan nuestras palabras, el tono en que escribimos y la forma en que nos expresamos, respondiendo de una manera coherente.
        """)

# IA EN ACCIÓN
elif seccion == "IA en acción":

    st.header("La IA en acción: ¿Qué dicen los estudios?")

    st.write("""
La investigación científica ha demostrado que herramientas basadas en inteligencia artificial pueden ayudar a reducir síntomas de depresión y ansiedad.

Entre las aplicaciones más comunes se encuentran:

- Chatbots terapéuticos
- Plataformas digitales de apoyo psicológico
- Sistemas de monitoreo emocional

Estas herramientas pueden ser especialmente útiles para personas que no tienen acceso fácil a servicios de salud mental.
    """)

# FENOTIPIFICACIÓN
elif seccion == "Fenotipificación digital":

    st.header("La IA en acción: Fenotipificación digital")

    st.write("""
La fenotipificación digital consiste en analizar datos que generamos con nuestros dispositivos, como el celular, para comprender nuestro estado emocional.

Por ejemplo:

- Cuánto dormimos
- Cuánto nos movemos
- Qué tan rápido escribimos
- Con qué frecuencia usamos ciertas aplicaciones

Estos datos pueden ayudar a detectar cambios emocionales importantes y prevenir crisis antes de que ocurran.
    """)

# RELACIÓN HUMANO MÁQUINA
elif seccion == "Relación humano-máquina":

    st.header("¿Sustitución o colaboración?")

    st.write("""
Muchas personas temen que la inteligencia artificial reemplace a los psicólogos. Sin embargo, el objetivo real de estas tecnologías es apoyar el trabajo del profesional.

La IA puede encargarse de analizar datos, monitorear síntomas y reducir tareas administrativas. Mientras tanto, el terapeuta aporta empatía, juicio clínico y comprensión del contexto humano.

Por ello, el futuro de la psicoterapia probablemente será un modelo híbrido donde humanos y tecnología trabajen juntos.
    """)

# REFERENCIAS
elif seccion == "Referencias":

    st.header("Referencias y resumen de los artículos")

    with st.expander("Bhatt, S. (2024)"):
        st.write("""
El artículo analiza el papel de la inteligencia artificial dentro de la psicoterapia digital, destacando cómo las tecnologías basadas en aprendizaje automático, procesamiento del lenguaje natural y sistemas conversacionales están transformando la prestación de servicios en salud mental. Se describe cómo la IA puede utilizarse para apoyar procesos terapéuticos mediante chatbots, monitoreo automatizado de síntomas, análisis de patrones emocionales y personalización de intervenciones.

El texto enfatiza que la inteligencia artificial puede aumentar la accesibilidad, reducir costos y ofrecer apoyo continuo entre sesiones terapéuticas. También se discuten aplicaciones en evaluación inicial, detección temprana de riesgo y adaptación dinámica de contenidos terapéuticos.

Sin embargo, el artículo advierte sobre limitaciones éticas, riesgos de dependencia tecnológica, problemas de privacidad y la necesidad de mantener el juicio clínico humano como elemento central. Se concluye que la IA representa una herramienta complementaria dentro de la psicoterapia, pero su implementación debe estar respaldada por evidencia científica sólida y regulaciones claras.
        """)

    with st.expander("D'Alfonso et al. (2017)"):
        st.write("""
El artículo explora la integración de la inteligencia artificial en la plataforma Moderated Online Social Therapy (MOST), diseñada para apoyar la salud mental de jóvenes con trastornos como la psicosis y la depresión. Este sistema combina una red social segura con recursos terapéuticos y el apoyo de expertos y pares. El objetivo principal es demostrar cómo tecnologías avanzadas pueden automatizar contenido personalizado y mejorar la moderación clínica.
        """)

    with st.expander("Gual-Montolio et al. (2022)"):
        st.write("""
El artículo analiza el uso de herramientas de inteligencia artificial como apoyo complementario en intervenciones psicológicas dirigidas a problemas emocionales como depresión y ansiedad. La IA puede analizar grandes volúmenes de datos clínicos, identificar patrones de respuesta al tratamiento y predecir riesgos de recaída.
        """)

    with st.expander("Higgins & Wilson (2025)"):
        st.write("""
El artículo analiza cómo la inteligencia artificial puede integrarse con soluciones de fuerza laboral en salud mental para abordar la creciente demanda de servicios. Se discuten aplicaciones como triage automatizado, priorización de casos, monitoreo de síntomas y documentación clínica.
        """)

    with st.expander("Milasan & Scott-Purdy (2025)"):
        st.write("""
Analiza el papel emergente de la inteligencia artificial en la práctica de enfermería en salud mental, destacando su potencial para transformar la evaluación, monitoreo clínico y gestión del cuidado.
        """)

    with st.expander("Ni & Jia (2025)"):
        st.write("""
Presenta una revisión de intervenciones digitales impulsadas por inteligencia artificial en salud mental, incluyendo chatbots, monitoreo automatizado y algoritmos predictivos.
        """)

    with st.expander("Rollwage et al. (2023)"):
        st.write("""
Analiza el uso de inteligencia artificial conversacional para facilitar evaluaciones de salud mental y mejorar la eficiencia clínica dentro de servicios de psicoterapia.
        """)

    with st.expander("Sadeh-Sharvit et al. (2023)"):
        st.write("""
Evalúa una plataforma de inteligencia artificial aplicada a la terapia cognitivo-conductual, mostrando reducción de síntomas depresivos y ansiosos y menor tiempo dedicado a notas clínicas.
        """)

    with st.expander("Vaidyam et al. (2019)"):
        st.write("""
Revisión de literatura sobre chatbots en salud mental, utilizados para psicoeducación, monitoreo de síntomas y apoyo emocional.
        """)

    with st.expander("Yeasmin et al. (2025)"):
        st.write("""
Examina avances recientes en inteligencia artificial aplicada a diagnóstico, terapia y bienestar emocional, destacando tanto su potencial como desafíos éticos.
        """)
