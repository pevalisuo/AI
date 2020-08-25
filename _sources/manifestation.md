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
Manifestation of AI
==========

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

## Earth observations

## Tackling with climate changes

## Spot fake networks
