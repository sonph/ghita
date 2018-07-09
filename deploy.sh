#!/bin/bash

confirm() {
  echo -n "Press any key to continue"
  read
}

CURRENT_BRANCH="$(git branch | grep '*' | awk '{print $2}')"
git checkout master && confirm && \
git pull origin master && confirm && \
git branch -D gh-pages && confirm && \
git checkout -b gh-pages && confirm && \
python3 -m transcrypt --build app.py && confirm && \
pug *.pug -o ./ && confirm && \
git add -f __javascript__ index.html && confirm && \
git commit -m "Deploy" && confirm && \
git push -f origin gh-pages && confirm && \
git checkout "$CURRENT_BRANCH"

# TODO: fix __javascript__/app.js not found
# TODO: include app.min.js
