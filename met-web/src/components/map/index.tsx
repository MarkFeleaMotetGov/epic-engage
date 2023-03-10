import React from 'react';
import ReactMapGL, { Marker, NavigationControl } from 'react-map-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import maplibregl from 'maplibre-gl';

interface MapProps {
    latitude: number;
    longitude: number;
}
const Map = ({ latitude, longitude }: MapProps) => {
    return (
        <ReactMapGL
            initialViewState={{
                longitude: longitude,
                latitude: latitude,
                zoom: 12,
            }}
            mapLib={maplibregl}
            mapStyle="https://governmentofbc.maps.arcgis.com/sharing/rest/content/items/bbe05270d3a642f5b62203d6c454f457/resources/styles/root.json"
            style={{
                width: '100%',
                height: '100%',
            }}
        >
            <NavigationControl />
            <Marker latitude={latitude} longitude={longitude} color="red"></Marker>
        </ReactMapGL>
    );
};
export default Map;