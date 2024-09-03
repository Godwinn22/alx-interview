#!/usr/bin/node

const request = require('request');
// Get the movie ID from the first command-line argument
const movieId = process.argv[2];

// The base URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Send a request to the Star Wars API to get the movie details
if (process.argv.length > 2) {
  request(apiUrl, (err, _, filmBody) => {
    // checking for errors
    if (err) {
      console.log('The error is :' + err);
      return;
    }

    // Parse the response body as JSON
    const movieData = JSON.parse(filmBody);

    // Get the list of character URLs from the movie data
    const characters = movieData.characters;

    // For each character URL, send a request to get the character details
    characters.map((charactersUrl) => {
      request(charactersUrl, (err, _, charBody) => {
        // checking for errors
        if (err) {
          console.log(err);
          return;
        }

        // Parse the response body as JSON and print the character's name
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
    });
  });
}
