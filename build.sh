#!/bin/bash

build_content () {
  echo "BUILD: begin"
  echo "branch: $CF_PAGES_BRANCH"
  echo "SITEURL: $SITEURL"
  echo "Creating symlinks of posts in posts/ into content/"
  cd content && python MAKESYMLINKS.py && cd ..
  pelican content
  echo "BUILD: end"
}

if [ "$CF_PAGES_BRANCH" == "main" ]; then

  # In ase we want to do something special for deploys to main
  build_content

else

  build_content

fi
