#!/bin/bash

build_content () {
  echo "branch: $CF_PAGES_BRANCH"
  echo "site_url: $SITEURL"
  pelican content
}

if [ "$CF_PAGES_BRANCH" == "production" ]; then
  # Run the "production" script in `package.json` on the "production" branch
  # "production" should be replaced with the name of your Production branch

  build_content

elif [ "$CF_PAGES_BRANCH" == "staging" ]; then
  # Run the "staging" script in `package.json` on the "staging" branch
  # "staging" should be replaced with the name of your specific branch

  build_content

else
  # Else run the dev script

  build_content

fi
