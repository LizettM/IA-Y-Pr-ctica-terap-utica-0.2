import streamlit as st

st.set_page_config(
    page_title="IA en la Práctica Terapéutica",
    page_icon="🧠",
    layout="wide"
)

# ESTILOS ROSADOS
st.markdown("""
<style>

.main {
background-color: #fff7fb;
}

h1 {
color: #e75480;
text-align: center;
}

h2, h3 {
color: #c94f7c;
}

section[data-testid="stSidebar"] {
background-color: #ffe4ef;
}

div[data-testid="stExpander"] {
background-color: #ffd6e7;
border-radius: 12px;
border: 1px solid #f5a3c7;
padding: 5px;
}

div[data-testid="stExpander"] summary {
font-size: 17px;
font-weight: 600;
color: #a83d6b;
}

</style>
""", unsafe_allow_html=True)

# TITULO
st.title("El Impacto de la Inteligencia Artificial en la Práctica Terapéutica")

st.markdown("> La innovación en salud mental comienza cuando usamos la tecnología con ética, conocimiento y humanidad.")

# SIDEBAR
st.sidebar.title("Contenido")

seccion = st.sidebar.radio(
"Selecciona una sección:",
[
"Artículo",
"Referencias"
]
)

# ARTÍCULO
if seccion == "Artículo":

    st.header("El Impacto de la Inteligencia Artificial en la Práctica Terapéutica")

    st.write("""
La salud mental ha dejado de ser un tema del que se habla en voz baja para convertirse en una prioridad para todos. Sin embargo, hoy nos enfrentamos a un gran problema: cada vez más personas necesitan apoyo psicológico, pero no hay suficientes psicólogos o expertos preparados para atender a tanta gente al mismo tiempo. En este escenario, la tecnología ha dado un paso al frente para ayudar a que nadie se quede sin la atención que necesita. La integración de la tecnología en este ámbito se basa en la necesidad de cerrar la brecha entre la gran cantidad de personas que buscan ayuda y la falta de especialistas disponibles para atenderlos (Bhatt, 2024).

Lo que antes parecía una película de ciencia ficción —una computadora que puede entendernos— es hoy una realidad que apoya a los terapeutas y a los pacientes en su día a día. Pero ¿cómo hemos llegado hasta aquí y qué significa realmente que un programa de computadora participe en nuestro bienestar emocional?
""")

    st.subheader("De los primeros robots a la inteligencia actual: Un poco de historia")

    st.write("""
La relación entre las computadoras y la psicología no es algo nuevo. De hecho, los primeros pasos se dieron en los años 60 con la creación de ELIZA, el primer programa de chat que intentaba imitar a un terapeuta. Aunque era muy sencillo, ELIZA demostró algo sorprendente: los seres humanos podemos sentir que una máquina nos entiende y nos acompaña si la comunicación está bien diseñada (Vaidyam et al., 2019).
""")

    st.subheader("¿Qué es exactamente la IA cuando hablamos de terapia?")

    st.write("""
Para entender este fenómeno sin complicaciones, podemos decir que la IA en la psicología es el uso de programas inteligentes para hacer tareas que normalmente haría un humano, como identificar qué nos pasa, planear cómo ayudarnos o vigilar cómo nos sentimos día tras día (Yeasmin et al., 2025).
""")

    st.subheader("La IA en acción: ¿Qué dicen los estudios?")

    st.write("""
La ciencia ya ha comprobado que estas herramientas funcionan de verdad. Por ejemplo, se ha demostrado que el uso de chatbots diseñados bajo reglas terapéuticas puede reducir de forma real los síntomas de la depresión y la ansiedad (Bhatt, 2024).
""")

    st.subheader('La IA en Acción: El "Fenotipo Digital"')

    st.write("""
Existe un concepto llamado "fenotipificación digital". Esto consiste en que la IA analiza datos que generamos sin darnos cuenta, como cuánto nos movemos, cómo dormimos o qué tan rápido escribimos, para entender nuestro estado de ánimo (Gual-Montolio et al., 2022).
""")

    st.subheader("¿Sustitución o Colaboración? El Vínculo Humano-Máquina")

    st.write("""
Es normal tener miedo a que una máquina nos quite el trato humano. Sin embargo, el objetivo de la IA no es reemplazar al psicólogo, sino mejorar la relación entre el experto y el paciente.
""")

# REFERENCIAS
elif seccion == "Referencias":

    st.header("Referencias")

    with st.expander("Bhatt (2024)"):
        st.write("""
El artículo analiza el papel de la inteligencia artificial dentro de la psicoterapia digital, destacando cómo las tecnologías basadas en aprendizaje automático, procesamiento del lenguaje natural y sistemas conversacionales están transformando la prestación de servicios en salud mental. Se describe cómo la IA puede utilizarse para apoyar procesos terapéuticos mediante chatbots, monitoreo automatizado de síntomas, análisis de patrones emocionales y personalización de intervenciones. El texto enfatiza que la inteligencia artificial puede aumentar la accesibilidad, reducir costos y ofrecer apoyo continuo entre sesiones terapéuticas. También se discuten aplicaciones en evaluación inicial, detección temprana de riesgo y adaptación dinámica de contenidos terapéuticos. Sin embargo, el artículo advierte sobre limitaciones éticas, riesgos de dependencia tecnológica, problemas de privacidad y la necesidad de mantener el juicio clínico humano como elemento central. Se concluye que la IA representa una herramienta complementaria dentro de la psicoterapia, pero su implementación debe estar respaldada por evidencia científica sólida y regulaciones claras.
""")

    with st.expander("D'Alfonso et al. (2017)"):
        st.write("""
El artículo explora la integración de la inteligencia artificial en la plataforma Moderated Online Social Therapy (MOST), diseñada para apoyar la salud mental de jóvenes con trastornos como la psicosis y la depresión. Este sistema combina una red social segura con recursos terapéuticos y apoyo de expertos y pares. El objetivo es demostrar cómo el procesamiento de lenguaje natural y tecnologías avanzadas pueden automatizar contenido personalizado y mejorar la eficiencia clínica sin perder el cuidado humano.
""")

    with st.expander("Gual-Montolio et al. (2022)"):
        st.write("""
El artículo analiza el uso de herramientas de inteligencia artificial como apoyo complementario en intervenciones psicológicas dirigidas a problemas emocionales como depresión y ansiedad. Los autores destacan que la IA puede analizar grandes volúmenes de datos clínicos, identificar patrones de respuesta al tratamiento y predecir riesgos de abandono o recaída, permitiendo ajustar las intervenciones de manera más precisa y oportuna.
""")

    with st.expander("Higgins & Wilson (2025)"):
        st.write("""
El artículo analiza cómo la inteligencia artificial puede integrarse con soluciones relacionadas con la fuerza laboral en salud mental para abordar la creciente demanda de servicios y la escasez de profesionales. Se discuten aplicaciones como triage automatizado, monitoreo de síntomas y optimización de recursos clínicos.
""")

    with st.expander("Milasan & Scott-Purdy (2025)"):
        st.write("""
El artículo analiza el papel emergente de la inteligencia artificial en la práctica de enfermería en salud mental, destacando su potencial para mejorar la evaluación clínica, el monitoreo y la toma de decisiones mediante análisis automatizado de datos.
""")

    with st.expander("Ni & Jia (2025)"):
        st.write("""
El artículo presenta una revisión de alcance sobre intervenciones digitales impulsadas por inteligencia artificial en salud mental, incluyendo aplicaciones para detección temprana, apoyo psicológico, monitoreo de síntomas y tratamiento clínico.
""")

    with st.expander("Rollwage et al. (2023)"):
        st.write("""
El artículo analiza cómo la inteligencia artificial conversacional puede facilitar evaluaciones de salud mental y mejorar la eficiencia clínica dentro de servicios psicoterapéuticos.
""")

    with st.expander("Sadeh-Sharvit et al. (2023)"):
        st.write("""
El estudio evalúa la eficacia de una plataforma de inteligencia artificial utilizada como apoyo a la terapia cognitivo-conductual para depresión y ansiedad, mostrando mejoras en reducción de síntomas y eficiencia clínica.
""")

    with st.expander("Vaidyam et al. (2019)"):
        st.write("""
El artículo revisa el uso de chatbots en salud mental, destacando su aplicación en psicoeducación, apoyo emocional, monitoreo de síntomas y entrega automatizada de intervenciones terapéuticas.
""")

    with st.expander("Yeasmin et al. (2025)"):
        st.write("""
El artículo examina avances recientes en inteligencia artificial aplicada a diagnóstico, terapia y bienestar emocional en salud mental.
""")
