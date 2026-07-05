En la reunión del **2 de julio** se llevó a cabo una planificación exhaustiva y minuciosa de la defensa del TFM, centrándose de manera prioritaria en el diseño, la lógica narrativa y el contenido detallado de las diapositivas de la presentación. Las tutoras (Carmen y Raquel) insistieron en que, debido al límite de tiempo (20 minutos), la exposición no debe perderse en detalles técnicos ni en demostraciones complejas, sino centrarse en contar de forma visual y fluida "cómo ocurrió" la investigación, destacando que el TFM es un trabajo redondo que resuelve y formaliza matemáticamente los hallazgos empíricos del TFG.

A continuación, se detalla la **estructura y el contenido exacto diapositiva por diapositiva** acordado en la reunión:

---

### Diapositiva 1: Contexto y Comparativa (Doble Columna)

Para evitar que el tribunal se pierda con tecnicismos de teoría de la medida, se acordó simplificar el preámbulo hablando directamente de **productos escalares** en el espacio de polinomios $\mathbb{P}(z)$. La diapositiva se estructurará en **dos columnas paralelas** para contrastar la teoría clásica con el caso de Sobolev:

- **Columna Izquierda (Caso Clásico):**
    - Se introduce una medida de Borel con soporte compacto e infinito. El soporte infinito es clave para asegurar la existencia de la sucesión de polinomios ortonormales.
    - Se presenta el producto escalar estándar y la sucesión de polinomios ortonormales.
    - Se expone la equivalencia fundamental: el soporte de la medida es compacto si y solo si el operador de multiplicación $D(p) = zp$ es acotado, lo cual equivale a que los ceros de los polinomios estén uniformemente acotados.
    - Se destaca que en este caso la norma del operador $\|D\|$ localiza exactamente el punto más alejado del soporte (la distancia máxima al origen).
- **Columna Derecha (Caso Sobolev Discreto):**
    - Se define el producto escalar de Sobolev discreto introduciendo la derivada y un conjunto de puntos o átomos discretos $c_1, \dots, c_n$.
    - Se explica que, con este producto, el operador de multiplicación $D$ es el mismo, pero **las equivalencias clásicas fallan por completo**: el operador $D$ puede no ser acotado ($\|D\| = \infty$) a pesar de que el soporte continuo sea compacto, mientras que los ceros de los polinomios ortonormales siguen estando uniformemente acotados.

### Diapositiva 2: Ejemplo Motivador (Castro-Durán)

- Se presenta de manera gráfica el ejemplo histórico de **Castro-Durán** (apoyado en los trabajos de Alfaro).
- Este ejemplo muestra un producto de Sobolev con la medida de Lebesgue en la circunferencia unidad y un átomo en la frontera o en el exterior.
- Se evidencia que en este escenario el operador de multiplicación no es acotado ($\|D\| = \infty$), lo que ilustra que la norma clásica deja de dar cualquier tipo de información sobre el soporte o la ubicación de los átomos.

### Diapositiva 3: Pregunta Central y el "Gran Descubrimiento"

- **La Pregunta:** Al fallar la acotación clásica, ¿cómo podemos medir la falta de acotación del operador $D$ más allá de la norma? ¿Y cómo podemos recuperar la información geométrica del soporte a partir de matrices finitas?.
- **El Enfoque:** Explicar que el objetivo inicial del estudio eran los ceros de los polinomios, pero que la investigación derivó hacia un análisis espectral inédito del operador $D$ basado en **valores singulares** (evitando el término "espectro" para que el tribunal no pregunte por autovalores de operadores no acotados).
- **El Descubrimiento:** Aunque la norma del operador (el primer valor singular) explota al infinito y es inútil, los siguientes valores singulares (que generalizan los números de Gelfand) contienen información matemática precisa que **localiza los átomos** y delimita la geometría del soporte.

### Diapositiva 4: Representación Matricial (Conexión con el TFG)

- Se muestra visualmente el operador de multiplicación mediante una **matriz infinita de Hessenberg** (con puntos suspensivos), lo cual resulta muy vistoso para el tribunal.
- Se recuerda brevemente que en tu TFG estudiaste de forma experimental los valores singulares $\sigma_{k,N}$ de las secciones truncadas de tamaño $N$ de esta matriz, observando que sus límites asintóticos existían.
- Se establece el **objetivo del TFM**: formalizar matemáticamente esos límites empíricos y extender los conceptos de la teoría de operadores para justificar esos comportamientos.

### Diapositiva 5: Números de Gelfand y el nuevo Índice $Q_k$

- Se definen los números de Gelfand clásicos $c_k(D)$ para operadores acotados en espacios de Hilbert, mostrando la fórmula del ínfimo de los supremos sobre subespacios de codimensión finita.
- Se expone el problema técnico: nuestro operador $D$ no es acotado y solo está definido en el espacio de polinomios $\mathbb{P}(z)$, por lo que la teoría clásica de Gelfand no es aplicable.
- Se introduce la gran aportación del TFM: el **índice $Q_k(D)$**, que define un índice análogo utilizando **codimensión algebraica** directamente sobre $\mathbb{P}(z)$.
- Se muestra la cadena decreciente de índices $Q_k(D)$ y se enuncia el teorema de consistencia: si el operador $D$ es acotado, el índice $Q_k(D)$ coincide exactamente con el número de Gelfand clásico de su extensión al espacio de Hilbert.

### Diapositiva 6: Ejemplo de la Cadena y Ruptura (Átomo en $z=2$)

- Se retoma el ejemplo con la medida de Lebesgue y un único átomo exterior en $z=2$.
- Se muestra cómo se comporta la cadena: $Q_0(D) = \infty$ (lo que confirma que el operador global no es acotado), pero al restringir al subespacio de codimensión 1 (anulando el átomo), el índice se vuelve finito: $Q_1(D) \le 2$ (y de hecho se estabiliza en 1, que es el radio del soporte).
- Esto demuestra de forma práctica que el índice $Q_1(D)$ es capaz de "esquivar" la no acotación y recuperar el soporte continuo de la medida.

### Diapositiva 7: Geometría, BPEs y Funcionales Estables

- Se definen formalmente los conceptos de **Ruptura** (cuando la cadena pasa de infinito a finito) y **Estabilización** (cuando la cadena se vuelve constante).
- Se introduce la distinción geométrica clave respecto al soporte de radio $R$:
    - **Puntos interiores ($|c| < R$):** Son de tipo BPE (Evaluaciones Puntuales Acotadas). Los funcionales de evaluación $\delta_c$ y de su derivada $\delta'_c$ son continuos, aportando estabilidad al espacio.
    - **Puntos exteriores o de frontera ($|c| \ge R$):** No son BPE. Los funcionales asociados son discontinuos y generan la inestabilidad que hace explotar al operador.
- Se presenta la fórmula de la norma de Sobolev para motivar la introducción de los funcionales de evaluación $\delta_c$, sus derivadas $\delta'_c$ y el funcional especial $\Phi_p$. Se explica que los subespacios de codimensión finita se construyen como intersecciones de los núcleos de estos funcionales para "anular" las direcciones inestables de los átomos exteriores.

### Diapositiva 8: El Teorema de Ruptura y Conteo

- Se enuncia el **Teorema Principal 3.2.2**: si el producto de Sobolev tiene $m$ átomos en el exterior o en la frontera ($|c| \ge R$), la cadena de índices de Gelfand algebraicos diverge a infinito exactamente hasta el índice $m-1$ ($Q_0 = Q_1 = \dots = Q_{m-1} = \infty$) y se vuelve finita a partir del índice $m$ ($Q_m < \infty$).
- Se acompaña de un **dibujo a color** de la circunferencia con los átomos pintados en rojo (exteriores) y azul (interiores).
- Se resalta el valor estético y conceptual de este resultado: el índice abstracto $Q_k(D)$ actúa de facto como un "contador" que nos dice exactamente cuántos átomos se han escapado al exterior del soporte continuo.

### Diapositiva 9: El Teorema de Estabilización

- Se presenta el **Teorema 3.2.5**: si el producto tiene un total de $n$ átomos (tanto interiores como exteriores), la cadena no solo se vuelve finita, sino que **se estabiliza exactamente en el radio $R$** de la circunferencia para todo índice mayor o igual a $n$ ($Q_n = Q_{n+1} = \dots = R$).
- Se conecta este resultado con la primera diapositiva: en el caso clásico, la norma $\|D\|$ daba el tamaño del soporte. En el caso Sobolev, el operador es no acotado, pero el índice estabilizado $Q_n(D)$ hereda esa propiedad clásica y recupera con precisión milimétrica el radio del soporte continuo $R$.

### Diapositiva 10: Teorema de Identificación Abstracto-Matricial ($Q_k = \sigma_k$)

- Se define el índice matricial $\sigma_k$ como el límite cuando $N \to \infty$ de los valores singulares $\sigma_{k,N}$ de las secciones finitas truncadas de la matriz infinita.
- Se expone el teorema estelar de identificación: **$\sigma_k = Q_k(D)$**.
- Se vende este resultado como el puente de oro del trabajo: el índice abstracto $Q_k(D)$ no es computable, pero los valores singulares de las matrices truncadas sí lo son mediante algoritmos numéricos. Este teorema da **consistencia matemática absoluta** a todos los experimentos empíricos y gráficos que se observaban en el TFG.

### Diapositiva 11: Ejemplos Numéricos y Simulaciones

- Se muestran gráficos de simulaciones numéricas para ilustrar los tres escenarios posibles del comportamiento de los límites asintóticos:
    1.  **Caso puramente interior:** Donde la cadena es acotada desde el principio.
    2.  **Caso puramente exterior:** Donde se ve la divergencia inicial y luego la estabilización.
    3.  **Caso mixto:** Con átomos dentro y fuera de la circunferencia.

### Diapositiva 12: Conclusiones (El Cuadro Resumen)

- Se acordó diseñar un **cuadro resumen muy visual** que conecte la teoría de operadores, el análisis matricial asintótico y la geometría de los átomos:
    - _Todos los átomos dentro:_ Muestra de forma paralela que el operador es acotado, los límites matriciales $\sigma_k$ son finitos desde el inicio y el dibujo de la circunferencia tiene solo puntos interiores.
    - _Un átomo fuera:_ Muestra que el primer valor singular es infinito ($\sigma_0 = \infty$), pero a partir de $\sigma_1$ se estabiliza en el radio.
    - _Múltiples átomos fuera:_ Muestra los primeros $\sigma_k$ infinitos (tantos como átomos fuera) y la posterior caída y estabilización asintótica en $R$.

### Diapositiva 13: Líneas Futuras de Investigación

- Se exponen de manera formal las tres líneas de continuación naturales del trabajo:
    1.  Extensión del estudio a **productos de Sobolev continuos** (no solo con masas discretas).
    2.  Generalización de la circunferencia a **curvas analíticas de Jordan generales**, utilizando parametrizaciones continuas y sabiendo que la teoría de BPE se comporta de manera análoga en sus interiores.
    3.  Conexión de este comportamiento espectral con la **localización asintótica de los ceros** de los polinomios ortogonales de Sobolev.
- Se cierra anunciando con orgullo que este trabajo ya ha dado lugar a la redacción de un **preprint de investigación conjunta** (Gabriel, Raquel y Carmen) listo para su envío a publicación.

---

🎨 ¿Quieres que redacte un borrador detallado del guión de exposición (_speech_) diapositiva por diapositiva para que puedas ensayar y controlar los tiempos de tu defensa de 20 minutos?
