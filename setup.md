Local Setup
===========

https://anaconda.org/conda-forge/ruby says to run:

```
conda create -yn guldmyr-com-ruby-env -c conda-forge ruby
conda activate guldmyr-com-ruby-env
conda install -c conda-forge c-compiler compilers cxx-compiler
gem install jekyll
```

resulted in:

```
$ conda --version
conda 23.1.0
$ gem --version
3.3.7
$ ruby --version
ruby 3.1.2p20 (2022-04-12 revision 4491bb740a) [x86_64-linux]
````

Install:  `gem install jekyll bundler`

Setup new jekyll

.... no let's try docker instead

https://github.com/Starefossen/docker-github-pages

```bash
docker run -it --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
```

But this still doesn't actually render anything :/

.. This other docker?

https://github.com/Starefossen/docker-github-pages/issues/74

Or:
```bash
git clone https://github.com/github/pages-gem
cd pages-gem
make image
cd ..
docker run -it --rm -p 4000:4000 -v $(pwd):/src/site gh-pages jekyll serve --watch --force_polling -H 0.0.0.0 -P 4000
```

Same here. OK I don't know ruby or jekyll :D

HMmm.. Actually it renders HTML - it just doesn't get it into the "minima" theme for some reason.

MMaybbbe
----

https://dev.to/derlin/testing-github-pages-with-remote-theme-locally-3nid
