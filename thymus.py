# Importar paquetes necesarios: pandas y folium 
import folium 
import pandas as pd

# Leer ficheros csv con el conjunto de ocurrencias de Thymus granatensis y Thymus serpylloides subsp. serpylloides descargado desde GBIF (https://www.gbif.org) como un DataFrame.
# Funcion: read_csv (pandas)
# Parametros: sep, [index_col], [parse_dates]
# Tutorial: http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#getting-data-in-out
# Referencia: http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
specie_1 = pd.read_csv('Thymus_granatensis.csv', sep='\t')
specie_2 = pd.read_csv('Thymus_serpylloides.csv', sep='\t')

# Crear un mapa para la visualizacion de las especies.
# Ojo: Es necesario ajustar las coordenadas (norte-este) y el zoom del mapa a la localizacion de la especie
# Funcion: Map (folium)
# Parametros: location, [zoom_start], [tiles]
# Tutorial: http://python-visualization.github.io/folium/quickstart.html#Getting-Started
# Referencia: http://python-visualization.github.io/folium/modules.html#folium.folium.Map
specie_map = folium.Map(location = [37.25, - 3], zoom_start=5, tiles='Stamen Terrain')

# Crear un loop; es decir, iterar por las ocurrencias y añadirlas al conjunto de puntos
for label, ocurrence in specie_1.iterrows():
    # Obtener la latitud y la longitud
    longitud = ocurrence['decimalLongitude']
    latitud = ocurrence['decimalLatitude']
    localidad = ocurrence['locality']
    localidad =str(localidad)
    nombre = ocurrence['scientificName']
    # Comprobar que existen coordenadas
    if not pd.isnull(latitud):
        # Crear el marcador
        # Funcion: Marker (folium)
        # Parametros: location, [popup]
        # Tutorial: http://python-visualization.github.io/folium/quickstart.html#Markers
        # Referencia: http://python-visualization.github.io/folium/modules.html#folium.map.Marker
        marker_green = folium.Marker(location=[latitud,longitud], popup=folium.Popup(nombre + '. \n' + localidad), icon=folium.Icon(color='green', icon='info-sign'))
        # Insertarlo en el mapa
        marker_green.add_to(specie_map)
# Crear el mismo loop para añadir al mapa la segunda especie
for label, ocurrence in specie_2.iterrows():
    # Obtener la latitud y la longitud
    longitud_1 = ocurrence['decimalLongitude']
    latitud_1 = ocurrence['decimalLatitude']
    localidad_1 = ocurrence['locality']
    localidad_1 =str(localidad)
    nombre_1 = ocurrence['scientificName']
    # Comprobar que existen coordenadas
    if not pd.isnull(latitud_1):
        # Crear el marcador
        marker_blue = folium.Marker(location=[latitud_1,longitud_1], popup=folium.Popup(nombre_1 + '. \n' + localidad_1), icon=folium.Icon(color='blue', icon='info-sign'))
        # Insertarlo en el mapa
        marker_blue.add_to(specie_map)
        
# Guardar el mapa como una pagina web
specie_map.save('mapa.html')