# MCOC2020-P2

## ENTREGA 4

En esta entrega nuevamente el Jefe de Repositorio es Maximiliano Poblete. Primero, cada integrante del grupo realizó todas las tareas por separado para poder contextualizarnos, apoyándonos mutuamente y discutiendo los resultados que cada uno obtuvo. Entre las principales diferencias que obtuvimos fue que el reticulado presentaba distintas fuerzas (para las combinaciones de carga), en función del orden de cómo se definían las barras, lo que nos resultó bastante extraño; probamos varias veces e incluso le cambiamos el orden a los nodos y se seguían provocando diferencias. Finalmente, una vez que nos reunimos para realizar la Entrega en forma grupal, llegamos a un consenso de definir las barras, restricciones y el orden de los nodos de la siguiente forma; según lo indicado en el enunciado: 

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/1.png)

A continuación se presenta el esquema del enrejado con cada uno de sus componentes (barras y nodos). Los nodos corresponden a los circulos negros (0-10) y las barras a los demas circulos (0-29). 

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/2.png)

Luego se definieron los 2 casos indicados para el reticulado; el caso de cargas muertas [ caso D ] que considera solo el peso del reticulado, y el caso de cargas vivas [ caso L ] que considera solo la carga distribuida: q = 400 kg/m2, sobre el tablero del reticulado. Para discretizar lo anterior, se asignó una porción de esta fuerza a cada nodo inferior del reticulado, en función del área tributaria que representa:

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/3.png)

Finalmente, se calcularon los factores de utilización (FU) y las fuerzas (en N) en cada barra, para cada caso de las combinaciones de carga; 1.2*D + 1.6*L   y  1.4*D. Los resultados para esta primera iteración se muestran a continuación. 

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/4.png)
![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/12.png)
![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/13.png)



Se puede observar que cada barra tiene una diferente fuerza última, esto se debe a que la fuerza distribuida se distribuye de forma diferente en el enrejado. Para optimizar la cantidad de acero que debe ocupar la estructura, se rediseña el reticulado con la fuerza máxima en valor absoluto de las combinaciones de cargas de todas la barras, la que resultó ser (93965.48 N) para la combinación 1.2*D + 1.6*L. Esta fuerza se da en las barras 28 y 29.
<br>
<br>
El siguiente paso en la entrega consiste en estudiar que barras resultan interesantes para rediseñar, minimizando el peso y llevando el factor de utilización a valores cercanos a 1. Las barras que parecen interesantes para analizar son las que se presentan en rojo en la siguiente imagen:
![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/5.png)
<br>
<br>
Corresponden a las barras: 
![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/6.png)

De esta manera, con el objetivo de rediseñar estas 5 barras, se definió la siguiente función en barra.py para realizar esta labor:

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/7.png)

La función rediseñar(self, Fu, ret, ɸ=0.9) recorre todas las barras del reticulado, las cuales son identificadas por una lista llamada “check” que incluye el nodo i y los nodo j que caracterizan a la barra. Como la función de rediseñar recorre todas las barras e interesa rediseñar solamente algunas, se establece un sistema de verificación que funciona de la siguiente manera: 

“Si la barra k del reticulado, identificada por sus nodos ni y nj, está dentro de la lista de barras_a_rediseñar (también caracterizadas por sus nodos), entonces las propiedades de la barra son modificadas”

Ahora, bien, ¿cómo funciona el rediseño de las barras? Según el enunciado, lo que interesa en esta parte es reducir el peso de la barra. ¿Para qué? Para reducir el FU < 1.0; y esto se puede conseguir disminuyendo el área que tiene la barra. Sin embargo, se hace necesario determinar que área debería tener la barra, en función de la fuerza última, para lograr este factor de utilización óptimo. De esta manera, se obtiene el “area_ideal”, la que representa el área para que el factor de utilización sea 1, con la fuerza máxima última de 93965 N, obtenida de las combinaciones de cargas; simplemente despejando de la ecuación que define el factor de utilización. A partir de esto, se compara con el área real que tienen las barras escogidas, y estas van disminuyendo su área hasta alcanzar el “area_ideal”.

Entonces, si el valor de “area_ideal” es mayor a la real se obtiene el nuevo parámetro del espesor t, el cual, por simplicidad, fue escogido para ser modificado reduciéndolo en un 10% cada vez, dejando fijo el mismo radio de 8 cm establecido en un principio.  Finalmente, a través de un proceso iterativo, se obtiene la nueva área real disminuida de estas 5 barras escogidas para ser rediseñadas con la carga de (93965.48 N); lo cual se ve reflejado en el peso inicial y final de la estructura:


![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/8.png)

Ahora bien, ¿qué supuestos se realizaron?

En primer lugar se están rediseñando 5 barras para una misma fuerza, por lo que probablemente se alcance un FU cercano a 1 en aquellas barras que estén sometidas a fuerzas más altas. Para alcanzar un FU cercano a 1 en todas las barras escogidas en el rediseño habría que realizar una reducción del área de forma selectiva en cada barra, de forma que cada una alcance un FU cercano a 1 en función del valor absoluto de fuerza máxima que soporta, en todas las combinaciones de carga; sin embargo, esto último se omite ya que se entiende del enunciado que se está pidiendo la primera situación explicada.
 
En segundo lugar, se está reduciendo el espesor de las barras en un 10% cada vez, lo que puede resultar en valores “exoticos” que escapan de la realidad de fabricación de estos elementos. Quizás el valor óptimo resultante que permite obtener un FU cercano a 1, considere una barra con espesor como 5.58423434 mm , lo cual en la práctica es imposible de lograr. No existen fábricas que produzcan estos elementos estructurales con tal precisión. Entonces, estos resultados son válidos dentro de un contexto para efectos académicos.

También se está asumiendo que las barras no se pandean, es decir, no estan siendo modeladas como elementos esbeltos que podrían pandearse bajo ciertas cargas ni se imponen restricciones.

Un clásico supuesto es que se consideran pequeñas deformaciones; reflejado para efectos de cálculo en los cosenos directores.

Por último, en el modelo se asumió que la carga distribuida era equivalente a aplicar fuerzas puntuales en los nodos del tablero de forma proporcional a las áreas tributarias. Al hacer esto, se ignoran los momentos que se generan en las barras transversales del tablero. 


![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/9.png)

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/10.png)

Como se logra apreciar en los primeros dos diagramas, las barras superiores 28 y 29 disminuyeron de a -3390 N y -92547 N para los casos de las tensiones 1 y 2 respectivamente, las cuales presentaron la mayor disminución entre todas las las demás escogidas. 
<br>

En los diagramas de factor de utilización se observa que las barras 28 y 29 aumentaron a 0.94 y 0.99 para el caso 1 y 2 respectivamente, esto ocurre al disminuir el espesor de las barras en un 10%, y manteniendo el radio en 5 mm. Algo similar ocurre en las barras 14,  24 y 27, las cuales su FU aumentan a 0.44 para las tres en el caso 2, y en el caso 1 no se logra apreciar un gran aumento de este factor, pues en este no se ve tan afectado por el cambio de peso propio de la estructura.  


¿Cual es el desplazamiento vertical máximo en los nodos del tablero del reticulado antes y después de los cambios?

El desplazamiento vertical máximo en los nodos del tablero del reticulado antes es de -0,00168 m y después es de -0,00208 m. 

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/14.png)



Comente respecto de la nueva distribución de FU del reticulado y el peso del mismo.

Como se mencionó anteriormente, la nueva distribución de FU para el caso 2 es la que más variación tiene, pues en esta se lograron obtener valores de 0.94 y 0.99 para las barras 28 y 29, es decir muy cercanos a 1. En la tabla a continuación se muestra un resumen de las barras modificadas con sus valores originales y nuevos, para el caso 2 de combinaciones de cargas. 

![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/11.png)

Por otro lado, se logró que la estructura disminuyera su peso desde 24197 kg hasta 20405 kg. 

¿Qué cambios globales se pueden hacer para mejorar aún más el costo (peso del acero) del mismo? 

Cambios en geometría del reticulado y agregando un pilar central. Por ejemplo, disminuyendo la altura del reticulado se reduce el material a utilizar. -> Menos acero -> Se obtiene un menor costo. 


![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/15.png)
![alt text](https://github.com/maxipoblete/MCOC2020-P2/blob/master/16.png)




