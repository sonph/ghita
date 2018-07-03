## Objective

Interactive comprehensive music theory assistance tool for guitarists.

## Development workflow

### Setup

    brew install node
    npm install -g pug-cli
    python3 -m pip install transcrypt

### Dev environment

    pug --watch *.pug -o ./
    transcrypt -b -m -n *.py
    python3 -m http.server

### References

  - [vue API](https://vuejs.org/v2/api/)
  - [pug js](https://pugjs.org/language/attributes.html)
  - [transcrypt docs](http://www.transcrypt.org/docs/html/index.html)
