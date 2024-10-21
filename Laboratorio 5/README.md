# Proyecto L05_Recetas

### Condiciones Iniciales:
Se facilita una carpeta **data** con el fichero denominado ``recetas.csv`` con datos sobre recetas culinarias. Ábralo para ver su estructura. 

Cree una carpeta **src** para incluir los siguientes módulos Python:

**receta.py** en el que implemente las funciones que se indican a continuación.

**test_receta.py** en el que incluirá las sentencias necesarias para ir probando las funciones a medida que las implemente.

La información de cada registro del fichero es la que se indica a continuación. **Observe en el fichero que los ingredientes están compuestos por tres campos y que a alguna receta le faltan los ingredientes**.
```
• denominación:  denominación de la receta.
• tipo: tipo de receta (Postre, Plato principal etc).
• dificultad: dificultad de elaboración (Baja, Media, Alta).
• ingredientes: ingredientes de la receta. Cada ingrediente lleva su nombre, la cantidad y las unidades con las que se confecciona la receta (u=unidades/gr=gramos/cl=centilitros)
• tiempo de preparación: tiempo de elaboración en minutos.
• calorías: número de calorías de una porción.
• fecha de creación: fecha en la que se añadió la receta al dataset.
• precio estimado: precio por persona.
```

### Ejercicio 1

Copie en receta.py los siguientes NamedTuple e importe los tipos y funciones que necesite:
```
Ingrediente = NamedTuple("Ingrediente",
					     [("nombre",str),
						  ("cantidad",float),
						  ("unidad",str)])
						 
Receta = NamedTuple("Receta", 
                    [("denominación", str),
                     ("tipo", str),
                     ("dificultad", str),
                     ("ingredientes", Optional[List[Ingrediente]]),
                     ("tiempo", int),
                     ("calorías", int),
                     ("fecha", date),
                     ("precio", float)])

```
### Ejercicio 2
Defina una función ``lee_recetas`` que reciba como parámetro el nombre de un fichero con la estructura de ``recetas.csv`` y devuelva una lista de tuplas de tipo **Receta** con los registros leídos del fichero.

Resultados esperados en el test:
```
test_lee_recetas
Registros leídos: 30
Los dos primeros: [Receta(denominación='Ensalada de Frutas', tipo='Postre', dificultad='Baja', ingredientes=[Ingrediente(nombre='fresas', cantidad=5.0, unidad='u'), Ingrediente(nombre='piña', cantidad=0.25, unidad='u'), Ingrediente(nombre='kiwi', cantidad=1.0, unidad='u'), Ingrediente(nombre='menta', cantidad=50.0, unidad='cl'), Ingrediente(nombre='zumo naranja', cantidad=100.0, unidad='cl')], tiempo=15, calorias=120, fecha=datetime.date(2024, 1, 14), precio=7.5), Receta(denominación='Spaghetti Bolognese', tipo='Plato principal', dificultad='Media', ingredientes=[Ingrediente(nombre='pasta', cantidad=200.0, unidad='gr'), Ingrediente(nombre='carne picada', cantidad=250.0, unidad='gr'), Ingrediente(nombre='tomate frito', cantidad=150.0, unidad='gr'), Ingrediente(nombre='cebolla', cantidad=0.5, unidad='u'), Ingrediente(nombre='dientes ajo', cantidad=4.0, unidad='u')], tiempo=45, calorias=400, fecha=datetime.date(2024, 1, 9), precio=12.5)]

Los dos últimos: [Receta(denominación='Sopa de Champiñones', tipo='Entrante', dificultad='Baja', ingredientes=[Ingrediente(nombre='champiñones', cantidad=200.0, unidad='gr'), Ingrediente(nombre='cebolla', cantidad=0.75, unidad='u'), Ingrediente(nombre='dientes ajo', cantidad=3.0, unidad='u'), Ingrediente(nombre='caldo de pollo', cantidad=500.0, unidad='cl'), Ingrediente(nombre='perejil', cantidad=10.0, unidad='gr')], tiempo=30, calorias=180, fecha=datetime.date(2024, 2, 27), precio=8.5), Receta(denominación='Arroz con Pollo', tipo='Plato principal', dificultad='Baja', ingredientes=[Ingrediente(nombre='arroz', cantidad=150.0, unidad='gr'), Ingrediente(nombre='pollo',cantidad=1.0, unidad='u'), Ingrediente(nombre='cebolla', cantidad=1.0, unidad='u'), Ingrediente(nombre='pimiento', cantidad=1.0, unidad='u'), Ingrediente(nombre='azafrán', cantidad=5.0, unidad='gr')], tiempo=40, calorias=380, fecha=datetime.date(2024, 2, 6), precio=14.99)]
```
### Ejercicio 3
Defina una función ``diferentes_ingredientes`` que reciba como parámetros una lista de tipo Receta y una unidad de medidas de los ingredientes de tipo str, que puede tomar el valor **None**, en cuyo caso no se filtra por unidad y devuelva el número de los diferentes ingredientes que se han medido en la unidad dada.

Resultados esperados en el test:
```
test_diferentes_ingredientes
Todos los diferentes ingredientes son: 68
Los diferentes ingredientes que se miden en gr son: 33
Los diferentes ingredientes que se miden en cl son: 11
```
### Ejercicio 4
Defina una función ``recetas_con_ingredientes`` que reciba como parámetros una lista de tipo Receta, un conjunto con nombres de ingredientes y devuelva una lista de tuplas con las denominaciones, las calorías y los precios de las recetas que entre sus ingredientes existe alguno de los dados como parámetro.

**Nota** Tenga en cuenta que si la receta tiene más de uno de los ingredientes dados, solo debe aparecer una vez.

Resultados esperados en el test:
```
test_recetas_con_ingredientes
Las recetas con alguno de los siguiente ingredientes {'harina', 'azúcar'} son: [('Mousse de Chocolate', 300, 9.5), ('Galletas de Avena', 150, 7.95), ('Pastel de Zanahoria', 300, 13.5), ('Muffins de Arándanos', 180, 7.95)]

Las recetas con alguno de los siguiente ingredientes {'pimiento', 'tomate', 'cebolla'} son: [('Spaghetti Bolognese', 400, 12.5), ('Sopa de Tomate', 120, 8.5), ('Risotto de Champiñones', 320, 13.99), ('Hamburguesa con Queso', 500, 11.25), ('Sopa de Calabaza', 150, 9.95), ('Gazpacho Andaluz', 150, 7.95), ('Bruschetta', 160, 7.25), ('Caponata', 160, 9.99), ('Ensalada de Atún', 180, 9.25), ('Pollo al Curry', 400, 15.75), ('Tortilla Española', 320, 11.25), ('Sopa de Champiñones', 180, 8.5), ('Arroz con Pollo', 380, 14.99)]
```

### Ejercicio 5
Defina una función ``receta_más_barata`` que reciba como parámetros una lista de tipo Receta, un conjunto con tipos de recetas y un parámetro "n" de tipo entero con valor por defecto **None**, y que devuelva la receta más barata de entre las "n" recetas con menos calorías de alguno de los tipos de receta dados como parámetro.
Si n toma el valor **None** se buscará la receta más barata de entre totas las recetas.
Resultados esperados en el test:
```
test_receta_más_barata
La receta más barata de que sean de alguno de los siguientes tipos {'Entrante', 'Postre'} es: Receta(denominación='Gazpacho', tipo='Entrante', dificultad='Baja', ingredientes=[], tiempo=25, calorías=120, fecha=datetime.date(2024, 2, 10), precio=6.95)

La receta más barata de que las 5 con menos calorías de los siguientes tipos {'Plato Principal', 'Postre'} es: Receta(denominación='Ensalada de Frutas', tipo='Postre', dificultad='Baja', ingredientes=[Ingrediente(nombre='fresas', cantidad=5.0, unidad='u'), Ingrediente(nombre='piña', cantidad=0.25, unidad='u'), Ingrediente(nombre='kiwi', cantidad=1.0, unidad='u'), Ingrediente(nombre='menta', cantidad=50.0, unidad='cl'), Ingrediente(nombre='zumo naranja', cantidad=100.0, unidad='cl')], tiempo=15, calorías=120, fecha=datetime.date(2024, 1, 14), precio=7.5)
```
