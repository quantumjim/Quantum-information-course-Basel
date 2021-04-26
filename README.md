# Quantum Information

This is a [course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/en/home?id=239410), given by James Wootton of [IBM Quantum](https://www.zurich.ibm.com/st/quantum/).

**Regarding the current health situation, keep track of the [university](https://www.unibas.ch/en/News-Events/Coronavirus.html) and [cantonal](https://www.coronavirus.bs.ch/) guidelines. Lectures will be distributed online. Information will be sent by email.**

The course begins on 2nd March 2021 and will have weekly lectures and exercises.

## Course Content

Quantum information theory is the basis of multiple emerging technologies, such as quantum computation and quantum crypotography. It allows us to understand how quantum effects in physical systems may be harnessed for new forms of information processing. The course will also feature some hands on experience with quantum technology, via the open-source Qiskit framework for quantum computing.

## Course Text

The course will be based on the [Qiskit textbook](https://qiskit.org/textbook/preface.html).

## Lectures

* **Week 1:** What is quantum? What are computers?
  - [The Atoms of Computation](https://qiskit.org/textbook/ch-states/atoms-computation.html)
  - [What is Quantum?](https://qiskit.org/textbook/what-is-quantum.html)
* **Week 2:** Basic programming prerequisites (classical and quantum).
  - [Python and Jupyter Notebooks](https://qiskit.org/textbook/ch-prerequisites/python-and-jupyter-notebooks.html)
  - [Basic Qiskit Syntax](https://qiskit.org/textbook/ch-appendix/qiskit.html)
  - [Hello Qiskit](https://qiskit.org/textbook/ch-ex/hello-qiskit.html)
* **Week 3:** Representing single qubit states and gates.
  - [Representing Qubit States](https://qiskit.org/textbook/ch-states/representing-qubit-states.html)
  - [Single Qubit Gates](https://qiskit.org/textbook/ch-states/single-qubit-gates.html)
* **Week 4:** Multi-qubit states and circuit identities.
  - [Multiple Qubits and Entangled States](https://qiskit.org/textbook/ch-gates/multiple-qubits-entangled-states.html)
  - [Phase Kickback](https://qiskit.org/textbook/ch-gates/phase-kickback.html)
  - [More Circuit Identities](https://qiskit.org/textbook/ch-gates/more-circuit-identities.html)
* **Week 5:** Fun with matrices.
  - [Proving Universality](https://qiskit.org/textbook/ch-gates/proving-universality.html)
* **Week 6:** Proving Universality and Implementing Oracles.
  - [Proving Universality](https://qiskit.org/textbook/ch-gates/proving-universality.html)
  - [Classical Computation on a Quantum Computer](https://qiskit.org/textbook/ch-gates/oracles.html)
* **Week 7:** Basic algorithms and protocols.
  - [Deutsch-Jozsa](https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html)
  - [Bernstein-Vazirani](https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html)
  - [Teleportation](https://qiskit.org/textbook/ch-algorithms/teleportation.html)
  - [Superdense Coding](https://qiskit.org/textbook/ch-algorithms/superdense-coding.html)
* **Week 8:** From the Fourier Transform to Shor's algorithm
  - [Quantum Fourier Transform](https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html)
  - [Quantum Phase Estimation](https://qiskit.org/textbook/ch-algorithms/quantum-phase-estimation.html)
  - [Shor's Algorithm](https://qiskit.org/textbook/ch-algorithms/superdense-coding.html)

## Exercises

Some exercises will be in the form of Jupyter notebooks. These can be run locally by installing [Python 3](https://www.python.org/downloads/), [Jupyter](https://jupyter.org/) and [Qiskit](https://qiskit.org/). They can also be run online without any installation using the [IBM Quantum Lab](https://quantum-computing.ibm.com/lab). When you are on the files menu of the lab, you can click on the 'upload file' icon to upload notebooks.

The easiest way to to download the exercises is to download the whole repository using [this link](https://github.com/quantumjim/Quantum-information-course-Basel/archive/master.zip).


## Exam: Final Project

Instead of the exam (and the final few exercises) we will have a Final Project.

The main aim of this is for you to demonstrate understanding of the topics in the course. The format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

Below are the different kinds of project you can choose from. Examples of existing work are given to give you and idea of what you can produce.

You can start whenever you like. The deadline is 4th June. To submit, send it to me by email.


### Write an explanation of a topic of your choice

You can write about one of the topics covered in the lectures, or about something that wasn't covered. You can include relevant example code in Qiskit, or you can avoid the programming and just have text and images

#### Examples

* [Qiskit Textbook section on Phase Kickback](https://qiskit.org/textbook/ch-gates/phase-kickback.html).
* [Qiskit Textbook section on Berstein-Vazirani](https://qiskit.org/textbook/ch-algorithms/bernstein-vazirani.html).
* [An attempt at a popular science article on quantum non-locality](https://bullshit.ist/some-quantum-weirdness-with-the-simplest-maths-possible-446d33046cf7).


### Make a game using quantum programming

Throughout the history of computing, people have been making simple games to help understand the new technology. Now we can do the same thing with quantum computing. I wrote a whole article on this idea, which you can find [here](https://medium.com/@decodoku/games-computers-and-quantum-84bfdd2c0fe0).

Basically, reasons why we might make a quantum game are:
* To provide a simple and accessible example of a quantum program in action.
* To educate people about quantum computing.
* To start looking for ways in which quantum computing might actually be useful for games.

To make a game, you need a game engine of some sort. Fortunately we at IBM Quantum have made one specifically to help people making quantum games with Qiskit. You can find it [here](https://github.com/qiskit-community/Qisge/blob/main/README.md). Also see [this video](https://www.twitch.tv/videos/996850668) on how to use it.

**Remember: don't just use quantum for a random number generator!**

#### Examples

* [Hello Qiskit](https://qiskit.org/textbook/ch-ex/hello-qiskit.html): a game that teaches quantum computing.
* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [QPong](https://www.youtube.com/watch?v=a1NZC5rqQD8): A game that implements the core game mechanic with a (simulation of).
* [Q Avrai](https://github.com/quantumjim/Q_Avrai/blob/master/papers/CoG/main.pdf): using quantum computing for map generation.
* See also the games from the recent [IndiQ Game Jam](https://itch.io/jam/indiq-quantum-game-jam/entries).


### Run benchmarks on prototype devices

You can access real quantum hardware at the [IBM Quantum Experience](quantum-computing.ibm.com/) and [Quantum Inspire](https://www.quantum-inspire.com/). But how well do they actually work? Many people have run various different types of quantum circuit and analyzed the results to give some insight into this.

You can come up with your own method for benchmarking, or reproduce something that has already been done on a different device. The easiest way is to implement repetition codes using [Qiskit's `topological_codes` module](https://github.com/Qiskit/qiskit-tutorials/blob/master/tutorials/ignis/6_repetition_code.ipynb). But since this package (hopefully) makes it easy, you'll need to try out more than just a single code on a single device

#### Examples

* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [Decoherence of entangled states](https://arxiv.org/abs/1712.07080): A paper looking at decoherence in GHZ states.
* [Repetition Codes](https://arxiv.org/abs/2004.11037): using Qiskit's `topological_codes` module to test a device.


