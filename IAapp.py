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
"El Impacto de la Inteligencia Artificial en la Práctica Terapéutica",
"De los primeros robots a la inteligencia actual: Un poco de historia",
"¿Qué es exactamente la IA cuando hablamos de terapia?",
"La IA en acción: ¿Qué dicen los estudios?",
"La IA en Acción: El \"Fenotipo Digital\"",
"¿Sustitución o Colaboración? El Vínculo Humano-Máquina",
"Referencias"
]
)

# SECCIONES

if seccion == "El Impacto de la Inteligencia Artificial en la Práctica Terapéutica":

    st.header(seccion)
    st.write("""La salud mental ha dejado de ser un tema del que se habla en voz baja para convertirse en una prioridad para todos. Sin embargo, hoy nos enfrentamos a un gran problema: cada vez más personas necesitan apoyo psicológico, pero no hay suficientes psicólogos o expertos preparados para atender a tanta gente al mismo tiempo. 
En este escenario, la tecnología ha dado un paso al frente para ayudar a que nadie se quede sin la atención que necesita. La integración de la tecnología en este ámbito se basa en la necesidad de cerrar la brecha entre la gran cantidad de personas que buscan ayuda y la falta de especialistas disponibles para atenderlos (Bhatt, 2024). 
Lo que antes parecía una película de ciencia ficción —una computadora que puede entendernos— es hoy una realidad que apoya a los terapeutas y a los pacientes en su día a día. Pero ¿cómo hemos llegado hasta aquí y qué significa realmente que un programa de computadora participe en nuestro bienestar emocional?""")

elif seccion == "De los primeros robots a la inteligencia actual: Un poco de historia":

    st.header(seccion)
    st.write("""La relación entre las computadoras y la psicología no es algo nuevo. De hecho, los primeros pasos se dieron en los años 60 con la creación de ELIZA, el primer programa de chat que intentaba imitar a un terapeuta. Aunque era muy sencillo, ELIZA demostró algo sorprendente: los seres humanos podemos sentir que una máquina nos entiende y nos acompaña si la comunicación está bien diseñada (Vaidyam et al., 2019). 
Hoy en día, la Inteligencia Artificial (IA) ha evolucionado muchísimo. Ya no es solo un medio para enviar mensajes, sino que se ha convertido en una herramienta activa que ofrece tratamientos basados en estudios científicos (Bhatt, 2024). La mayoría de estos avances se basan en la Terapia Cognitivo-Conductual (TCC). Este tipo de terapia es muy efectiva porque se centra en pasos prácticos y reglas claras, lo que permite que sea "traducida" fácilmente a un lenguaje que las computadoras pueden procesar para ayudarnos a cambiar pensamientos negativos (Sadeh-Sharvit et al., 2023). Estos sistemas han pasado de ser simples páginas de autoayuda a complejos programas que aprenden de nosotros para darnos un cuidado mucho más personal (Ni & Jia, 2025).""")

elif seccion == "¿Qué es exactamente la IA cuando hablamos de terapia?":

    st.header(seccion)
    st.write("""Para entender este fenómeno sin complicaciones, podemos decir que la IA en la psicología es el uso de programas inteligentes para hacer tareas que normalmente haría un humano, como identificar qué nos pasa, planear cómo ayudarnos o vigilar cómo nos sentimos día tras día (Yeasmin et al., 2025). Dentro de este mundo tecnológico, hay dos piezas clave que debemos conocer: 
1. El Aprendizaje Automático: Es como un asistente que tiene la capacidad de revisar millones de datos en segundos para adivinar qué tratamiento funcionará mejor para cada persona (Milasan & Scott-Purdy, 2025). 
2. El Procesamiento de Lenguaje: Es lo que permite que la computadora entienda nuestras palabras, nuestro tono y la forma en que escribimos, respondiéndonos de una manera coherente y profesional (Milasan & Scott-Purdy, 2025). 
Además, la IA ayuda a los psicólogos con el papeleo y las tareas administrativas. Estos sistemas de apoyo permiten que el profesional no pierda tiempo en formularios y pueda concentrarse totalmente en escuchar a su paciente durante la consulta (Higgins & Wilson, 2025). Al final, esto crea un modelo de atención "híbrido", donde se combina el corazón y la intuición del psicólogo con la memoria y la precisión de la máquina (Rollwage et al., 2023).""")

elif seccion == "La IA en acción: ¿Qué dicen los estudios?":

    st.header(seccion)
    st.write("""La ciencia ya ha comprobado que estas herramientas funcionan de verdad. Por ejemplo, se ha demostrado que el uso de chatbots (programas de conversación) diseñados bajo reglas terapéuticas puede reducir de forma real los síntomas de la depresión y la ansiedad (Bhatt, 2024). Estos programas son una gran solución para personas que, por falta de dinero o porque viven lejos de una ciudad, no pueden ir a un consultorio tradicional. Otro avance impresionante es la rapidez. En clínicas grandes, la IA ayuda a evaluar a los pacientes apenas llegan, lo que permite que reciban el tratamiento adecuado mucho más rápido que si tuvieran que esperar semanas a una cita de evaluación inicial (Rollwage et al., 2023).""")

elif seccion == "La IA en Acción: El \"Fenotipo Digital\"":

    st.header(seccion)
    st.write("""Existe un concepto llamado "fenotipificación digital". Esto consiste en que la IA analiza datos que generamos sin darnos cuenta, como cuánto nos movemos, cómo dormimos o qué tan rápido escribimos, para entender nuestro estado de ánimo (Gual-Montolio et al., 2022). Esto es vital para la prevención, ya que estos modelos pueden detectar si alguien está en peligro de una crisis o tiene pensamientos muy oscuros antes de que ocurra una tragedia, permitiendo que un humano intervenga a tiempo (Ni & Jia, 2025). 
Incluso los psicólogos de carne y hueso se benefician: aquellos que usan estas plataformas para analizar sus sesiones dicen que les ayuda a seguir mejor las guías de salud y a que sus pacientes mejoren más rápido (Sadeh-Sharvit et al., 2023).""")

elif seccion == "¿Sustitución o Colaboración? El Vínculo Humano-Máquina":

    st.header(seccion)
    st.write("""Es normal tener miedo a que una máquina nos quite el trato humano. Sin embargo, el objetivo de la IA no es reemplazar al psicólogo, sino mejorar la relación entre el experto y el paciente. Al dejar que la IA se encargue de las tareas aburridas y del análisis de datos, el terapeuta tiene más tiempo y energía para conectar emocionalmente con la persona (Higgins & Wilson, 2025). 
La IA nos da información en tiempo real sobre cómo va progresando el paciente fuera del consultorio, algo que antes era imposible de saber (Gual-Montolio et al., 2022). Es una relación donde todos ganan: el psicólogo aporta su ética y su capacidad de entender el contexto de la vida del paciente, mientras que la IA aporta una vigilancia constante y detecta detalles que a cualquier humano se le podrían pasar por alto (D'Alfonso et al., 2017).""")

# REFERENCIAS
elif seccion == "Referencias":

    st.header("Referencias")

    with st.expander("Bhatt, S. (2024)"):
        st.write("""El artículo analiza el papel de la inteligencia artificial dentro de la psicoterapia digital, destacando cómo las tecnologías basadas en aprendizaje automático, procesamiento del lenguaje natural y sistemas conversacionales están transformando la prestación de servicios en salud mental. Se describe cómo la IA puede utilizarse para apoyar procesos terapéuticos mediante chatbots, monitoreo automatizado de síntomas, análisis de patrones emocionales y personalización de intervenciones. El texto enfatiza que la inteligencia artificial puede aumentar la accesibilidad, reducir costos y ofrecer apoyo continuo entre sesiones terapéuticas. También se discuten aplicaciones en evaluación inicial, detección temprana de riesgo y adaptación dinámica de contenidos terapéuticos. Sin embargo, el artículo advierte sobre limitaciones éticas, riesgos de dependencia tecnológica, problemas de privacidad y la necesidad de mantener el juicio clínico humano como elemento central. Se concluye que la IA representa una herramienta complementaria dentro de la psicoterapia, pero su implementación debe estar respaldada por evidencia científica sólida y regulaciones claras.""")

    with st.expander("D'Alfonso et al. (2017)"):
        st.write("""El artículo explora la integración de la inteligencia artificial en la plataforma Moderated Online Social Therapy mejor conocida como MOST la cual está diseñada para apoyar la salud mental de jóvenes con trastornos como la psicosis y la depresión. Este sistema combina una red social segura con recursos terapéuticos y el apoyo de expertos y pares. El objetivo principal de los autores es demostrar cómo las tecnologías de computación avanzada y el procesamiento de lenguaje natural pueden automatizar la entrega de contenido personalizado y mejorar la eficiencia de la moderación clínica permitiendo que el sistema sea escalable para llegar a más personas sin perder la calidad del cuidado humano.""")

    with st.expander("Gual-Montolio et al. (2022)"):
        st.write("""El artículo analiza el uso de herramientas de inteligencia artificial como apoyo complementario en intervenciones psicológicas dirigidas a problemas emocionales, especialmente depresión y ansiedad, dentro de la práctica clínica rutinaria. El objetivo principal es explorar cómo la IA puede mejorar tratamientos ya en curso, optimizando la personalización, el seguimiento y la toma de decisiones clínicas. Los autores destacan que la inteligencia artificial puede utilizarse para analizar grandes volúmenes de datos clínicos, identificar patrones de respuesta al tratamiento y predecir posibles riesgos de abandono o recaída. Esto permitiría ajustar las intervenciones de manera más precisa y oportuna. El estudio enfatiza que la IA no sustituye al terapeuta, sino que actúa como herramienta de apoyo para aumentar la eficacia y eficiencia del proceso terapéutico. Se concluye que la integración de IA en la psicoterapia tiene potencial para mejorar resultados clínicos, aunque todavía enfrenta desafíos metodológicos, éticos y técnicos.""")

    with st.expander("Higgins & Wilson (2025)"):
        st.write("""El artículo analiza cómo la inteligencia artificial puede integrarse con soluciones relacionadas con la fuerza laboral en salud mental para abordar la creciente demanda de servicios y la escasez de profesionales. Se centra en la necesidad de combinar innovación tecnológica con estrategias organizacionales que fortalezcan al personal clínico, en lugar de reemplazarlo. La autora discute cómo la IA puede apoyar procesos como el triage automatizado, la priorización de casos, el monitoreo de síntomas, la documentación clínica y la optimización de recursos humanos. Se enfatiza que la implementación efectiva depende de una adecuada capacitación del personal, liderazgo institucional y marcos regulatorios claros. El artículo concluye que la IA puede contribuir a mejorar la eficiencia, reducir la carga administrativa y ampliar el acceso a la atención, siempre que se integre de manera ética, segura y centrada en el profesional y el paciente.""")

    with st.expander("Milasan & Scott-Purdy (2025)"):
        st.write("""El artículo analiza el papel emergente de la inteligencia artificial en la práctica de enfermería en salud mental, destacando su potencial para transformar la evaluación, el monitoreo clínico y la gestión del cuidado. Se examinan aplicaciones como sistemas predictivos de riesgo, análisis automatizado de datos clínicos, herramientas de apoyo a la toma de decisiones y tecnologías de monitoreo remoto. La autora enfatiza que la IA no debe entenderse como sustituto del profesional de enfermería, sino como una herramienta complementaria que puede optimizar procesos, reducir carga administrativa y fortalecer la calidad del cuidado centrado en el paciente. También se subraya la importancia de competencias digitales en la formación de enfermería y la necesidad de liderazgo profesional en la implementación tecnológica. El artículo concluye que el futuro de la enfermería en salud mental dependerá de una integración ética, regulada y colaborativa entre tecnología y práctica clínica humana.""")

    with st.expander("Ni & Jia (2025)"):
        st.write("""El artículo presenta una revisión de alcance cuyo objetivo es mapear y sistematizar las aplicaciones de intervenciones digitales impulsadas por inteligencia artificial en el ámbito de la salud mental. Se analizan herramientas que abarcan desde el tamizaje y detección temprana de trastornos, hasta el apoyo psicológico y el tratamiento clínico. Los autores identifican que la inteligencia artificial se utiliza principalmente en chatbots conversacionales, sistemas de monitoreo automatizado, algoritmos predictivos y plataformas digitales de intervención. Estas tecnologías permiten ampliar el acceso a servicios, ofrecer apoyo continuo y personalizar intervenciones según patrones de datos individuales. La revisión muestra un crecimiento acelerado de investigaciones en el área, especialmente en depresión y ansiedad. Sin embargo, también señala que muchas aplicaciones aún se encuentran en etapas iniciales de validación y que existe variabilidad significativa en calidad metodológica. Se concluye que la IA tiene un alto potencial transformador, pero requiere mayor estandarización y evidencia robusta.""")

    with st.expander("Rollwage et al. (2023)"):
        st.write("""El artículo analiza el papel actual de la inteligencia artificial en el campo de la salud mental, explorando sus aplicaciones clínicas, ventajas potenciales y desafíos éticos y metodológicos. Se describe cómo los sistemas de aprendizaje automático y procesamiento del lenguaje natural pueden utilizarse para la detección temprana de trastornos, predicción de riesgo, personalización de tratamientos y apoyo a la toma de decisiones clínicas. El texto enfatiza que la inteligencia artificial puede mejorar la accesibilidad y eficiencia de los servicios de salud mental, especialmente en contextos con escasez de profesionales. Sin embargo, también subraya riesgos importantes relacionados con sesgos algorítmicos, privacidad de datos, falta de transparencia en los modelos y posibles implicaciones éticas en la relación terapéutica. Se concluye que la integración de IA en salud mental debe realizarse con validación científica rigurosa, supervisión clínica y marcos regulatorios claros.""")

    with st.expander("Sadeh-Sharvit et al. (2023)"):
        st.write("""El estudio evalúa la factibilidad, aceptabilidad y eficacia preliminar de una plataforma de inteligencia artificial aplicada a la terapia psicológica ambulatoria para adultos con depresión y ansiedad. La plataforma de Eleos Health se utilizó como apoyo a la terapia cognitivo-conductual y se comparó con el tratamiento habitual (TAU). Los resultados muestran que los pacientes cuyos terapeutas utilizaron la plataforma de IA asistieron a más sesiones y presentaron una mayor reducción de síntomas depresivos y ansiosos en un periodo de dos meses. Además, el uso de la IA redujo significativamente el tiempo de elaboración de notas clínicas, sin afectar la satisfacción ni la percepción de utilidad del tratamiento por parte de los pacientes.""")

    with st.expander("Vaidyam et al. (2019)"):
        st.write("""El artículo presenta una revisión de la literatura sobre el uso de chatbots y agentes conversacionales en el ámbito de la salud mental. Analiza su desarrollo, aplicaciones clínicas, fundamentos tecnológicos y evidencia empírica disponible hasta el momento. Los autores señalan que estos sistemas se han utilizado principalmente para psicoeducación, apoyo emocional, monitoreo de síntomas y entrega automatizada de intervenciones basadas en terapia cognitivo conductual. Aunque los resultados preliminares muestran mejoras en síntomas de depresión, ansiedad y estrés, la evidencia aún es limitada y heterogénea. El estudio concluye que los chatbots representan una herramienta prometedora para ampliar el acceso a servicios de salud mental, pero enfatiza la necesidad de mayor regulación, validación clínica rigurosa y análisis ético.""")

    with st.expander("Yeasmin et al. (2025)"):
        st.write("""El artículo examina los avances recientes en el uso de la inteligencia artificial dentro de la intervención psicológica y la atención en salud mental. Analiza cómo herramientas basadas en aprendizaje automático, procesamiento del lenguaje natural y sistemas predictivos están siendo aplicadas en evaluación clínica, monitoreo de síntomas, apoyo terapéutico y prevención de recaídas. Se destaca que la IA puede mejorar la precisión diagnóstica, facilitar intervenciones personalizadas y ampliar el acceso a servicios psicológicos, especialmente en contextos con limitaciones de recursos. No obstante, el artículo también enfatiza preocupaciones éticas relacionadas con privacidad, confidencialidad, sesgo algorítmico y responsabilidad profesional. Los autores concluyen que la integración efectiva de la IA requiere evidencia empírica sólida, regulación adecuada y una colaboración estrecha entre desarrolladores tecnológicos y profesionales de la salud mental.""")
