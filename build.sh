#!/bin/bash

build_content () {
  echo "BUILD: begin"
  echo "branch: $CF_PAGES_BRANCH"
  echo "SITEURL: $SITEURL"
  echo "Creating symlinks of posts in posts/ into content/"
  cd content && python MAKESYMLINKS.py && cd ..
  pelican content "$@"
  sed -i 's/\.html</</' output/sitemap.xml
  python3 tags_sorter.py
  echo "BUILD: end"
}

if [ "$CF_PAGES_BRANCH" == "main" ]; then

  # In case we want to do something special for deploys to main
  build_content "$@"

else

  build_content "$@"

fi
