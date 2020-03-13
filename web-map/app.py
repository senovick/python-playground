import folium
import pandas

map = folium.Map(
    location=[38.8356645, -104.8326115], zoom_start=10, tiles="Stamen Terrain"
)
fg = folium.FeatureGroup(name="My Map")
coordinates = [
    {
        "location": [38.8239219, -104.8334947],
        "popup": "Colorado Springs Pioneers Museum",
    },
    {"location": [38.7925303, -104.8512365], "popup": "Broadmoor Hotel"},
]
for coord in coordinates:
    fg.add_child(
        folium.Marker(
            location=coord["location"],
            popup=coord["popup"],
            icon=folium.Icon(color="green"),
        )
    )
map.add_child(fg)
map.save("map.html")
