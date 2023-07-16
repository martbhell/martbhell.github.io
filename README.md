Source for the Blog where I blog about IT, Finnish Things and sometimes about Storage (but not so much anymore on this topic).

Workflow:
----
   - build content with `bash build.sh` - same as in deployment but
     without defining `SITEURL` when running `pelican content`.
     In cloudflare deploy we set it to https://guldmyr.com
     Having it unset makes links work when developing locally
   - Test stuff locally with `pelican -l`
   - minimize changes to output/content, if needed keep in separate commits than ones to:
     - any config files
     - posts
     - tests
   - merge request
     - sets up a preview page in cloudflare pages
     - when it looks OK merge yo

Directories:
----

   - content/
     - symlinks to posts in posts/
     - cd content; python MAKESYMLINKS.py # done by `build.sh`
   - Makefile
   - output/
     - generated from `pelican content` and most of it should not be commited 
       as it's being built on every deploy in cloudflare in `build.sh`
   - output/images
     - images go here only or also under `posts/yyyy/mm/images/` ?? TODO
   - pelicanconf.py
   - posts/
     - the posts are in here sorted by year
     - there's also a MODIFYTAGS.py here that was used to modify all the posts
   - publishconf.py
   - requirements.txt
   - security.txt
   - tag/
   - tasks.py
   - tests/
     - To Be Added:
       - Ensure only symlinks in content/
  	 - Moar
  	 - Profit
