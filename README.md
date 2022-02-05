# Wordski

Inspiration from the original Wordle by [Josh Wardle](https://github.com/powerlanguage).

In Wordski, you have 6 guesses to guess the 6-letter word of the day. After you submit a guess, the colors of the
letter tiles in your guess will change. 
- Grey letter tile means that letter does not appear anywhere in the word.
- Yellow letter tile means that letter is somewhere in the word, just not where you have it in the guess.
- Green letter tile means that letter is in the correct spot.

The wordlist comes from [SCOWL](http://app.aspell.net/create).

## Setup

Install the NPM packages with:
```
cd ./wordguy/
npm install
```

For production deployment with SSL, the certificates `iamcoleman.io.chained.crt` and `iamcoleman.io.key` must be placed 
in the directory `./wordguy/nginx_prod/certs/`.

## Deployment

### Building the Docker image

#### Production Build

1. Build the Docker image using `Dockerfile-prod`

```
cd ./wordguy/
docker build -t wordski:0.0.0 -f Dockerfile-prod .
```

2. Tag the image to go to my Dockerhub repo

```
docker tag wordski:0.0.0 iamcoleman/wordski:0.0.0
```

3. Push the tagged image

```
docker push iamcoleman/wordski:0.0.0
```

#### Development Build

Build the Docker image using `Dockerfile`

```
cd ./wordguy/
docker build -t wordski:0.0.0 .
```

### Running the container

#### Production with SSL
```
docker run -it -d -p 80:8080 -p 443:8090 --name wordski [iamcoleman/]wordski:0.0.0
```

#### Development
```
docker run -it -d -p 80:8080 --name wordski [iamcoleman/]wordski:0.0.0
```
