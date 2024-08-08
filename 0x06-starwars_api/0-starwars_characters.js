#!/usr/bin/node

// Import the required 'request' module
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Send a GET request to the API to retrieve movie data
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch and print each character's name
    characters.forEach(characterUrl => {
      request(characterUrl, (err, res, charBody) => {
        if (!err && res.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
