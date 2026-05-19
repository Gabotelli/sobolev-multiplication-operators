# Estructura objetivo del TFM

Este documento fija en el repositorio la estructura de referencia del TFM a partir de las directrices de las directoras en la reunión del 7 de mayo.

## Criterios globales de escritura

- Uso intensivo de referencias cruzadas (`\label`, `\ref`, `\eqref`).
- Contextualización explícita: no asumir en qué caso estamos sin decirlo.
- Prioridad de la geometría visual sobre formulaciones analíticas oscuras en los enunciados.
- No introducir notación propia demasiado pronto en la introducción.
- No abrir líneas nuevas de investigación: reestructurar, depurar y cerrar lo ya desarrollado.

## Estructura por capítulos

### Capítulo 1 — Introducción y estado del arte

- Marco general: medidas de Borel, productos de Sobolev, estado del arte, BPE si hace falta.
- Motivo central del trabajo: queríamos acotar ceros, la norma del operador no bastó, y eso forzó el paso a valores singulares e índices nuevos.

### Capítulo 2 — Codimensión, dicotomía topológica e índice \texorpdfstring{$Q_k$}{Qk}

La versión actual del capítulo 2 ya fija una lógica estable y no debe volver a desordenarse. La motivación avanza desde el fracaso del conteo topológico hasta la necesidad del índice algebraico:

1. marco hilbertiano y codimensión topológica,
2. dicotomía topológica para funcionales no acotados,
3. paso a codimensión algebraica y restricciones lineales finitas,
4. relación entre codimensión algebraica y topológica,
5. definición y propiedades básicas de \(Q_k\),
6. equivalencia con Gelfand en el caso acotado.

#### Títulos ya asentados para el Capítulo 2

1. `Marco hilbertiano y codimensión topológica`
2. `Límite de la codimensión topológica`
3. `Codimensión algebraica y restricciones lineales finitas`
4. `Relación entre codimensión algebraica y topológica`
5. `Índice Q_k`
6. `Equivalencia con los números de Gelfand`

#### Justificación de la diferencia respecto del esquema original

Aunque la propuesta original pedía introducir primero la codimensión algebraica, el orden actual se adoptó porque hace más visible la lógica conceptual del capítulo:

- primero se presenta la noción clásica (topológica y Gelfand),
- luego se muestra por qué no alcanza para contar la inestabilidad,
- recién entonces se pasa al nivel algebraico y al índice \(Q_k\).

La intención es que \(Q_k\) se lea como una generalización necesaria, no como una invención aislada.

### Capítulo 3 — Estabilización y régimen no acotado

- Secuencia ya fijada: ejemplos iniciales, clasificación geométrica/BPE, definición del subespacio estable canónico \(V_{\mathrm{out}}\), necesidad de codimensión \(m\), teorema de estabilización, refinamientos.
- Aparición formal de la notación propia: \(I_{\mathrm{in}}\), \(I_{\mathrm{out}}\), puntos \(\delta\)-singulares, \(V_{\mathrm{out}}\).
- Resultado principal: la cadena \(Q_0(\mathcal D),Q_1(\mathcal D),\dots\) permanece infinita hasta \(m-1\) y colapsa por primera vez en \(m\).
- La lectura debe seguir siendo geométrica antes que técnica: interior, exterior y frontera no son adornos, sino la clasificación estructural que organiza todo el capítulo.
- La estructura algebraica fina de \(V_{\mathrm{out}}\) ya quedó desplazada al apéndice; en el cuerpo principal solo debe entrar lo necesario para el umbral de estabilización y su transición al capítulo matricial.

### Capítulo 4 — Análisis asintótico y secciones matriciales

- Capítulo puente: traduce el umbral abstracto de \(Q_k\) al lenguaje observable de las truncaciones \(\mathbf D_n\).
- Secuencia ya asentada: Hessenberg y compresiones finitas, valores singulares, desigualdad \(\sigma_{k,n}\le Q_k(\mathcal D)\), lectura del umbral singular, observaciones numéricas mínimas.
- No sobreactuar el alcance inverso: desde \(Q_k\) se obtienen cotas singulares; la dirección matricial \(\to\) abstracta no debe insinuarse sin prueba.
- Estrategia de cierre fijada: resultado principal, dos remarcas cortas de lectura (matricial y numérica), y transición inmediata al paso singular-espectral del Capítulo 5.

### Capítulo 5 — Ceros, conteo y atracción

- El título y la función del capítulo ya están fijados: pasar del umbral singular a resultados de localización de ceros.
- Separación estructural obligatoria:
  - Weyl--Horn da solo el puente macroscópico singular-espectral y el techo de conteo.
  - El conteo exacto y la localización fina vienen después, por reducción racional exterior y Rouché.
- Tratamiento principal ya asentado en cuatro regímenes: puramente exterior, mixto sin frontera, frontera pura, mixto con frontera.
- La escala macroscópica y la escala fina no deben mezclarse: el desacople exterior gobierna conteo y atracción exterior; la frontera introduce un perfil local de escala \(1/n\).
- La vía de cuasi-ortogonalidad queda como comparación/apoyo en apéndice, no como línea principal del capítulo.
- El cierre del capítulo debe dejar explícito qué queda resuelto y qué queda abierto: la localización de ceros sí; el valor exacto de \(Q_m(\mathcal D)\) en el caso mixto, no.

## Estado narrativo que se quiere transmitir

El TFM debe leerse con madurez suficiente en el tema. Para eso se busca:

- más economía verbal,
- más frontalidad en la presentación de resultados,
- menos reintroducción de justificaciones ya asentadas,
- más foco en el núcleo estructural,
- separación limpia entre puente macroscópico y argumentos de localización fina,
- evitar secciones tituladas de cierre; si hace falta cerrar un capítulo, se prefiere un párrafo final de transición o balance sin abrir una sección específica para ello,
- sin perder claridad de tesis ni autosuficiencia en los resultados que sostienen capítulos posteriores.

## Uso de este documento

Este fichero debe usarse como referencia activa al revisar o reescribir capítulos del TFM.

### Regla para auditorías internas

Al evaluar un capítulo hay que comprobar simultáneamente:

1. si sigue la estructura global fijada aquí;
2. si prepara bien el capítulo siguiente;
3. si mantiene el tono ya asentado en el Capítulo 2:
   - más sobrio,
   - más frontal,
   - más estructural,
   - menos escolar o explicativo en exceso;
4. si la madurez importada del artículo de referencia se nota en la economía verbal y en la jerarquía de resultados;
5. si evita adelantar notación o ideas fuera del momento estructural previsto.

### Criterios de auditoría ya asentados para los Capítulos 4 y 5

1. No atribuir a Weyl--Horn más de lo que prueba: controla productos/autovalores en escala macroscópica, no reemplaza la reducción racional ni a Rouché.
2. Verificar que el Capítulo 4 termine en secuencia sobria: resultado, lectura, transición; no con desarrollo nuevo.
3. Verificar que el Capítulo 5 mantenga separadas las dos escalas de análisis:
   - macroscópica: umbral singular, techo de conteo, desacople exterior;
   - fina: conteo exacto, atracción, perfil de frontera.
4. Comprobar que lo complementario quede fuera de la línea principal cuando ya está desplazado al apéndice:
   - estructura algebraica adicional de \(V_{\mathrm{out}}\),
   - vía clásica de cuasi-ortogonalidad,
   - notación matricial de apoyo.
5. Exigir que cada cierre de capítulo prepare el siguiente con una transición explícita y sin reabrir el capítulo que se acaba de cerrar.

### Referencia obligatoria para subagentes

Todo subagente que revise estructura o estilo del manuscrito debe consultar primero:

- `Plantilla TFM/ESTRUCTURA_DOCUMENTO.md`

y usarlo como criterio explícito de evaluación, no solo como contexto pasivo.
