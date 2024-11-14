def seleccionar_caracteristicas(data):
   
    datos_seleccionados = {
        'Country or region': data['Country or region'],
        'Region': data['Region'],
        'GDP per capita': data['GDP per capita'],
        'Social support': data['Social support'],
        'Healthy life expectancy': data['Healthy life expectancy'],
        'Freedom to make life choices': data['Freedom to make life choices'],
        'Perceptions of corruption': data['Perceptions of corruption'],
        'Generosity': data['Generosity'],
        'Dystopia_Residual': data['Dystopia_Residual'],
    }
    return datos_seleccionados