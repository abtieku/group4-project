// js functions
// Create the map object with a center and zoom level.

console.log("working");

console.log(latLng);

let map = L.map(
    'mapid', {
    center: [40.7, -94.5], 
    zoom: 4
});

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

for (let i =0, size = latLng["lat"].length; i < size ; i++) {
    var marker = new L.marker([parseFloat(latLng["lat"][i]), parseFloat(latLng["lng"][i])]);
    marker.addTo(map);
    // Adding pop-up to the marker
    marker.bindPopup( "<h3>"+ latLng["state"][i] +" "+ latLng['name'][i] + "</h3><b></b><h4>review count: " + latLng["review_count"][i]).openPopup();
};


streets.addTo(map);