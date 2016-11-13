/**
 * Created by Ciff on 2016-11-13.
 */

function initMap(pointA, pointB) {
    myOptions = {
      zoom: 7,
      center: pointA
    },
    map = new google.maps.Map(document.getElementById('map-canvas'), myOptions),
    // Instantiate a directions service.
    directionsService = new google.maps.DirectionsService,
    directionsDisplay = new google.maps.DirectionsRenderer({
      map: map
    }),
    markerA = new google.maps.Marker({
      position: pointA,
      title: "Your Position",
      label: "You",
      map: map
    }),
    markerB = new google.maps.Marker({
      position: pointB,
      title: "Bike Station",
      label: "Station",
      map: map
    });

  // get route from A to B
  calculateAndDisplayRoute(directionsService, directionsDisplay, pointA, pointB);

}

function calculateAndDisplayRoute(directionsService, directionsDisplay, pointA, pointB) {
  directionsService.route({
    origin: pointA,
    destination: pointB,
    travelMode: google.maps.TravelMode.WALKING
  }, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });
}