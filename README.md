# Quantum Information

**Regarding the current health situation, keep track of the [university](https://www.unibas.ch/en/News-Events/Coronavirus.html) and [cantonal](https://www.coronavirus.bs.ch/) guidelines. Lectures will be distributed online until further notice. Information will be sent by email.**

[Course at the University of Basel](https://vorlesungsverzeichnis.unibas.ch/en/home?id=239410), given by James Wootton of IBM Research.

The course begins on 19th Feb 2020 and will have weekly lectures and exercises. If you are not able to attend the course in person, you can follow along with the materials below.


## Course Content

Quantum information theory is the basis of multiple emerging technologies, such as quantum computation and quantum crypotography. It allows us to understand how quantum effects in physical systems may be harnessed for new forms of information processing. The course will also feature some hands on experience with quantum technology, via the open-source Qiskit framework for quantum computing;

## Course Text

The course will be based on the [Qiskit textbook](https://qiskit.org/textbook/preface.html).

## Lectures

* Lecture 1: Based on [The atoms of computation](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-states/atoms-computation.ipynb) and [The unique properties of qubits](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-states/unique-properties-qubits.ipynb).

* Lecture 2: This is not a course on Python and Qiskit, though we will be using them. So in this lecture we'll review [Python and Jupyter Notebooks](qiskit-textbook/content/ch-prerequisites/python-and-jupyter-notebooks.ipynb) and [Qiskit](qiskit-textbook/content/ch-prerequisites/qiskit.ipynb). You'll need to run these notebooks. See the information in 'Exercises' for more information on this.

* Lecture 3: Based on [Writing Down Qubit States](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-states/writing-down-qubit-states.ipynb) and [Pauli Matrices and the Bloch Sphere](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-states/pauli-matrices-bloch-sphere.ipynb).

* Lecture 4: Based on [States for Many Qubits](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-states/states-many-qubits.ipynb), [Quantum Gates](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-gates/quantum-gates.ipynb) and [Fun with Matrices](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-gates/fun-matrices.ipynb).

* Lecture 5: Based on [Standard Gate Set](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-gates/standard-gate-set.ipynb) and [Proving Universality](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-gates/proving-universality.ipynb).

* Lecture 6: Based on [Basic Circuit Identities](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-gates/basic-circuit-identities.ipynb).

* Lecture 7: Based on [Superdense Coding](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-algorithms/superdense-coding.ipynb) and [Quantum Teleportation](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-algorithms/teleportation.ipynb).

* Lecture 8: Based on [Classical Computation on a Quantum Computer](extra/Oracle-Intro.pdf) and [Bernstein-Vazirani Algorithm](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-algorithms/bernstein-vazirani.ipynb).

* Lecture 9: Based on [Grover's Algorithm](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-algorithms/grover.ipynb) and [Measurement Error Mitigation](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-quantum-hardware/measurement-error-mitigation.ipynb).

* Lecture 10: Based on [Introduction to Quantum Error Correction via the Repetition Code](https://nbviewer.jupyter.org/github/quantumjim/Quantum-information-course-Basel/blob/master/qiskit-textbook/content/ch-quantum-hardware/error-correction-repetition-code.ipynb) and [these slides](extra/QEC-Lecture.pdf).

## Exercises

Some exercises will be in the form of Jupyter notebooks. These can be run locally by installing [Python 3](https://www.python.org/downloads/), [Jupyter](https://jupyter.org/) and [Qiskit](https://qiskit.org/). They can also be run online without any installation using the [IBM Quantum Experience](https://quantum-computing.ibm.com/jupyter/). For this, just use the 'import' function.

The easiest way to to download the exercises is to download the whole repository using [this link](https://github.com/quantumjim/Quantum-information-course-Basel/archive/master.zip).

* **Exercise 1** Work through [this notebook](exercises/Hello_Qiskit.ipynb). Note that [this file](exercises/hello_quantum.py) needs to be located in the same directory. If using the IBM Quantum Experience, simply upload both. Hand in the completed notebook by email.

* **Exercise 2** Use quantum gates to make classical logic gates in [this notebook](exercises/classical_logic_gates.ipynb).

* **Exercise 3** [Try out your linear algebra](exercises/exercise_3.pdf).

* **Exercise 4** [Get to know your Paulis](exercises/exercise_4.pdf).

* **Exercise 5** [Using Clifford gates](exercises/exercise_5.pdf).

* **Exercise 6** [Simulate a simple Hamiltonian](exercises/exercise_6.ipynb).

* **Exercise 7** [Beam a qubit up, Scotty!](exercises/exercise_7.pdf).

* **Exercise 8** [Clean up your garbage](exercises/exercise_8.pdf).

* **Exercise 9** [Implement Grover's algorithm](exercises/exercise_9.pdf).


### Bonus exercises

These won't be graded, but they will help you out.

* **Python and Qiskit on PewPews** Using a PewPew you can experiment with Python and Qiskit in a simple and fun environment. You can even try making a game! See the guide [here](https://nbviewer.jupyter.org/github/qiskit-community/MicroQiskit/blob/master/versions/MicroPython/tutorials/index.ipynb) to get started. You can either use a physical PewPew (handed out in lecture), or an emulator.


## Exam

Instead of the exam (and the final few exercises) we will have a Final Project.

The main aim of this is for you to demonstrate understanding of the topics in the course. But the format is fairly free to allow you to do this in a way that suits you best. Collaboration will be fine. But everyone needs something unique to submit.

Below are the different kinds of project you can choose from. Examples of existing work are given to give you and idea of what you can produce.

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

To make a game, you typically use a game engine. But getting game engines to work with Qiskit can be tricky! I've put some tools together to help you with this, which you can find [here](https://twitter.com/decodoku/status/1249700657159782405).

#### Examples

* [Hello Qiskit](https://qiskit.org/textbook/ch-ex/hello-qiskit.html): a game that teaches quantum computing.
* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [QPong](https://www.youtube.com/watch?v=a1NZC5rqQD8): A game that implements the core game mechanic with a (simulation of).
* [Q Avrai](https://github.com/quantumjim/Q_Avrai/blob/master/papers/CoG/main.pdf): using quantum computing for map generation.


### Run benchmarks on prototype devices

You can access real quantum hardware at the [IBM Quantum Experience](quantum-computing.ibm.com/) and [Quantum Inspire](https://www.quantum-inspire.com/). But how well do they actually work? Many people have run various different types of quantum circuit and analyzed the results to give some insight into this.

You can come up with your own method for benchmarking, or reproduce something that has already been done on a different device. The easiest way is to implement repetition codes using [Qiskit's `topological_codes` module](https://github.com/Qiskit/qiskit-tutorials/blob/master/tutorials/ignis/6_repetition_code.ipynb). But since this package (hopefully) makes it easy, you'll need to try out more than just a single code on a single device

#### Examples

* [Quantum Awesomeness](https://github.com/Qiskit/qiskit-community-tutorials/blob/master/games/quantum_awesomeness.ipynb): a game that gives insight into real devices (and [featured in the NZZ](https://www.nzz.ch/wissenschaft/games-with-james-ld.1367435)).
* [Decoherence of entangled states](https://arxiv.org/abs/1712.07080): A paper looking at decoherence in GHZ states.
* [Repetition Codes](https://arxiv.org/abs/2004.11037): using Qiskit's `topological_codes` module to test a device.
