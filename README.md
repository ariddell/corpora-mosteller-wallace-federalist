Data used in *Inference and Disputed Authorship*
================================================

(work in progress)

This repository contains a reconstruction of the data used in Mosteller,
Frederick, and David L Wallace. *Inference and Disputed Authorship: The
Federalist.* Reading, MA: Addison-Wesley, 1964.

Mosteller and Wallace made use of 98 items of writing (Mosteller and Wallace
1964, 17):

- 48 by Hamilton
- 50 by Madison

Since Madison is the acknowledged writer of only 14 of *The Federalist* essays,
36 samples of Madison's writing come from "external" sources (Mosteller and
Wallace 1964, 20). This repository collects those 36 samples, some of which are
concatenations of shorter pieces of writing.

Reconstruct samples
===================

Running ``make`` should result in
``mosteller-wallace-federalist-papers.csv`` appearing in the current
directory.

Variables
---------

``mosteller-wallace-federalist-papers.csv`` is a document-term matrix. With
the following two additional columns:

-   ``code_number`` corresponds to the "code number" used by Mosteller and Wallace. In the case of *The Federalist*, the
    code number is the same as *The Federalist* number.
-   ``AUTHOR`` is one of {``HAMILTON``, ``HAMILTON AND MADISON``, ``HAMILTON OR MADISON``, ``JAY``, ``MADISON``}. The
    samples with disputed authorship are those with ``AUTHOR`` equal to ``HAMILTON OR MADISON``.


Sources
=======

*The Federalist*
----------------

- Hamilton: 48 known papers
- Madison: 14 known papers

Obtained from ``federalist.csv`` was downloaded from
``http://www-stat.wharton.upenn.edu/~stine/mich/data/federalist.csv``.

Madison samples exterior to *The Federalist*
--------------------------------------------

These are described on pages 269 and 270 of Mosteller and Wallace (1964).

Misc
====

``misc/swright/`` contains files downloaded from
``http://pages.cs.wisc.edu/~swright/525/project/`` on 2016-03-01.
