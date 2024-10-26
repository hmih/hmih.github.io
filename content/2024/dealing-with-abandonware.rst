Dealing with abandonware
========================

:date: 2024-10-20 17:45
:description: reverse engineering, abandonware

My father designs, plans and helps in the construction of SPA centers and
wellness facilities. He primarily uses mossaics and ceramics. To do his job he
uses a program from the early 2000s called `TileCreatorPro
<https://web.archive.org/web/20050520075658/http://www.tilecreatorpro.com/>`_.
I bought this program for him in 2017 from `thoughtfishmedia.com
<http://www.thoughtfishmedia.com/>`_ (now defunct). He uses it often and has
many custom designs in its bespoke format. He spent a lot of time manually
filling in the many types of tiles to create a complete inventory.

.. figure:: /images/tile-creator-pro.jpg
   :height: 30em

The woes began in 2021 when my dad decided to upgrade the family desktop
computer. Before the upgrade he asked me if there will be a problem with the
program when going from Windows 7 to Windows 10. I suspected the program would
not work at all, so I decided to first email the manufacturer and check if the
OS is supported. Then I discovered the website does not exist. Someone did not
paid their DNS provider.

I decided to google around for the program and queried for the exact name
"tilecreatorpro". It returned 4 junk results. Then I looked up
"thoughtfishmedia". Boom. I found an article from the owner of the company
`Andrew Simmons <https://x.com/thoughtfishmedi>`_ who told `CBS news
<https://www.cbsnews.com/news/less-work-higher-profits-why-i-outsourced-my-entire-operation/>`_
in 2011 that he has recently become the adoptive father of 6 and has no time
for software. Can't blame him.

Since google didn't yield anything useful, I decided to look inside the
program. I asked my dad to send me the installation file and the main binary. I
use a MacBook, and this application is Windows only, so executing it is out of
the question. I ran *strings* on it and went through the output. One item stood
out to me: ::

    <DIV><SELECT class="field select medium" id=Field13 tabIndex=14 name=Field13> 
    <OPTION value=<BeadCreatorPro>BeadCreatorPro</OPTION>
    <OPTION value=<BeadCreator Publisher>BeadCreator Publisher</OPTION>
    <OPTION value=<Cross Stitch Supreme>Cross Stitch Supreme</OPTION>
    <OPTION value=<MuralCreator>MuralCreator</OPTION>
    <OPTION value=<TileCreator>TileCreator</OPTION>
    <OPTION value=<TileCreatorPro>TileCreatorPro</OPTION>
    <OPTION value=<TileCreator Artistic>TileCreator Artistic</OPTION>

You can see the names of other thoughtfishmedia products. And after looking up
"BeadCreatorPro" I got many results from `reddit
<https://www.reddit.com/r/Beading/comments/16qe6s8/bead_creator_pro_download/>`_!
Digging through reddit, other forums, and facebook groups, I found a support
email `support@beadcreatorpro` and sent this email: ::

  Hello! I purchased TileCreatorPro 4 several years ago. Now I am forced to
  switch over from Windows 7 to Windows 10. Will TCP continue working? If not,
  is there an upgrade available for TCP, or is it abandoned? It was difficult
  to find your BeadCreator website and contact you, so if TCP is not offered
  anymore, do you know some software I can use to replace it? 

I was very surprised to see a reply the following day: ::

  Hello there,

  I will be able to provide you with some support for TileCreator. I can
  provide you a download link, with which you can test to see if it works on
  Windows 10. I suspect there will be no issues with compatibility.

  I am sorry you had difficulty finding us, TileCreator is mostly unsupported
  at this point in time. I do not personally know of any similar software.

  Please look for an email from SendOwl with a download link for you. This may
  end up in your spam folder.

  And please do let me know if you run into any issues with it.

  Kind regards,
  Bryce

Okay, amazing. I then asked if I can test out the installation on a spare
machine before upgrading the main one. This way my dad still has his program if
it doesn't work out. Bryce said that separate machines require separate serial
numbers, and offered to give me spare serial numbers for the purpose of
testing. However, he needed a "PC-ID" to issue me a serial number: ::

  I just need you to let me know what the "PC-ID" is that shows when you open
  the software. This should be a 4 to 8 digit code. I can use these to generate
  serial numbers for you. Let me know if you have any trouble finding those.

So, I installed Windows 10 and TileCreatorPro on a spare machine, sent
Bryce my PC-ID and tried out the serial number he gave me. Success!

To recapitulate the registeration process: when you buy the software you must
first install an unlicensed version, get a 4 character magic number (aka PC-ID)
from the unlicensed program, and request your serial number for that specific
magic number. (AFAIK the first regular purchase I made had a serial number
submission form where you can request the key after purchasing the software.
This form does not work anymore.)

My dad then upgraded the family desktop computer. I installed the program,
entered the working serial number aaaaaand the key did not work. I told Bryce
and he said the magic number is known to change from time to time and issued me
yet another serial number. This one worked and the family desktop computer had
a licensed version of Tile Creator Pro!

Two years later my dad upgraded the family desktop again to install a new GPU.
After the upgrade the magic number changed, which invalidated the previous
serial number and registration. I contacted Bryce several times but got no
response. With no support available I decided it's time to crack the
abandonware.

I have zero reverse engineering experience but I've been scrolling through
HackerNews for years and it was finally time to put that knowledge to the test.

I tried three reverse engineering tools: Ghidra, Binary Ninja, and IDA. I
decided to go with Binary Ninja because of the pleasant interface and ease of
use. I've written some C / C++, have some experience writing compilers, and
know a little bit about embedded devices and x86_64 / riscv5 assembly.

The first thing I needed to do was find a way to run Windows 10. My Macbook is
too slow to emulate both x86_64 and Windows 10. Thus, I got my dusty old
Thinkpad T440p and ran QEMU on it.

Windows 7 ran too slow, as did Windows 10. NixOS worked well even after several
years of neglect. Luckily my work laptop is a powerful x86_64 machine. After
looking around for a Windows emulator I found out about `quickemu
<https://github.com/quickemu-project/quickemu>`_. Amazing software! Runs like a
charm. I quickly set up Windows 10 and installed Tile Creator Pro on it.

The first thing I did was to look for registration and licensing related
strings in the binary. I renamed some functions with speculative purposes like
"calls_busted_with_cb", or "perhaps_parse_magic_number_inner_for_real".

It's difficult to understand the cobweb of jumps and decompiled symbols just by
reading them. I used the Binary Ninja debugger and ran the target under it.
Execution showed me actual values and I got a better sense of the code paths.
My reasoning was: I have a valid serial number, what matters is getting the
same magic number so the serial number is valid, I need to check where the
magic number is generated.

It was difficult to find out **where** exactly the code was generated and I did
not have much time to continue rummaging around the binary. My dad needed the
program ASAP because of a new client. Plus, I have a regular job and this was
done after working hours. (Not to mention the girlfriend who I completed
neglected, she confirms this whilst proofreading my article.) I turned to the
company slack channel and asked if someone knows someone who does reverse
engineering or might have clues themselves. Several colleagues offered tips and
most thought what I was doing was cool. One person had a contact but it was not
a sure deal. I looked on reddit for freelancers and even messaged one company
to hire them, no response though.

I refused to give up and I decided to start debugging from **_init** and see
what I find. At one point I got into a function where the registers gradually
accumulated the **new** magic number. I got super excited. I looked more
closely into the related calls and found **it**:

.. figure:: /images/tile-creator-pro-magic-number-code.png

My mind was instantly flooded with questions: Will changing this code brick the
entire program? What if it is not the only place where the magic number is
generated? What if there are multiple ways of getting the magic number and
checking against eachother? What if there is already a value in my registry
that it is checked against? What if there is self-modifying code and the real
magic number is already stored at some address in the binary?

.. figure:: /images/tile-creator-pro-indiana-johnes.jpeg

I silenced all those questions and decided to try and hardcode the result to
the magic number I need:

.. figure:: /images/tile-creator-pro-fix.png

I re-ran the program in the debugger and saw my old magic number! I used the
serial number I had and it worked!

.. figure:: /images/tile-creator-pro-registered.png

Success!

Now my dad has the program for as long as Windows 10 exists and I won't have to
worry about him as much... until the next Windows upgrade.
