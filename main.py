import streamlit as st
import folium

# Create a map
map = folium.Map(location=[40.7128, -74.0059], zoom_start=12)

# Add a marker to the map
marker = folium.Marker([40.7128, -74.0059], popup="This is a marker!")
map.add_child(marker)

# Add a clickable area to the map
clickable_area = folium.GeoJson(
    data={
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[-74.009, 40.713], [-74.009, 40.710], [-74.005, 40.710], [-74.005, 40.713], [-74.009, 40.713]]]
                },
                "properties": {"popup": "This is a clickable area!"},
            }
        ],
    }
)
map.add_child(clickable_area)

# Add a callback to the clickable area
def on_click(event):
    st.write(f"You clicked on the clickable area at {event.coordinate}")

clickable_area.add_event_listener("click", on_click)

# Display the map in Streamlit
st.map(map)