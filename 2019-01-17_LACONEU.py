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
 author_link='<a href="https://laurentperrinet.github.io">Laurent Perrinet</a>',
 short_title='Role of dynamics in neural computations underlying visual processing',
 title='Role of dynamics in neural computations underlying visual processing',
 conference_url='http://www.laconeu.cl',
 short_conference='LACONEU 2019',
 conference='LACONEU 2019: 5th Latin-American Summer School in Computational Neuroscience',
 location='Valparaiso (Chile)',
 YYYY=YYYY, MM=MM, DD=DD,
 tag=tag,
 url=f'https://laurentperrinet.github.io/{tag}',
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
<BR>
{Karl}{Mina}{Anna}<a href="https://github.com/laurentperrinet/slides.py">{Python}</a>
"""
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         intro  - motivation - teaser        🏄🏄🏄🏄🏄🏄🏄🏄
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
some key challenges in understanding the role of dynamics in visual perception

* please interrupt me !

* (ACKNO) this endeavour involves different techniques and tools ...
From the head on, I wish to thanks people who collaborated  and in particular ..
  mostly funded by the ANR horizontal V1
(fregnac chavane) + ANR TRAJECTORY (o marrre bruno cessac palacios )
+ LONDON (Mina, Anna, Rick, Karl)

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
    """.format('https://raw.githubusercontent.com/laurentperrinet/2019-01-16_LACONEU/master/figures/ssc.mp4')+review_bib)

#
s.add_slide(content=s.content_figures(
   [os.path.join(home, 'pool/science/PerrinetBednar15/talk/scheme_thorpe.jpg')], bgcolor="black",
   height=s.meta['height']*.90),
notes="""

 * today, I would like  to focus on a particular problem which will help us unravel the dynamics of decision making: oculomotor delays.
 *
  The central nervous system has to contend with axonal delays, both at the sensory and the motor levels. For instance, in the human visuo-oculomotor system, it takes approximately $ \tau_s=50~ms$ for the retinal image to reach the visual areas implicated in motion detection, and a further $ \tau_m=40~ms $ to reach the oculomotor muscles.

 * how does this impact behaviour? Indeed, one challenge for modelling is to understand EMs using AI as a problem of optimal motor control under axonal delays.
 """)

figpath_2017 = os.path.join(home, 'Desktop/2017-01_LACONEU/figures/')

s.add_slide(content=s.content_figures(
   [os.path.join(figpath_2017, 'tsonga.png')], bgcolor="black",
   height=s.meta['height']*.90),
   notes="""
* let's move to a human, in particular a tennis player ---here (highly trained) Jo-Wilfried Tsonga at Wimbledon---...

* ...  trying to intercept a passing-shot ball at a (conservative) speed of $20~m.s^{-1}$, the position sensed on the retinal space corresponds to the instant when its image formed on the photoreceptors of the retina and reaches our hypothetical motion perception area behind:

 """)
s.add_slide(content=s.content_figures(
   [os.path.join(figpath_2017, 'figure-tsonga.png')], bgcolor="black",
   height=s.meta['height']*.90),
   #image_fname=os.path.join(figpath, 'figure-tsonga.png'), embed=False,
       notes="""

* and at this instant, the sensed physical position is lagging behind (as represented here by $\tau_s \cdot v 1~m$ ), that is, approximately at $45$ degrees of eccentricity (red dotted line),

* while the  position at the moment of emitting the motor command will be $.8~m$ ahead of its present physical position ($\tau_m \cdot v$).

* As a consequence, note that the player's gaze is directed to the ball at its **present** position (red  line), in anticipatory fashion. Optimal control directs action (future motion  of the eye) to the expected position (red dashed line) of the ball in the  future --- and the racket (black dashed line) to the expected position of the  ball when motor commands reach the periphery (muscles). This is obviously an interesting challenge for modelling an optimal control theory.

""")

s.add_slide(content=s.content_figures(
   [os.path.join(figpath_2017, 'back-to-the-future-quotes-dr-emmett-brown.jpg')], bgcolor="black",
   height=s.meta['height']*.90),
   notes="""
WOW! THIS LOOKS COMPLICATED!

Luckily, we can integrat'e that in the free-energy formalism
 """)


s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄              Active inference               🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################
s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
Let's set up the problem
""")

#     figpath = 'figures/'
#     # karl_bib = s.content_bib("Friston", "2010", "Nat Neuro Reviews")
#
#     s.add_slide(content=s.content_figures(
#       [os.path.join(figpath, 'figure-tsonga-B.png')], bgcolor="black",
#       height=s.meta['height']*.90),
#       #image_fname=os.path.join(figpath, 'figure-tsonga-AB.png'),
#        notes="""
#
# In that order, we will now show how to include oculomotor delays
#
# and include constraints from EMs as a model for a generic model of decision making
#
# thanks to a one year sabbatical visit at Karl Friston's lab in London at the WTCI UCL and in collaboration with Rick Adams, I have had the chance to collaborate in the ellaboration of a series of studies on Active inference and EMs:
#
# """)

# s.add_slide(content=s.content_figures(
# [os.path.join(figpath, 'friston10c_fig4.png')], bgcolor="black",
# title=title, height=s.meta['height']*.6) + karl_bib,
#    notes="""
#
# As we now all know, the ...
#
# Unification des theories computationnelles par la minimisation de l'energie libre (MEL).
# Cette figure extraite de {Friston10c} represente la place central du principe de MEL dans l'ensemble des theories computationnelles. En particulier, on peut noter que les principes que nous avons detailles plus haut dans les chapitres precedents (reseaux de neurones heuristiques, principes d'optimisation, codage predictif, ...) peuvent se rapporter a ce langage commun. %
#
# ... when including action in such models, it becomes ...
#
# """)

s.add_slide(content=s.content_figures(
[os.path.join(figpath_2017, figname) for figname in ['Friston12.png', 'Adams12.png', 'PerrinetAdamsFriston14header_small.png']], bgcolor="black",
#title=title,
fragment=True,
transpose=True, height=s.meta['height']*.75,
url=['http://invibe.net/LaurentPerrinet/Publications/' + name for name in ['Friston12', 'Adams12', 'PerrinetAdamsFriston14']]),
notes="""
* in a first study, we have proposed that PERCEPTION (following Helmhotz 1866) is an active process of hypothesis testing by which we seek to confirm our predictive models of the (hidden) world: Active inference: (cite TITLE). In theory, one could find any prior to fit any experimental data, but the beauty of the theory comes from the simplicity of the models chosen to model the data at hand, such as saccades...

* ... and even better if these models may find a possible correspondance into the neural anatomy and explain some deviation to a control  behaviour, such as that we modelled for understanding some aspects of the EMs of schizophrenic patients

* Today, I will again focus on the problem of sensorimotor delays in the optimal control of (smooth) eye movements under uncertainty. Specifically, we consider delays in the visuo-oculomotor loop and their implications for active inference and I will present the results presented in the following paper (show TITLE).

""")

freemove_bib = s.content_bib("LP, Adams and Friston", "2015", 'Biological Cybernetics, <a href="http://invibe.net/LaurentPerrinet/Publications/PerrinetAdamsFriston14">http://invibe.net/LaurentPerrinet/Publications/PerrinetAdamsFriston14</a>')

for fname, note in zip(['friston_figure1.png', 'friston_figure2.png', 'PAF14equations.png', 'PAF14equations2.png'], ["""

* This schematic shows the dependencies among various quantities modelling exchanges of an agent with the environment. It shows the states of the environment and the system in terms of a probabilistic dependency graph, where connections denote directed (causal) dependencies. The quantities are described within the nodes of this graph -- with exemplar forms for their dependencies on other variables.

* Hidden (external) and internal states of the agent are separated by action and sensory states. Both action and internal states -- encoding a conditional probability density function over hidden states -- minimise free energy. Note that hidden states in the real world and the form of their dynamics can be different from that assumed by the generative model; (this is why hidden states are in bold. )
""","""
*  Active inference uses a generalisation of Kalman filtering to provide Bayes optimal estimates of hidden states and action in generalized coordinates of motion. As we have seen previously, the central nervous system has to contend with axonal delays, both at the sensory and the motor levels. Representing hidden states in generalized coordinates provides a simple way of compensating for both these delays.

* This mathematical framework can be mapped to the anatomy of the visual system. Similar to the sketch that we have shown above, "compiling" (that is, solving) the equations of Free-energy minimization forms a set of coupled differential equations which correpond to different node along the visuo-oculomotor pathways.
""","""

* a novelty of our approach including known delays was to take advantage of genralized coordinates to create an operator $T$ to travel back and forth in time with a delay $\tau$. It is simply formed by using a Taylor expansion of the succesive orders in the generalized coordinates which takes this form in matrix form and thus simply by taking the exponential matrix form.
""","""
Applying such an operator to the FEM generates a slightly different and more complicated formulation but it is important to note that to compensate for delays, there is no change in the structure of the network but just in how the synaptic weights are tuned (similar to what we had done in the first part)

* The efficacy of this scheme will be illustrated using neuronal simulations of pursuit initiation responses, with and without compensation.

"""]):
    s.add_slide(#image_fname=os.path.join(figpath, fname),
    content=s.content_figures(
[os.path.join(figpath_2017, fname)], bgcolor="black",
#title=title,
 height=s.meta['height']*.85),# + freemove_bib,
# >>> Lup IS HERE <<<
notes=note)

s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath_2017, 'flash_lag_dot.mp4'))),
notes="""

Pursuit initiation

""")
#figpath = os.path.join(home, 'tmp/2015_RTC/2014-12-31_PerrinetAdamsFriston14/poster/12-06-25_AREADNE/')
#for fname in ['Slide3.png', 'Slide4.png']:
#figpath = os.path.join(home, 'tmp/2015_RTC/2014-04-17_HDR/friston/')
for fname in ['friston_figure3.png',
              'friston_figure4-A.png',
              'friston_figure4-B.png',
               'friston_figure4-C.png']:

    s.add_slide(#image_fname=os.path.join(figpath, fname),
    content=s.content_figures(
[os.path.join(figpath_2017, fname)], bgcolor="black",
#title=title,
 height=s.meta['height']*.90),# + freemove_bib,
notes="""

This figure reports the conditional estimates of hidden states and causes during the simulation of pursuit initiation, using a single rightward (positive) sweep of a visual target, while compensating for sensory motor delays. We will use the format of this figure in subsequent figures: the upper left panel shows the predicted sensory input (coloured lines) and sensory prediction errors (dotted red lines) along with the true values (broken black lines). Here, we see horizontal excursions of oculomotor angle (upper lines) and the angular position of the target in an intrinsic frame of reference (lower lines). This is effectively the distance of the target from the centre of gaze and reports the spatial lag of the target that is being followed (solid red line). One can see clearly the initial displacement of the target that is suppressed after a few hundred milliseconds. The sensory predictions are based upon the conditional expectations of hidden oculomotor (blue line) and target (red line) angular displacements shown on the upper right. The grey regions correspond to 90% Bayesian confidence intervals and the broken lines show the true values of these hidden states. One can see the motion that elicits following responses and the oculomotor excursion that follows with a short delay of about 64ms. The hidden cause of these displacements is shown with its conditional expectation on the lower left. The true cause and action are shown on the lower right. The action (blue line) is responsible for oculomotor displacements and is driven by the proprioceptive prediction errors.

* This figure illustrates the effects of sensorimotor delays on pursuit initiation (red lines) in relation to compensated (optimal) active inference -- as shown in the previous figure (blue lines). The left panels show the true (solid lines) and estimated sensory input (dotted lines), while action is shown in the right panels. Under pure sensory delays (top row), one can see clearly the delay in sensory predictions, in relation to the true inputs. The thicker (solid and dotted) red lines correspond respectively to (true and predicted) proprioceptive input, reflecting oculomotor displacement. The middle row shows the equivalent results with pure motor delays and the lower row presents the results with combined sensorimotor delays. Of note here is the failure of optimal control with oscillatory fluctuations in oculomotor trajectories, which become unstable under combined sensorimotor delays.

""")

#figpath = 'figures/'
s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath_2017, 'flash_lag_sin.mp4'))),
notes="""

Smooth Pursuit
We then consider an extension of the generative model to simulate smooth pursuit eye movements --- in which the visuo-oculomotor system believes both the target and its centre of gaze are attracted to a (hidden) point moving in the visual field.
""")
#figpath = os.path.join(home, 'tmp/2015_RTC/2014-04-17_HDR/friston/')
for fname in ['friston_figure6.png', 'friston_figure7.png']:
    s.add_slide(#image_fname=os.path.join(figpath, fname),
    content=s.content_figures(
[os.path.join(figpath_2017, fname)], bgcolor="black",
#title=title,
 height=s.meta['height']*.90),# + freemove_bib,
notes="""


* This figure uses the same format as the previous figure -- the only difference is that the target motion has been rectified so that it is (approximately) hemi-sinusoidal. The thing to note here is that the improved accuracy of the pursuit previously apparent at the onset of the second cycle of motion has now disappeared -- because active inference does not have access to the immediately preceding trajectory. This failure of an anticipatory improvement in tracking is contrary to empirical predictions. \item \odot

* the generative model has been equipped with a second hierarchical level that contains hidden states, modelling latent periodic behaviour of the (hidden) causes of target motion. With this addition, the improvement in pursuit accuracy apparent at the onset of the second cycle of motion is reinstated. This is because the model has an internal representation of latent causes of target motion that can be called upon even when these causes are not expressed explicitly in the target trajectory.

""")
figpath = 'figures/'
s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath_2017, 'flash_lag_sin2.mp4'))),
notes="""

Smooth Pursuit with oclusion
Finally, the generative model is equipped with a hierarchical structure, so that it can recognise and remember unseen (occluded) trajectories and emit anticipatory responses.
""")
#figpath = os.path.join(home, 'tmp/2015_RTC/2014-12-31_PerrinetAdamsFriston14/poster/12-06-25_AREADNE/')

#figpath = os.path.join(home, 'tmp/2015_RTC/2014-04-17_HDR/friston/')
for fname in ['friston_figure8.png', 'friston_figure9bis.png']:
    s.add_slide(#image_fname=os.path.join(figpath, fname),
    content=s.content_figures(
[os.path.join(figpath_2017, fname)], bgcolor="black",
#title=title,
 height=s.meta['height']*.90),# + freemove_bib,
notes="""


* This figure uses the same format as the previous figure -- the only difference is that the target motion has been rectified so that it is (approximately) hemi-sinusoidal. The thing to note here is that the improved accuracy of the pursuit previously apparent at the onset of the second cycle of motion has now disappeared -- because active inference does not have access to the immediately preceding trajectory. This failure of an anticipatory improvement in tracking is contrary to empirical predictions. \item \odot

* the generative model has been equipped with a second hierarchical level that contains hidden states, modelling latent periodic behaviour of the (hidden) causes of target motion. With this addition, the improvement in pursuit accuracy apparent at the onset of the second cycle of motion is reinstated. This is because the model has an internal representation of latent causes of target motion that can be called upon even when these causes are not expressed explicitly in the target trajectory.

""")

s.close_section()

i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         Back to the present - 15''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
let's move to the second part : at the cortical leval


""")

fle_bib = s.content_bib("Khoei, Masson and LP", "2017", 'PLoS CB', url="http://invibe.net/LaurentPerrinet/Publications/KhoeiMassonPerrinet17")

s.add_slide(content="""
    <video controls autoplay loop width=99%/>
      <source type="video/mp4" src="{}">
    </video>
    """.format(s.embed_video(os.path.join(figpath_2017, 'flash_lag.mp4'))) + fle_bib,
   notes="""

so let's go back on earth

* ... but first let now apply this model compensating for the aforementioned visual delays using a well described visual illusion: the flash-lag effect:

a first stimulus moves continuously across the screen along the central horizontal axis. In the FLE, as this moving stimulus reaches the center of the screen, a second stimulus is flashed just above it and in perfect vertical alignment. Despite the fact that the respective horizontal positions of each stimulus are physically identical when the flash occurs, the moving stimulus is most often perceived *ahead* of the flashed one.

debate for 80 years revived recently

- motion extrapolation
- differential latency
- post-diction

we propose to extend the hypothesis previously proposed by Nihjawan that this effect is caused by the extrapolation of the stimulus' motion to compensate for the neural delay. However, this hypothesis was challenged by other hypothesis that this effect is due to either anatomy (differential latencies) or to the way visual awareness processes the sequence of events (the post-diction from Eagleman)

As a matter of fact, the motion extrapolation hypothesis was challenged because you can notice that the FLE is still present at initiation of the movement but this effect is not seen if the moving dot abruptly stops at the moment of the flash



""")


for txt in ['', '2']:
    s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, 'FLE_DiagonalMarkov_simple' + txt + '.png')], title=title, height=s.meta['height']*.75) + fle_bib,
   notes="""
* Our model is very simple:  Following what Nihjawan called a "diagonal model", we have proposed to extend a motion-based predictive coding model by including the known sensory delay in the prediction-estimation loop

* More formally, the estimated state vector $z = \{x, y, u, v\}$ is composed of the 2D position ($x$ and $y$) and velocity ($u$ and $v$) of a (possibly moving) stimulus. As such, we extend  Nijhawan's diagonal model into a classical Markov chain in order to take into account the known neural delay $\tau$: At time $t$, information is integrated until time $t-\tau$, using a Markov chain and a model of state transitions $p(z_t |z_{t-\delta t})$ such that one can infer the state until the last accessible information $p(z_{t-\tau} | I_{0:(t-\tau)})$. This information can then be ``pushed'' forward in time by predicting its trajectory from $t-\tau$ to $t$. Interestingly, we use the same model of state transition at the time scale of the delay, that is, $p(z_t | z_{t-\tau})$.

* Importantly, the model for transition is based on a simple model of the transport of visual information *knowing the velocity*. Indeed, knowing $z(t-\Delta t)$ we may infer the future position of this motion at time $t$ by using Newton's first law of mechanics. The precision of the state transition (as given by the shaded area) tunes the strength of this prediction as a diffusion parameter.

* Such a model can be implemented in a two-layered neural network including a source (input) and a target (predictive) layer~\citep{KaplanKhoei14}. The source layer receives the delayed sensory information and encodes both position and velocity topographically on the different retinotopic maps of each layer. Notice that here, for simplicity, we show only one 2D map of the motions $(x, v)$. Crucially, the delay compensation in this motion-based prediction model, is simply implemented by connecting each source neuron to a predictive neuron corresponding to the corrected position of stimulus $(x+v\cdot \tau, v)$ in the target layer. The precision of this anisotropic connectivity map can be tuned by the width of convergence from the source to the target populations. We will see on Friday that this property (that it is implemented in the connectivity) extends to more complex, multi-layered systems which may generalize to more complex trajectories.

""")
# * In particular we have used an efficient implementation using particle filtering and all the code for reproducing this theory is available on my github.


for method in ['PBP', 'MBP']:
    s.add_slide(content="""
	   <video controls autoplay loop width=50%/>
          <source type="video/mp4" src="{urldata}">
        </video>
        """.format(method=method, urldata=s.embed_video(os.path.join(figpath_2017, method + '_spatial_readout.mp4'))),
notes="""
* Let me show you now the results of our simulations on the standard flash-lag stimulus by first showing the results of a predictive system with no delay compensation. We here simply show the source layer in the prediction model which tries to track moving patterns but do not compensate for the known delay.

* We observe that the moving dot is correctly tracked and the flash correctly detected. I have slowed down the speed of the movie to show that relative to each other, the flash and moving dot appear at the same position at the time of the flash.

* The situation is different in the motion-based predictive system : in this slowed down movie, at the time the flash appears, the dot's position was predicted *ahead* of the position of the flash, similarly to what is reported in psychophysics.

* Moreover, we have predicted a similar effect with a large range of parameters of the stimulus, such as speed or contrast. But for the moment, let us focus on the reasons why the model shows a similar behavior

""")

# for fname in ['FLE', 'FLE_histogram', 'FLE_MotionReversal']:
for fname in ['FLE_histogram', 'FLE_MotionReversal_MBP', 'FLE_MotionReversal']:
    s.add_slide(content=s.content_figures(
[os.path.join(figpath_talk, fname + '.png')], title=title,
height=s.meta['height']*.8) + fle_bib,
   notes="""

* For that, we replot the movies I have just shown by showing for the dot the Histogram of the estimated positions as a function of time for the source layer (Left) and the target layer (right). The left-hand column illustrates the predictive model before delay compensation. The right-hand column illustrates the motion extrapolation model with delay compensation. Histograms of the inferred horizontal positions (blueish bottom panel) and  horizontal speed (redish top panel) are shown in columns  as a function  of time. A darker level corresponds to a higher probability, while a light  color corresponds to an unlikely estimation. In particular, we focus on three  particular epochs along the trajectory, corresponding to the standard, flash  initiated and terminated cycles. The timing of these epochs flashes are indicated by  dashed vertical lines. In dark, the physical time and in green the delayed  input knowing $\tau=100~ms$.

* Activity in both models shows three different phases. First, there is a rapid  build-up of the precision of the target after the first appearance of the  moving dot (at $t=300~ms$). Consistently with the Frölich effect, the  beginning of the trajectory is seen ahead of its physical position. During the second phase, the moving dot is correctly tracked as both its velocity and position are correctly inferred. In the source layer, there is no extrapolation and the trajectory follows the delayed trajectory of the dot (green dotted line). In the target layer, motion extrapolation correctly predicts the position at the present time and the position follows the actual physical position of the dot (black dotted line). Finally, the third phase corresponds to  motion termination. The moving dot disappears and the corresponding activity vanishes in the source layer at $t=900~ms$. However, between $t=800~ms$ and $t=900~ms$, the dot position was extrapolated and predicted ahead of the terminal position. At $t=900~ms$, while motion information is absent, the position information is still transiently consistent and extrapolated using a broad, centered prior distribution of speeds. Although it is less precise, this position of the dot at flash termination is therefore not perceived as leading the flash.

* Interestingly, and thanks to the reviewers of the paper, we could extend our results to the estimation of the dot position from the dMBP model during the motion reversal experiment. In the motion reversal experiment, the moving dot reverses its direction  at the middle of the trajectory (i.e., at $t=500~ms$,  as indicated by the mid-point vertical dashed line).  In the left column (target layer) and as in previous slide, we show the histogram of inferred positions  during the dot motion and a trace of its position with the highest probability  as a function of time.  As expected, results are identical to that in the previous slide in the first half period.  At the moment of the motion reversal,  the model output is consistent with previous psychophysical reports.  First, the estimated position follows the extrapolated trajectory  until the (delayed) sensory information about the motion reversal reaches the system  (at $t=600~ms$, green vertical dashed line).  Then, the velocity is quickly reseted and converges to the new (reversed) motion  such that the estimated position ``jumps'' to a position corresponding  to the updated velocity.  In the right column (smoothed layer), we show the results of the same data  after a smoothing operation of $\tau_s=100~ms$ in subjective time.  This different read-out from the inferred positions  corresponds to the behavioral results obtained in some experiments,  such as that from~\citet{Whitney98}.

""")
s.close_section()


i_section += 1
###############################################################################
# 🏄🏄🏄🏄🏄🏄🏄🏄         Perspectives - 5''              🏄🏄🏄🏄🏄🏄🏄🏄
###############################################################################
###############################################################################

s.open_section()
title = meta['sections'][i_section]
s.add_slide_outline(i_section,
notes="""
what are the consequences?

""")

# https://invibe.net/LaurentPerrinet/Publications/Chemla18
# Chemla S, Reynaud A, di Volo M, Zerlaut Y, Perrinet L, Destexhe A, Chavane F. Suppressive waves disambiguate the representation of long-range apparent motion in awake monkey V1, URL . 2018 abstract.
AM_bib = s.content_bib("Chemla, Reynaud, di Volo, Zerlaut, LP, Destexhe, Chavane", "2019", 'in revision', url=" https://invibe.net/LaurentPerrinet/Publications/Chemla18")
for i in ['1', '3a']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'Chemla18_'+ i + '.png')], bgcolor="white", embed=False,
        title=None, height=s.meta['height']*.85) + AM_bib,
           notes="""
Figure 1:
​
​
Experimental protocol and time-sequence of the cortical response to the long-range
apparent motion (lrAM).
​​
A:
​
 Two-step lrAM stimuli are presented to two awake fixating monkeys in
their bottom left visual field, while recording in their right visual cortex using VSDI.
​
B:
​
 Spatio-temporal
characteristics of lrAM stimuli, i.e. duration (DUR) , interstimulus interval (ISI) and spatial interval (SI),
were varied to cover a [5-66.6]°/s range of speed.
​
C-E:
​
 Cortical representation of evoked VSDI activity as
a function of time, in response to respectively, a 100 ms local stimulus in the down position, another one
Explaining away ambiguous representations in V1
in the up position, and the sequence of these two stimuli (ISI  = 50 ms and SI = 1°). The cortical area
imaged is shown at upper left. The edge of the image color codes the retinotopic borders as represented
in A such as the vertical meridian (magenta), eccentricities (green and blue). Scale bar: 2 mm; A:
anterior, P: posterior, M: medial, L: lateral. Time in milliseconds after stimulus onset is shown at the top,
while stimulation time is drawn at the bottom of each row (black lines).
​
F:
​
 Activity pattern predicted by
the linear combination in space and time of the response to stimulus 1 (row C) and the response to
stimulus 2 (row D).
​
G:
​
Suppression pattern obtained by subtracting the observed apparent motion
response (row E) and the linear prediction (row F). Red contours delimit amplitude activity above a
certain threshold: 1
 in panels C-F and  -0.5
 in panel G.

Figure 3:  The apparent motion stimulus induces a systematic suppression wave.
​
 Spatio-temporal
representation of VSDI responses to two-stroke apparent motion stimuli for three different speed
(6.6°/s, 10°/s and 33.3 °/s) and two animals (
​
A:
​
 monkey WA,
​
B:
​
 monkey BR). The upper rows of A and B
represent the observed response and the lower rows the non-linearities of the response (observed -
linear prediction). Estimates of speed propagation are reported on each ST diagram (black stairs-step are
contours at threshold level, slanting lines are the slope of the linear regression). Similar values are
observed for both the observed activity and the non-linearities.

""")

# benvenuti & Taouali
BT_bib = s.content_bib("benvenuti, Taouali, LP, Chavane", "", 'in prep')
for i in ['1', '2', '3']:
    s.add_slide(content=s.content_figures(
        [os.path.join(figpath_talk, 'ExperimentalResult_'+ i + '.png')], bgcolor="white", embed=False,
        title=None, height=s.meta['height']*.85) + BT_bib,
           notes="""

""")

# waves with B. Cessac

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

 What:: talk @ the [[{conference_url}|{conference}]]
 Who:: {author}
 When:: {DD}/{MM}/{YYYY}
 Where:: {location}
 Slides:: https://laurentperrinet.github.io/{tag}
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
