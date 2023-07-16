#!/bin/bash

build_content () {
  echo "branch: $CF_PAGES_BRANCH"
  echo "site_url: $SITEURL"
  echo "Creating symlinks of posts in posts/ into content/"
  cd content && python MAKESYMLINKS.py && cd ..
  pelican content
}

if [ "$CF_PAGES_BRANCH" == "main" ]; then

  # In ase we want to do something special for deploys to main
  build_content

else

  build_content

fi
