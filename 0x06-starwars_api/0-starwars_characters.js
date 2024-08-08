#!/usr/bin/node

/**
 * Script that fetches and prints the names of all characters 
 * from a specific Star Wars movie using the Star Wars API.
 *
 * Usage: ./0-starwars_characters.js <movie_id>
 *
 * Example: ./0-starwars_characters.js 3
 * This will print the names of all characters in "Return of the Jedi".
 */

const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];

  // Request the film data from the API
  request(`${API_URL}/films/${movieId}/`, (err, response, body) => {
    if (err) {
      return console.error(err);
    }
    if (response.statusCode === 200) {
      // Parse the response body to get character URLs
      const charactersURLs = JSON.parse(body).characters;

      // Create an array of promises to fetch character names
      const characterPromises = charactersURLs.map(url => {
        return new Promise((resolve, reject) => {
          request(url, (error, res, charBody) => {
            if (error) {
              reject(error);
            } else {
              // Resolve the promise with the character's name
              resolve(JSON.parse(charBody).name);
            }
          });
        });
      });

      // Wait for all promises to resolve and print the names
      Promise.all(characterPromises)
        .then(names => {
          names.forEach(name => console.log(name));
        })
        .catch(error => console.error(error));
    } else {
      console.error(`Failed to get film data: Status code ${response.statusCode}`);
    }
  });
} else {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
}
