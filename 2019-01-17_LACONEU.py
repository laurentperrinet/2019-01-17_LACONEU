#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Laurent Perrinet INT - CNRS"
__licence__ = 'BSD licence'
DEBUG = True
DEBUG = False

import os
home = os.environ['HOME']
figpath_talk = 'figures'
figpath_slides = os.path.join(home, 'nextcloud/libs/slides.py/figures/')
#
import sys
print(sys.argv)
tag = sys.argv[0].split('.')[0]
if len(sys.argv)>1:
    slides_filename = sys.argv[1]
else:
    slides_filename = None

print('😎 Welcome to the script generating the slides for ', tag)
YYYY = int(tag[:4])
MM = int(tag[5:7])
DD = int(tag[8:10])

# see https://github.com/laurentperrinet/slides.py
from slides import Slides

height_px = 80
height_ratio = .7

meta = dict(
 embed = True,
 draft = DEBUG, # show notes etc
 width= 1600,
 height= 1000,
 # width= 1280, #1600,
 # height= 1024, #1000,
 margin= 0.1618,#
 reveal_path='https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.7.0/',
 theme='simple',
 bgcolor="white",
 author='Laurent Perrinet, INT',
 author_link='<a href="http://invibe.net">Laurent Perrinet</a>',
 short_title='Role of dynamics in neural computations underlying  visual processing',
 title='Role of dynamics in neural computations underlying  visual processing',
 conference_url='http://www.laconeu.cl',
 short_conference='LACONEU 2019',
 conference='LACONEU 2019: 5th Latin-American Summer School in Computational Neuroscience',
 location='Valparaiso (Chile)',
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 url='http://invibe.net/LaurentPerrinet/Presentations/' + tag,
 abstract="""
""",
wiki_extras="""
----
<<Include(BibtexNote)>>
----
<<Include(AnrHorizontalV1Aknow)>>
----
TagYear{YY} TagTalks [[TagAnrHorizontalV1]]""".format(YY=str(YYYY)[-2:]),
sections=['About Dynamics, vision and neurons',
          'Active Inference',
          'Back to the present',
          'Perspectives ?']
)

# https://pythonhosted.org/PyQRCode/rendering.html
# pip3 install pyqrcode
# pip3 install pypng

import pathlib
pathlib.Path(figpath_talk).mkdir(parents=True, exist_ok=True)

figname = os.path.join(figpath_talk, 'qr.png')
if not os.path.isfile(figname):
    import pyqrcode as pq
    code = pq.create(meta['url'])
    code.png(figname, scale=5)

print(meta['sections'])

s = Slides(meta)
figpath_people = os.path.join(home, 'Desktop/2017-01_LACONEU/people')
Karl = s.content_imagelet(os.path.join(figpath_people, 'karl.jpg'), height_px)
Mina = s.content_imagelet(os.path.join(figpath_people, 'mina.jpg'), height_px)
Anna = s.content_imagelet(os.path.join(figpath_people, 'anna.jpg'), height_px)
Python = s.content_imagelet('https://www.python.org/static/community_logos/python-powered-h-140x182.png', height_px)
s.meta['Acknowledgements'] =f"""<h3>Acknowledgements:</h3>
   <ul>
    <li>Rick Adams and Karl Friston @ UCL - Wellcome Trust Centre for Neuroimaging</li>
    <li>Mina Aliakbari Khoei and Anna Montagnini - FACETS-ITN Marie Curie Training</li>
   </ul>

   {Karl}{Mina}{Anna}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
"""
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 intro  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
i_section = 0
s.open_section()
###############################################################################

s.hide_slide(content=s.content_figures(
    #[os.path.join(figpath_talk, 'qr.png')], bgcolor="black",
    [os.path.join(figpath_slides, 'mire.png')], bgcolor=meta['bgcolor'],
    height=s.meta['height']*.90),
    #image_fname=os.path.join(figpath_aSPEM, 'mire.png'),
    notes="""
Check-list:
-----------

* (before) bring VGA adaptors, AC plug, remote, pointer
* (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
* (VP) open monitor preferences / calibrate / title page
* (timer) start up timer
* (look) @ audience

http://pne.people.si.umich.edu/PDF/howtotalk.pdf

 """)

intro = """
<h2 class="title">{title}</h2>
<h3>{author_link}</h3>
""".format(**meta)
intro += s.content_imagelet(os.path.join(figpath_slides, "troislogos.png"), s.meta['height']*.2) #bgcolor="black",
intro += """
{Acknowledgements}
<h4><a href="{conference_url}">{conference}</a>, {DD}/{MM}/{YYYY} </h4>
""".format(**meta)

s.hide_slide(content=intro)

s.hide_slide(content=s.content_figures([figname], cell_bgcolor=meta['bgcolor'], height=s.meta['height']*height_ratio) + '<BR><a href="{url}"> {url} </a>'.format(url=meta['url']),
            notes=" All the material is available online - please flash this QRcode this leads to a page with links to further references and code ")

s.add_slide(content=intro,
            notes="""
* (AUTHOR) Hello, I am Laurent Perrinet from the Institute of Neurosciences of
la Timone in Marseille, a joint unit from the CNRS and the AMU

* (OBJECTIVE) in this talk, I will be focus in highlighting
some key challenges in understanding visual perception
in terams of efficient coding
using modelization and neural data
* please interrupt

* (ACKNO) this endeavour involves different techniques and tools ...
From the head on, I wish to thanks people who collaborated  and in particular ..
  mostly funded by the ANR horizontal V1
(fregnac chavane) + ANR TRAJECTORY (o marrre bruno cessac palacios )
+ LONDON (Jim Bednar, Friston)

* (SHOW TITLE) I am interested in ...

""")


review_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="http://invibe.net/LaurentPerrinet/Publications/Perrinet15bicv">Biologically Inspired Computer Vision</a>')

figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('https://raw.githubusercontent.com/laurentperrinet/2019-01-16_LACONEU/master/figures/v1_tiger.mp4')+review_bib,
            notes="""
... this video shows this intuition in a quantitative way. from a natural image,
we extracted independent sources as individual edges at different scales and
orientations

when we reconstruct this image frame by frame (see N)
we can quickly recognize the image

natural images are sparse
""")


s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('https://raw.githubusercontent.com/laurentperrinet/2019-01-16_LACONEU/master/figures//ssc.mp4'))

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 Sparse coding  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
one can go one step before the cortex and ask the same question in the retina
are the same process present ?
""")

ravelllo_bib = s.content_bib('Ravello, LP, Escobar, Palacios', '2018', 'Scientific Reports', url='https://dx.doi.org/10.1101/350330')
for si in ['2', '1', '5ac', '5dh']:
    s.add_slide(content=s.content_figures(
            [os.path.join(figpath_talk, 'Ravello2018_'+ si + '.png')], title=None, embed=False, height=s.meta['height']*.7)+ravelllo_bib,
            notes="""
figure 3 of MS1

""")

# figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=85%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/v1_tiger.mp4'), #s.embed_video(os.path.join(figpath,     """.format(s.embed_video(os.path.join(figpath_talk, 'v1_tiger.mp4'))),
notes="""
same procedure with retinal filters (scale, no orientation) = sparseness
""")


droplets_bib = s.content_bib('Ravello, Escobar, Palacios, LP', '2019', 'in prep', url=None)
s.add_slide(content=s.content_figures(
                    ['figures/Droplets_1.png'], fragment=True, transpose=True,
                    title=None, embed=False, height=s.meta['height']*.8)+droplets_bib,
            notes="""
figure 1 of droplets

""")


ols_bib = s.content_bib("Olshausen and Field", "1997", 'Sparse coding with an overcomplete basis set: A strategy employed by V1?')
for i in [2]:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'Olshausen_'+ str(i) + '.png')], bgcolor="white",
        title=None, embed=False, height=s.meta['height']*.85) + ols_bib,
           notes="""
since we assume the retina would invert this model, let's use the forward model
to generate stimuli = droplets

""")

figpath = os.path.join(home,  'pool/science/RetinaCloudsSparse/2015-11-13_droplets/2015-11-13_1310_full_files/droplets_full')
for fname in ['00012_droplets_i_sparse_3_n_sf_8.mp4', '00006_droplets_i_sparse_5_n_sf_1.mp4', ]:
    s.add_slide(content="""
        <video controls loop width=60%/>
          <source type="video/mp4" src="{}">
        </video>
        """.format(s.embed_video(os.path.join(figpath, fname))),
                notes="""
very sparse to very dense

    """)


droplets_bib = s.content_bib('Ravello, Escobar, Palacios, LP', '2019', 'in prep', url=None)
for suffix in ['a', 'b']:
    s.add_slide(content=s.content_figures(
                    [#os.path.join(figpath, 'retina_sparseness_droplets.png'),
                     os.path.join(figpath_talk, 'Droplets_3_' + suffix + '.png')], fragment=False, transpose=True,
                    title=None, embed=False, height=s.meta['height']*.75)+droplets_bib,
            notes="""
figure 3 of droplets

""")

s.add_slide(content=s.content_figures(
                    ['figures/Droplets_5.png'],
                    title=None, embed=False, height=s.meta['height']*.75)+droplets_bib,
            notes="""
figure 5 of droplets

""")

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         Sparse Hebbian Learning - 15''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
let's move to the second part : learning

the main goal of Olshasuen was not only sparse coding but
the fact that using the sparse code, a simple linear hebbian learning allows
to separate independent sources

""")

figpath = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')
s.add_slide(content="""
    <video controls loop width=60%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format('figures/ssc.mp4')) #s.embed_video(os.path.join(figpath,         s.embed_video(os.path.join('figures', 'ssc.mp4'))))
#

figpath = os.path.join(home, 'science/ABC/HULK/')

for suffix in ['map', 'HAP']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'figure_' + suffix + '.png')], bgcolor="black",
    title=None, height=s.meta['height']*.75),
           notes="""
a contribution we made to this algorithm is homeostasis



""")
CNN_ref = '(from <a href="http://cs231n.github.io/convolutional-networks/">http://cs231n.github.io/convolutional-networks/</a>)'
s.add_slide(content=s.content_figures(
    ['http://cs231n.github.io/assets/cnn/depthcol.jpeg'], bgcolor="black",
title=None,  embed=False, height=s.meta['height']*.85) + CNN_ref,
       notes="""

this can be extended to a convolutional neural networks

""")

for suffix in ['CNN']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath, 'figure_' + suffix + '.png')], bgcolor="black",
    title=None, height=s.meta['height']*.85),
           notes="""

discussion...

""")

for suffix in ['1', '2a', '2b']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'SDPC_' + suffix + '.png')], bgcolor="black",
    title=None, embed=False, height=s.meta['height']*.85),
           notes="""

Multi-layered unsupervised Learning


""")


s.add_slide(content=s.content_figures(
    [os.path.join(figpath_talk, 'SDPC_' + suffix + '.png') for suffix in ['3', '4']],
    bgcolor="black", fragment=True,
    title=None, embed=False, height=s.meta['height']*.75),
       notes="""

allows for a better classification as here for MNIST digits
""")
s.close_section()

###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄 OUTRO - 5''  🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
s.add_slide(content=intro,
            notes="""


* Thanks for your attention!
""")
s.close_section()


if slides_filename is None:

    with open("/tmp/wiki.txt", "w") as text_file:
        text_file.write("""\
#acl All:read

= {title}  =

 Quoi:: [[{conference_url}|{conference}]]
 Qui:: {author}
 Quand:: {DD}/{MM}/{YYYY}
 Où:: {location}
 Support visuel:: http://blog.invibe.net/files/{tag}.html


 What:: talk @ the [[{conference_url}|{conference}]]
 Who:: {author}
 When:: {DD}/{MM}/{YYYY}
 Where:: {location}
 Slides:: http://blog.invibe.net/files/{tag}.html
 Code:: https://github.com/laurentperrinet/{tag}/
== reference ==
{{{{{{
#!bibtex
@inproceedings{{{tag},
    Author = "{author}",
    Booktitle = "{conference}, {location}",
    Title = "{title}",
    Url = "{url}",
    Year = "{YYYY}",
}}
}}}}}}
## add an horizontal rule to end the include
{wiki_extras}
""".format(**meta))

else:
    s.compile(filename=slides_filename)

# Check-list:
# -----------
#
# * (before) bring miniDVI adaptors, AC plug, remote, pointer
# * (avoid distractions) turn off airport, screen-saver, mobile, sound, ... other running applications...
# * (VP) open monitor preferences / calibrate / title page
# * (timer) start up timer
# * (look) @ audience
#
# Preparing Effective Presentations
# ---------------------------------
#
# Clear Purpose - An effective image should have a main point and not be just a collection of available data. If the central theme of the image isn't identified readily, improve the paper by revising or deleting the image.
#
# Readily Understood - The main point should catch the attention of the audience immediately. When trying to figure out the image, audience members aren't fully paying attention to the speaker - try to minimize this.
#
# Simple Format - With a simple, uncluttered format, the image is easy to design and directs audience attention to the main point.
#
# Free of Nonessential Information - If information doesn't directly support the main point of the image, reserve this content for questions.
#
# Digestible - Excess information can confuse the audience. With an average of seven images in a 10-minute paper, roughly one minute is available per image. Restrict information to what is extemporaneously explainable to the uninitiated in the allowed length of time - reading prepared text quickly is a poor substitute for editing.
#
# Unified - An image is most effective when information is organized around a single central theme and tells a unified story.
#
# Graphic Format - In graphs, qualitative relationships are emphasized at the expense of precise numerical values, while in tables, the reverse is true. If a qualitative statement, such as "Flow rate increased markedly immediately after stimulation," is the main point of the image, the purpose is better served with a graphic format. A good place for detailed, tabular data is in an image or two held in reserve in case of questions.
#
# Designed for the Current Oral Paper - Avoid complex data tables irrelevant to the current paper. The audience cares about evidence and conclusions directly related to the subject of the paper - not how much work was done.
#
# Experimental - There is no time in a 10-minute paper to teach standard technology. Unless the paper directly examines this technology, only mention what is necessary to develop the theme.
#
# Visual Contrast - Contrasts in brightness and tone between illustrations and backgrounds improves legibility. The best color combinations include white letters on medium blue, or black on yellow. Never use black letters on a dark background. Many people are red/green color blind - avoid using red and green next to each other.
#
# Integrated with Verbal Text - Images should support the verbal text and not merely display numbers. Conversely, verbal text should lay a proper foundation for each image. As each image is shown, give the audience a brief opportunity to become oriented before proceeding. If you will refer to the same image several times during your presentation, duplicate images.
#
# Clear Train of Thought - Ideas developed in the paper and supported by the images should flow smoothly in a logical sequence, without wandering to irrelevant asides or bogging down in detail. Everything presented verbally or visually should have a clear role supporting the paper's central thesis.
#
# Rights to Use Material - Before using any text, image, or other material, make sure that you have the rights to use it. Complex laws and social rules govern how much of someone's work you can reproduce in a presentation. Ignorance is no defense. Check that you are not infringing on copyright or other laws or on the customs of academic discourse when using material.
#
# http://pne.people.si.umich.edu/PDF/howtotalk.pdf
#
