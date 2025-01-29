Title: Pelican nvim and categories
Date: 2020-02-25
Category: blog
Tags: pelican, blog
Status: draft

This post is a post I wrote in 2020 and updated in 2023.
As you have already noticed from the "Powered by" in this blog,  
I recently moved from [ikiwiki](https://ikiwiki.info/) to [Pelican](https://blog.getpelican.com/).
They are both static site generators.  
The main difference is that Pelican is wrote in python and  
ikiwiki in haskell/perl  
I'm still the maintainer (currently I dropped ikiwiki pacakge) of ikiwiki and  
sometime was a bit painful to make work perl dependency and various plugins.  
Because I moved out the server I thought to give a try to pelican.  
I found pelican actually pretty stable and functional and don't need
to depend to perl is a good plus, I actually didn't mind to had to deal with  
the haskell part.  
I shipped everything in a nginx docker container and managing everything through git.  
I usually manage everything from git.  

Personal use only services:
- nextcloud - collabora
- znc
- pelican
- email

Currently deprecated personal services:
- yacy
- searx
- privatebin
- backup
- kanboard
- dokuwiki
- languagetool

currently down services are for personal restrictions and not decided yet if they will be back up again 
in the future.  

I didn't dockerized gitolite but as is used for pelican it could just complicate things to use something like gitea,
but is in my todo list (not anymore).

So if you want to drop a static blog, Pelican and ikiwiki are both good options I think.
Mostly depends from your taste.  

Why nvim in the title... most of the blog post are wrote pushing to git and using nvim for 
editing. Recently I started to use [spacevim](https://spacevim.org) (toml configuration!) and with spacevim 
you can enable lang#markdown  
lang#markdown use [markdown-preview.nvim](https://github.com/iamcco/markdown-preview.nvim) 
A really nice live markdown preview.

The next task will be to probaly add [isso](https://isso-comments.de/) for comments to this blog.  

The old blog is currently private. (2023)

