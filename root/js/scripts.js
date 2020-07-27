var mymap = L.map('mapid').setView([14.0446622,121.3204835], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiaGVsbG9wcmFnbWEiLCJhIjoiY2tkMWppcWM2MTN0bTJ5bXl1NWgxZjJiaiJ9.p7mxtmQeyiPSkP9sXzlIrw'
}).addTo(mymap);