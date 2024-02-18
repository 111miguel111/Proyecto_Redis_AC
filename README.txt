Programa realizado por Roberto Castilla y Miguel Gonzalez.

Este programa es un gestor de partes de Mechas(AC) y montador de estos.

Es necesario hacer pip -install Redis para que este programa funcione.

El programa si detecta que no hay fichero de configuracion, a la hora de crearlo pedira los datos al usuario, tambien puedes modificarlo a mano una vez haya sido creado, pero puedes eliminarlo manualmente o a traves del programa para que vuelva a solicitarte los datos.

FUNCIONAMIENTO----------------------------------------

Los ACs constan de piezas(Cabeza, Torso, Brazos, Piernas) y armas(ArmaBD, ArmaBI, ArmaHD, ArmaHI)

Para poder construir un AC es necesario que haya una pieza de cada tipo y minimo un arma de brazo(que no sea de hombro). Las armas de brazo podran ser equipadas en los hombros, pero las de hombro no podran equiparse en los brazos.

Para facilitar el testeo de los AC se ha facilitado un "Catalogo.txt" que contiene partes suficientes para montar diversos ACs, para añadir las partes que se encuentran en el catalogo se podra hacer desde el menu principal con la opcion "Agregar Catalogo".

Tener en cuenta que las piezas no pueden repetir nombre independientemente de que sean de tipo diferente, esto tambien se aplica a las armas ya que no pueden tener el mismo nombre independientemente de que sean de hombro o brazo. Entre armas y piezas si se podra repetir nombre.

Tambien informar de que un AC puede estar incompleto si se elimina una de las partes que tiene equipadas, pero este comportamiento es parte de la funcionalidad deseada.

OTROS--------------------------------------------------

El programa esta diseñado para funcionar de manera optima en PyCharm pero tambien funciona en Geany y CMD. Esto se debe a que el programa muestra colores por consola cosa que ni Geany ni CMD soportan. El texto permanece legible pero las partes que estarian coloreadas mostraran el codigo de color que tendrian PyCharm. 

Tambien dentro del programa se puede ver el UML original para apreciar la evolucion del proyecto
