Title: Searx and Gentoo wiki search
Date: 2020-02-24
Category: gentoo
Tags: gentoo, searx
Status: published

Two years ago I started to get interested in selfhosting services.
I started to go away from private services and implementing selfhosting,
manly because private services was disabling most of the features that 
I liked and I had no way to contribute or see how they was working.  
That is what made look into https://old.reddit.com/r/selfhosted/ and
https://www.privacytools.io/
That is when I disovered searx, as the github page say [searx](https://github.com/asciimoo/searx) is a
"Privacy-respecting metasearch engine".  
As any selfhost service, you can install easily on your server or  
also on the local computer.   
For the installation instruction go [here](https://github.com/asciimoo/searx#if-you-are-in-a-hurry) or use
the [searx-docker project](https://github.com/searx/searx-docker).  
As I use selfhosted services also because I like to contribute back,  
after a few look I decided to add a meta-engine in searx.  
Specifically a Gentoo wiki search meta-engine.
Pull requeset [#1368](https://github.com/asciimoo/searx/pull/1368)

Gentoo wiki search is usually enabled by default in the   
it tab :)

![searx_gentoo_default]({static}/images/searx_gentoo_default.png)

Gentoo wiki search can also be used by the searx shortcut system (same as bang in duckduckgo if you have familiarity)  

The Gentoo wiki search shortcut is !ge  
for example  
https://search.stinpriza.org/?q=%21ge%20project%3Akernel&categories=none&language=en

will give you this:  
![searx_shortcut_ge]({static}/images/searx_shortcut_ge.png)

for concluding,
have fun with searx and Gentoo!

I also highly recommend to have your own searx instance but you can play with [public instances](https://searx.space/#).
