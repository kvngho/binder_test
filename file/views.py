from django.shortcuts import render, redirect
from .firns import FileUploadForm
from .models import FileUpload
import time
import os
# Create your views here.

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        fileupload = FileUpload(
            title=title,
            file = file,
        )
        fileupload.save()
        FRAMERATE = 60 # 분당
        import pandas as pd
        import numpy as np
        # print(os.getcwd())
        # data = pd.read_excel("SpooledGPSData-1.xlsx", engine="openpyxl")
        # def set_frame(arr, frame):
        #     interval = int(FRAMERATE / frame)
        #     return np.asarray(arr[::interval])
        # latitude = data['Latitude']
        # altitude = data['Altitude']
        # longitude = data['Longitude']
        # la = set_frame(latitude, 3)
        # al = set_frame(altitude, 3)
        # lo = set_frame(longitude, 3)
        # la_v = la[1:] - la[:-1]
        # al_v = al[1:] - al[:-1]
        # lo_v = lo[1:] - lo[:-1]
        # total = np.vstack([la_v, lo_v]).transpose()
        # from sklearn.cluster import KMeans
        # import folium
        # # db_scan = DBSCAN(eps=0.07, min_samples=10).fit(total)
        # kmeans = KMeans(n_clusters=6)
        # pred = kmeans.fit_predict(total)
        # # db_scan = DBSCAN(eps=0.005, min_samples=5).fit(total)
        # map_osm = folium.Map(location=[latitude[1], longitude[1]], zoom_start=17)
        # one = []
        # two = []
        # three = []
        # four = []
        # color_set = {
        #     0: 'red',
        #     1: 'blue',
        #     2: 'green',
        #     -1: 'black',
        #     3: 'purple',
        #     4: 'gray',
        #     5: 'black',
        # }
        # for index, color in enumerate(list(pred)):
        #     print(color)
        #     if color == 0:
        #         one.append([la[index], lo[index]])
        #     elif color == 2:
        #         two.append([la[index], lo[index]])
        #     elif color == 3:
        #         three.append([la[index], lo[index]])
        #     else:
        #         four.append([la[index], lo[index]])
        #     # folium.CircleMarker([la[index], lo[index]], radius=0.01, color=color_set[color], fill = True).add_to(map_osm)
        # folium.Polygon(locations=one,fill=True,tooltip='Polygon', color=color_set[0]).add_to(map_osm)
        # folium.Polygon(locations=two,fill=True,tooltip='Polygon', color=color_set[2]).add_to(map_osm)
        # folium.Polygon(locations=three,fill=True,tooltip='Polygon', color=color_set[3]).add_to(map_osm)
        # folium.Polygon(locations=four,fill=True,tooltip='Polygon', color=color_set[4]).add_to(map_osm)
        #
        # map_osm.save('../templates/result.html')

        time.sleep(4)
        return render(request, 'result.html')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm' : fileuploadForm,
        }
        return render(request, 'fileupload.html', context)