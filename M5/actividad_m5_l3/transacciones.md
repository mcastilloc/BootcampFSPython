### 4. Transacciones

❔ ¿Qué es una transacción en bases de datos y por qué es importante?
📖 Describe brevemente qué significa:

- Atomicidad: Una transacción se ejecuta completa o no se ejecuta nada.
- Consistencia: Los datos siempre pasan de un estado válido a otro válido.
- Aislamiento: Las transacciones no interfieren entre sí.
- Durabilidad: Los cambios confirmados no se pierden, aunque el sistema falle.


Realiza el siguiente ejercicio en SQL y documenta lo ocurrido:
```sql
	BEGIN;
	UPDATE pedidos SET total = 0 WHERE id=1;
	ROLLBACK;
```
```
Realiza lo solicitado pero no guarda los cambios
```
Repite con:
```sql
	BEGIN;
	DELETE FROM pedidos WHERE id = 2;
	COMMIT;
```
```
Realiza lo solicitado y aplica los cambios
```

Comenta qué diferencia notaste entre ROLLBACK y COMMIT. 

```
ROLLBACK deshace todos los cambios realizados desde BEGIN.
COMMIT guarda los cambios definitivamente en la base de datos.
```

#### Entregables
- Carpeta comprimida (.zip) que contenga:
- Archivo manipulacion_datos.sql con las sentencias comentadas
- Archivo transacciones.md con respuestas conceptuales y reflexión sobre ROLLBACK y COMMIT
- (Opcional) Captura de pantalla del resultado desde el entorno usado (CLI o GUI)

