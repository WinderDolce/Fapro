# Fapro
Creación de API para consultar la Unidad de Fomento en Python

# La aplicación permite obtener el valor de la UF (Unidad de Fomento) para una fecha dada. La UF es una unidad monetaria de Chile que se ajusta diariamente por la inflación y es utilizada principalmente en transacciones financieras y contratos. Utiliza la librería Flask para crear una API que recibe una fecha en el formato 'dd-mm-yyyy' y devuelve el valor de la UF correspondiente a esa fecha. Para obtener el valor, hace una solicitud HTTP a una página web que publica los valores de la UF diariamente y luego extrae la información relevante de la tabla HTML obtenida. Si no se encuentra el valor de la UF correspondiente a la fecha solicitada, la aplicación devuelve un error 404. Si hay algún problema con la solicitud o el procesamiento de la información, devuelve un error 500.

# La query para realizar peticiones es la siguiente: "/api/uf/dd-mm-yyyy"


# Desarrollador:
Winder Jesús Machado García
jaysydolcebooking@gmail.com
Fullstack Developer