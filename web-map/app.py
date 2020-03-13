import folium
import json

map = folium.Map(
    location=[38.8356645, -104.8326115], zoom_start=10, tiles="Stamen Terrain"
)
fg = folium.FeatureGroup(name="My Map")
coordinates = json.load(open("web-map/map-data.json"))
for coord in coordinates:
    fg.add_child(
        folium.Marker(
            location=coord["location"],
            popup=coord["popup"],
            icon=folium.Icon(color="green"),
        )
    )
map.add_child(fg)
map.save("web-map/map.html")
