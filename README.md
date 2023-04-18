# Hypotheses and Models in Data Intensive Domains Course, @hamc2023, Masters 1/2
Faculty of Computational Mathematics and Cybernetics, Moscow State University

**Classes: Tuesday, 17.00 - 18.20, room 579**

  > **M. Jordan:** *... current focus on doing AI research via the gathering of data, the deployment of “deep learning” infrastructure, and the demonstration of systems that mimic certain narrowly-defined human skills — with little in the way of emerging explanatory principles —  tends to deflect attention from major open problems in classical AI. These problems include the need to bring meaning and reasoning into systems that perform natural language processing, the need to infer and represent causality, the need to develop computationally-tractable representations of uncertainty and the need to develop systems that formulate and pursue long-term goals. These are classical goals in human-imitative AI, but in the current hubbub over the “AI revolution,” it is easy to forget that they are not yet solved.*

 > *We have to have error bars around all our predictions ... Otherwise it's gambling, and too many failed predictions can lead to big disappointment with Big Data - a Big Data Winter.*
 
 > **M. Brodie:** *Yet there is a potential Big Data Winter ahead if people blindly apply Big Data and more specifically machine learning.*

 > **[Causal Machine Learning for Real-World Impact:](https://nips.cc/virtual/2022/workshop/49992)** *Causality has a long history, providing it with many principled approaches to identify a causal effect (or even distill cause from effect). However, these approaches are often restricted to very specific situations, requiring very specific assumptions. This contrasts heavily with recent advances in machine learning. Real-world problems aren’t granted the luxury of making strict assumptions, yet still require causal thinking to solve. Armed with the rigor of causality, and the can-do-attitude of machine learning, we believe the time is ripe to start working towards solving real-world problems.*

## Course overview
This is one term course, which provides a survey of the theory and application of methods to work with hypotheses and models in data intensive domains. Topics covered include overview of different approaches to hypotheses and models formulation, representation, tests, logic and probabilistic inference, model quality assessment.
This course is part of a sequence of courses on Big Data track and is taught for 1st and 2nd year masters students.


## Course outcomes
- The main objective of this course is to overview hypothesis-driven approach and the skills needed to do empirical research in data-intensive domains 
- The course aims to provide students with techniques and receipts for applying statistical/probabilistic framework to assess quality of models 
- The course will also emphasize recent developments in hypothesis management and will present some open questions and areas of ongoing research

## How students time is spent
- 2 hours per week - lectures
- 4 hour per week - homeworks

## Assessment
- 50% - Final Oral Exam
- 50% - Homeworks

grade
5: 80 - 100%; 
4: 60 - 79%;
3: 40 - 59%;
<3: 0 - 39%.

## Instructor
Dmitry Kovalev

## Assistants
TBD

## Course Materials
This repository contains lectures and homeworks for @hamc2023. It will be updated as the class progresses.

| Week | Lecture notes | Supplementary materials | Homework | Tests |
|:------:|:----------|:----------|:----------|-------|
|1| [Introduction](./lectures/intro.pdf) <br> [Outline](./lectures/hamc_outline.pdf)| [M. Jordan about AI revolution](https://medium.com/@mijordan3/artificial-intelligence-the-revolution-hasnt-happened-yet-5e1d5812e1e7) <br> [J. Gray. Fourth Paradigm](https://www.microsoft.com/en-us/research/publication/fourth-paradigm-data-intensive-scientific-discovery/) <br> [M. Brodie. Understanding Data Science](https://www.researchgate.net/publication/285586313_Understanding_Data_Science_An_Emerging_Discipline_for_Data-Intensive_Discovery) <br> [L. Kalinichenko. Methods and Tools for Hypothesis-Driven Research Support](http://synthesis.ipi.ac.ru/synthesis/staff/dmkovalev/15ia-hypoth.pdf)|||
|2| [Statistics in DID: part 1](./lectures/L01_ham_statistics.ipynb) <br> [Statistics in DID: part 2](./lectures/L02_freq_bayes.ipynb) | [Video lecture from 2021](./supplementary/statistics_2021_course.mp4) <br> [Course at KhanAcademy](https://www.khanacademy.org/math/statistics-probability) <br> [Limitations of CLT](https://stats.stackexchange.com/questions/61798/example-of-distribution-where-large-sample-size-is-necessary-for-central-limit-t/61849#61849) <br> [CI and hypotheses](http://www.mit.edu/~6.s085/notes/lecture2.pdf) <br> [Statistical paradoxes slides](./supplementary/stats_paradox.pdf)<br> [Statistical paradoxes (lecture from 2021)](./supplementary/zoom_1.mp4) |||
|3-4| [Bayesian approach to A/B testing](./lectures/L03_bayes.ipynb) | [Conjugate Priors](https://www.cs.ubc.ca/labs/lci/mlrg/slides/Conjugate.pdf) <br> [Course at Udemy](https://www.udemy.com/course/bayesian-machine-learning-in-python-ab-testing)  |  [homework1](./homeworks/hypoth_hw1.ipynb) ||
|5-6| Homework 1 and test 1|  | [homework2](./homeworks/test2_.ipynb)  <br> [hw1_results](./homeworks/hw1/hw1_results.md) | [test1_results](./homeworks/test1/test1_results.md) |
|7| [Other approaches to model selection](./lectures/L04_metrics_scoring.ipynb) | | [hw2_results](./homeworks/hw2/hw2_results.md) | |
|8| [Hypothesis representation: structures](./lectures/L05_hypothesis_repr.ipynb)| [Video lecture part 1](./supplementary/video1820715075.mp4) <br> [Video lecture part 2](./supplementary/video1943057871.mp4) <br>[Causality and independence in systems of equations](https://pure.uva.nl/ws/files/63630379/Thesis.pdf) <br> [Elements of Causal Inference](https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/) | | |
|9| [Hypothesis representation: structures](./lectures/L05_hypothesis_repr.ipynb) | [Reusable mechanisms (lecture from 2021)](./supplementary/zoom_4.mp4) <br> [Causality (lecture from 2021)](./supplementary/zoom_2.mp4) <br> [A note on the complexity of the causal ordering problem](https://arxiv.org/abs/1508.05804) <br> [Constructing Hypothesis Lattices for Virtual Experiments in Data Intensive Research](https://ieeexplore.ieee.org/abstract/document/8880738/)| | | 
|Exam| [Questions](./lectures/questions.md) | | | |