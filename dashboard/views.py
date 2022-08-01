from django.shortcuts import render
from .models import Vessel
import folium
from folium import plugins
# Create your views here.


def index(request):
    data = Vessel.objects.all()
    vessels = Vessel.objects.values_list('latitude', 'longitude', 'datetime','name', 'callsign', 
                    'destination', 'eta', 'course','speed','mmsi', 'heading', 'navstat', 'imo', 'aistype','a','b','c','draught')

    if vessels:
        lat, lg = vessels[0][0], vessels[0][1]
    else:
        lat, lg =  30.57277778, 32.49194444
        
    map1 = folium.Map(location=[lat, lg], zoom_start=7,
                   tiles='Stamen Terrain')
    vessels1 = []
    for latitude, longitude, datetime,name, callsign, destination, eta, course, speed, mmsi, heading, navstat, imo, aistype,a,b,c,draught in vessels:
        plugins.BoatMarker(location=(latitude, longitude),
              popup=f"""<i>Vessel:{name}<i>
              <i>Callsign:{callsign}<i>""",
              icon=folium.Icon(color='red',icon='ship', prefix='fa') ,
             ).add_to(map1)
        
        vessels1.append((name, callsign))
    
    plugins.Fullscreen(position='topright').add_to(map1)
    map1 = map1._repr_html_()
    context = {
        'map1': map1,
        'vessels': vessels1
    }
    return render(request, 'dashboard/index.html', context)