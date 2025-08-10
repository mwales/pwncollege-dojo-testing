# challenge-legacy

My docker image is based on the base pwn.college image.  Basic things I tried
to update from what pwn.college had originally:

* Updated image to Ubuntu 24.04 LTS base (it was 20.04)
* Removed custom kernel
* Removed busybox
* Removed anything that needed to be installed via pip (installed most of the
  same tools via Ubuntu packages)

# Package Updates

## New things I want to add

[x] FCEux NES 
[ ] ImHex editor
[ ] rot13 (bsdgames)
[ ] cowsay
[ ] ristretto (lightweight xfce image viewer)
[ ] nano

## Things I want to remove

[ ] racket (380MB)

## Things that should be redone

[ ] capstone is compiled from git commit with specific hash, but has a
    libcapstone-dev, libcapstone, and python3-capstone packages
[ ] tcpdump is compiled, and source / temps all left in the image

# Sharing the image

I updated this image to hub.docker.com.  That way the pwn.college instances
can download it.  This image is also used to build the challenges (you will
see podman scripts in the chal_crafting folder)
