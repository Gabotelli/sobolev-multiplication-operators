# Notas del orador — Defensa del TFM

**Título:** Análisis espectral y matricial del operador de multiplicación en espacios de Sobolev discretos.  
**Autor:** Gabriel Suárez.  
**Tutoras:** Carmen Escribano y Raquel Gonzalo.  
**Duración objetivo:** 20 minutos aprox.  
**Estructura real:** 21 diapositivas.

> Criterio general: tono formal, sobrio y matemático.  
> No leer fórmulas completas salvo una vez cuando sea imprescindible.  
> Insistir en dos ideas durante toda la exposición: **contar obstrucciones** y **recuperar la información desde matrices finitas**.

---

## 1. Portada — (~0,4 min)

- Saludar y presentar el título, el marco del TFM y a las tutoras.
- Anunciar en una frase el hilo de la charla: estudiar qué ocurre con el operador de multiplicación en Sobolev discreto cuando la norma clásica deja de servir, y cómo esa información se recupera matricialmente.

---

## 2. Caso clásico frente a Sobolev discreto — (~1,3 min)

- Presentar la diapositiva como un paralelo entre dos marcos construidos sobre \(\Poly\): a izquierda el caso clásico, a derecha el caso Sobolev discreto.
- En ambas columnas, mencionar primero el dato de partida \(\mu\); en Sobolev añadir además los puntos \(c_1,\dots,c_N\). Presentarlas como dos columnas limpias, sin enfatizarlas con cajas.
- Una vez recorridas las dos columnas, bajar al recuadro central y presentar ahí la definición del **operador de multiplicación**: \(\D p(z)=zp\).
- Decir explícitamente que en ambos productos aparecen familias de polinomios ortonormales.
- Cerrar abajo con dos ideas separadas: primero la triple equivalencia clásica entre acotación de \(\D\), compacidad del soporte y acotación uniforme de los ceros; después, en el lado Sobolev, marcar solo las implicaciones que fallan y que se justificarán inmediatamente.
- En concreto, señalar dos flechas hacia \(\D\): soporte compacto \(\not\Rightarrow\) \(\D\) acotado y ceros uniformemente acotados \(\not\Rightarrow\) \(\D\) acotado.
- Decir que la diapositiva siguiente da el mismo ejemplo para ambas: el producto de Castro--Durán / Alfaro tiene soporte continuo compacto y ceros uniformemente acotados, pero \(\D\) no es acotado.

---

## 3. Ejemplo motivador: Castro--Durán / Alfaro — (~1,1 min)

- Presentar el ejemplo como la primera señal de que el caso Sobolev no se comporta como el clásico.
- Señalar el dibujo de la derecha de forma muy breve: segmento real para el soporte continuo y punto destacado en \(x=1/2\) para la parte discreta.
- Decir explícitamente que, aun con soporte continuo acotado, los ceros siguen uniformemente acotados pero \(\D\) no es acotado.
- Añadir en una frase que este fenómeno tiene mucha literatura, sobre todo en el caso de medidas con soporte sobre la recta real.
- Concluir: la norma del operador ya no basta; hace falta otra forma de medir la falta de acotación.
- Leer la pregunta guía al final de la diapositiva.

---

## 4. Estudio del operador de multiplicación por z en Sobolev general — (~1,2 min)

- Empezar arriba, sin cuadros y sin redefinir \(\D\): si \(\D\) es acotado respecto de la norma de Sobolev, entonces los ceros quedan contenidos en \(\overline{D(0,\|\D\|_S)}\); por tanto, estudiar \(\D\) da control geométrico sobre los ceros.
- Añadir inmediatamente la frase bibliográfica, también arriba y de forma compacta: existe mucha literatura sobre este problema, especialmente para medidas con soporte sobre la recta real; mencionar explícitamente Alfaro--Marcellán--Rezola--Ronveaux (1992), Alfaro--López--Rezola (1996), Alfaro--Rezola (2001), Meijer (1993), Gautschi--Kuijlaars (1997), López Lagomasino--Pijeira (1999) y López Lagomasino--Pijeira--Pérez Izquierdo (2001).
- Pasar después al reparto en dos columnas. En la columna izquierda, entrar primero en el cuadro de definición y leerla casi literalmente: un punto \(a\) es \(\operatorname{bpe}\) si \(|p(a)|^2\le C_a\int_{\C}|p(z)|^2\,d\mu(z)\) para todo \(p\in\Poly\). Añadir oralmente que esto distingue las evaluaciones puntuales controladas por la parte continua.
- Seguir en la misma columna izquierda con el teorema de estabilidad discreta y atribuirlo a Escribano--Gonzalo (2025, clave \texttt{EG25-2}): si \(\D\) es acotado en \(L^2(\mu)\) y los puntos \(a_1,\dots,a_N\) pertenecen a \(\operatorname{bpe}(\mu)\), entonces \(\D\) sigue siendo acotado para la norma de Sobolev discreta; en consecuencia, los ceros quedan uniformemente acotados.
- Cerrar mirando la columna derecha, ahora sí como bloque destacado: aunque \(\D\) pueda no extenderse acotadamente a la compleción, su acción sobre \(\Poly\) sigue determinando una matriz infinita de Hessenberg. Subrayar que ahora la diapositiva la muestra visualmente, con su esquema infinito y la banda de Hessenberg visible mediante puntos suspensivos; después leer la identidad \(d_{i,j}=\langle z\phi_j,\phi_i\rangle_S\). Atribuir esta perspectiva al enfoque matricial de Escribano--Gonzalo--Torrano (2023, \texttt{EGT23}) y Escribano--Gonzalo (2025, \texttt{EG25-2}).
- Enlazar con la siguiente diapositiva diciendo que el TFG estudió precisamente las secciones finitas de esa matriz infinita.

---

## 5. Punto de partida del TFG y objetivo del TFM — (~1,4 min)

- Empezar recordando que en el TFG se estudiaban las secciones finitas de la matriz infinita anterior. Como ahora toda la diapositiva va apilada en una única columna y a ancho completo, presentar en la frase de apertura, de forma inline, \(\mathbb P_n=[\phi_0,\dots,\phi_n]\), \(\mathcal D_n(p)=\pi_n(\D p)\) y \(\mathbf D_n\) como la sección principal correspondiente.
- Bajar después al bloque de definición, que ocupa todo el ancho. Leer \(\sigma_{k,n}\) como el \(k\)-ésimo valor singular de \(\mathbf D_n\), ordenado de forma decreciente, y explicar que la fórmula relevante es la formulación min-max de Courant--Fischer: un ínfimo sobre subespacios de codimensión menor que \(k+1\) de la norma restringida, equivalentemente un esquema inf-sup.
- Continuar, sin cambio de columna, con el bloque rojo de observación empírica y afirmar de forma directa lo que se observó en el TFG: para cada \(k\) fijo, \(\sigma_{k,n}\) converge a un valor \(\sigma_k\).
- Cerrar con el bloque \textbf{Objetivo del TFM}, también a ancho completo: formalizar ese comportamiento, definir el análogo infinito de los valores singulares, precisar el umbral de finitud y la estabilización, y recuperar ambos fenómenos desde las matrices finitas.

---

## 6. Números de Gelfand y codimensión — (~1,2 min)

- Empezar por la definición clásica de número de Gelfand en un espacio de Hilbert.
- Leer debajo la cadena y remarcar que \(c_0(\widetilde{\mathcal D})=\|\widetilde{\mathcal D}\|\), de modo que el primer término recupera la norma del operador cuando la extensión existe y es acotada.
- En el bloque de alerta, separar con claridad los dos problemas: necesitamos un operador acotado en la compleción y, además, nuestro operador está definido de manera natural solo sobre \(\Poly\).
- Cerrar con la definición de codimensión, porque será la variable que sustituya a la norma en el marco general.

---

## 7. Codimensión, núcleos y funcionales relevantes — (~1,1 min)

- Presentar la diapositiva como un paralelo en dos columnas: a la izquierda la caracterización hilbertiana para subespacios cerrados, y a la derecha la versión algebraica sobre \(\Poly\).
- En ambas proposiciones insistir en la misma idea: codimensión finita equivale a imponer un número finito de restricciones lineales independientes; en el marco de Hilbert, además, los funcionales deben ser continuos.
- Bajar después al bloque \textbf{Funcionales relevantes} y definir, sin entretenerse, \(\delta_c(p)=p(c)\), \(\delta'_c(p)=p'(c)\) y \(\psi_c(p)=(\D p)'(c)=p(c)+cp'(c)\).
- Cerrar con la frase final: si los puntos son distintos, entonces las familias de funcionales \(\{\delta_{c_j}\}\), \(\{\delta'_{c_j}\}\) y \(\{\psi_{c_j}\}\) son linealmente independientes.
- Enlazar con la siguiente diapositiva diciendo que esa independencia permitirá contar cuántas restricciones hacen falta para recuperar acotación.

---

## 8. Índice \(Q_k\): definición y propiedades — (~1,3 min)

- Presentar \(Q_k\) como el objeto central del trabajo.
- Leer la definición con calma: es el ínfimo de las normas restringidas a subespacios de codimensión menor que \(k+1\).
- Después bajar a la lista, ahora a ancho completo, y resaltar tres propiedades y nada más: admite \(+\infty\), empieza en \(Q_0=\|T\|\), y forma una cadena decreciente.
- Terminar con el bloque \textbf{Proposición}, también a ancho completo, para enunciar la fórmula max--min que servirá de puente con el análisis matricial.

---

## 9. Ejemplo: norma infinita pero codimensión 1 suficiente — (~1,0 min)

- Volver a un ejemplo concreto para que la definición no quede en abstracto.
- Decir explícitamente que la norma global explota: \(\|\D\|_S=Q_0(\D)=\infty\).
- Luego pasar al subespacio \(V=\{p\in\Poly: p(2)=0\}\) y remarcar que, en esa restricción, la constante óptima es \(2\), es decir, \(\sup_{p\in V\setminus\{0\}} \|\D p\|_S/\|p\|_S = 2\).
- Cerrar con la idea conceptual: aunque \(\D\) sea no acotado, la cadena de los \(Q_k\) no tiene por qué quedarse enteramente en \(+\infty\).
- Frase clave: **el índice cuenta cuántas restricciones hacen falta para recuperar acotación**.

---

## 10. Compatibilidad con Gelfand — (~0,8 min)

- Enunciar el teorema empezando en \(\Poly\): si \(T:\Poly\to\Poly\) es acotado y \(\widetilde T\) es su extensión acotada a la compleción hilbertiana, entonces \(Q_k(T)=c_k(\widetilde T)\).
- Interpretación oral: el índice nuevo no contradice la teoría clásica, sino que recupera exactamente el número de Gelfand de la extensión hilbertiana cuando esta existe.
- No dar demostración.

---

## 11. Modelo del TFM y dos fenómenos a estudiar — (~1,0 min)

- Recordar el modelo concreto que se estudia en toda la segunda parte.
- Introducir los dos enteros con papeles distintos: \(m\) = número de átomos fuera o sobre la circunferencia; \(N\) = número total de átomos.
- Definir oralmente ruptura y estabilización de la cadena.
- Avisar: la charla entra ahora en el núcleo de los resultados.

---

## 12. Primeros casos: todos dentro y primer ejemplo de ruptura — (~1,1 min)

- Empezar por el caso estable: si todos los átomos son interiores, \(\D\) es acotado.
- Eso sirve para fijar que los átomos interiores no fuerzan ruptura.
- Después pasar al ejemplo con un átomo exterior: ya aparece \(Q_0=\infty\) pero \(Q_1<\infty\).
- Decir que esto sugiere que la ruptura depende exactamente del número de átomos exteriores.

---

## 13. Teorema de ruptura — (~1,2 min)

- Éste es uno de los teoremas centrales.
- Leer el enunciado sin prisas: si hay \(m\) átomos con \(|c_j|\ge R\), entonces los primeros \(m\) índices menos uno son infinitos y el primero finito es \(Q_m\).
- Explicarlo en lenguaje simple: el índice cuenta cuántas obstrucciones exteriores hay.
- Señalar el dibujo: los puntos exteriores son los que generan el bloque infinito inicial.

---

## 14. Idea de la prueba de ruptura — (~1,2 min)

- Presentarla en dos bloques paralelos: \textbf{suficiencia} y \textbf{necesidad}.
- En la suficiencia, construir \(V_m=\bigcap\ker(\psi_{c_j})\), decir que tiene codimensión \(m\) y que ahí las contribuciones exteriores desaparecen, con lo que \(Q_m(\D)\) ya es finito.
- En la necesidad, explicar que con codimensión estrictamente menor que \(m\) todavía sobrevive alguna dirección singular, así que \(Q_{m-1}(\D)=\infty\).
- Mencionar sin entrar en detalles la interpolación de Hermite y los paquetes diagonales \(u_{j,n}\).
- Idea verbal a repetir: **hay que anular exactamente las \(m\) direcciones singulares**.

---

## 15. Teorema de estabilización — (~1,0 min)

- Presentar ahora el segundo fenómeno.
- Enunciar: a partir del índice \(N\), la cadena ya no solo es finita, sino constante, y vale exactamente \(R\).
- Usar el esquema lineal de la diapositiva para distinguir visualmente los tres regímenes: infinito, finito intermedio y cola constante.

---

## 16. Idea de la prueba de estabilización y aplicación directa — (~1,2 min)

- Presentarla en dos columnas: primero \textbf{cota inferior}, después \textbf{cota superior}, y cerrar con la aplicación conceptual de abajo.
- En la cota inferior, introducir el subespacio \(E=\{p\in\Poly:p'(c_j)=0\ \forall j\}\) y decir que, al intersectarlo con cualquier subespacio admisible \(W\), la parte discreta de \(\|p\|_S\) desaparece.
- Leer solo la desigualdad clave: \(\|\D p\|_S^2\ge R^2\|p\|_S^2\), de donde sale \(Q_k(\D)\ge R\) para todo \(k\).
- En la cota superior, pasar al subespacio \(V_N=\bigcap_{j=1}^N\ker\psi_{c_j}\), remarcar que tiene codimensión \(N\) y que allí se anulan todas las contribuciones discretas de \((\D p)'(c_j)\).
- Concluir con la aplicación: para la medida de Lebesgue sobre la circunferencia, la norma clásica de \(\D\) detecta el punto del soporte más alejado del origen; en el caso Sobolev discreto, ese papel lo recupera \(Q_N(\D)=R\).

---

## 17. Análisis matricial — (~1,4 min)

- Empezar recordando que \(\mathbf D\) es la matriz infinita de Hessenberg asociada a \(\D\), y que \(\mathbf D_n\) es su sección finita de tamaño \((n+1)\times(n+1)\).
- Señalar inmediatamente que lo relevante ahora son los valores singulares \(\sigma_{0,n}\ge\cdots\ge\sigma_{n,n}\).
- Enunciar el resultado de monotonía: para cada \(k\) fijo, la sucesión \(\sigma_{k,n}\) es creciente, así que el límite existe.
- Introducir entonces la definición \(\sigma_k(\mathbf D):=\lim_{n\to\infty}\sigma_{k,n}\).
- Cerrar con el teorema \(\sigma_k(\mathbf D)=Q_k(\D)\): el índice abstracto definido por codimensión finita coincide exactamente con el límite matricial computable.

---

## 18. Cuadro resumen — (~0,9 min)

- Presentar la diapositiva como un cuadro visual de tres columnas: a la izquierda el análisis espectral con los \(Q_k(\D)\), en el centro el análisis matricial con los límites \(\sigma_k(\mathbf D)\), y a la derecha el soporte.
- Recorrerla estrictamente por filas: **todos los átomos dentro**, **solo un átomo en 2** y **mixto**.
- En las tres filas señalar la misma idea geométrica: la parte continua siempre vive sobre la circunferencia unidad \(\mathbb S_1\), y lo que cambia es la posición de los átomos discretos.
- Al leer las dos primeras columnas, usar el color como guía: en rojo queda el régimen infinito inicial, y en verde la cola estable donde el valor ya es \(1\).
- En la fila intermedia remarcar que, con un único átomo en \(2\), la ruptura ocurre en \(k=0\) y la estabilización aparece inmediatamente en \(k=1\).
- En la fila mixta insistir en la diferencia entre \(m\) y \(N\): primero hay \(m\) obstrucciones infinitas, después un tramo finito intermedio, y desde \(N\) en adelante se recupera otra vez el valor \(1\).
- No añadir matemática nueva: usarla solo como síntesis final de ruptura, estabilización y traducción matricial.

---

## 19. Conclusiones y líneas futuras — (~1,0 min)

- Cerrar con tres ideas: el problema no es solo acotado/no acotado; \(Q_k\) mide cuántas obstrucciones hay; y la igualdad con \(\sigma_k\) da computabilidad.
- Mencionar tres líneas futuras muy concretas: primero, sustituir la circunferencia por **curvas de Jordan**, explicando que si una semejanza da un problema equivalente, entonces tiene sentido preguntar si una deformación continua del soporte también preserva un problema equivalente.
- Segunda línea: considerar el caso con dos medidas compactamente soportadas, una en la parte de posición y otra en la derivada, leyendo solo la idea de la fórmula \(\int p\overline q\,d\mu_0 + \int p'\overline{q'}\,d\mu_1\).
- Tercera línea: pasar a un producto de Sobolev general de orden \(r\), con la suma de integrales de las derivadas hasta orden \(r\), sin desarrollar detalles técnicos.
- Cerrar agradeciendo y dejando paso a preguntas.

---

## 20--21. Referencias — (~0,2 min)

- Las dos diapositivas finales de referencias salen automáticamente de la misma bibliografía de la memoria, con etiquetas alfabéticas del mismo estilo.
- No hace falta leerlas en la exposición ordinaria; sirven como cierre documental y como apoyo inmediato si el tribunal pregunta por alguna fuente concreta.
- Si se llega a ellas, cerrar simplemente agradeciendo de nuevo y dejando visible la bibliografía.

---

## Resumen de tiempos

| # | Diapositiva | Tiempo aprox. |
|---|---|---:|
| 1 | Portada | 0,4 |
| 2 | Caso clásico frente a Sobolev discreto | 1,3 |
| 3 | Ejemplo motivador | 1,1 |
| 4 | Antecedentes operatoriales y matriciales | 1,1 |
| 5 | Punto de partida del TFG y objetivo del TFM | 1,4 |
| 6 | Números de Gelfand y codimensión | 1,2 |
| 7 | Codimensión, núcleos y funcionales relevantes | 1,1 |
| 8 | Índice \(Q_k\) | 1,3 |
| 9 | Ejemplo de codimensión 1 | 1,0 |
| 10 | Compatibilidad con Gelfand | 0,8 |
| 11 | Modelo y dos fenómenos | 1,0 |
| 12 | Primeros casos | 1,1 |
| 13 | Teorema de ruptura | 1,2 |
| 14 | Idea de la prueba de ruptura | 1,2 |
| 15 | Teorema de estabilización | 1,0 |
| 16 | Idea de la prueba de estabilización | 1,2 |
| 17 | Análisis matricial | 1,4 |
| 18 | Cuadro resumen | 0,9 |
| 19 | Conclusiones y líneas futuras | 1,0 |
| 20 | Referencias I | 0,1 |
| 21 | Referencias II | 0,1 |
|   | **Total aprox.** | **20,9** |

Si hace falta ajustar a 20 minutos reales en ensayo, recortar primero en las diapositivas 4, 8, 15 y 17, que están pensadas para poder comprimirse sin romper el hilo lógico.
