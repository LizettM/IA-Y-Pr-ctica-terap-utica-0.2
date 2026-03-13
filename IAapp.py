import streamlit as st

st.set_page_config(
    page_title="IA en la Práctica Terapéutica",
    page_icon="🧠",
    layout="wide"
)

# ESTILOS
st.markdown("""
<style>

.main {
background-color: #fff7fb;
}

h1 {
color: #e75480;
text-align: center;
}

h2 {
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

.block-container {
padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# TITULO
st.title("El Impacto de la Inteligencia Artificial en la Práctica Terapéutica")

st.markdown(
"> La innovación en salud mental comienza cuando usamos la tecnología con ética, conocimiento y humanidad."
)

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

Hoy en día, la Inteligencia Artificial (IA) ha evolucionado muchísimo. Ya no es solo un medio para enviar mensajes, sino que se ha convertido en una herramienta activa que ofrece tratamientos basados en estudios científicos (Bhatt, 2024). La mayoría de estos avances se basan en la Terapia Cognitivo-Conductual (TCC). Este tipo de terapia es muy efectiva porque se centra en pasos prácticos y reglas claras, lo que permite que sea "traducida" fácilmente a un lenguaje que las computadoras pueden procesar para ayudarnos a cambiar pensamientos negativos (Sadeh-Sharvit et al., 2023). Estos sistemas han pasado de ser simples páginas de autoayuda a complejos programas que aprenden de nosotros para darnos un cuidado mucho más personal (Ni & Jia, 2025).
""")

    st.subheader("¿Qué es exactamente la IA cuando hablamos de terapia?")

    st.write("""
Para entender este fenómeno sin complicaciones, podemos decir que la IA en la psicología es el uso de programas inteligentes para hacer tareas que normalmente haría un humano, como identificar qué nos pasa, planear cómo ayudarnos o vigilar cómo nos sentimos día tras día (Yeasmin et al., 2025).
""")

    st.markdown("""
1. **El Aprendizaje Automático:** Es como un asistente que tiene la capacidad de revisar millones de datos en segundos para adivinar qué tratamiento funcionará mejor para cada persona (Milasan & Scott-Purdy, 2025).

2. **El Procesamiento de Lenguaje:** Es lo que permite que la computadora entienda nuestras palabras, nuestro tono y la forma en que escribimos, respondiéndonos de una manera coherente y profesional (Milasan & Scott-Purdy, 2025).
""")

    st.write("""
Además, la IA ayuda a los psicólogos con el papeleo y las tareas administrativas. Estos sistemas de apoyo permiten que el profesional no pierda tiempo en formularios y pueda concentrarse totalmente en escuchar a su paciente durante la consulta (Higgins & Wilson, 2025). Al final, esto crea un modelo de atención "híbrido", donde se combina el corazón y la intuición del psicólogo con la memoria y la precisión de la máquina (Rollwage et al., 2023).
""")

# REFERENCIAS
elif seccion == "Referencias":

    st.header("Referencias")

    with st.expander("Bhatt (2024)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("D'Alfonso et al. (2017)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Gual-Montolio et al. (2022)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Higgins & Wilson (2025)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Milasan & Scott-Purdy (2025)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Ni & Jia (2025)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Rollwage et al. (2023)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Sadeh-Sharvit et al. (2023)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Vaidyam et al. (2019)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")

    with st.expander("Yeasmin et al. (2025)"):
        st.write("PEGA AQUÍ TU RESUMEN COMPLETO EXACTO")
