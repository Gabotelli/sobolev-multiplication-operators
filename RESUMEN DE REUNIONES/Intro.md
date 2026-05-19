Aquí tienes la estructura y contenidos extraídos de tus fuentes y de nuestras conversaciones para redactar el **Capítulo 1** de tu TFM, cumpliendo estrictamente con tus restricciones y utilizando el formato de cita requerido.

### 1. Introducción, contexto y motivación

*   **Ideas centrales:** La teoría clásica de polinomios ortogonales es una herramienta robusta, pero la introducción de derivadas en el producto escalar (espacios de Sobolev) altera profundamente sus propiedades algebraicas y analíticas. El propósito inicial es acotar y localizar los ceros de estos polinomios, pero nos encontramos con el obstáculo de que el operador natural para estudiarlos (el operador multiplicación) puede "romperse" (volverse no acotado) al introducir masas discretas.
*   **Resultados o hechos concretos:** En los productos de Sobolev, el operador de multiplicación pierde su simetría y puede no estar acotado, lo que hace que los métodos clásicos fallen.
*   **Referencias o autores asociados:** D.C. Lewis (1947), quien introdujo los productos para la aproximación simultánea de funciones y derivadas; y P. Althammer (1962), quien dio el primer ejemplo donde un cero escapa del intervalo de ortogonalidad.
*   **Conexión con los ceros:** La imposibilidad de confinar los ceros a la geometría natural de la medida original es el "germen" de la investigación.
*   **Conexión con el operador de multiplicación:** Para estudiar los ceros, clásicamente se acota el operador de multiplicación $D(p) = zp$; la motivación del trabajo surge precisamente cuando se descubre que esta norma infinita ($||D|| = \infty$) inutiliza la teoría estándar, obligando a buscar nuevas métricas espectrales.
*   **Qué NO afirmar:** No debes introducir todavía tu notación propia ($I_{in}, I_{out}$, índices $Q_k$) ni hablar de la "estabilización de la cadena de valores singulares". El tono debe ser genérico.
*   **Propuesta de párrafo:**
    > El estudio de la localización de los ceros de los polinomios ortogonales constituye un problema central en la teoría de aproximación. Históricamente, la introducción de los productos escalares de Sobolev por Lewis en 1947 amplió este campo al incorporar información sobre las derivadas de las funciones. Sin embargo, esta generalización altera drásticamente las propiedades geométricas del espacio subyacente; en particular, el operador de multiplicación por la variable independiente pierde sus propiedades clásicas de simetría y acotación. Esta anomalía, evidenciada por primera vez por Althammer al demostrar que los ceros pueden escapar del soporte de ortogonalidad, constituye la motivación principal de este trabajo: ante la imposibilidad de acotar globalmente el operador de multiplicación, resulta imperativo desarrollar un nuevo marco funcional que permita localizar rigurosamente los ceros en el plano complejo.

---

### 2. Marco clásico mínimo

*   **Ideas centrales:** Definición estándar del producto escalar mediante medidas de Borel finitas y positivas con soporte compacto (recta real o circunferencia). Equivalencias clásicas de acotación.
*   **Resultados o hechos concretos:** En el caso clásico, tres propiedades son matemáticamente equivalentes: la acotación del soporte de la medida, la acotación del operador de multiplicación, y la acotación de los ceros (que residen estrictamente en la envoltura convexa del soporte). En la circunferencia, se utiliza la medida de Lebesgue normalizada.
*   **Referencias o autores asociados:** G. Szegő y Ya. L. Geronimus (teoría en la circunferencia).
*   **Conexión con los ceros:** Los ceros son siempre simples, reales (si el soporte es real) o confinados al disco unidad abierto, y se entrelazan.
*   **Conexión con el operador de multiplicación:** El operador de multiplicación es simétrico (en la recta real) o se representa mediante una matriz de Hessenberg isométrica/unitaria acotada (en la circunferencia).
*   **Qué NO afirmar:** No mezclar la topología de los espacios funcionales de Sobolev aquí; mantente estrictamente en el espacio de Hilbert estándar $L^2(\mu)$.
*   **Propuesta de párrafo:**
    > En la teoría clásica de Szegő, la ortogonalidad se define mediante una medida de Borel finita y positiva $\mu$ con soporte compacto. Bajo este producto escalar estándar, el operador de multiplicación $D(p) = zp$ exhibe un comportamiento regular y es simétrico cuando el soporte es real. Existe un resultado bien conocido que establece la equivalencia matemática entre la acotación del soporte de la medida, la acotación de la norma del operador $D$, y la localización estricta de los ceros de los polinomios ortogonales en el interior de la envoltura convexa del soporte.

---

### 3. Paso a productos de Sobolev discretos

*   **Ideas centrales:** Modificación del producto escalar clásico añadiendo masas discretas (átomos) que actúan sobre las derivadas de los polinomios. El contraste entre la geometría continua base y la perturbación puntual.
*   **Resultados o hechos concretos:** El producto toma la forma mixta (continuo-discreto): $\langle p,q\rangle_{S} = \int p(z) \overline{q(z)} d\mu_0(z) + \sum \lambda_k p^{(j)}(c_k)\overline{q^{(j)}(c_k)}$. Esto destruye la simetría del operador de multiplicación.
*   **Referencias o autores asociados:** M. Alfaro, F. Marcellán, M. L. Rezola (desarrollo de los casos discretos-continuos).
*   **Conexión con los ceros:** La inclusión de derivadas evaluadas en puntos (átomos) provoca que los ceros puedan migrar al plano complejo, abandonando el soporte continuo.
*   **Conexión con el operador de multiplicación:** La presencia de los átomos discretos en la derivada introduce funcionales que pueden disparar la norma del operador al infinito, $\|D\| = \infty$, incluso cuando el soporte continuo base es un compacto.
*   **Qué NO afirmar:** No debes afirmar que los funcionales de evaluación son siempre cerrados o continuos en esta etapa.
*   **Propuesta de párrafo:**
    > La transición hacia los espacios de Sobolev discretos se formaliza al incorporar al producto interno estándar una parte discreta que evalúa derivadas en un conjunto finito de puntos o átomos. Esta estructura mixta altera profundamente la topología del espacio: el operador de multiplicación pierde su simetría y las relaciones de recurrencia clásicas dejan de ser válidas. Como consecuencia analítica directa, la acotación global del operador puede perderse, provocando un comportamiento anómalo en el que los ceros de los polinomios ortogonales ya no están confinados a la geometría natural de la medida base.

---

### 4. Estado del arte

#### 4.1 Caso clásico
*   **Ideas centrales/Resultados:** Comportamiento asintótico de los ceros. Introducción de la clase **Reg** de medidas regulares. Si $\mu \in \textbf{Reg}$, la medida contadora de ceros convergerá débilmente a la medida de equilibrio del soporte.
*   **Referencias:** H. Stahl y V. Totik (General Orthogonal Polynomials, clase Reg).

#### 4.2 Caso Sobolev
*   **Ideas centrales/Resultados:** Intentos previos de acotar el operador. Concepto de medidas "secuencialmente dominadas" (donde $d\mu_k = f_{k-1} d\mu_{k-1}$ con funciones acotadas) que garantizan que el operador $D$ sea acotado. Teorema fundamental: Si $\|D\| < \infty$, entonces todos los ceros están uniformemente acotados y contenidos en el disco $\{z \in \mathbb{C} : |z| \le 2\|D\|\}$.
*   **Referencias:** G. López Lagomasino y H. Pijeira Cabrera (teorema del disco acotado por $2\|D\|$), J. M. Rodríguez (medidas admisibles y dominadas).
*   **Qué NO afirmar:** No afirmar que los ceros divergen a infinito si $\|D\|=\infty$. (La literatura demuestra que aunque el operador explote, los ceros pueden estabilizarse y ser atraídos por los átomos).

#### 4.3 Evaluaciones Puntuales Acotadas (BPE) y geometría interior-frontera-exterior
*   **Ideas centrales:** La dicotomía topológica generada por la ubicación de los átomos en el plano complejo y la condición de Szegő.
*   **Resultados o hechos concretos:** Un punto $c$ es una Evaluación Puntual Acotada (BPE) si existe una constante tal que $|p(c)| \le C \|p\|_S$. Si la medida satisface la condición de Szegő ($\int \log w(\theta) d\theta > -\infty$), los polinomios no son densos y existen BPEs en el interior del disco. Si un átomo se coloca en el exterior ($|c| > R$), el funcional de evaluación no está acotado (no es BPE), el núcleo algebraico es denso y el operador de multiplicación se vuelve no acotado.
*   **Referencias:** Miller, Smith y Yang (BPEs).
*   **Conexión con los ceros/operador:** La existencia de BPEs estabiliza el operador. Los puntos exteriores (no BPE) destruyen la acotación de $\|D\|$, y asintóticamente provocan que algunos ceros "escapen" de la circunferencia y sean atraídos hacia dichos átomos exteriores.
*   **Qué NO afirmar:** **Red Flag crítica**: Nunca debes afirmar que el núcleo de un funcional de evaluación en un átomo exterior (no BPE) es un subespacio topológicamente cerrado. Al no ser un funcional continuo, su núcleo algebraico puede ser denso en el espacio de Hilbert.

*   **Propuesta de párrafo (Englobando 4.1 a 4.3):**
    > El estado del arte revela una profunda relación entre las propiedades analíticas de la medida y la geometría de los ceros. Clásicamente, si la medida es regular, la distribución asintótica de los ceros converge a la medida de equilibrio del soporte. En el marco de Sobolev, López Lagomasino y Pijeira demostraron que si el operador de multiplicación es acotado, los ceros quedan confinados en un disco delimitado por $2\|D\|$. Los estudios de Rodríguez establecen que esta acotación exige condiciones de dominancia secuencial sobre las medidas. Sin embargo, la topología del espacio depende vitalmente de las Evaluaciones Puntuales Acotadas (BPE). Si la medida satisface la condición de Szegő, existen BPEs en el interior del recinto; pero la inclusión de átomos exteriores (no BPE) introduce funcionales no continuos cuyos núcleos no son necesariamente cerrados en la compleción de Hilbert. Esta inestabilidad rompe la acotación del operador y provoca un fenómeno de atracción, donde ceros excepcionales escapan del soporte continuo convergiendo hacia dichos átomos aislados.

Para redactar la introducción de tu Trabajo de Fin de Máster (TFM) con el rigor académico adecuado, aquí tienes el desarrollo de cada uno de los puntos solicitados. Esta estructura traza una narrativa natural: parte de la solidez de la teoría clásica, introduce la herramienta principal (el operador de multiplicación), presenta la perturbación (Sobolev) y culmina con el problema abierto (la pérdida de acotación) que motiva tu investigación.

### 1. La importancia de los ceros en la teoría clásica
**Explicación para el TFM:** 
En la teoría clásica de aproximación, el estudio de los ceros de los polinomios ortogonales es un pilar fundamental debido a su aplicación directa en la teoría de interpolación, el diseño de fórmulas de cuadratura numéricas y la teoría espectral. Cuando la ortogonalidad se define mediante un producto escalar estándar (basado en una medida de Borel finita y positiva), los ceros exhiben un comportamiento geométrico y analítico perfecto: son raíces simples, se entrelazan entre polinomios de grados consecutivos y, lo más importante, se encuentran estrictamente confinados en el interior de la envoltura convexa del soporte de la medida. 

**Referencias que lo respaldan:** 
*   *Dialnet-CerosDePolinomiosOrtogonalesDeSobolev-599694.pdf*: Establece explícitamente la importancia de los ceros en cuadraturas e interpolación, y su confinamiento en la envoltura convexa clásica,.

### 2. El operador de multiplicación por $z$ como objeto natural
**Explicación para el TFM:** 
La herramienta natural y más potente para estudiar la localización y el comportamiento asintótico de estos ceros es el operador lineal de multiplicación por la variable independiente, definido como $\mathcal{D}(p) = z p(z)$. La conexión matemática es profunda: al representar este operador matricialmente respecto a la base de polinomios ortonormales, se obtiene una matriz de Hessenberg. Los ceros del $n$-ésimo polinomio ortogonal coinciden exactamente con los autovalores de la sección finita truncada de esta matriz. Por consiguiente, acotar el operador de multiplicación es equivalente a acotar los ceros: un resultado clásico garantiza que si el operador está acotado, la totalidad de los ceros de los polinomios ortogonales residen en un disco compacto cuyo radio depende de la norma del operador $\| \mathcal{D} \|$,.

**Referencias que lo respaldan:**
*   *Convergencia del Segundo Valor Singular.pdf*: Explica la representación matricial de Hessenberg, la conexión de los autovalores con los ceros y el teorema de acotación en función de $\| \mathcal{D} \|$,,.
*   *1-s2.0-S0021904598933184-main.pdf*: Aborda cómo la acotación del operador de multiplicación garantiza que los ceros estén contenidos en un disco compacto,.

### 3. El cambio paradigmático al introducir productos de Sobolev
**Explicación para el TFM:** 
Históricamente, la introducción de los espacios de Sobolev por Lewis (1947) buscaba resolver problemas de aproximación simultánea de una función y sus derivadas. Al añadir derivadas evaluadas en puntos concretos (átomos discretos) al producto escalar, se altera drásticamente la geometría del espacio subyacente. La consecuencia analítica más notable es que se rompe el confinamiento clásico: Althammer (1962) demostró por primera vez que, bajo un producto de Sobolev, los ceros de los polinomios ortogonales ya no están obligados a permanecer en la envoltura convexa del soporte de ortogonalidad, pudiendo "escapar" hacia el plano complejo. 

**Referencias que lo respaldan:**
*   *2020Eigenvalue Problem for Discrete Jacobi Sobolev Orthogonal Polynomials.pdf*: Cita a Lewis (1947) y la motivación original de aproximación simultánea.
*   *Dialnet-CerosDePolinomiosOrtogonalesDeSobolev-599694.pdf*: Documenta el hito de Althammer (1962) y la existencia de ceros complejos o externos a la medida,.

### 4. La pérdida de acotación del operador como fenómeno central
**Explicación para el TFM:** 
La verdadera motivación de este problema de investigación surge de una anomalía funcional. Al incluir masas discretas actuando sobre las derivadas, el operador de multiplicación pierde su simetría habitual. Más aún, la evaluación de derivadas en puntos inestables introduce funcionales no acotados que provocan que la norma global del operador de multiplicación diverja a infinito ($\| \mathcal{D} \| = \infty$). Este fenómeno es crítico: al ser la norma infinita, los teoremas clásicos que acotaban los ceros en el disco de radio proporcional a $\| \mathcal{D} \|$ quedan completamente inutilizados. Se presenta entonces una paradoja matemática aparente, ya que experimentalmente los ceros a menudo permanecen acotados a pesar de que el operador que los rige no lo está,. Esto hace imperativa la búsqueda de nuevas métricas espectrales que permitan localizar los ceros cuando la teoría de operadores estándar falla.

**Referencias que lo respaldan:**
*   *Convergencia del Segundo Valor Singular.pdf*: Expone claramente el problema de la no acotación ($\| \mathcal{D} \| = \infty$), la inutilidad del teorema clásico bajo esta premisa, y la paradoja de que los ceros (radio espectral) sigan acotados mientras el primer valor singular diverge,,,.
*   *Dialnet-CerosDePolinomiosOrtogonalesDeSobolev-599694.pdf*: Menciona la pérdida de simetría del operador de multiplicación al introducir el parámetro $\lambda > 0$ en la parte discreta.

---

### Propuesta de Párrafo Resumen para tu Introducción:
*(Puedes utilizar este texto como base para hilar las secciones en tu documento)*

> "En la teoría clásica de aproximación, la localización de los ceros de los polinomios ortogonales es un problema ampliamente resuelto; dichos ceros gozan de excelentes propiedades de entrelazamiento y se confinan estrictamente en la envoltura convexa del soporte de la medida. El enfoque natural para su estudio analítico se basa en el operador de multiplicación por la variable independiente, cuyas representaciones matriciales finitas tienen por autovalores exactamente a los ceros de dichos polinomios. Bajo la ortogonalidad estándar, este operador es simétrico y acotado, lo que garantiza el confinamiento de los ceros en un disco proporcional a la norma del operador. Sin embargo, la transición hacia los espacios de Sobolev discretos —motivada por la aproximación simultánea de funciones y derivadas— quiebra esta armonía geométrica. La inclusión de evaluaciones puntuales sobre las derivadas destruye la simetría del operador y, fundamentalmente, puede provocar que su norma diverja a infinito. Ante la pérdida de acotación del operador de multiplicación, las cotas clásicas colapsan, permitiendo teóricamente que los ceros escapen del soporte hacia el plano complejo. Este fenómeno constituye la motivación central de la presente investigación: la necesidad de desarrollar un nuevo marco de análisis espectral que permita resolver el problema de la localización de los ceros cuando la métrica habitual del operador resulta matemáticamente inoperante."

**El Marco Clásico de los Polinomios Ortogonales**

La teoría clásica de los polinomios ortogonales se asienta sobre la definición de un producto escalar estándar en el espacio de los polinomios, $\mathbb{P}[z]$. Dada una medida de Borel finita y positiva $\mu$, con soporte compacto $S_\mu$, la ortogonalidad clásica entre dos polinomios $p$ y $q$ se define mediante la integral sobre dicho soporte:
$\langle p, q \rangle = \int_{S_\mu} p(z)\overline{q(z)} d\mu(z)$. 

Este marco proporciona una base geométrica y analítica perfecta, donde el soporte de la medida, el operador de multiplicación y la localización de los ceros interactúan de manera armónica.

**El papel del soporte de la medida y su relación con el operador de multiplicación**
El soporte de la medida $S_\mu$ determina el dominio donde los polinomios son evaluados e integrados. La herramienta natural y más potente para estudiar la distribución de los ceros en este contexto es el operador lineal de multiplicación por la variable independiente, definido como $D(p) = z p(z)$. 

Existe un resultado general y clásico que establece una triple equivalencia matemática fundamental: **la acotación del soporte de la medida $S_\mu$ es estrictamente equivalente a la acotación del operador de multiplicación $D$ ($\|D\| < \infty$), lo cual a su vez es equivalente a que el conjunto de los ceros de los polinomios ortogonales esté uniformemente acotado**. 

**Localización de los ceros y propiedades según la geometría del soporte**
El comportamiento del operador de multiplicación y la localización exacta de los ceros difieren según la naturaleza geométrica del soporte de la medida:

*   **En la Recta Real ($\mathbb{R}$):**
    Cuando el soporte $S_\mu$ es un intervalo o un subconjunto compacto de la recta real, el operador de multiplicación $D$ es simétrico respecto al producto escalar ($\langle xp, q \rangle = \langle p, xq \rangle$). Matricialmente, esto se traduce en una matriz tridiagonal simétrica (matriz de Jacobi). En este entorno, la geometría de los ceros es excelente: todos los ceros de los polinomios ortogonales son reales, simples, se entrelazan rígidamente entre polinomios de grados consecutivos, y se ubican estrictamente en el interior de la envoltura convexa del soporte $S_\mu$.

*   **En el Plano Complejo ($\mathbb{C}$):**
    Si la medida se soporta en un conjunto compacto del plano complejo, la simetría del operador se pierde y su representación pasa a ser una matriz de Hessenberg. Sin embargo, la equivalencia clásica se mantiene: al estar el soporte acotado, el operador $D$ es acotado, lo que garantiza formalmente que la totalidad de los ceros de los polinomios residen en un disco compacto del plano complejo delimitado por la norma del operador, es decir, dentro del disco $\{z \in \mathbb{C} : |z| \le \|D\|\}$. Además, a nivel asintótico, si la medida es regular (clase **Reg**), la distribución de los ceros converge hacia la medida de equilibrio del soporte.

*   **En la Circunferencia Unidad ($\mathbb{T}$) y la Medida de Lebesgue:**
    El estudio sobre la circunferencia unidad ($|z|=1$) constituye un campo propio conocido como la teoría de Szegő. Aquí, el operador de multiplicación es siempre acotado e isométrico (y de hecho unitario si la base es de polinomios de Laurent o la medida es la de Lebesgue), ya que el multiplicador cumple $|z|=1$ en todo el soporte. Una de las características principales de las medidas en la circunferencia unidad es que los ceros de los polinomios ortogonales recaen estrictamente en el interior del disco unidad abierto. 
    Específicamente, en el caso más estandarizado donde $\mu$ es la **medida de Lebesgue normalizada** sobre la circunferencia, los polinomios ortogonales mónicos resultan ser simplemente $z^n$, confirmando la simetría rotacional absoluta y haciendo que todos los ceros colapsen exactamente en el origen (que está trivialmente acotado en el interior del disco).

**Referencias Principales de la Literatura Clásica**
Para fundamentar esta subsección en el TFM, el estado del arte se apoya en los textos canónicos presentes en la literatura de teoría de aproximación y análisis armónico:
*   **G. Szegő** (*Orthogonal Polynomials*, 1975): Es la referencia absoluta para los resultados fundamentales, especialmente para ortogonalidad en la recta real y la construcción completa de la teoría sobre la circunferencia unidad.
*   **T. S. Chihara** (*An introduction to orthogonal polynomials*, 1978): Fuente esencial para los resultados de entrelazamiento, simplicidad y confinamiento de ceros en la envoltura convexa.
*   **P. Duren** (*Theory of $H^p$ spaces*): Referencia clave para entender las evaluaciones puntuales acotadas (BPE) asociadas a medidas en la circunferencia y propiedades de operadores en estos espacios.
*   **H. Stahl y V. Totik** (*General Orthogonal Polynomials*, 1992): Obra central para citar el comportamiento asintótico de los ceros, la capacidad logarítmica, la medida de equilibrio y la definición de las medidas regulares (clase **Reg**) en el plano complejo.
*   **Ya. L. Geronimus** (*Orthogonal polynomials: estimates, asymptotic formulas...*, 1961): Utilizado para la teoría clásica en la circunferencia y las relaciones de recurrencia.

Para estructurar conceptualmente el Capítulo 1 de tu TFM, es fundamental establecer cómo el operador de multiplicación actúa como el "puente" analítico y algebraico entre la medida de ortogonalidad (su soporte) y la geometría de los ceros. A continuación, te detallo cada uno de los puntos solicitados con el rigor y tono adecuados para tu marco teórico, fundamentado estrictamente en las fuentes de tu investigación.

### 1. Definición informal del operador de multiplicación
En el contexto de los espacios de polinomios $\mathbb{P}[z]$, el **operador lineal de multiplicación por la variable independiente**, frecuentemente denotado como $\mathcal{D}$, $D$ o $M_z$, se define de la forma más natural e intuitiva posible: toma un polinomio $p(z)$ y lo multiplica por $z$. Es decir, su acción es **$\mathcal{D}(p)(z) = z p(z)$**,. 

### 2. Por qué es natural en la base ortogonal y su reflejo matricial
Este operador es el objeto central de estudio porque "codifica" las relaciones de recurrencia que definen a los polinomios ortogonales. Cuando aplicas el operador $\mathcal{D}$ a un elemento de la base de polinomios ortonormales $\{\varphi_n\}_{n=0}^\infty$, el resultado $z\varphi_n(z)$ es un polinomio de grado $n+1$, el cual puede expresarse unívocamente como una combinación lineal de los propios elementos de la base hasta el grado $n+1$,.

Al escribir esta transformación en forma matricial, la topología del espacio se refleja en la estructura de la matriz resultante:
*   **Matriz de Jacobi (Caso Real):** Si la ortogonalidad viene dada por una medida soportada en la recta real $\mathbb{R}$, el operador de multiplicación es **simétrico** ($\langle xp, q \rangle = \langle p, xq \rangle$). Esto provoca que la representación matricial sea una **matriz tridiagonal simétrica** conocida como matriz de Jacobi,.
*   **Matriz de Hessenberg (Caso Complejo/Circunferencia):** Si la medida está soportada en el plano complejo $\mathbb{C}$ (como la circunferencia unidad), se pierde la simetría y la representación pasa a ser una matriz infinita de **Hessenberg superior**,,. 
*   *(Nota adicional)*: Para polinomios ortogonales de Laurent en la circunferencia, existen representaciones alternativas mediante matrices unitarias pentadiagonales (matrices CMV).

### 3. Acotación en el caso clásico
En la teoría clásica (usando un producto escalar estándar inducido por una medida finita de Borel $\mu$), la norma del operador de multiplicación depende directa y exclusivamente de la geometría del soporte de la medida. 

El resultado clásico establece que **el operador $\mathcal{D}$ es acotado (es decir, $\|\mathcal{D}\| < \infty$) si y solo si el soporte de la medida $\mu$ es un conjunto acotado (compacto)**. Si el soporte está acotado, la variable $z$ no puede "escapar" a infinito al integrar, por lo que la norma del operador se mantiene finita.

### 4. Relación con la localización de los ceros
La conexión más profunda y útil del operador $\mathcal{D}$ es que permite localizar los ceros de los polinomios sin necesidad de calcularlos explícitamente, traduciendo un problema analítico a uno de álgebra matricial finita.

Se demuestra que **los ceros del $n$-ésimo polinomio ortonormal $\varphi_n(z)$ coinciden exactamente con los autovalores de $D_n$** (la $n$-ésima sección principal truncada de la matriz infinita $D$, o su transpuesta),. 

A partir de aquí, el límite espectral dicta la geometría:
*   Si el operador $\mathcal{D}$ está acotado, se garantiza formalmente que **todos los ceros de la sucesión de polinomios están contenidos uniformemente en un disco compacto** delimitado por la norma del operador, típicamente acotados en el disco $\{z \in \mathbb{C} : |z| \le \|\mathcal{D}\|\}$ (o proporcionales a esta norma, como el disco de radio $2\|\mathcal{D}\|$ en algunas formulaciones),,,.

### 5. Limitaciones y Matices: Cuándo la relación es directa y cuándo requiere cuidado

Para tu TFM, es crucial establecer **dónde funciona perfectamente esta equivalencia y dónde "se rompe"**, ya que esta ruptura es la justificación de tu investigación con los productos de Sobolev.

*   **Relación directa y perfecta (La Recta Real):** 
    Para medidas estándar soportadas en la recta real, la relación es absoluta y directa. La acotación del soporte de la medida equivale a la acotación del operador $\mathcal{D}$, lo cual equivale a la acotación de los ceros. Además, gracias a que la matriz de Jacobi es hermitiana, se aplica el **Teorema de entrelazamiento de Cauchy** para autovalores, lo que garantiza que los ceros son reales, simples, se entrelazan y residen estrictamente en el interior de la envoltura convexa del soporte,.

*   **Formulación cuidadosa y ruptura (Plano Complejo y Espacios de Sobolev):** 
    Cuando pasamos al plano complejo, el operador ya no es simétrico (matriz de Hessenberg). Aunque en el caso estándar complejo la equivalencia clásica (Soporte Acotado $\iff$ Operador Acotado $\iff$ Ceros Acotados) se mantiene cierta, el verdadero quiebre ocurre al introducir derivadas discretas en los **productos de Sobolev**.
    
    En los espacios de Sobolev discretos (como $\langle p,q\rangle_{S} = \int K_0 p\overline{q} d\mu_0 + \lambda |p'(c)|^2$), **la relación directa se destruye**. La introducción de funcionales puntuales inestables (átomos) en la derivada provoca que el operador de multiplicación $\mathcal{D}$ pierda su acotación, es decir, **$\|\mathcal{D}\| = \infty$**, a pesar de que la medida base tenga soporte compacto,,. 
    
    *El gran matiz que justifica tu trabajo:* A pesar de que la norma del operador diverge a infinito ($\lim_{n\to\infty} \sigma_{1,n} = \infty$), inutilizando los teoremas clásicos, **el radio espectral $\rho(D_n)$ (que representa el módulo del cero más lejano) puede converger y mantenerse acotado**,. Es decir, se produce una **disociación espectral**: los ceros ignoran la patología del espacio y permanecen acotados, revelando que medir la cota de los ceros usando únicamente la norma global clásica del operador ($\|\mathcal{D}\|$ o el primer valor singular $\sigma_1$) es insuficiente y exige definir nuevos índices (como tu análisis de $\sigma_2$ o las codimensiones restrictivas),,.

Aquí tienes una síntesis estructurada con rigor académico, ideal para ser adaptada directamente en la introducción de tu Trabajo de Fin de Máster (TFM):

**Los Productos Internos de Sobolev Discretos: Una Ruptura del Paradigma Clásico**

La teoría clásica de los polinomios ortogonales se asienta sobre la definición de un producto escalar estándar dado por una integral respecto a una medida de Borel finita y positiva. En este marco, los polinomios exhiben propiedades sumamente regulares: satisfacen una relación de recurrencia de tres términos, y sus ceros son siempre reales, simples y residen en el interior de la envoltura convexa del soporte de la medida. Sin embargo, la generalización hacia los espacios de Sobolev introduce un cambio de paradigma que quiebra esta armonía clásica.

**1. Definición general de un producto de Sobolev discreto**
Un producto interno de Sobolev discreto se define al incorporar a la medida continua base (soportada en un intervalo o en una curva) una perturbación discreta formada por un número finito de evaluaciones puntuales que involucran las derivadas de los polinomios. Su forma general se expresa como:
$$\langle p, q\rangle_S = \int_{S_{\mu}} p(z) q(z) d\mu(z) + \sum_{i=1}^m M_i p^{(k_i)}(c_i) q^{(k_i)}(c_i)$$
donde $S_{\mu}$ es el soporte de la medida base, $M_i > 0$ son las masas, $c_i$ son los puntos de evaluación (o "átomos"), y $k_i \ge 0$ indican el orden de derivación en cada punto. 

**2. Diferencia conceptual: Integral clásica vs. Derivadas puntuales**
Conceptualmente, la ortogonalidad clásica mide exclusivamente el "tamaño" global o "masa" de las funciones sobre un soporte. En contraste, los productos de Sobolev incorporan información sobre la **regularidad** local de la función. Al añadir derivadas puntuales, el producto escalar no solo evalúa el comportamiento global del polinomio, sino que fuerza a la topología del espacio a registrar cómo varían y qué pendientes toman los polinomios de forma instantánea en los puntos $c_i$. Esta mezcla de geometría continua y perturbaciones discretas altera profundamente la estructura topológica y algebraica del espacio funcional.

**3. Efectos de la ruptura: Recurrencias, ceros y el operador de multiplicación**
La adición de la parte discreta provoca el colapso inmediato de las herramientas estándar:
*   **Pérdida de la Simetría del Operador:** El efecto más devastador es que el operador de multiplicación por la variable independiente, $D(p) = zp$, deja de ser simétrico respecto al nuevo producto interno ($\langle xp, q\rangle_S \neq \langle p, xq\rangle_S$).
*   **Ruptura de las Recurrencias:** Al perderse la simetría del operador, los polinomios de Sobolev ya no satisfacen la clásica relación de recurrencia de tres términos. En su lugar, requieren relaciones de orden superior o "recurrencias largas" que, matricialmente, se traducen en matrices multidiagonales o matrices de Hessenberg completas.
*   **No Acotación del Operador:** Incluso si la medida continua posee un soporte compacto, la introducción de átomos inestables en las derivadas puede hacer que el operador de multiplicación no esté acotado, es decir, $\|D\| = \infty$.
*   **Fuga de los Ceros:** Los ceros de los polinomios ya no están confinados rígidamente a la envoltura convexa del soporte de ortogonalidad. Pueden "escapar" hacia el plano complejo y, asintóticamente, verse atraídos por los átomos exteriores $c_i$.

**4. Resultados fundamentales y estado del arte**
Para cimentar esta ruptura en la introducción, el estado del arte se apoya en los siguientes hitos y autores clave de la literatura:
*   **El primer contraejemplo (P. Althammer, 1962):** Históricamente, Althammer proporcionó el primer ejemplo de un producto de Sobolev donde un polinomio exhibía un cero estrictamente fuera del intervalo de ortogonalidad, evidenciando empíricamente la pérdida del confinamiento clásico.
*   **Acotación de ceros y el operador (G. López Lagomasino y H. Pijeira Cabrera, 1999):** Estos autores establecieron que, en el plano complejo, la acotación de los ceros está directamente subyugada a la norma del operador de multiplicación. Probaron que si $\|D\| < \infty$, entonces la totalidad de los ceros de los polinomios ortogonales de Sobolev están contenidos en un disco cerrado dependiente de la norma del operador.
*   **Condiciones para la acotación (J. M. Rodríguez):** Para evitar la explosión de la norma del operador y garantizar su acotación, los trabajos de Rodríguez introdujeron la exigencia de que las medidas involucradas debían ser "secuencialmente dominadas" (donde una medida controla topológicamente a la siguiente). 
*   **Pérdida general de propiedades algebraicas (F. Marcellán, Y. Xu, y otros):** Extensos trabajos recopilatorios de Marcellán, Xu, Alfaro y Rezola documentan rigurosamente que las anomalías espectrales y asintóticas (como la pérdida de la recurrencia a tres términos y la atracción anómala de los ceros) son inherentes a los productos de tipo Sobolev discreto, requiriendo nuevas métricas para su estudio.

Esta síntesis presenta el problema directamente: evidencia por qué las herramientas de la teoría clásica colapsan (debido a la pérdida de simetría) y prepara el terreno para tu investigación sobre cómo domar a los ceros cuando la norma habitual del operador diverja a infinito.

A partir de la literatura proporcionada, el análisis de la pérdida de acotación del operador de multiplicación por $z$ ($D(p) = zp$) en espacios de Sobolev discretos es uno de los temas centrales del estado del arte. Aquí tienes la síntesis detallada:

**Autores que estudian este fenómeno**
*   **G. López Lagomasino, H. Pijeira Cabrera e I. Pérez Izquierdo:** Relacionan la acotación del operador con la ubicación de los ceros y definen las condiciones de dominancia entre medidas.
*   **J. M. Rodríguez, V. Álvarez, E. Romera, D. Pestana:** Caracterizan la acotación del operador a través del concepto de medidas "admisibles" y espacios de Sobolev con pesos generalizados.
*   **M. Alfaro, F. Marcellán y M. L. Rezola:** Documentan ampliamente el comportamiento anómalo de estos polinomios y la pérdida de simetría estructural frente al caso clásico.
*   **C. Escribano, R. Gonzalo (y aportes de tu propio análisis en el TFM):** Analizan el problema mediante un enfoque matricial (valores singulares de Hessenberg), estudiando casos específicos donde $\|D\| = \infty$ debido a átomos discretos.

**Contextos en los que aparece**
El fenómeno surge de forma natural al trabajar con **productos internos de Sobolev discretos o mixtos**. Esto ocurre cuando a una medida base absolutamente continua con soporte compacto (por ejemplo, en un intervalo real o en la circunferencia unidad) se le suma una perturbación discreta consistente en evaluar las derivadas de los polinomios en un número finito de puntos (átomos). 

**Hipótesis que suelen garantizar la acotación**
Para que la norma del operador se mantenga finita ($\|D\| < \infty$), la literatura establece que deben cumplirse condiciones muy restrictivas:
1.  **Medidas "secuencialmente dominadas":** Es decir, el soporte de cada medida de las derivadas debe estar contenido en la anterior ($\text{supp}(\mu_k) \subset \text{supp}(\mu_{k-1})$) y deben poder expresarse como $d\mu_k = f_{k-1} d\mu_{k-1}$ mediante funciones acotadas en $L^\infty$. 
2.  **Equivalencia de normas:** El producto debe ser esencialmente secuencialmente dominado (equivalente topológicamente a uno que sí lo sea).
3.  **Puntos de Evaluación Acotados (BPE):** Los átomos donde se evalúan las derivadas deben estar situados en zonas donde la evaluación funcional sea continua respecto a la norma de Sobolev, usualmente el interior de la envoltura convexa o el disco geométrico.

**Situaciones que provocan la no acotación**
La no acotación ($\|D\| = \infty$) es provocada principalmente por la **inclusión de masas atómicas en las derivadas ubicadas en puntos "inestables"** (fuera de la geometría natural de la medida continua, o en fronteras donde el funcional de evaluación deja de ser continuo). Al no ser los funcionales de evaluación continuos en esos puntos, la topología del espacio se rompe, el operador $D$ pierde su simetría natural, y el término discreto de las derivadas se dispara, haciendo que la norma global del operador tienda a infinito en las secciones matriciales límite ($\lim_{n \to \infty} \sigma_{1,n} = \infty$).

**Conexión con la localización de ceros**
*   **Caso acotado:** Si $\|D\| < \infty$, es un resultado sólidamente establecido que los ceros de los polinomios ortogonales de Sobolev están confinados uniformemente en un disco compacto dictado por la norma del operador, típicamente el disco $\{z \in \mathbb{C} : |z| \le \|D\|\}$ (o $2\|D\|$ en otras formulaciones).
*   **Caso no acotado (La ruptura):** Cuando $\|D\| = \infty$, el teorema clásico colapsa y no puede aplicarse. Sin embargo, ocurre un fenómeno de **"disociación espectral"**: aunque la norma del operador explota arrastrada por el término discreto, los ceros (cuyo límite máximo en módulo es el radio espectral de las matrices truncadas, $\rho(D_n)$) suelen permanecer acotados o simplemente convergen hacia el átomo que originó la perturbación. Esta discrepancia revela que medir la cota de los ceros usando solo la norma global ($\|D\|$) es insuficiente y exige tu investigación sobre restricciones a hiperplanos y nuevos valores singulares.

**Frases o resultados que puedes citar en tu estado del arte**
1. *"Si el operador multiplicación está acotado, entonces los ceros de los polinomios [...] están contenidos en el disco $\{z \in \mathbb{C} : |z| \le \|D\|\}$."* (López Lagomasino, Pijeira y Pérez Izquierdo).
2. *"La acotación del operador multiplicación exige que las medidas involucradas sean secuencialmente dominadas, o que la norma asociada sea equivalente a la de un producto secuencialmente dominado."* (J. M. Rodríguez / G. López).
3. *"En los productos de Sobolev discretos, la simetría del operador multiplicación se pierde, lo que conlleva diferencias fundamentales respecto a las propiedades de entrelazamiento y contención de los ceros en la envoltura convexa clásica."* (Alfaro y Rezola).

---

### Tabla Resumen para el Capítulo 1

| Autor / Referencia | Contexto | Resultado principal | Utilidad para mi Capítulo 1 |
| :--- | :--- | :--- | :--- |
| **López Lagomasino, Pijeira Cabrera** | Polinomios de Sobolev en $\mathbb{R}$ y $\mathbb{C}$. Relación matriz-operador. | Si el operador $D$ es acotado, todos los ceros están confinados en el disco $\{z : \|z\| \le \|D\|\}$. Introducen el concepto de "medidas secuencialmente dominadas". | Exponer la teoría canónica de cómo el operador de multiplicación se usa clásicamente para localizar los ceros en subconjuntos compactos. |
| **J.M. Rodríguez, V. Álvarez, et al.** | Espacios de Sobolev generalizados. Propiedades analíticas y de completitud funcional. | El operador multiplicación está acotado *si y solo si* la norma Sobolev es equivalente a una norma de un producto "secuencialmente dominado" (o es generada por medidas "admisibles"). | Fundamentar topológicamente las condiciones ultra-restrictivas que se necesitan para que el operador no diverja. |
| **M. Alfaro, F. Marcellán, M.L. Rezola** | *Surveys* históricos sobre productos Sobolev discretos y continuos. | La introducción de las derivadas (incluso con $\lambda > 0$ constante) rompe la simetría geométrica y las relaciones clásicas de ortogonalidad; los ceros ya no están forzados a la envoltura convexa. | Brindar el contexto histórico ("el quiebre") desde el ejemplo de Althammer (1962) demostrando que los ceros escapan del soporte. |
| **C. Escribano, R. Gonzalo** (y tu propio TFM) | Inclusión de átomos exteriores a un soporte compacto (ej. Circunferencia) analizado como perturbaciones matriciales. | Los átomos inestables fuerzan $\|D\| = \infty$ (divergencia del primer valor singular $\sigma_1$). Aún así, los ceros (radio espectral $\rho(D_n)$) experimentan disociación y se mantienen acotados o atraídos asintóticamente por el átomo. | Formular la *motivación y la paradoja central* de tu trabajo: los teoremas clásicos colapsan por tener norma infinita, a pesar de que los ceros experimentalmente no se van al infinito globalmente. |

En la teoría clásica de polinomios ortogonales (asociados a una medida estándar sin derivadas), los ceros gozan de propiedades perfectas: son reales, simples y se ubican estrictamente en el interior de la envoltura convexa del soporte de la medida de ortogonalidad. Sin embargo, la literatura presente en tus fuentes demuestra que la introducción de productos escalares de Sobolev (que involucran derivadas) rompe este paradigma geométrico debido a la pérdida de simetría del operador de multiplicación.

A continuación, se detalla lo que establecen las fuentes sobre las anomalías en la localización de estos ceros, clasificando la información en ejemplos, teoremas y observaciones heurísticas:

### 1. Ceros fuera del soporte y de su envoltura convexa
**Ejemplos históricos:**
El primer caso documentado en la literatura de un cero que escapa de la región clásica fue proporcionado por P. Althammer en 1962. Althammer construyó el primer ejemplo explícito de un producto de Sobolev donde un polinomio poseía un cero estrictamente fuera del intervalo de ortogonalidad.

**Teoremas generales:**
En el marco de los productos de Sobolev discretos (donde se añade una suma finita de derivadas evaluadas en puntos $c$ fuera del interior del soporte continuo), los teoremas generales garantizan que los ceros escapan de la envoltura convexa del soporte de la medida base. 
*   Para un producto con $m$ términos en la parte discreta, un teorema general (Alfaro et al.) asegura que el polinomio ortogonal $Q_n$ tiene *al menos* $n-\mathfrak{n}$ cambios de signo (ceros) en el interior de la envoltura convexa, donde $\mathfrak{n}$ es el número de términos discretos cuyo orden de derivación es menor que $n$. Esto implica matemáticamente que los ceros restantes pueden estar (y de hecho, a menudo están) ubicados fuera de dicha envoltura convexa.
*   En el caso en el que la parte continua y discreta son disjuntas (por ejemplo, si la envoltura convexa del soporte de la medida base $\mu_0$ y la medida de las derivadas $\mu_1$ no se intersecan, $co(S_{\mu_0}) \cap co(S_{\mu_1}) = \emptyset$), un teorema riguroso garantiza que los ceros de $Q_n$ quedan confinados en un disco centrado en el punto de $co(S_{\mu_1})$ más alejado de $co(S_{\mu_0})$, con un radio igual al diámetro de la unión de ambas envolturas.

### 2. Ceros no reales en problemas originalmente reales
**Observaciones y resultados documentados:**
Una de las consecuencias más sorprendentes de la pérdida de simetría del operador de multiplicación es la aparición de ceros complejos. La literatura señala explícitamente que, en los productos de Sobolev discretos, la adición de perturbaciones puntuales provoca la existencia de ceros fuera de la envoltura convexa que **pueden ser incluso complejos**, a pesar de que el soporte continuo de la medida esté enteramente contenido en la recta real $\mathbb{R}$. De manera análoga, para productos de Sobolev generales (continuos o multivariados), ejemplos sencillos en la literatura demuestran que los ceros pueden adentrarse en el plano complejo aunque todas las medidas $\mu_k$ involucradas en el producto escalar estén estrictamente soportadas en $\mathbb{R}$.

### 3. Influencia de masas discretas (átomos) en la localización
**Observaciones heurísticas y experimentales:**
Los experimentos numéricos y el análisis asintótico revelan un comportamiento de "atracción". Cuando se introduce un átomo discreto (un punto $c$ donde se evalúa la derivada) que se encuentra alejado del soporte de la medida continua, la gran mayoría de los ceros del polinomio (el espectro esencial) se mantiene en el soporte continuo, pero un número reducido de "ceros excepcionales" se escapan y son atraídos físicamente hacia la ubicación del átomo. 

En los casos en que el átomo vuelve no acotado al operador de multiplicación (haciendo que su norma diverja a infinito, $\|D\| = \infty$), se observa heurísticamente el fenómeno de **disociación espectral**: la norma global explota debido a la patología del espacio generada por la derivada puntual, pero el radio espectral de las matrices truncadas (que mide el módulo del cero más grande) permanece acotado y converge exactamente hacia la magnitud del átomo $|c|$. 

**Teoremas generales sobre la atracción:**
Esto se ha formalizado asintóticamente. Para medidas cuya derivada de Radon-Nikodym es mayor que cero casi en todas partes de su soporte, un teorema establece que, para grados $n$ suficientemente grandes, los polinomios $Q_n$ tienen exactamente $n-m$ ceros en el interior del soporte y **los $m$ ceros restantes son atraídos inevitablemente por el punto perturbador $c$**. 

### 4. Resultados de acotación y distribución asintótica
**Teorema del Disco Acotado (López Lagomasino y Pijeira):**
Para poder acotar el escape de estos ceros hacia el plano complejo, el resultado general más poderoso de la literatura establece que la localización de los ceros está subordinada a la acotación del operador de multiplicación por la variable independiente $M$ (o $D$). Un teorema fundamental demuestra que **si el operador de multiplicación está acotado, entonces la totalidad de los ceros de los polinomios ortogonales de Sobolev están contenidos uniformemente en el disco compacto $\{z \in \mathbb{C} : |z| \le \|M\|\}$**.

**Distribución Asintótica de Ceros (Medidas Regulares):**
Para analizar cómo se distribuyen estos ceros cuando el grado $n \to \infty$, se utiliza la medida de contar ceros normalizada $\nu(p)$. Los teoremas generales estipulan que si las medidas subyacentes pertenecen a la clase de medidas regulares **Reg** (en el sentido de Stahl y Totik) y satisfacen ciertas condiciones de regularidad y dominancia, la sucesión de las medidas de los ceros converge débilmente en topología estrella a la **medida de equilibrio** del soporte conjunto de las medidas ($\nu(Q_n) \xrightarrow{*} \omega_{S_\mu}$). Esto significa que, asintóticamente y a gran escala, la masa principal de los ceros recupera un comportamiento regular y se distribuye según la capacidad logarítmica de la geometría base, ignorando las anomalías puntuales.

Aquí tienes una propuesta de redacción académica estructurada en tres párrafos, diseñada específicamente para tu Trabajo de Fin de Máster. Esta síntesis establece el marco clásico, introduce el concepto de evaluaciones puntuales acotadas (BPE) y culmina evidenciando la ruptura que representan los productos de Sobolev:

En la teoría clásica (con particular énfasis en los trabajos de Szegő), la ortogonalidad se define mediante un producto escalar dado por la integral respecto a una medida de Borel finita y positiva con soporte compacto, ya sea en la recta real, la circunferencia o el plano complejo. Este marco dota al espacio de una geometría sumamente rígida en la que el operador lineal de multiplicación por la variable independiente, $\mathcal{D}(p) = zp$, juega un rol central. Para medidas soportadas en la recta real, este operador resulta ser simétrico, lo que garantiza que los ceros de los polinomios ortogonales estándar posean propiedades analíticas perfectas: son siempre reales, simples, se entrelazan y residen estrictamente en el interior de la envoltura convexa del soporte de la medida. Cuando el soporte se encuentra en el plano complejo o en la circunferencia unidad, la compacidad del soporte es equivalente a la acotación de la norma del operador ($\|\mathcal{D}\| < \infty$). Esta acotación es fundamental, ya que obliga matemáticamente a que la totalidad de los ceros queden confinados de manera uniforme en un disco acotado delimitado por la norma del operador, típicamente dentro de $\{z \in \mathbb{C} : |z| \le \|\mathcal{D}\|\}$.

Para estudiar el comportamiento local y la topología de estos funcionales en la circunferencia y en el plano complejo, la literatura clásica recurre a las propiedades de los espacios de Hardy y a los trabajos canónicos de P. Duren, esenciales para entender el concepto de las Evaluaciones Puntuales Acotadas (BPE). En los espacios clásicos, un punto es una BPE si el funcional que evalúa un polinomio en dicho lugar es continuo respecto a la norma del espacio subyacente. Clásicamente, si la medida satisface ciertas condiciones (como la condición de Szegő), las BPEs se encuentran confinadas al interior de la curva de ortogonalidad (como el disco unidad abierto). Sin embargo, la introducción de los productos escalares de Sobolev altera drásticamente esta estructura al añadir derivadas evaluadas en puntos discretos o "átomos". Al incorporar esta parte discreta, el operador de multiplicación pierde inmediatamente su simetría natural. Más aún, si se ubican átomos en regiones exteriores inestables donde la evaluación funcional ya no es continua (puntos que no son BPE), la topología se quiebra, provocando que la norma global del operador de multiplicación diverja a infinito ($\|\mathcal{D}\| = \infty$) a pesar de que la medida continua base conserve un soporte compacto.

Esta asimetría estructural y la pérdida de acotación del operador representan una ruptura paradigmática frente al caso de Szegő. A diferencia de los polinomios ortogonales estándar, los polinomios de Sobolev discretos no están obligados a mantener sus ceros dentro de la envoltura convexa del soporte original; de hecho, a partir de los históricos ejemplos de Althammer, está sobradamente documentado que los ceros pueden migrar hacia el plano complejo y escapar del intervalo o curva de ortogonalidad, viéndose atraídos por los átomos exteriores. Esta divergencia inutiliza por completo los teoremas clásicos de acotación basados en la norma global del operador, motivando la necesidad de restringir el análisis a hiperplanos de codimensión finita y definir nuevos valores singulares que permitan localizar los ceros cuando la teoría estándar colapsa.

Aquí tienes una síntesis del estado del arte sobre polinomios ortogonales de Sobolev, estructurada temáticamente en torno al problema de los ceros y el operador de multiplicación, tal como se solicita para tu trabajo:

### 1. El cambio de paradigma: La teoría de Sobolev frente al caso clásico
En la teoría clásica de aproximación (cimentada por Szegő), la ortogonalidad se define mediante un producto escalar estándar dado por la integral respecto a una medida de Borel finita y positiva. Bajo este marco, el operador lineal de multiplicación por la variable independiente, $D(p) = zp$, es simétrico. Esta simetría garantiza un comportamiento geométrico perfecto de los ceros de los polinomios ortogonales: son siempre reales, simples, se entrelazan y están estrictamente confinados en el interior de la envoltura convexa del soporte de la medida.

La teoría de Sobolev rompe este esquema al incorporar derivadas en el producto escalar interno. Esta alteración topológica destruye la simetría del operador de multiplicación. Como consecuencia directa, los polinomios ortogonales de Sobolev pierden sus propiedades clásicas; la relación de recurrencia a tres términos se transforma en relaciones de orden superior (asociadas a matrices de Hessenberg o multidiagonales), y lo más notable: sus ceros ya no están forzados a permanecer en la envoltura convexa del soporte de ortogonalidad. Históricamente, fue P. Althammer (1962) quien documentó el primer ejemplo explícito de un cero de Sobolev que escapaba del intervalo original. 

### 2. Acotación del operador y localización de los ceros (López Lagomasino, Pijeira y colaboradores)
Ante la "fuga" de los ceros hacia el plano complejo, G. López Lagomasino, H. Pijeira Cabrera y sus colaboradores establecieron una de las herramientas teóricas más importantes para su control: vincular la ubicación de los ceros a la acotación del operador de multiplicación. 

En trabajos fundamentales (1999, 2001), demostraron que si el operador de multiplicación $D$ está acotado en el espacio de Sobolev, entonces la totalidad de los ceros de los polinomios ortogonales están contenidos uniformemente en un disco compacto dictado por la norma del operador, típicamente el disco $\{z \in \mathbb{C} : |z| \le \|D\|\}$.
Además, exploraron el comportamiento asintótico (raíz $n$-ésima) de estos polinomios. Determinaron que la acotación del operador se garantiza si las medidas involucradas son "secuencialmente dominadas". Posteriormente, trabajos de J.M. Rodríguez caracterizaron rigurosamente esta acotación demostrando que es equivalente a que la norma de Sobolev sea comparable a la de un producto secuencialmente dominado.

### 3. Productos discretos, cuasi-ortogonalidad y la dinámica de los ceros
Una vertiente muy prolífica aborda los productos de Sobolev discretos (o mixtos), donde la perturbación de las derivadas se aplica únicamente sobre un conjunto finito de puntos o átomos fuera o dentro del soporte continuo.

En este contexto, M. Alfaro, F. Marcellán, M.L. Rezola y colaboradores explotaron el concepto de **cuasi-ortogonalidad**. Demostraron que los polinomios de Sobolev asociados a un producto con una parte discreta de $m$ términos son cuasi-ortogonales de cierto orden respecto a una modificación de la medida base. Esta propiedad permite afirmar que, para un grado $n$ suficientemente grande, al menos $n-m$ ceros permanecen confinados en el interior de la envoltura convexa de la medida base. Los $m$ ceros excepcionales restantes "escapan" de dicho soporte y, asintóticamente, son atraídos hacia la ubicación de los átomos que originaron la perturbación discreta.

### 4. Panorámicas de Marcellán, Xu y la consolidación espectral
Las panorámicas exhaustivas, como el extenso *survey* "On Sobolev Orthogonal Polynomials" de F. Marcellán y Y. Xu (2015), han servido para consolidar los enfoques dispares de esta teoría. Estos trabajos recopilatorios exponen cómo la pérdida de la recurrencia tridiagonal clásica motiva el uso de herramientas de álgebra matricial avanzada (matrices de Hessenberg, representaciones banda) para analizar tanto los polinomios de Sobolev continuos como los discretos. Además, estos *surveys* organizan históricamente los avances sobre el comportamiento asintótico, la desigualdad de normas y el entrelazamiento, conectándolos con aplicaciones en problemas de aproximación simultánea, y la teoría espectral de perturbaciones de rango finito.

### 5. Problemas abiertos y enfoques contemporáneos matriciales
A pesar de los profundos avances, el problema de la localización global de los ceros cuenta con notables vacíos:

*   **Acotación uniforme para medidas no dominadas:** Como señalan en la literatura, sigue siendo una pregunta abierta si los ceros de los polinomios ortogonales de Sobolev están uniformemente acotados en el caso general donde todos los soportes de las medidas son compactos, pero el producto escalar *no* es secuencialmente dominado. 
*   **Operadores no acotados ($\|D\| = \infty$):** Cuando se ubican átomos inestables en la frontera o en el exterior del soporte continuo, los funcionales de evaluación sobre las derivadas pierden la continuidad. Esto provoca que el operador de multiplicación tenga una norma infinita, volviendo inaplicables los teoremas clásicos de López Lagomasino y Pijeira.
*   **El análisis de valores singulares:** Ante la ruptura de la norma global, problemas contemporáneos (liderados por autores como C. Escribano y R. Gonzalo, y centrales en el enfoque de tu investigación) abordan la **disociación espectral**. A través de una aproximación matricial de dimensiones infinitas, se estudia el comportamiento asintótico de los valores singulares generalizados. Se explora cómo, aunque el primer valor singular diverja a infinito, restringiendo el operador a subespacios de codimensión finita (hiperplanos que anulan los átomos), el segundo valor singular ($\sigma_2$) o los índices sucesivos de Gelfand ($Q_k$) logran estabilizarse y acotar los ceros fugados. Este enfoque matricial para sortear la no acotación del operador sigue siendo un área fértil y poco desarrollada en el estado del arte.

Aquí tienes una propuesta de redacción académica, estructurada y sintetizada, ideal para incluir en la sección del estado del arte de tu TFM. Se centra en los conceptos topológicos y su repercusión en la teoría, sin adentrarse en demostraciones técnicas:

**El papel de las Evaluaciones Puntuales Acotadas (BPE) en los Espacios de Sobolev**

En el marco del análisis funcional y la teoría de aproximación, el concepto de **Evaluación Puntual Acotada (BPE, por sus siglas en inglés, *Bounded Point Evaluation*)** es una herramienta topológica fundamental para comprender la estructura de los espacios de polinomios. Conceptualmente, se dice que un punto $c \in \mathbb{C}$ es una BPE para un espacio normado de polinomios si existe una constante $C > 0$ tal que $|p(c)| \le C \|p\|$ para todo polinomio $p$. En términos funcionales, esta desigualdad es la definición misma de continuidad; es decir, afirmar que un punto es una BPE equivale a establecer que el funcional lineal de evaluación $\delta_c(p) = p(c)$ es un operador **continuo** y acotado respecto a la norma del espacio subyacente.

**Distinción geométrica y la medida de Lebesgue**
La noción de BPE actúa de facto como un detector analítico para clasificar los puntos del plano complejo respecto al soporte de ortogonalidad. En la teoría de los espacios $P^t(\mu)$, el teorema de dicotomía de Thomson establece que la existencia de BPEs define regiones analíticas ligadas intrínsecamente al "interior" del soporte de la medida. 
Un ejemplo canónico y central en la literatura es la ortogonalidad respecto a la **medida de Lebesgue normalizada en la circunferencia unidad**. Para esta medida geométrica, la teoría clásica de los espacios de Hardy garantiza que todos los puntos ubicados estrictamente en el **interior del disco abierto** son BPEs (y, de hecho, evaluaciones puntuales analíticas o ABPE). Por el contrario, la topología cambia drásticamente en la frontera geométrica (la propia circunferencia) y en el exterior del disco, regiones donde los funcionales de evaluación pierden su continuidad y, por tanto, los puntos dejan de ser BPEs.

**Conexión con el operador de multiplicación en espacios de Sobolev**
La continuidad de las evaluaciones puntuales resulta ser el eslabón crítico para resolver el problema de la acotación del operador de multiplicación, $\mathcal{D}(p) = zp$, cuando se transita hacia los productos internos de Sobolev discretos. Al añadir a una medida continua una serie de masas o "átomos" que evalúan derivadas puntuales en puntos $c_k$, la estabilidad topológica del espacio queda supeditada a la naturaleza de dichos átomos:
*   **Caso estable (Átomos interiores / BPEs):** Si las masas se ubican en puntos interiores donde la evaluación es una BPE, los funcionales involucrados son continuos respecto a la norma base. En consecuencia, el núcleo de estos funcionales conforma un subespacio topológicamente cerrado, la estructura funcional se preserva y el operador de multiplicación mantiene su acotación ($\|\mathcal{D}\| < \infty$).
*   **La ruptura espacial (Átomos exteriores / no BPEs):** Si, por el contrario, los átomos se sitúan en el exterior del soporte geométrico (puntos que no son BPE), los funcionales de evaluación asociados a las derivadas se vuelven discontinuos. Esta inestabilidad provoca que el núcleo del funcional sea denso algebraicamente (no cerrado), lo que induce una patología en el espacio que dispara irremisiblemente la norma global del operador de multiplicación a infinito ($\|\mathcal{D}\| = \infty$).

**Respaldo en la literatura**
En el estado del arte, la fundamentación de las BPE se apoya en los textos clásicos de P. Duren sobre espacios $H^p$, así como en las investigaciones de J.B. Conway, L. Yang y J.R. Akeroyd en la caracterización de los espacios $R^t(K,\mu)$ y $P^s(\omega)$. La conexión directa de esta propiedad analítica con la acotación de operadores en espacios de polinomios de Sobolev ha sido formalizada a través del estudio de medidas secuencialmente dominadas por autores como J.M. Rodríguez, V. Álvarez, E. Romera y D. Pestana, y expandida hacia un enfoque algebraico y matricial contemporáneo por C. Escribano y R. Gonzalo, quienes emplean las BPE y los índices restrictivos de valores singulares para caracterizar la viabilidad del operador de multiplicación y acotar los ceros fugados.

Para redactar el estado del arte de tu Capítulo 1, aquí tienes una síntesis precisa y académica sobre cómo las Evaluaciones Puntuales Acotadas (BPE) actúan como el detector topológico fundamental frente a la medida de Lebesgue en la circunferencia:

**El papel de las BPE en la medida de Lebesgue sobre la circunferencia**

En la teoría de aproximación, cuando se trabaja con la medida de Lebesgue normalizada sobre una circunferencia de radio $R$, la posición geométrica de un punto determina categóricamente si la evaluación funcional en dicho punto es continua respecto a la norma del espacio. 

*   **Puntos BPE vs. no BPE:** Los resultados clásicos de la teoría de espacios de Hardy establecen que la medida de Lebesgue no es densa en los polinomios, lo que propicia que todos los puntos estrictamente en el **interior del disco ($|c| < R$)** sean Evaluaciones Puntuales Acotadas (e incluso evaluaciones analíticas, ABPE). Por el contrario, los puntos ubicados en la **frontera geométrica ($|c| = R$)** y en la región **exterior ($|c| > R$)** carecen de continuidad topológica, por lo que **no son BPEs**.

*   **Implicación conceptual en productos de Sobolev:** Al definir un producto escalar de Sobolev discreto, se añaden perturbaciones (átomos) que evalúan las derivadas de los polinomios en ciertos puntos $c_k$. La viabilidad de este espacio depende directamente de si el funcional de evaluación asociado a estos átomos discretos hereda o no la continuidad de la métrica base.

*   **Estabilidad de los puntos interiores:** Si los átomos de las derivadas se sitúan en el interior del disco, al ser BPEs, garantizan que los funcionales de evaluación (y sus derivadas) sean operadores continuos. Topológicamente, esto asegura que el núcleo de dichos funcionales forme un subespacio cerrado, lo que preserva la cohesión del espacio de Hilbert y permite que el operador de multiplicación por la variable independiente mantenga su acotación ($\|\mathcal{D}\| < \infty$). En estas condiciones, los ceros de los polinomios ortogonales de Sobolev se mantienen controlados uniformemente.

*   **Inestabilidad en la frontera y el exterior:** Si los átomos se ubican en la circunferencia o fuera de ella (no BPE), el funcional que evalúa la derivada discreta es intrínsecamente discontinuo respecto a la norma $L^2$ base. La consecuencia analítica es que el núcleo de este funcional deja de ser cerrado (se vuelve algebraicamente denso). Esta ruptura topológica actúa como una perturbación inestable severa que destruye la simetría y dispara la norma del operador de multiplicación a infinito ($\|\mathcal{D}\| = \infty$). 

**Referencias bibliográficas de respaldo:**
Esta interpretación se fundamenta en los trabajos de teoría de espacios $P^t(\mu)$ y análisis funcional de J.B. Conway, L. Yang y J.R. Akeroyd para la clasificación de las ABPEs en el disco. A su vez, la traslación de este fenómeno de continuidad hacia la acotación de los operadores y la localización asintótica en espacios de Sobolev está respaldada por los resultados recientes desarrollados a través de las matrices truncadas de Hessenberg y la convergencia de valores singulares.

Analizando detenidamente las fuentes de tu notebook y nuestras conversaciones previas, aquí tienes la revisión académica de cada una de las cinco afirmaciones. Te detallo qué matices debes cuidar para que tu Capítulo 1 sea impecable y no asuma generalidades falsas.

### 1. “En el caso clásico, soporte compacto equivale a acotación del operador de multiplicación”

*   **¿Está respaldada por las fuentes?** Sí, está respaldada, pero es una afirmación que requiere un marco preciso. 
*   **Bajo qué hipótesis es correcta:** Esta equivalencia es cierta estrictamente bajo el producto escalar clásico (sin derivadas) inducido por una medida de Borel finita y positiva. 
*   **Qué referencia citar:** Puedes citar los trabajos de López Lagomasino y Pijeira Cabrera, o las introducciones sobre valores singulares y acotación del operador.
*   **Cómo debería redactarla con precisión:** 
    > *"En el marco de la ortogonalidad clásica inducida por una medida de Borel finita y positiva, existe una equivalencia directa: la compacidad del soporte de la medida es condición necesaria y suficiente para garantizar la acotación del operador de multiplicación por la variable independiente (es decir, $\|D\| < \infty$)."*

### 2. “En el caso clásico, los ceros están en la envoltura convexa del soporte”

*   **¿Está respaldada por las fuentes?** Sí, pero **cuidado**, formularla así en general es peligroso. La propiedad estricta de la "envoltura convexa" se aplica clásicamente a la recta real.
*   **Bajo qué hipótesis es correcta:** Es cierta cuando el soporte de la medida está contenido en la recta real $\mathbb{R}$. Si trabajas en el plano complejo $\mathbb{C}$, los ceros están acotados en un disco, pero no necesariamente se usa el término "envoltura convexa" de la misma manera que en el intervalo real.
*   **Qué referencia citar:** El artículo de M. Alfaro y M.L. Rezola,, donde se detalla el comportamiento clásico frente a Sobolev y se cita el intervalo de ortogonalidad.
*   **Cómo debería redactarla con precisión:** 
    > *"En la teoría clásica de polinomios ortogonales asociados a una medida soportada en la recta real, los ceros exhiben un confinamiento estricto: son reales, simples y se ubican necesariamente en el interior de la envoltura convexa del soporte de la medida."*

### 3. “En Sobolev discreto, los ceros pueden salir de la envoltura convexa”

*   **¿Está respaldada por las fuentes?** Totalmente respaldada. Es uno de los hitos fundamentales que justifican la teoría de Sobolev.
*   **Bajo qué hipótesis es correcta:** Para productos internos de Sobolev que incorporen evaluaciones discretas (átomos) en puntos situados fuera o en los extremos de la geometría de la medida base.
*   **Qué referencia citar:** El ejemplo histórico de Althammer (1962) y los trabajos de M. Alfaro, F. Marcellán y M.L. Rezola.
*   **Cómo debería redactarla con precisión:** 
    > *"La introducción de productos escalares de tipo Sobolev discreto quiebra el principio del confinamiento clásico. Como demostró Althammer (1962), la inclusión de evaluaciones puntuales de las derivadas provoca que los ceros de los polinomios ortogonales ya no estén obligados a permanecer en la envoltura convexa del soporte de la medida base, pudiendo incluso migrar hacia el plano complejo."*

### 4. “En Sobolev discreto, el operador de multiplicación puede no ser acotado aunque el soporte continuo sea compacto”

*   **¿Está respaldada por las fuentes?** Sí, de manera central en tu investigación y en la bibliografía.
*   **Bajo qué hipótesis es correcta:** Ocurre cuando se introducen masas atómicas en puntos donde el funcional de evaluación asociado a las derivadas no es continuo respecto a la norma topológica del espacio base (puntos no BPE).
*   **Qué referencia citar:** Tu análisis asintótico de convergencia del segundo valor singular,, y la discusión matricial y de codimensión de tu propio TFM.
*   **Cómo debería redactarla con precisión:** 
    > *"A diferencia del paradigma clásico, en los espacios de Sobolev discretos el operador de multiplicación por la variable independiente puede perder globalmente su acotación ($\|D\| = \infty$), a pesar de que la medida continua subyacente posea un soporte estrictamente compacto. Esta divergencia surge por la inestabilidad introducida por átomos en los que el funcional de evaluación carece de continuidad."*

### 5. “Los BPE distinguen puntos interiores de puntos de frontera/exteriores para la medida de Lebesgue en circunferencia”

*   **¿Está respaldada por las fuentes?** Sí, pero debes enfatizar que esto es particular de ciertas medidas, no una regla universal de todos los espacios funcionales.
*   **Bajo qué hipótesis es correcta:** Es correcto, de forma rigurosa, para medidas que cumplen la condición de Szegő, y en el caso modélico de tu trabajo: la medida de Lebesgue normalizada en la circunferencia unidad.
*   **Qué referencia citar:** Las transcripciones de tus reuniones ("se sabe que en el círculo... los puntos interiores son BPE") y las definiciones del bloque 1 de tu TFM ("Puntos de Evaluación Acotados de la medida $\mu$").
*   **Cómo debería redactarla con precisión:** 
    > *"Para el caso modélico de ortogonalidad respecto a la medida de Lebesgue en la circunferencia unidad, el concepto de Evaluación Puntual Acotada (BPE) permite clasificar topológicamente el plano complejo: los puntos estrictamente interiores al disco abierto actúan como BPEs (garantizando la continuidad del funcional), mientras que la frontera geométrica y la región exterior carecen de esta propiedad."*

A continuación, se presenta una propuesta de redacción académica para las secciones indicadas de tu primer capítulo, estructurada con un tono formal propio de un Trabajo de Fin de Máster en matemáticas y fundamentada estrictamente en las fuentes proporcionadas.

### 1. Introducción, contexto y motivación

El estudio de la localización y distribución asintótica de los ceros de los polinomios ortogonales constituye un problema central en la teoría de aproximación, motivado históricamente por sus profundas aplicaciones en la interpolación, el diseño de fórmulas de cuadratura numéricas y la teoría espectral. En la teoría clásica, el comportamiento de estos ceros es sumamente regular y predecible; sin embargo, la introducción de los productos escalares de tipo Sobolev altera drásticamente este panorama geométrico. Al incorporar información sobre las derivadas de las funciones en puntos discretos, la topología del espacio subyacente se modifica, provocando que el operador natural de estudio —el operador de multiplicación por la variable independiente— pierda sus propiedades clásicas de simetría y acotación. Esta anomalía, puesta de manifiesto por primera vez en 1962 por P. Althammer al constatar que los ceros pueden escapar del soporte de ortogonalidad, es la motivación fundamental de la presente memoria. Surge entonces la necesidad de investigar el comportamiento espectral del espacio funcional cuando la norma del operador de multiplicación diverge a infinito, inutilizando los teoremas métricos estándar y obligando a desarrollar nuevos enfoques para comprender cómo y por qué los ceros se mantienen acotados a pesar de la inestabilidad del operador.

### 2. Marco clásico mínimo

En el marco de la teoría clásica cimentada por G. Szegő, la ortogonalidad de una sucesión de polinomios se define mediante un producto escalar inducido por una medida de Borel finita y positiva, con soporte compacto en la recta real o en el plano complejo. La herramienta principal para el estudio de los polinomios ortogonales estándar es el operador de multiplicación, definido de forma natural como $D(p) = zp$. Existe un resultado analítico bien conocido que establece una equivalencia fundamental: la compacidad del soporte de la medida es condición necesaria y suficiente para garantizar la acotación de la norma del operador $D$. Como consecuencia directa de esta acotación, los ceros de los polinomios ortogonales gozan de un confinamiento estricto. Cuando el soporte de la medida es un subconjunto de la recta real, los ceros son reales, simples, se entrelazan y residen necesariamente en el interior de la envoltura convexa del soporte. Si el soporte se encuentra en el plano complejo, los ceros quedan acotados uniformemente en un disco compacto cuyo radio está determinado por la norma del propio operador de multiplicación.

### 3. Paso a productos de Sobolev discretos

La generalización hacia los espacios de Sobolev se formaliza añadiendo al producto interno estándar respecto a una medida base, una perturbación discreta consistente en la evaluación de las derivadas de los polinomios en un conjunto finito de puntos o masas atómicas. Esta adición, aunque aparentemente inocua, quiebra el paradigma geométrico clásico: el operador de multiplicación por la variable independiente deja de ser simétrico con respecto al nuevo producto escalar. El impacto analítico más severo de esta asimetría es que, aun cuando la medida continua subyacente posea un soporte estrictamente compacto, la presencia de átomos discretos puede disparar la norma del operador al infinito, volviéndolo globalmente no acotado. A raíz de esta pérdida de acotación topológica, los polinomios ortogonales de Sobolev discretos sufren un comportamiento anómalo en el cual sus ceros ya no están obligados a permanecer en la envoltura convexa de la medida base, posibilitando su migración hacia el plano complejo. 

### 4. Estado del arte

**a) Caso clásico**
En la literatura canónica, la relación entre el soporte de la medida y la distribución de los ceros está exhaustivamente documentada. Autores como H. Stahl y V. Totik han consolidado los resultados sobre el comportamiento asintótico general en el plano complejo, demostrando que si las medidas subyacentes son regulares (pertenecientes a la clase **Reg**), la medida contadora de los ceros de los polinomios ortogonales converge débilmente en topología estrella hacia la medida de equilibrio soportada en la geometría continua base.

**b) Caso Sobolev**
En el ámbito de los polinomios de Sobolev, G. López Lagomasino, H. Pijeira Cabrera y sus colaboradores han establecido resultados fundamentales para el control de la "fuga" de los ceros. Han demostrado rigurosamente que si el operador de multiplicación se mantiene acotado, entonces la totalidad de los ceros de los polinomios ortogonales de Sobolev están confinados en un disco acotado en el plano complejo, delimitado precisamente en función de la norma del operador $\|D\|$. Complementariamente, los trabajos de J. M. Rodríguez dictaminan que esta exigencia de acotación del operador obliga a que las medidas del producto interno estén "secuencialmente dominadas", lo cual es una restricción severa sobre el espacio. Adicionalmente, *surveys* comprensivos como los de F. Marcellán y Y. Xu recopilan el comportamiento de las anomalías asintóticas asociadas a perturbaciones de rango finito y los fenómenos de atracción de los ceros.

**c) Evaluaciones Puntuales Acotadas (BPE)**
Para comprender desde una perspectiva topológica la pérdida de acotación del operador, el estado del arte recurre a la teoría de espacios de funciones analíticas y al concepto de Evaluación Puntual Acotada (BPE). Un punto se considera una BPE si el funcional lineal que evalúa un polinomio en dicho lugar es continuo respecto a la norma del espacio funcional. Para el caso modélico de la medida de Lebesgue en la circunferencia unidad, la teoría de espacios de Hardy establece una clara dicotomía: los puntos estrictamente interiores al disco abierto son BPEs, mientras que la frontera geométrica y la región exterior carecen de esta continuidad. La literatura contemporánea vincula directamente esta propiedad con los productos de Sobolev: si las masas discretas de las derivadas recaen sobre puntos interiores (BPEs), el núcleo del funcional es cerrado, preservando la estructura del espacio y la acotación de $\|D\|$. Por el contrario, ubicar masas atómicas en regiones exteriores introduce inestabilidad y funcionales discontinuos que quiebran el espacio y provocan inevitablemente que la norma del operador de multiplicación diverja a infinito.