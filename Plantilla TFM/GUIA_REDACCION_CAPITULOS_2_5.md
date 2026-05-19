# Guía de redacción y revisión de los Capítulos 1 a 5

## Objetivo del documento

- Servir como referencia práctica para escribir y revisar el Capítulo 5.
- Preservar en el repositorio las decisiones estructurales, de estilo, notación y cierre ya asentadas en los Capítulos 1, 2, 3, 4 y 5.
- Evitar volver a abrir debates ya resueltos o recaer en errores corregidos.

## Decisiones ya asentadas por capítulo

### Capítulo 1

- La estructura ya asentada es: contexto y motivación -> medidas de Borel, regularidad y medida de Lebesgue -> espacios de polinomios y ortogonalidad clásica -> espacios de Sobolev y productos discretos -> estado del arte.
- El Capítulo 1 DEBE funcionar como capítulo de entrada al problema, no como anticipo técnico de la maquinaria propia de los capítulos posteriores.
- Debe dejar claro qué problema motiva la memoria: el control de ceros en el paso del caso clásico al caso Sobolev, y por qué la norma del operador de multiplicación deja de bastar.
- `Intro.md` debe tratarse como banco de material e ideas, no como texto para copiar literalmente. Hay que destilar, seleccionar y reescribir en la voz actual del manuscrito.
- La notación propia fuerte NO debe nacer aquí si todavía no es estructuralmente necesaria. El Capítulo 1 fija solo la notación geométrica y funcional mínima para que el lector entre en el problema.
- La discusión de BPE debe quedarse dentro del encuadre del estado del arte y de la lectura conceptual del régimen interior/exterior. No debe adelantarse aquí como desarrollo técnico autónomo ni como sustituto del trabajo estructural del Capítulo 3.
- Qué sí pertenece al Capítulo 1: marco clásico, motivación histórica, producto de Sobolev discreto modelo, papel conceptual del operador de multiplicación, mapa del problema y estado del arte que justifica el salto a invariantes más finos.
- Qué NO debe aparecer todavía: desarrollo completo de `I_{\mathrm{in}}`, `I_{\mathrm{out}}`, `V_{\mathrm{out}}`, puntos `\delta`-singulares, umbrales `Q_k`, estabilización, formulación matricial, ni análisis fino de ceros.
- Sensibilidad actual: aunque los TODOs introductorios principales quedaron cerrados, sigue siendo importante vigilar que el estado del arte no crezca de más ni empiece a sonar como Capítulo 3 disfrazado.

### Capítulo 2

- La lógica ya fijada es: marco hilbertiano y codimensión topológica -> límite de la codimensión topológica -> codimensión algebraica -> relación entre ambas -> índice `Q_k` -> equivalencia con Gelfand.
- El capítulo DEBE empezar por el lado topológico/Gelfand antes que por el algebraico.
- Motivo: primero se presenta la noción clásica, luego se muestra por qué falla en el régimen no acotado y solo entonces se introduce `Q_k` como generalización necesaria.
- `Q_k` no debe aparecer como invento aislado, sino como respuesta al fracaso del conteo topológico tras la clausura.

### Capítulo 3

- Este es el capítulo donde la notación propia se gana; no debe adelantarse antes.
- La clasificación `interior / frontera / exterior` no es decorativa: organiza toda la lectura geométrica del capítulo.
- La distinción analítica correcta en el modelo de Lebesgue es: `c \in I_out` si y solo si `psi_c` no es acotado si y solo si `c` no es BPE.
- El subespacio canónico es `V_out = \bigcap_{c\in I_{\mathrm{out}}} \ker(\psi_c)`; su papel es neutralizar exactamente las direcciones inestables y solo esas.
- La secuencia conceptual asentada es: ejemplos iniciales -> clasificación geométrica/BPE -> `V_out` -> necesidad de codimensión `m` -> teorema de estabilización -> refinamientos.
- Convención importante: las enumeraciones finitas de `I_out` son temporales y locales a una prueba; no deben convertirse en notación global del capítulo.

### Capítulo 4

- Es un capítulo puente, no un nuevo frente técnico autónomo.
- Su función es traducir el umbral abstracto de `Q_k` al lenguaje matricial observable de las truncaciones `\mathbf D_n`.
- La dirección correcta es abstracto -> singular/matricial. NO insinuar la dirección inversa sin prueba.
- Cierre correcto ya fijado: resultado principal -> dos remarcas cortas de lectura -> transición inmediata al Capítulo 5.
- La notación de matrices de momentos queda como apoyo/apéndice; en la línea principal basta Hessenberg + secciones truncadas + valores singulares.

### Capítulo 5

- Sigue siendo el capítulo más delicado y el que más disciplina estructural necesita.
- La separación ya asentada es obligatoria: `Weyl--Horn` solo da el puente macroscópico singular-espectral y un techo de conteo.
- El conteo exacto y la localización fina vienen después, por reducción racional exterior + Rouché.
- La escala macroscópica y la escala fina NO deben mezclarse en un mismo enunciado si no es imprescindible.
- Regímenes ya fijados: puramente exterior, mixto sin frontera, frontera pura, mixto con frontera.
- En la versión actual, el cierre correcto del capítulo es: queda resuelta la localización de ceros en los regímenes tratados; queda abierto el valor exacto de `Q_m(\D)` en el caso mixto.

## Reglas de estilo ya consolidadas

- Priorizar geometría y lectura estructural antes que caracterizaciones analíticas artificiales.
- Los enunciados principales deben hablar primero en términos geométricos y de fenómeno visible; lo más técnico debe bajar a lemas, remarcas o pruebas.
- Mantener tono sobrio, frontal y con economía verbal.
- No reexplicar demasiado lo que ya está asentado en capítulos anteriores.
- Cada capítulo debe cerrar preparando el siguiente, no reabriendo el anterior.
- Cuando exista referencia exacta, citarla de forma exacta: teorema, proposición, lema, ecuación o capítulo.
- Evitar fórmulas vagas como "como veremos" o "como vimos" si puede ponerse una referencia concreta.
- No introducir notación propia antes del momento estructural en que el manuscrito ya la justifica.
- Si un bloque parece adelantar resultados o notación que pertenecen a un capítulo posterior, reubicarlo o rebajarlo a motivación.

## Terminología y notación que no debe volver a romperse

- `I_in` e `I_out` son conjuntos de puntos, no conteos ni listas fijas.
- `I_out^*` denota el subconjunto estrictamente exterior: `I_{\mathrm{out}}^* = \{c\in I_{\mathrm{out}}: |c|>R\}`.
- En el Capítulo 5, "puramente exterior" significa EXTERIOR ESTRICTO: `|c|>R`, no meramente `|c|\ge R`.
- Los puntos de frontera pertenecen a `I_out`, pero deben separarse cuando la geometría fina del capítulo lo exige.
- `V_out` es el subespacio estable canónico definido por anulación de los funcionales `psi_c` en `I_out`.
- `m = |I_out|` es el índice de ruptura de la cadena `Q_0, Q_1, ...`.
- Las enumeraciones como `c_1,\dots,c_m`, `a_1,\dots,a_m`, `b_1,\dots,b_q` deben quedarse locales al resultado/prueba donde se introducen.

## Qué va en línea principal y qué va en apéndice

- En línea principal debe quedar: la lógica conceptual `Q_k -> estabilización -> umbral singular -> autovalores -> localización de ceros`.
- En línea principal debe quedar: el puente Hessenberg/valores singulares/autovalores.
- En línea principal debe quedar: la reducción racional exterior y los argumentos de Rouché que dan conteo y atracción.
- En apéndice puede quedar: notación de matrices de momentos en base monomial.
- En apéndice puede quedar: estructura algebraica complementaria de `V_out` cuando sobrecargue la línea principal.
- En apéndice puede quedar: vía clásica alternativa por cuasi-ortogonalidad para acotación uniforme.
- En apéndice puede quedar: rutas clásicas o comparativas que no sean necesarias para sostener la columna vertebral del argumento.

## Errores ya detectados y corregidos

- NO usar `Intro.md` como texto base literal. Es una cantera de ideas, no un borrador pegable.
- NO convertir el Capítulo 1 en un pseudo-Capítulo 3 adelantado.
- NO sacar BPE del marco de estado del arte en el Capítulo 1 para empezar allí una teoría técnica propia.
- NO presentar antes la parte algebraica de Capítulo 2 y dejar Gelfand/topología como apéndice conceptual. Ese orden ya se descartó.
- NO tratar la clasificación interior/exterior/frontera como comentario visual secundario. Es estructura, no decoración.
- NO usar la frontera y el exterior estricto como si fueran el mismo régimen en la geometría fina del Capítulo 5.
- NO atribuir a `Weyl--Horn` más de lo que da. No sustituye ni la reducción racional exterior ni a Rouché.
- NO mezclar en un mismo plano expositivo el techo macroscópico de conteo con la localización exacta átomo por átomo.
- NO convertir enumeraciones locales en notación global persistente.
- NO dejar cierres blandos; el Capítulo 4 debe cerrar con resultado, lectura y transición.
- NO dejar referencias vagas cuando el manuscrito ya dispone de etiquetas exactas.

## Checklist de revisión para el Capítulo 5

- [ ] La apertura distingue con claridad puente macroscópico (`Weyl--Horn`) y mecanismo fino (reducción racional exterior + `Rouché`).
- [ ] Cada enunciado principal está formulado primero con la geometría correcta del régimen que trata.
- [ ] "Puramente exterior" se usa solo para `|c|>R`.
- [ ] `I_out^*` se usa solo para exterior estricto; frontera queda fuera de ese subconjunto.
- [ ] Los puntos de frontera no se venden como simple variación del caso exterior estricto; aparece explícitamente la escala `1/n`.
- [ ] En el caso mixto sin frontera queda explícito que los átomos interiores deforman constantes pero no la ley exterior dominante.
- [ ] En el caso mixto con frontera queda explícito el análisis a dos escalas: macroscópica por `F_out`, microscópica por `H(x)`.
- [ ] Las referencias a resultados anteriores son exactas (`thm`, `prop`, `lem`, `eqref`).
- [ ] No hay sobreventa del alcance inverso desde matrices a resultados abstractos.
- [ ] La vía de cuasi-ortogonalidad aparece, si hace falta, como comparación o respaldo, no como columna principal.
- [ ] El cierre del capítulo deja explícito: localización de ceros resuelta en los regímenes tratados; `Q_m(\D)` exacto en el caso mixto sigue abierto.

## Pendientes abiertos o puntos a vigilar

- El Capítulo 5 sigue siendo el más frágil narrativamente: puede romperse si mezcla demasiado pronto escalas, regímenes o mecanismos.
- Vigilar que los enunciados no arranquen desde fórmulas cuando el fenómeno geométrico puede decirse primero.
- Vigilar que los bloques "mixto sin frontera" y "mixto con frontera" no oculten la idea central bajo exceso de álgebra lineal de detalle.
- Vigilar que el lector entienda que frontera pura y exterior estricto comparten estabilización algebraica en Capítulo 3, pero NO la misma geometría fina en Capítulo 5.
- Mantener visible el problema abierto real: la dificultad pendiente está en determinar exactamente `Q_m(\D)` en el caso mixto, no en el patrón de localización de ceros ya demostrado.

## Checklist rápido para el Capítulo 1

- [ ] La estructura visible sigue la secuencia ya acordada y no abre secciones técnicas impropias.
- [ ] La motivación deja claro el problema de ceros y la pérdida de fuerza de la norma del operador en Sobolev.
- [ ] `Intro.md` se ha usado como fuente de apoyo y cribado, no como texto trasplantado.
- [ ] BPE aparece solo como parte del mapa conceptual y del estado del arte, no como núcleo técnico anticipado.
- [ ] La notación que prepara Capítulos 2--5 se mantiene en nivel mínimo y no invade antes de tiempo.

## Regla de uso rápido

- Antes de tocar cualquier capítulo, comprobar siempre tres cosas: qué papel estructural cumple, qué notación ya está legitimada en ese punto del manuscrito y qué resultado exacto debe preparar para el capítulo siguiente.
- Antes de tocar el Capítulo 5, comprobar además qué escala se está usando, qué régimen geométrico se está tratando y cuál es el resultado exacto que ya quedó demostrado en capítulos anteriores.
