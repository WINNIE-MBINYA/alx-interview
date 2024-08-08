# Star Wars Characters

This project contains a Node.js script that prints the names of all characters from a specific Star Wars movie. The movie is identified by its Movie ID, which is passed as a positional argument to the script.

## Features

- The script retrieves and displays character names in the order they appear in the movie's "characters" list.
- Uses the Star Wars API to fetch movie and character data.
- The script is compliant with semistandard guidelines and uses semicolons.

## Requirements

- Node.js version 10.14.x
- `request` module (installed globally or locally)

## Installation

To install Node.js version 10.x on Ubuntu 20.04 LTS, run the following commands:

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
