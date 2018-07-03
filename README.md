## Objective

Interactive comprehensive music theory assistance tool for guitarists.

## Development workflow

### Setup

    brew install node
    npm install -g pug-cli
    python3 -m pip install transcrypt

### Dev environment

    pug --watch *.pug -o ./
    transcrypt --dstat --build --map --nomin *.py
    python3 -m http.server

### References

  - [vue API](https://vuejs.org/v2/api/)
  - [pug js](https://pugjs.org/language/attributes.html)
  - [transcrypt docs](http://www.transcrypt.org/docs/html/index.html)
  - [transcrypt differences vs CPython](http://www.transcrypt.org/docs/html/differences_cpython.html)
