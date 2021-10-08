---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.1+dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

% Some modifications to table style
<style>
table.mytable {
  //border: 1px solid black;
  border-collapse: collapse;
  border-color: grey;
}
table.mytable td {
  padding: 2px;
  text-align: left;
  height: 5px;
  line-height: 1;
  vertical-align: bottom;
  border-top: 0px;
}

table.mytable th {
  padding: 2px;
  text-align: left;
  height: 5px;
  line-height: 1;
  vertical-align: bottom;
}
</style>

Manifestation of AI
==========


## Automated lawnmowers and vacuum cleaners

```{image} figures/lawnmower.jpg
---
width: 500px
align: center
---

```
[^from_pixabay_monika]

[^from_pixabay_monika]: Image by <a href="https://pixabay.com/users/MonikaP-2515080/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2914172">MonikaP</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2914172">Pixabay</a>

We have already taken into use simple robots to automatize everyday routine works, such as vacuum cleaning or lawn clipping. A robot performing these tasks requires the blocks shown in {numref}`tbl:lawnmower`.

%```{code-cell} ipython3
%:tags: ["hide-input"]
%import pandas as pd
%
%```

```{table} The potential building blocks of the lawnmower or vacuum cleaner robot.
---
name: tbl:lawnmower
class: "mytable"
---
| Activity   | Category   | Example implementation                        |
|------------|------------|-----------------------------------------------|
| Perception | Position   | GPS, camera, velocity sensors                 |
|            | Collision  | Proximity sensors                             |
|            | Charge     | Measure the voltage of the battery            |
| Cognition  | Location   | GPS evalution, machine vision, dead reckoning |
|            | Model      | Map                                           |
|            | Planning   | Search solutions to find optimal path         |
|            | Collision  | Implement a tactics to deal with obstacles    |
|            | Charge     | Estimate the state of the battery             |
| Action     | Drive      | Control speed and steering                    |
|            | Start/Stop | Start and stop operation.                     |
|            | Charging   | Go to charging station when needed            |
```

## Self driving cars
```{image} figures/autonomous_vehicle.jpg
---
width: 500px
align: center
---

```
[^from_pixabay_falco]

[^from_pixabay_falco]: Image by <a href="https://pixabay.com/users/falco-81448/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4759347">falco</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=4759347">Pixabay</a>

The self driving car would be much more complex than a lawnmower, but it has similar high level functions. The self driving car needs more sophisticated sensors and algorithms, because the risks in car driving are bigger due to the higher energy, larger world, and denser traffic, for example.

```{table} Some potential building blocks of the self driving electric car.
---
name: tbl:car
class: "mytable"
---
| Activity   | Category   | Example implementation                        |
|------------|------------|-----------------------------------------------|
| Perception | Position   | GPS, camera, velocity sensors                 |
|            | Collision  | Proximity sensors, radar, camera              |
|            | Charge     | Measure the voltage of the battery            |
| Cognition  | Location   | GPS evalution, machine vision, dead reckoning |
|            | Model      | Map, physical models                          |
|            | Planning   | Search solutions to find optimal path         |
|            | Collision  | Implement a tactics to deal with obstacles    |
|            | Charge     | Estimate the state of the battery             |
| Action     | Drive      | Control speed and steering                    |
|            | Start/Stop | Start and stop operation.                     |
|            | Charging   | Inform the driver of the charging needs, or go to charging station when needed       |
```

An interesting environment for developing AI for self driving cars is the [CARLA simulator](http://carla.org/)

## Humanoid robots
```{image} figures/robot_woman.jpg
---
width: 500px
align: center
name: fig:robot_woman

---

```
[^from_pixabay_comfreak]

[^from_pixabay_comfreak]: Image by <a href="https://pixabay.com/users/Comfreak-51581/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3010309">Comfreak</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=3010309">Pixabay</a>]


Humanoid robots can mimic humans. They walk like a person, and can make tricks like a person and therefore they seem intelligent. It is also evident that these robots needs a huge amount of sensors to control each of its' joints to keep the balance and walk, navigate through complex environments performing human-like tasks. It seems quite apparent that they are machines performing complex tasks, so perhaps they are a manifestation of AI?

You may also take a look at this video, but do not take it too seriously. What do you think is true and what is fake? Is it Ok to bully a robot? Does an intelligent robot with artificial feelings deserve human rights?

<https://www.youtube.com/watch?v=y3RIHnK0_NE&t=7s>

## Medical diagnosis


```{figure} figures/ComputerAidedDiagnosisBoom.png
---
width: 500px
align: center
name: fig:ComputerAidedDiagnosis
---

The utilization of AI for Computer Aided Diagnostis (CAD) in medical fields.
{cite}`fujitaAIbasedComputeraidedDiagnosis2020`
```




The most succesful areas for computer aided diagnostics according to Fujita 
{cite}`fujitaAIbasedComputeraidedDiagnosis2020` are:
 - Fundus photographs: Mass screening of eye dieseases such as glaucoma and retinopathy. Google published a paper which implies that even heart disesases could be recognized frmo fundus images using deep learning.
 - Dermatology imaging: Skin cancer diagnostics where AI has observerd to outperform a human specialist. However it is good to know that the main method for diagnosing skin cancer is still biopsy, not visual examination. 
 - Pathological imaging, detection of lymph node metastasis.
 - Breast imaging, mammography
 - Chest imaging, classify normal and abnormal major thoracic diseases
 
 The figure {numref}`fig:DeepOrgans` shos the utilization of deep learning to segment the human organs based on the example segmentation made by human experts. 
 
 ```{figure} figures/Organs.png
---
width: 500px
align: center
name: fig:DeepOrgans
---

The automated segmentation of organs from Computer Tomograhpy (CT) images.
{cite}`fujitaAIbasedComputeraidedDiagnosis2020`
```

 
 Deep learning has been particularly succesfull in medical diagnostics. The disadvantege of deep learning is that the decision algorithm is a "black box", which structure cannot be easily examined and explained. It is very important particularly in medicine, to explain how the diagnosis has been made.
 
 University of Vaasa has also a few publications and few PhD thesis about AI based medical diagnostics, such as {cite}`valisuoPhotonicsSimulationModelling2011b,alabiMachineLearningPersonalized2021`


## Earth observations

Earth observation is the gathering of information about the physical, chemical, and biological systems of the planet via remote-sensing technologies, supplemented by Earth-surveying techniques, which encompasses the collection, analysis, and presentation of data. Earth observation is used to monitor and assess the status of and changes in natural and built environments.

### Söderfjärden spectral image example

A satellite image of Söderjärden region is shown in {numref}`fig:Soderfjarden_image`. The original satellite image acquired by European [Sentinel-2 satellite](https://sentinel.esa.int/web/sentinel/home) consist of 13 different channels, representing different wavelenght. The figure below is a normal 3-channel RGB image constructed from 13 original channels.

```{figure} figures/Soderfjarden_image.png
---
width: 500px
align: center
name: fig:Soderfjarden_image
---

An RGB visualisation of a satellite image of Söderjärden region, including training data for the classification of  land use.
```

The image also contains some example data shown with polygons, which represent certain types of land use, such as forest, water, dark soil, hay field and grass. This data can be seen as a true classification results performed by an expert. An AI algorithm can now be trained to repeat the same classification using all 13 channels of data from the original image. The trained classification algorithm can then be applied to the rest of the image as well, and classify all pixels. The result of this is shown in {numref}`fig:Soderfjarden_classified` image below.

```{figure} figures/Soderfjarden_classified.png
---
width: 500px
align: center
name: fig:Soderfjarden_classified
---

An RGB visualisation of the land use classification results from Söderjärden region.
```

If the training data provided by the expert wouldn't have been available, then supervised classification had not been possible, but unsupervised clustering could have been tried instead.

```{admonition} Discussion point
What could be achieved using unsupervised methods for analyzing satellite images when compared with supervised methods?
```

### Further information about EO

Read more about earth observations from ESA's [Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth) page or try the [Windy application](https://www.windy.com/) to see some interesting facts about Earth based on both space-based and terrestial observations.

To get facts about the climate and pollution from all over the Globe would not be possible without space based Earth Observations (EO). Thefore EO is also very importanc for climate change mitigation activities. 

## Tackling with climate changes

AI can be useful for many purposes when tackling with climate change, as listed by National Geography, in [How artificial intelligence can tackle climate change](https://www.nationalgeographic.com/environment/2019/07/artificial-intelligence-climate-change/). The climatologists have been using AI methods in predicting 

The figure {numref}`fig:CCAI` shows which AI methods have been popular in prevention of climate change

```{figure} figures/ClimateChangeAI.png
---
width: 700px
align: center
name: fig:CCAI
---

The popularity of different AI methods in domains related to climate change mitigation and prevention {cite}`rolnickTacklingClimateChange2019`
``` 

## Spot fake news

```{figure} figures/Fakenews.png
---
width: 500px
align: center
name: fig:fakenews
---

A proposed structure of AI tool for detecting fake news  {cite}`jadhavFakeNewsIdentification2019`
``` 

```{figure} figures/FakenewsConfusionMatrix.png
---
width: 500px
align: center
name: fig:fakenesCM
---

The accuracy of the fakenews detection expressed as so called Confusion Matrix. The matrix shows how many samples which are fake news were classified as fake news by the algorithm and how many of them were misclassified as original news, and the same for true original news.  {cite}`jadhavFakeNewsIdentification2019`
``` 


## Write documents

[A robot wrote this entire article. Are you scared yet, human?](https://www.graphic.com.gh/features/opinion/a-robot-wrote-this-entire-article-are-you-scared-yet-human.html)
