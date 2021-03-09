// js functions
// Create the map object with a center and zoom level.

console.log("working");

console.log(state);
console.log(selection);

if (selection == "all categories") {
    selection = "all";
};


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


if (state == "all" && selection == "all") {
    d3.json("https://groupfour.ngrok.io/json_data/data.json").then(function(data) {
    console.log(data);
    for (var i = 0; i < data["lat"].length; i++) {
        {
        var marker = new L.marker([parseFloat(data["lat"][i]), parseFloat(data["lng"][i])]);
        marker.bindPopup( "<h3>"+ data["state"][i] +" "+ data['name'][i] + "</h3><b></b><h4>review count: " + data["review_count"][i] +"<b></b><h4> Star Rating: "+ data["stars"][i] +"</h4>").openPopup();
        marker.addTo(map)
        }
    }
});
};






if (state == "all" && selection != "all" && selection != "select category") {
    d3.json("https://groupfour.ngrok.io/json_data/data.json").then(function(data) {
    console.log(data);
    for (var i = 0; i < data["lat"].length; i++) {
        if (data[selection][i] == 1) {
        var marker = new L.marker([parseFloat(data["lat"][i]), parseFloat(data["lng"][i])]);
        marker.bindPopup( "<h3>"+ data["state"][i] +" "+ data['name'][i] + "</h3><b></b><h4>review count: " + data["review_count"][i] +"<b></b><h4> Star Rating: "+ data["stars"][i] +"</h4>").openPopup();
        marker.addTo(map)
        }
    }
});
};

if (selection == "all" && state != "all") {
    d3.json("https://groupfour.ngrok.io/json_data/data.json").then(function(data) {
        console.log(data);
        for (var i = 0; i < data["lat"].length; i++) {
            if (data["state"][i] == state) {
            var marker = new L.marker([parseFloat(data["lat"][i]), parseFloat(data["lng"][i])]);
            marker.bindPopup( "<h3>"+ data["state"][i] +" "+ data['name'][i] + "</h3><b></b><h4>review count: " + data["review_count"][i] +"<b></b><h4> Star Rating: "+ data["stars"][i] +"</h4>").openPopup();
            marker.addTo(map)
            }
        }
    });
};

if (selection != "all" && state != "all") { 
d3.json("https://groupfour.ngrok.io/json_data/data.json").then(function(data) {
    console.log(data);
    for (var i = 0; i < data["lat"].length; i++) {
        if (data["state"][i] == state && data[selection][i] == 1) {
        var marker = new L.marker([parseFloat(data["lat"][i]), parseFloat(data["lng"][i])]);
        marker.bindPopup( "<h3>"+ data["state"][i] +" "+ data['name'][i] + "</h3><b></b><h4>review count: " + data["review_count"][i] +"<b></b><h4> Star Rating: "+ data["stars"][i] +"</h4>").openPopup();
        marker.addTo(map)
        }
    }
});
};

streets.addTo(map);