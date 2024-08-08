#!/usr/bin/node

// Print the list of characters in a Star Wars movie.

const request = require('request');

/**
 * Print the list of characters in a Star Wars movie.
 * @param movieId The id of the movie.
 */
function getStarWarCharacters (movieId) {
  if (isNaN(movieId)) {
    console.error('Invalid movie id');
    return;
  }

  if (movieId < 1 || movieId > 7) {
    console.error('Invalid movie id');
    return;
  }

  const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;

      // occurs when the movieId is invalid
      if (characters === undefined) {
        console.error('No characters found');
        return;
      }

      const allCharacters = {};
      characters.forEach(character => {
        request(character, async (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            const characterData = await JSON.parse(body);
            allCharacters[character] = characterData.name;
            if (Object.keys(allCharacters).length === characters.length) {
              characters.forEach(character => {
                console.log(allCharacters[character]);
              });
            }
          }
        });
      });
    }
  });
}

if (process.argv.length === 3) {
  getStarWarCharacters(process.argv[2]);
} else {
  console.error('Usage: ./0-starwars_characters.js <film_id>');
}
