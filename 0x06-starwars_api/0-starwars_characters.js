#!/usr/bin/node
// Fetch Starwars API endpoint
// Prints all characters of a Star Wars movie
// The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint

const request = require('request')
const args = process.argv[2]
//const url = `https://swapi-api.alx-tools.com/api/films/${args}`

//request(url, (error, resp, body)=> {
//	if (!error && resp.statusCode == 200) {
//		const filmApi = JSON.parse(body);
//		const characters = filmApi.characters; // Ensure correct property name
//		console.log(characters)
//		let api = [];
//		let names = []
//		characters.forEach((characterUrl) => {
//			request(characterUrl, (chErr, resp, body) => {
//				if (!chErr && resp.statusCode == 200) {
//					let api = JSON.parse(body)
//					names.push(api)
//					if (names.length === characters.length) {
//						names.forEach(chara => console.log(chara.name))
//					}
//				}
//				else {console.log(resp.statusCode)}
//			})
//		})
//	}
//	else {
//		console.log(`error fetching api: ${resp.statusCode}`)
//	}
//})

const acquireFilmApi = (url) => {
	return new Promise((resolve, reject) => {
		request(url, (err, resp, body) => {
			if (!err && resp.statusCode == 200) {
				const filmApi = JSON.parse(body)
				resolve(filmApi.characters)
			} else {
				reject(`${err} error with ${resp ? resp.statusCode : 'unknown stsus code'}`)
			}
		}
		)}
	)
}

const getCharacterList = async (characters) => {
	const names = []
	for (const characterUrl of characters) {
	  try {
		  const api = await new Promise((resolve, reject) => {
				request(characterUrl, (err, resp, body) => {
					if (!err && resp.statusCode == 200) {
						resolve(JSON.parse(body))
					} else {
						reject(err)
					}
				})
			})
			names.push(api.name)
		} catch (err) {
			console.log(err)
		}
	}
	return names
}

const run = async () => {
	try {
		const url = `https://swapi-api.alx-tools.com/api/films/${args}`
		const characters = await acquireFilmApi(url)
		const names = await getCharacterList(characters)
		names.forEach(name => console.log(name))
	} catch(err) {
		console.log(err)
	}
}

run()
