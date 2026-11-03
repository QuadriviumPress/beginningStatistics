(src-fwk-shafer-ch03)=

# Chapter 3 Basic Concepts of Probability

Suppose a polling organization questions 1,200 voters in order to estimate the proportion of all voters who favor a particular bond issue. We would expect the proportion of the 1,200 voters in the survey who are in favor to be close to the proportion of all voters who are in favor, but this need not be true. There is a degree of randomness associated with the survey result. If the survey result is highly likely to be close to the true proportion, then we have confidence in the survey result. If it is not particularly likely to be close to the population proportion, then we would perhaps not take the survey result too seriously. The likelihood that the survey proportion is close to the population proportion determines our confidence in the survey result. For that reason, we would like to be able to compute that likelihood. The task of computing it belongs to the realm of probability, which we study in this chapter.

## 3.1 Sample Spaces, Events, and Their Probabilities

````````````{note} Learning Objectives

1.  To learn the concept of the sample space associated with a random experiment.
2.  To learn the concept of an event associated with a random experiment.
3.  To learn the concept of the probability of an event.

````````````

### Sample Spaces and Events

Rolling an ordinary six-sided die is a familiar example of a *random experiment*, an action for which all possible outcomes can be listed, but for which the actual outcome on any given trial of the experiment cannot be predicted with certainty. In such a situation we wish to assign to each outcome, such as rolling a two, a number, called the *probability* of the outcome, that indicates how likely it is that the outcome will occur. Similarly, we would like to assign a probability to any *event*, or collection of outcomes, such as rolling an even number, which indicates how likely it is that the event will occur if the experiment is performed. This section provides a framework for discussing probability problems, using the terms just mentioned.

````````````{important} Definition

*A* **random experiment** *is a mechanism that produces a definite outcome that cannot be predicted with certainty. The* sample space[^stats-1] *associated with a random experiment is the set of all possible outcomes. An* event[^stats-2] *is a subset of the sample space.*

````````````

````````````{important} Definition

*An event* *E* *is said to* **occur** *on a particular trial of the experiment if the outcome observed is an element of the set* *E*.

````````````

(src-fwk-shafer-ch03-s01-s01-n03)=

### Example 1

Construct a sample space for the experiment that consists of tossing a single coin.

Solution:

The outcomes could be labeled *h* for heads and *t* for tails. Then the sample space is the set $S = \left\{ {h,t} \right\}.$

(src-fwk-shafer-ch03-s01-s01-n04)=

### Example 2

Construct a sample space for the experiment that consists of rolling a single die. Find the events that correspond to the phrases "an even number is rolled" and "a number greater than two is rolled."

Solution:

The outcomes could be labeled according to the number of dots on the top face of the die. Then the sample space is the set $S = \left\{ 1,2,3,4,5,6 \right\}.$

The outcomes that are even are 2, 4, and 6, so the event that corresponds to the phrase "an even number is rolled" is the set {2,4,6}, which it is natural to denote by the letter *E*. We write $E = \left\{ 2,4,6 \right\}.$

Similarly the event that corresponds to the phrase "a number greater than two is rolled" is the set $T = \left\{ 3,4,5,6 \right\}$, which we have denoted *T*.

A graphical representation of a sample space and events is a **Venn diagram**, as shown in [Figure 3.1 \"Venn Diagrams for Two Sample Spaces\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-f01) for [Note 3.6 \"Example 1\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-n03) and [Note 3.7 \"Example 2\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-n04). In general the sample space *S* is represented by a rectangle, outcomes by points within the rectangle, and events by ovals that enclose the outcomes that compose them.

``````{figure} /images/section_07/97b468eaa2da56c52e300c556c23a24f.jpg
:alt: Statistical diagram: Figure 3.1 Venn Diagrams for Two Sample Spaces
:name: src-fwk-shafer-ch03-s01-s01-f01

Figure 3.1 Venn Diagrams for Two Sample Spaces
``````

(src-fwk-shafer-ch03-s01-s01-n05)=

### Example 3

A random experiment consists of tossing two coins.

1.  Construct a sample space for the situation that the coins are indistinguishable, such as two brand new pennies.
2.  Construct a sample space for the situation that the coins are distinguishable, such as one a penny and the other a nickel.

Solution:

1.  After the coins are tossed one sees either two heads, which could be labeled $2h$, two tails, which could be labeled $2t$, or coins that differ, which could be labeled *d*. Thus a sample space is $S = \left\{ {2h,2t,d} \right\}.$
2.  Since we can tell the coins apart, there are now two ways for the coins to differ: the penny heads and the nickel tails, or the penny tails and the nickel heads. We can label each outcome as a pair of letters, the first of which indicates how the penny landed and the second of which indicates how the nickel landed. A sample space is then ${S\prime} = \left\{ {hh,ht,th,tt} \right\}.$

A device that can be helpful in identifying all possible outcomes of a random experiment, particularly one that can be viewed as proceeding in stages, is what is called a **tree diagram**. It is described in the following example.

(src-fwk-shafer-ch03-s01-s01-n06)=

### Example 4

Construct a sample space that describes all three-child families according to the genders of the children with respect to birth order.

Solution:

Two of the outcomes are "two boys then a girl," which we might denote $bbg$, and "a girl then two boys," which we would denote $gbb.$ Clearly there are many outcomes, and when we try to list all of them it could be difficult to be sure that we have found them all unless we proceed systematically. The tree diagram shown in [Figure 3.2 \"Tree Diagram For Three-Child Families\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-f02), gives a systematic approach.

``````{figure} /images/section_07/e9de1d9b1c09ed5a0870567d7e5ad809.jpg
:alt: Statistical diagram: Figure 3.2 Tree Diagram For Three-Child Families
:name: src-fwk-shafer-ch03-s01-s01-f02

Figure 3.2 Tree Diagram For Three-Child Families
``````

The diagram was constructed as follows. There are two possibilities for the first child, boy or girl, so we draw two line segments coming out of a starting point, one ending in a *b* for "boy" and the other ending in a *g* for "girl." For each of these two possibilities for the first child there are two possibilities for the second child, "boy" or "girl," so from each of the *b* and *g* we draw two line segments, one segment ending in a *b* and one in a *g*. For each of the four ending points now in the diagram there are two possibilities for the third child, so we repeat the process once more.

The line segments are called **branches** of the tree. The right ending point of each branch is called a **node**. The nodes on the extreme right are the **final nodes**; to each one there corresponds an outcome, as shown in the figure.

From the tree it is easy to read off the eight outcomes of the experiment, so the sample space is, reading from the top to the bottom of the final nodes in the tree,

$$S = \left\{ {bbb,bbg,bgb,bgg,gbb,gbg,ggb,ggg} \right\}$$

### Probability

````````````{important} Definition

*The* probability of an outcome[^stats-3] *e* *in a sample space* *S* *is a number* *p* *between 0 and 1 that measures the likelihood that* *e* *will occur on a single trial of the corresponding random experiment. The value* *p* = 0 *corresponds to the outcome* *e* *being impossible and the value* *p* = 1 *corresponds to the outcome* *e* *being certain.*

````````````

````````````{important} Definition

*The* probability of an event[^stats-4] *A* *is the sum of the probabilities of the individual outcomes of which it is composed. It is denoted* $P(A).$

````````````

The following formula expresses the content of the definition of the probability of an event:

If an event *E* is $E = \left\{ {e_{1},e_{2},\ldots,e_{k}} \right\}$, then

$$P(E) = P\left( e_{1} \right) + P\left( e_{2} \right) + \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } + P\left( e_{k} \right)$$

[Figure 3.3 \"Sample Spaces and Probability\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s02-f01) graphically illustrates the definitions.

``````{figure} /images/section_07/b1371037e2e863e76e91bc00adf37f63.jpg
:alt: Statistical diagram: Figure 3.3 Sample Spaces and Probability
:name: src-fwk-shafer-ch03-s01-s02-f01

Figure 3.3 Sample Spaces and Probability
``````

Since the whole sample space *S* is an event that is certain to occur, the sum of the probabilities of all the outcomes must be the number 1.

In ordinary language probabilities are frequently expressed as percentages. For example, we would say that there is a 70% chance of rain tomorrow, meaning that the probability of rain is 0.70. We will use this practice here, but in all the computational formulas that follow we will use the form 0.70 and not 70%.

### Example 5

A coin is called "balanced" or "fair" if each side is equally likely to land up. Assign a probability to each outcome in the sample space for the experiment that consists of tossing a single fair coin.

Solution:

With the outcomes labeled *h* for heads and *t* for tails, the sample space is the set $S = \left\{ {h,t} \right\}.$ Since the outcomes have the same probabilities, which must add up to 1, each outcome is assigned probability 1/2.

### Example 6

A die is called "balanced" or "fair" if each side is equally likely to land on top. Assign a probability to each outcome in the sample space for the experiment that consists of tossing a single fair die. Find the probabilities of the events *E*: "an even number is rolled" and *T*: "a number greater than two is rolled."

Solution:

With outcomes labeled according to the number of dots on the top face of the die, the sample space is the set $S = \left\{ 1,2,3,4,5,6 \right\}.$ Since there are six equally likely outcomes, which must add up to 1, each is assigned probability 1/6.

Since $E = \left\{ 2,4,6 \right\}$, $\left. P(E) = 1/ 6 + 1/ 6 + 1/ 6 = 3/ 6 = 1/ 2. \right.$

Since $T = \left\{ 3,4,5,6 \right\}$, $\left. P(T) = 4/ 6 = 2/ 3. \right.$

### Example 7

Two fair coins are tossed. Find the probability that the coins match, i.e., either both land heads or both land tails.

Solution:

In [Note 3.8 \"Example 3\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-n05) we constructed the sample space $S = \left\{ {2h,2t,d} \right\}$ for the situation in which the coins are identical and the sample space $S\prime = \left\{ {hh,ht,th,tt} \right\}$ for the situation in which the two coins can be told apart.

The theory of probability does not tell us *how* to assign probabilities to the outcomes, only what to do with them once they are assigned. Specifically, using sample space *S*, matching coins is the event $M = \left\{ {2h,2t} \right\}$, which has probability $P\left( {2h} \right) + P\left( {2t} \right).$ Using sample space $S\prime$, matching coins is the event $M\prime = \left\{ {hh,tt} \right\}$, which has probability $P\left( {hh} \right) + P\left( {tt} \right).$ In the physical world it should make no difference whether the coins are identical or not, and so we would like to assign probabilities to the outcomes so that the numbers $P(M)$ and $P\left( {M\prime} \right)$ are the same and best match what we observe when actual physical experiments are performed with coins that seem to be fair. Actual experience suggests that the outcomes in $S\prime$ are equally likely, so we assign to each probability 1∕4, and then

$$P\left( {M\prime} \right) = P\left( {hh} \right) + P\left( {tt} \right) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

Similarly, from experience appropriate choices for the outcomes in *S* are:

$$P\left( {2h} \right) = \frac{1}{4}\quad P\left( {2t} \right) = \frac{1}{4}\quad P(d) = \frac{1}{2}$$

which give the same final answer

$$P(M) = P\left( {2h} \right) + P\left( {2t} \right) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

The previous three examples illustrate how probabilities can be computed simply by counting when the sample space consists of a finite number of equally likely outcomes. In some situations the individual outcomes of any sample space that represents the experiment are unavoidably unequally likely, in which case probabilities cannot be computed merely by counting, but the computational formula given in the definition of the probability of an event must be used.

(src-fwk-shafer-ch03-s01-s02-n07)=

### Example 8

The breakdown of the student body in a local high school according to race and ethnicity is 51% white, 27% black, 11% Hispanic, 6% Asian, and 5% for all others. A student is randomly selected from this high school. (To select "randomly" means that every student has the same chance of being selected.) Find the probabilities of the following events:

1.  *B*: the student is black,
2.  *M*: the student is minority (that is, not white),
3.  *N*: the student is not black.

Solution:

The experiment is the action of randomly selecting a student from the student population of the high school. An obvious sample space is $S = \left\{ {w,b,h,a,o} \right\}.$ Since 51% of the students are white and all students have the same chance of being selected, $P(w) = 0.51$, and similarly for the other outcomes. This information is summarized in the following table:

$$\begin{array}{lccccc}
\text{Outcome} & w & b & h & a & o \\
\text{Probability} & 0.51 & 0.27 & 0.11 & 0.06 & 0.05
\end{array}$$

1.  Since $B = \left\{ b \right\}$, $P(B) = P(b) = 0.27.$
2.  Since $M = \left\{ {b,h,a,o} \right\}$, $P(M) = P(b) + P(h) + P(a) + P(o) = 0.27 + 0.11 + 0.06 + 0.05 = 0.49$
3.  Since $N = \left\{ {w,h,a,o} \right\}$, $P(N) = P(w) + P(h) + P(a) + P(o) = 0.51 + 0.11 + 0.06 + 0.05 = 0.73$

### Example 9

The student body in the high school considered in [Note 3.18 \"Example 8\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s02-n07) may be broken down into ten categories as follows: 25% white male, 26% white female, 12% black male, 15% black female, 6% Hispanic male, 5% Hispanic female, 3% Asian male, 3% Asian female, 1% male of other minorities combined, and 4% female of other minorities combined. A student is randomly selected from this high school. Find the probabilities of the following events:

1.  *B*: the student is black,
2.  $MF$: the student is minority female,
3.  $FN$: the student is female and is not black.

Solution:

Now the sample space is $S = \left\{ {wm,bm,hm,am,om,wf,bf,hf,af,of} \right\}.$ The information given in the example can be summarized in the following table, called a *two-way* *contingency table*:

````````{list-table}
:header-rows: 2

- - Gender
  - Race / Ethnicity
  - Race / Ethnicity
  - Race / Ethnicity
  - Race / Ethnicity
  - Race / Ethnicity
- - Gender
  - White
  - Black
  - Hispanic
  - Asian
  - Others
- - Male
  - 0.25
  - 0.12
  - 0.06
  - 0.03
  - 0.01
- - Female
  - 0.26
  - 0.15
  - 0.05
  - 0.03
  - 0.04

````````

1.  Since $B = \left\{ {bm,bf} \right\}$, $P(B) = P\left( {bm} \right) + P\left( {bf} \right) = 0.12 + 0.15 = 0.27.$
2.  Since $MF = \left\{ {bf,hf,af,of} \right\}$, $P(MF) = P\left( {bf} \right) + P\left( {hf} \right) + P\left( {af} \right) + P\left( {of} \right) = 0.15 + 0.05 + 0.03 + 0.04 = 0.27$
3.  Since $FN = \left\{ {wf,hf,af,of} \right\}$, $P\left( {FN} \right) = P\left( {wf} \right) + P\left( {hf} \right) + P\left( {af} \right) + P\left( {of} \right) = 0.26 + 0.05 + 0.03 + 0.04 = 0.38$

````````````{important} Key Takeaways

- The sample space of a random experiment is the collection of all possible outcomes.
- An event associated with a random experiment is a subset of the sample space.
- The probability of any outcome is a number between 0 and 1. The probabilities of all the outcomes add up to 1.
- The probability of any event *A* is the sum of the probabilities of the outcomes in *A*.

````````````

### Exercises

### Basic

1.  A box contains 10 white and 10 black marbles. Construct a sample space for the experiment of randomly drawing out, with replacement, two marbles in succession and noting the color each time. (To draw "with replacement" means that the first marble is put back before the second marble is drawn.)

2.  A box contains 16 white and 16 black marbles. Construct a sample space for the experiment of randomly drawing out, with replacement, three marbles in succession and noting the color each time. (To draw "with replacement" means that each marble is put back before the next marble is drawn.)

3.  A box contains 8 red, 8 yellow, and 8 green marbles. Construct a sample space for the experiment of randomly drawing out, with replacement, two marbles in succession and noting the color each time.

4.  A box contains 6 red, 6 yellow, and 6 green marbles. Construct a sample space for the experiment of randomly drawing out, with replacement, three marbles in succession and noting the color each time.

5.  In the situation of Exercise 1, list the outcomes that comprise each of the following events.

    1.  At least one marble of each color is drawn.
    2.  No white marble is drawn.

6.  In the situation of Exercise 2, list the outcomes that comprise each of the following events.

    1.  At least one marble of each color is drawn.
    2.  No white marble is drawn.
    3.  More black than white marbles are drawn.

7.  In the situation of Exercise 3, list the outcomes that comprise each of the following events.

    1.  No yellow marble is drawn.
    2.  The two marbles drawn have the same color.
    3.  At least one marble of each color is drawn.

8.  In the situation of Exercise 4, list the outcomes that comprise each of the following events.

    1.  No yellow marble is drawn.
    2.  The three marbles drawn have the same color.
    3.  At least one marble of each color is drawn.

9.  Assuming that each outcome is equally likely, find the probability of each event in Exercise 5.

10. Assuming that each outcome is equally likely, find the probability of each event in Exercise 6.

11. Assuming that each outcome is equally likely, find the probability of each event in Exercise 7.

12. Assuming that each outcome is equally likely, find the probability of each event in Exercise 8.

13. A sample space is $S = \left\{ {a,b,c,d,e} \right\}.$ Identify two events as $U = \left\{ {a,b,d} \right\}$ and $V = \left\{ {b,c,d} \right\}.$ Suppose $P(a)$ and $P(b)$ are each 0.2 and $P(c)$ and $P(d)$ are each 0.1.

    1.  Determine what $P(e)$ must be.
    2.  Find $P(U).$
    3.  Find $P(V).$

14. A sample space is $S = \left\{ {u,v,w,x} \right\}.$ Identify two events as $A = \left\{ {v,w} \right\}$ and $B = \left\{ {u,w,x} \right\}.$ Suppose $P(u) = 0.22$, $P(w) = 0.36$, and $P(x) = 0.27.$

    1.  Determine what $P(v)$ must be.
    2.  Find $P(A).$
    3.  Find $P(B).$

15. A sample space is $S = \left\{ {m,n,q,r,s} \right\}.$ Identify two events as $U = \left\{ {m,q,s} \right\}$ and $V = \left\{ {n,q,r} \right\}.$ The probabilities of some of the outcomes are given by the following table:

    $$\begin{array}{lccccc}
    \text{Outcome} & m & n & q & r & s \\
    \text{Probability} & 0.18 & 0.16 & & 0.24 & 0.21
    \end{array}$$

    1.  Determine what $P(q)$ must be.
    2.  Find $P(U).$
    3.  Find $P(V).$

16. A sample space is $S = \left\{ {d,e,f,g,h} \right\}.$ Identify two events as $M = \left\{ {e,f,g,h} \right\}$ and $N = \left\{ {d,g} \right\}.$ The probabilities of some of the outcomes are given by the following table:

    $$\begin{array}{lccccc}
    \text{Outcome} & d & e & f & g & h \\
    \text{Probability} & 0.22 & 0.13 & 0.27 & & 0.19
    \end{array}$$

    1.  Determine what $P(g)$ must be.
    2.  Find $P(M).$
    3.  Find $P(N).$

### Applications

17. The sample space that describes all three-child families according to the genders of the children with respect to birth order was constructed in [Note 3.9 \"Example 4\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-n06). Identify the outcomes that comprise each of the following events in the experiment of selecting a three-child family at random.

    1.  At least one child is a girl.
    2.  At most one child is a girl.
    3.  All of the children are girls.
    4.  Exactly two of the children are girls.
    5.  The first born is a girl.

18. The sample space that describes three tosses of a coin is the same as the one constructed in [Note 3.9 \"Example 4\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s01-s01-n06) with "boy" replaced by "heads" and "girl" replaced by "tails." Identify the outcomes that comprise each of the following events in the experiment of tossing a coin three times.

    1.  The coin lands heads more often than tails.
    2.  The coin lands heads the same number of times as it lands tails.
    3.  The coin lands heads at least twice.
    4.  The coin lands heads on the last toss.

19. Assuming that the outcomes are equally likely, find the probability of each event in Exercise 17.

20. Assuming that the outcomes are equally likely, find the probability of each event in Exercise 18.

### Additional Exercises

21. The following two-way contingency table gives the breakdown of the population in a particular locale according to age and tobacco usage:

    ````````{list-table}
    :header-rows: 2

    - - Age
      - Tobacco Use
      - Tobacco Use
    - - Age
      - Smoker
      - Non-smoker
    - - Under 30
      - 0.05
      - 0.20
    - - Over 30
      - 0.20
      - 0.55

    ````````

    A person is selected at random. Find the probability of each of the following events.

    1.  The person is a smoker.
    2.  The person is under 30.
    3.  The person is a smoker who is under 30.

22. The following two-way contingency table gives the breakdown of the population in a particular locale according to party affiliation (*A*, *B*, *C*, or *None*) and opinion on a bond issue:

    ````````{list-table}
    :header-rows: 2

    - - Affiliation
      - Opinion
      - Opinion
      - Opinion
    - - Affiliation
      - Favors
      - Opposes
      - Undecided
    - - *A*
      - 0.12
      - 0.09
      - 0.07
    - - *B*
      - 0.16
      - 0.12
      - 0.14
    - - *C*
      - 0.04
      - 0.03
      - 0.06
    - - *None*
      - 0.08
      - 0.06
      - 0.03

    ````````

    A person is selected at random. Find the probability of each of the following events.

    1.  The person is affiliated with party *B*.
    2.  The person is affiliated with some party.
    3.  The person is in favor of the bond issue.
    4.  The person has no party affiliation and is undecided about the bond issue.

23. The following two-way contingency table gives the breakdown of the population of married or previously married women beyond child-bearing age in a particular locale according to age at first marriage and number of children:

    ````````{list-table}
    :header-rows: 2

    - - Age
      - Number of Children
      - Number of Children
      - Number of Children
    - - Age
      - 0
      - 1 or 2
      - 3 or More
    - - Under 20
      - 0.02
      - 0.14
      - 0.08
    - - 20--29
      - 0.07
      - 0.37
      - 0.11
    - - 30 and above
      - 0.10
      - 0.10
      - 0.01

    ````````

    A woman is selected at random. Find the probability of each of the following events.

    1.  The woman was in her twenties at her first marriage.
    2.  The woman was 20 or older at her first marriage.
    3.  The woman had no children.
    4.  The woman was in her twenties at her first marriage and had at least three children.

24. The following two-way contingency table gives the breakdown of the population of adults in a particular locale according to highest level of education and whether or not the individual regularly takes dietary supplements:

    ````````{list-table}
    :header-rows: 2

    - - Education
      - Use of Supplements
      - Use of Supplements
    - - Education
      - Takes
      - Does Not Take
    - - No High School Diploma
      - 0.04
      - 0.06
    - - High School Diploma
      - 0.06
      - 0.44
    - - Undergraduate Degree
      - 0.09
      - 0.28
    - - Graduate Degree
      - 0.01
      - 0.02

    ````````

    An adult is selected at random. Find the probability of each of the following events.

    1.  The person has a high school diploma and takes dietary supplements regularly.
    2.  The person has an undergraduate degree and takes dietary supplements regularly.
    3.  The person takes dietary supplements regularly.
    4.  The person does not take dietary supplements regularly.

### Large Data Set Exercises

25. Large Data Sets 4 and 4A record the results of 500 tosses of a coin. Find the relative frequency of each outcome 1, 2, 3, 4, 5, and 6. Does the coin appear to be "balanced" or "fair"?

    <http://www.flatworldknowledge.com/sites/all/files/data4.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data4A.xls>

26. Large Data Sets 6, 6A, and 6B record results of a random survey of 200 voters in each of two regions, in which they were asked to express whether they prefer Candidate *A* for a U.S. Senate seat or prefer some other candidate.

    1.  Find the probability that a randomly selected voter among these 400 prefers Candidate *A*.
    2.  Find the probability that a randomly selected voter among the 200 who live in Region 1 prefers Candidate *A* (separately recorded in Large Data Set 6A).
    3.  Find the probability that a randomly selected voter among the 200 who live in Region 2 prefers Candidate *A* (separately recorded in Large Data Set 6B).

    <http://www.flatworldknowledge.com/sites/all/files/data6.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data6A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data6B.xls>

`````````````{admonition} Answers
:class: dropdown

1.  $S = \left\{ {bb,bw,wb,ww} \right\}$

2. &nbsp;

3.  $S = \left\{ {rr,ry,rg,yr,yy,yg,gr,gy,gg} \right\}$

4. &nbsp;

5.  1.  $\left\{ {bw,wb} \right\}$
    2.  $\left\{ {bb} \right\}$

6. &nbsp;

7.  1.  $\left\{ {rr,rg,gr,gg} \right\}$
    2.  $\left\{ {rr,yy,gg} \right\}$
    3.  ∅

8. &nbsp;

9.  1.  2/4
    2.  1/4

10. &nbsp;

11. 1.  4/9
    2.  3/9
    3.  0

12. &nbsp;

13. 1.  0.4
    2.  0.5
    3.  0.4

14. &nbsp;

15. 1.  0.21
    2.  0.6
    3.  0.61

16. &nbsp;

<!-- -->

17. 1.  $\left\{ {bbg,bgb,bgg,gbb,gbg,ggb,ggg} \right\}$
    2.  $\left\{ {bbb,bbg,bgb,gbb} \right\}$
    3.  $\left\{ {ggg} \right\}$
    4.  $\left\{ {bgg,gbg,ggb} \right\}$
    5.  $\left\{ {gbb,gbg,ggb,ggg} \right\}$
18. &nbsp;
19. 1.  7/8
    2.  4/8
    3.  1/8
    4.  3/8
    5.  4/8
20. &nbsp;

<!-- -->

21. 1.  0.25
    2.  0.25
    3.  0.05
22. &nbsp;
23. 1.  0.55
    2.  0.76
    3.  0.19
    4.  0.11
24. &nbsp;

<!-- -->

25. The relative frequencies for 1 through 6 are 0.16, 0.194, 0.162, 0.164, 0.154 and 0.166. It would appear that the die is not balanced.

26. &nbsp;

`````````````

## 3.2 Complements, Intersections, and Unions

````````````{note} Learning Objectives

1.  To learn how some events are naturally expressible in terms of other events.
2.  To learn how to use special formulas for the probability of an event that is expressed in terms of one or more other events.

````````````

Some events can be naturally expressed in terms of other, sometimes simpler, events.

### Complements

````````````{important} Definition

*The* complement of an event[^stats-5] *A* *in a sample space* *S*, *denoted* *A*<sup>c</sup>, *is the collection of all outcomes in* *S* *that are not elements of the set* *A*. *It corresponds to negating any description in words of the event* *A*.

````````````

### Example 10

Two events connected with the experiment of rolling a single die are *E*: "the number rolled is even" and *T*: "the number rolled is greater than two." Find the complement of each.

Solution:

In the sample space $S = \left\{ 1,2,3,4,5,6 \right\}$ the corresponding sets of outcomes are $E = \left\{ 2,4,6 \right\}$ and $T = \left\{ 3,4,5,6 \right\}.$ The complements are $E^{c} = \left\{ 1,3,5 \right\}$ and $T^{c} = \left\{ 1,2 \right\}.$

In words the complements are described by "the number rolled is not even" and "the number rolled is not greater than two." Of course easier descriptions would be "the number rolled is odd" and "the number rolled is less than three."

If there is a 60% chance of rain tomorrow, what is the probability of fair weather? The obvious answer, 40%, is an instance of the following general rule.

````````````{important} Probability Rule for Complements

$$P\left( A^{c} \right) = 1 - P(A)$$

````````````

This formula is particularly useful when finding the probability of an event directly is difficult.

### Example 11

Find the probability that at least one head will appear in five tosses of a fair coin.

Solution:

Identify outcomes by lists of five *h*s and *t*s, such as $tthtt$ and $hhttt.$ Although it is tedious to list them all, it is not difficult to count them. Think of using a tree diagram to do so. There are two choices for the first toss. For each of these there are two choices for the second toss, hence $2 \times 2 = 4$ outcomes for two tosses. For each of these four outcomes, there are two possibilities for the third toss, hence $4 \times 2 = 8$ outcomes for three tosses. Similarly, there are $8 \times 2 = 16$ outcomes for four tosses and finally $16 \times 2 = 32$ outcomes for five tosses.

Let *O* denote the event "at least one head." There are many ways to obtain at least one head, but only one way to fail to do so: all tails. Thus although it is difficult to list all the outcomes that form *O*, it is easy to write $O^{c} = \left\{ {ttttt} \right\}.$ Since there are 32 equally likely outcomes, each has probability 1/32, so $\left. P\left( O^{c} \right) = 1/ 32 \right.$, hence $\left. P(O) = 1 - 1/ 32 \approx 0.97 \right.$ or about a 97% chance.

### Intersection of Events

````````````{important} Definition

*The* intersection of events[^stats-6] *A* *and* *B*, *denoted* *A* ∩ *B*, *is the collection of all outcomes that are elements of both of the sets* *A* *and* *B*. *It corresponds to combining descriptions of the two events using the word "and."*

````````````

To say that the event *A* ∩ *B* occurred means that on a particular trial of the experiment both *A* and *B* occurred. A visual representation of the intersection of events *A* and *B* in a sample space *S* is given in [Figure 3.4 \"The Intersection of Events \"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s02-s02-f01). The intersection corresponds to the shaded lens-shaped region that lies within both ovals.

``````{figure} /images/section_07/c839ee4bf3bb6c5efce796861aee5142.jpg
:alt: Statistical diagram: Figure 3.4 The Intersection of Events A and B
:name: src-fwk-shafer-ch03-s02-s02-f01

Figure 3.4 The Intersection of Events *A* and *B*
``````

### Example 12

In the experiment of rolling a single die, find the intersection *E* ∩ *T* of the events *E*: "the number rolled is even" and *T*: "the number rolled is greater than two."

Solution:

The sample space is $S = \left\{ 1,2,3,4,5,6 \right\}.$ Since the outcomes that are common to $E = \left\{ 2,4,6 \right\}$ and $T = \left\{ 3,4,5,6 \right\}$ are 4 and 6, $E \cap T = \left\{ 4,6 \right\}.$

In words the intersection is described by "the number rolled is even and is greater than two." The only numbers between one and six that are both even and greater than two are four and six, corresponding to *E* ∩ *T* given above.

### Example 13

A single die is rolled.

1.  Suppose the die is fair. Find the probability that the number rolled is both even and greater than two.
2.  Suppose the die has been "loaded" so that $\left. P(1) = 1/ 12 \right.$, $\left. P(6) = 3/ 12 \right.$, and the remaining four outcomes are equally likely with one another. Now find the probability that the number rolled is both even and greater than two.

Solution:

In both cases the sample space is $S = \left\{ 1,2,3,4,5,6 \right\}$ and the event in question is the intersection $E \cap T = \left\{ 4,6 \right\}$ of the previous example.

1.  Since the die is fair, all outcomes are equally likely, so by counting we have $\left. P\left( {E \cap T} \right) = 2/ 6. \right.$

2.  The information on the probabilities of the six outcomes that we have so far is

    $$\begin{array}{lcccccc}
    \text{Outcome} & 1 & 2 & 3 & 4 & 5 & 6 \\
    \text{Probability} & \frac{1}{12} & p & p & p & p & \frac{3}{12}
    \end{array}$$

Since $\left. P(1) + P(6) = 4/ 12 = 1/ 3 \right.$ and the probabilities of all six outcomes add up to 1,

$$P(2) + P(3) + P(4) + P(5) = 1 - \frac{1}{3} = \frac{2}{3}$$

Thus $\left. 4p = 2/ 3 \right.$, so $\left. p = 1/ 6. \right.$ In particular $\left. P(4) = 1/ 6. \right.$ Therefore

$$P\left( {E \cap T} \right) = P(4) + P(6) = \frac{1}{6} + \frac{3}{12} = \frac{5}{12}$$

````````````{important} Definition

*Events* *A* *and* *B* *are* mutually exclusive[^stats-7] *if they have no elements in common.*

````````````

For *A* and *B* to have no outcomes in common means precisely that it is impossible for both *A* and *B* to occur on a single trial of the random experiment. This gives the following rule.

````````````{important} Probability Rule for Mutually Exclusive Events

Events *A* and *B* are mutually exclusive if and only if

$$P\left( {A \cap B} \right) = 0$$

````````````

Any event *A* and its complement *A*<sup>c</sup> are mutually exclusive, but *A* and *B* can be mutually exclusive without being complements.

### Example 14

In the experiment of rolling a single die, find three choices for an event *A* so that the events *A* and *E*: "the number rolled is even" are mutually exclusive.

Solution:

Since $E = \left\{ 2,4,6 \right\}$ and we want *A* to have no elements in common with *E*, any event that does not contain any even number will do. Three choices are {1,3,5} (the complement *E*<sup>c</sup>, the odds), {1,3}, and {5}.

### Union of Events

````````````{important} Definition

*The* union of events[^stats-8] *A* *and* *B*, *denoted* *A* ∪ *B*, *is the collection of all outcomes that are elements of one or the other of the sets* *A* *and* *B*, *or of both of them. It corresponds to combining descriptions of the two events using the word "or."*

````````````

To say that the event *A* ∪ *B* occurred means that on a particular trial of the experiment either *A* or *B* occurred (or both did). A visual representation of the union of events *A* and *B* in a sample space *S* is given in [Figure 3.5 \"The Union of Events \"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s02-s03-f01). The union corresponds to the shaded region.

``````{figure} /images/section_07/2b9ac417d3f9501644f5bcc1cfdd8ebb.jpg
:alt: Statistical diagram: Figure 3.5 The Union of Events A and B
:name: src-fwk-shafer-ch03-s02-s03-f01

Figure 3.5 The Union of Events *A* and *B*
``````

### Example 15

In the experiment of rolling a single die, find the union of the events *E*: "the number rolled is even" and *T*: "the number rolled is greater than two."

Solution:

Since the outcomes that are in either $E = \left\{ 2,4,6 \right\}$ or $T = \left\{ 3,4,5,6 \right\}$ (or both) are 2, 3, 4, 5, and 6, $E \cup T = \left\{ 2,3,4,5,6 \right\}.$ Note that an outcome such as 4 that is in both sets is still listed only once (although strictly speaking it is not incorrect to list it twice).

In words the union is described by "the number rolled is even or is greater than two." Every number between one and six except the number one is either even or is greater than two, corresponding to *E* ∪ *T* given above.

### Example 16

A two-child family is selected at random. Let *B* denote the event that at least one child is a boy, let *D* denote the event that the genders of the two children differ, and let *M* denote the event that the genders of the two children match. Find *B* ∪ *D* and $B \cup M.$

Solution:

A sample space for this experiment is $S = \left\{ {bb,bg,gb,gg} \right\}$, where the first letter denotes the gender of the firstborn child and the second letter denotes the gender of the second child. The events *B*, *D*, and *M* are

$$B = \left\{ {bb,bg,gb} \right\}\quad D = \left\{ {bg,gb} \right\}\quad M = \left\{ {bb,gg} \right\}$$

Each outcome in *D* is already in *B*, so the outcomes that are in at least one or the other of the sets *B* and *D* is just the set *B* itself: $B \cup D = \left\{ {bb,bg,gb} \right\} = B.$

Every outcome in the whole sample space *S* is in at least one or the other of the sets *B* and *M*, so $B \cup M = \left\{ {bb,bg,gb,gg} \right\} = S.$

The following **Additive Rule of Probability** is a useful formula for calculating the probability of $A \cup B.$

````````````{important} Additive Rule of Probability

$$P\left( {A \cup B} \right) = P(A) + P(B) - P\left( {A \cap B} \right)$$

````````````

The next example, in which we compute the probability of a union both by counting and by using the formula, shows why the last term in the formula is needed.

### Example 17

Two fair dice are thrown. Find the probabilities of the following events:

1.  both dice show a four
2.  at least one die shows a four

Solution:

As was the case with tossing two identical coins, actual experience dictates that for the sample space to have equally likely outcomes we should list outcomes as if we could distinguish the two dice. We could imagine that one of them is red and the other is green. Then any outcome can be labeled as a pair of numbers as in the following display, where the first number in the pair is the number of dots on the top face of the green die and the second number in the pair is the number of dots on the top face of the red die.

$$\begin{matrix}
11 & 12 & 13 & 14 & 15 & 16 \\
21 & 22 & 23 & 24 & 25 & 26 \\
31 & 32 & 33 & 34 & 35 & 36 \\
41 & 42 & 43 & 44 & 45 & 46 \\
51 & 52 & 53 & 54 & 55 & 56 \\
61 & 62 & 63 & 64 & 65 & 66
\end{matrix}$$

1.  There are 36 equally likely outcomes, of which exactly one corresponds to two fours, so the probability of a pair of fours is 1/36.

2.  From the table we can see that there are 11 pairs that correspond to the event in question: the six pairs in the fourth row (the green die shows a four) plus the additional five pairs other than the pair 44, already counted, in the fourth column (the red die is four), so the answer is 11/36. To see how the formula gives the same number, let *A<sub>G</sub>* denote the event that the green die is a four and let *A<sub>R</sub>* denote the event that the red die is a four. Then clearly by counting we get $\left. P\left( A_{G} \right) = 6/ 36 \right.$ and $\left. P\left( A_{R} \right) = 6/ 36. \right.$ Since $A_{G} \cap A_{R} = \left\{ 44 \right\}$, $\left. P\left( {A_{G} \cap A_{R}} \right) = 1/ 36 \right.$; this is the computation in part (a), of course. Thus by the Additive Rule of Probability,

    $$P(A_{G} \cup A_{R}) = P(A_{G}) + P(A_{R}) - P(A_{G} - A_{R}) = \frac{6}{36} + \frac{6}{36} - \frac{1}{36} = \frac{11}{36}$$

### Example 18

A tutoring service specializes in preparing adults for high school equivalence tests. Among all the students seeking help from the service, 63% need help in mathematics, 34% need help in English, and 27% need help in both mathematics and English. What is the percentage of students who need help in either mathematics or English?

Solution:

Imagine selecting a student at random, that is, in such a way that every student has the same chance of being selected. Let *M* denote the event "the student needs help in mathematics" and let *E* denote the event "the student needs help in English." The information given is that $P(M) = 0.63$, $P(E) = 0.34$, and $P\left( {M \cap E} \right) = 0.27.$ The Additive Rule of Probability gives

$$P\left( {M \cup E} \right) = P(M) + P(E) - P\left( {M \cap E} \right) = 0.63 + 0.34 - 0.27 = 0.70$$

Note how the naïve reasoning that if 63% need help in mathematics and 34% need help in English then 63 plus 34 or 97% need help in one or the other gives a number that is too large. The percentage that need help in both subjects must be subtracted off, else the people needing help in both are counted twice, once for needing help in mathematics and once again for needing help in English. The simple sum of the probabilities would work if the events in question were mutually exclusive, for then $P\left( {A \cap B} \right)$ is zero, and makes no difference.

### Example 19

Volunteers for a disaster relief effort were classified according to both specialty (*C*: construction, *E*: education, *M*: medicine) and language ability (*S*: speaks a single language fluently, *T*: speaks two or more languages fluently). The results are shown in the following *two-way classification* *table*:

````````{list-table}
:header-rows: 2

- - Specialty
  - Language Ability
  - Language Ability
- - Specialty
  - *S*
  - *T*
- - *C*
  - 12
  - 1
- - *E*
  - 4
  - 3
- - *M*
  - 6
  - 2

````````

The first row of numbers means that 12 volunteers whose specialty is construction speak a single language fluently, and 1 volunteer whose specialty is construction speaks at least two languages fluently. Similarly for the other two rows.

A volunteer is selected at random, meaning that each one has an equal chance of being chosen. Find the probability that:

1.  his specialty is medicine and he speaks two or more languages;
2.  either his specialty is medicine or he speaks two or more languages;
3.  his specialty is something other than medicine.

Solution:

When information is presented in a two-way classification table it is typically convenient to adjoin to the table the row and column totals, to produce a new table like this:

````````{list-table}
:header-rows: 2

- - Specialty
  - Language Ability
  - Language Ability
  - Total
- - Specialty
  - *S*
  - *T*
  - Total
- - *C*
  - 12
  - 1
  - 13
- - *E*
  - 4
  - 3
  - 7
- - *M*
  - 6
  - 2
  - 8
- - Total
  - 22
  - 6
  - 28

````````

1.  The probability sought is $P\left( {M \cap T} \right).$ The table shows that there are 2 such people, out of 28 in all, hence $\left. P\left( {M \cap T} \right) = 2/ 28 \approx 0.07 \right.$ or about a 7% chance.

2.  The probability sought is $P\left( {M \cup T} \right).$ The third row total and the grand total in the sample give $\left. P(M) = 8/ 28. \right.$ The second column total and the grand total give $\left. P(T) = 6/ 28. \right.$ Thus using the result from part (a),

    $$P\left( {M \cup T} \right) = P(M) + P(T) - P\left( {M \cap T} \right) = \frac{8}{28} + \frac{6}{28} - \frac{2}{28} = \frac{12}{28} \approx 0.43$$

    or about a 43% chance.

3.  This probability can be computed in two ways. Since the event of interest can be viewed as the event *C* ∪ *E* and the events *C* and *E* are mutually exclusive, the answer is, using the first two row totals,

    $$P\left( {C \cup E} \right) = P(C) + P(E) - P\left( {C \cap E} \right) = \frac{13}{28} + \frac{7}{28} - \frac{0}{28} = \frac{20}{28} \approx 0.71$$

    On the other hand, the event of interest can be thought of as the complement *M*<sup>c</sup> of *M*, hence using the value of $P(M)$ computed in part (b),

    $$P\left( M^{c} \right) = 1 - P(M) = 1 - \frac{8}{28} = \frac{20}{28} \approx 0.71$$

    as before.

````````````{important} Key Takeaway

- The probability of an event that is a complement or union of events of known probability can be computed using formulas.

````````````

### Exercises

### Basic

1.  For the sample space $S = \left\{ {a,b,c,d,e} \right\}$ identify the complement of each event given.

    1.  $A = \left\{ {a,d,e} \right\}$
    2.  $B = \left\{ {b,c,d,e} \right\}$
    3.  *S*

2.  For the sample space $S = \left\{ {r,s,t,u,v} \right\}$ identify the complement of each event given.

    1.  $R = \left\{ {t,u} \right\}$
    2.  $T = \left\{ r \right\}$
    3.  ∅ (the "empty" set that has no elements)

3.  The sample space for three tosses of a coin is

    $$S = \left\{ {hhh,hht,hth,htt,thh,tht,tth,ttt} \right\}$$

    Define events

    $$\begin{array}{l}
    {H:\text{at least one head is observed}} \\
    {M:\text{more heads than tails are observed}}
    \end{array}$$

    1.  List the outcomes that comprise *H* and *M*.
    2.  List the outcomes that comprise *H* ∩ *M*, *H* ∪ *M*, and *H*<sup>c</sup>.
    3.  Assuming all outcomes are equally likely, find $P\left( {H \cap M} \right)$, $P\left( {H \cup M} \right)$, and $P\left( H^{c} \right).$
    4.  Determine whether or not *H*<sup>c</sup> and *M* are mutually exclusive. Explain why or why not.

4.  For the experiment of rolling a single six-sided die once, define events

    $$\begin{array}{l}
    {T:\text{the number rolled is three}} \\
    {G:\text{the number rolled is four or greater}}
    \end{array}$$

    1.  List the outcomes that comprise *T* and *G*.
    2.  List the outcomes that comprise *T* ∩ *G*, *T* ∪ *G*, *T*<sup>c</sup>, and $\left( {T \cup G} \right)^{c}.$
    3.  Assuming all outcomes are equally likely, find $P\left( {T \cap G} \right)$, $P\left( {T \cup G} \right)$, and $P\left( T^{c} \right).$
    4.  Determine whether or not *T* and *G* are mutually exclusive. Explain why or why not.

5.  A special deck of 16 cards has 4 that are blue, 4 yellow, 4 green, and 4 red. The four cards of each color are numbered from one to four. A single card is drawn at random. Define events

    $$\begin{array}{l}
    {B:\text{the card is blue}} \\
    {R:\text{the card is red}} \\
    {N:\text{the number on the card is at most two}}
    \end{array}$$

    1.  List the outcomes that comprise *B*, *R*, and *N*.
    2.  List the outcomes that comprise *B* ∩ *R*, *B* ∪ *R*, *B* ∩ *N*, *R* ∪ *N*, *B*<sup>c</sup>, and $\left( {B \cup R} \right)^{c}.$
    3.  Assuming all outcomes are equally likely, find the probabilities of the events in the previous part.
    4.  Determine whether or not *B* and *N* are mutually exclusive. Explain why or why not.

6.  In the context of the previous problem, define events

    $$\begin{array}{l}
    {Y:\text{the card is yellow}} \\
    {I:\text{the number on the card is not a one}} \\
    {J:\text{the number on the card is a two or a four}}
    \end{array}$$

    1.  List the outcomes that comprise *Y*, *I*, and *J*.
    2.  List the outcomes that comprise *Y* ∩ *I*, *Y* ∪ *J*, *I* ∩ *J*, *I*<sup>c</sup>, and $\left( {Y \cup J} \right)^{c}.$
    3.  Assuming all outcomes are equally likely, find the probabilities of the events in the previous part.
    4.  Determine whether or not *I*<sup>c</sup> and *J* are mutually exclusive. Explain why or why not.

7.  The Venn diagram provided shows a sample space and two events *A* and *B*. Suppose $P(a) = 0.13$, $P(b) = 0.09$, $P(c) = 0.27$, $P(d) = 0.20$, and $P(e) = 0.31.$ Confirm that the probabilities of the outcomes add up to 1, then compute the following probabilities.

    ``````{figure} /images/section_07/3ba777e453d1118c377ee69b788d0a74.jpg
    :alt: Statistical diagram: The Venn diagram provided shows a sample space and two events A and B . Suppose P ( a ) = 0.13 , P ( b ) = 0.09 , P ( c ) = 0.27 , P ( d ) = 0.20 , and P ( e ) = 0.31 . Confirm that the probabilities of the outcomes add up to 1, then compute the following probabilities.
    :name: src-fwk-shafer-ch03-s02-qs01-fx02


    ``````



    1.  $P(A).$
    2.  $P(B).$
    3.  $P\left( A^{c} \right)$ two ways: (i) by finding the outcomes in *A*<sup>c</sup> and adding their probabilities, and (ii) using the Probability Rule for Complements.
    4.  $P\left( {A \cap B} \right).$
    5.  $P\left( {A \cup B} \right)$ two ways: (i) by finding the outcomes in *A* ∪ *B* and adding their probabilities, and (ii) using the Additive Rule of Probability.

8.  The Venn diagram provided shows a sample space and two events *A* and *B*. Suppose $P(a) = 0.32$, $P(b) = 0.17$, $P(c) = 0.28$, and $P(d) = 0.23.$ Confirm that the probabilities of the outcomes add up to 1, then compute the following probabilities.

    ``````{figure} /images/section_07/cd8dc002db8c5f132bed316a3634ec00.jpg
    :alt: Statistical diagram: The Venn diagram provided shows a sample space and two events A and B . Suppose P ( a ) = 0.32 , P ( b ) = 0.17 , P ( c ) = 0.28 , and P ( d ) = 0.23 . Confirm that the probabilities of the outcomes add up to 1, then compute the following probabilities.
    :name: src-fwk-shafer-ch03-s02-qs01-fx01


    ``````



    1.  $P(A).$
    2.  $P(B).$
    3.  $P\left( A^{c} \right)$ two ways: (i) by finding the outcomes in *A*<sup>c</sup> and adding their probabilities, and (ii) using the Probability Rule for Complements.
    4.  $P\left( {A \cap B} \right).$
    5.  $P\left( {A \cup B} \right)$ two ways: (i) by finding the outcomes in *A* ∪ *B* and adding their probabilities, and (ii) using the Additive Rule of Probability.

9.  Confirm that the probabilities in the two-way contingency table add up to 1, then use it to find the probabilities of the events indicated.

    ````````{list-table}
    :header-rows: 1

    - -
      - *U*
      - *V*
      - *W*
    - - *A*
      - 0.15
      - 0.00
      - 0.23
    - - *B*
      - 0.22
      - 0.30
      - 0.10

    ````````

    1.  $P(A)$, $P(B)$, $P\left( {A \cap B} \right).$
    2.  $P(U)$, $P(W)$, $P\left( {U \cap W} \right).$
    3.  $P\left( {U \cup W} \right).$
    4.  $P\left( V^{c} \right).$
    5.  Determine whether or not the events *A* and *U* are mutually exclusive; the events *A* and *V*.

10. Confirm that the probabilities in the two-way contingency table add up to 1, then use it to find the probabilities of the events indicated.

    ````````{list-table}
    :header-rows: 1

    - -
      - *R*
      - *S*
      - *T*
    - - *M*
      - 0.09
      - 0.25
      - 0.19
    - - *N*
      - 0.31
      - 0.16
      - 0.00

    ````````

    1.  $P(R)$, $P(S)$, $P\left( {R \cap S} \right).$
    2.  $P(M)$, $P(N)$, $P\left( {M \cap N} \right).$
    3.  $P\left( {R \cup S} \right).$
    4.  $P\left( R^{c} \right).$
    5.  Determine whether or not the events *N* and *S* are mutually exclusive; the events *N* and *T*.

### Applications

11. Make a statement in ordinary English that describes the complement of each event (do not simply insert the word "not").

    1.  In the roll of a die: "five or more."
    2.  In a roll of a die: "an even number."
    3.  In two tosses of a coin: "at least one head."
    4.  In the random selection of a college student: "Not a freshman."

12. Make a statement in ordinary English that describes the complement of each event (do not simply insert the word "not").

    1.  In the roll of a die: "two or less."
    2.  In the roll of a die: "one, three, or four."
    3.  In two tosses of a coin: "at most one head."
    4.  In the random selection of a college student: "Neither a freshman nor a senior."

13. The sample space that describes all three-child families according to the genders of the children with respect to birth order is

    $$S = \left\{ {bbb,bbg,bgb,bgg,gbb,gbg,ggb,ggg} \right\}.$$

    For each of the following events in the experiment of selecting a three-child family at random, state the complement of the event in the simplest possible terms, then find the outcomes that comprise the event and its complement.

    1.  At least one child is a girl.
    2.  At most one child is a girl.
    3.  All of the children are girls.
    4.  Exactly two of the children are girls.
    5.  The first born is a girl.

14. The sample space that describes the two-way classification of citizens according to gender and opinion on a political issue is

    $$S = \left\{ {mf,ma,mn,ff,fa,fn} \right\},$$

    where the first letter denotes gender (*m*: male, *f*: female) and the second opinion (*f*: for, *a*: against, *n*: neutral). For each of the following events in the experiment of selecting a citizen at random, state the complement of the event in the simplest possible terms, then find the outcomes that comprise the event and its complement.

    1.  The person is male.
    2.  The person is not in favor.
    3.  The person is either male or in favor.
    4.  The person is female and neutral.

15. A tourist who speaks English and German but no other language visits a region of Slovenia. If 35% of the residents speak English, 15% speak German, and 3% speak both English and German, what is the probability that the tourist will be able to talk with a randomly encountered resident of the region?

16. In a certain country 43% of all automobiles have airbags, 27% have anti-lock brakes, and 13% have both. What is the probability that a randomly selected vehicle will have both airbags and anti-lock brakes?

17. A manufacturer examines its records over the last year on a component part received from outside suppliers. The breakdown on source (supplier *A*, supplier *B*) and quality (*H*: high, *U*: usable, *D*: defective) is shown in the two-way contingency table.

    ````````{list-table}
    :header-rows: 1

    - -
      - *H*
      - *U*
      - *D*
    - - *A*
      - 0.6937
      - 0.0049
      - 0.0014
    - - *B*
      - 0.2982
      - 0.0009
      - 0.0009

    ````````

    The record of a part is selected at random. Find the probability of each of the following events.

    1.  The part was defective.
    2.  The part was either of high quality or was at least usable, in two ways: (i) by adding numbers in the table, and (ii) using the answer to (a) and the Probability Rule for Complements.
    3.  The part was defective and came from supplier *B*.
    4.  The part was defective or came from supplier *B*, in two ways: by finding the cells in the table that correspond to this event and adding their probabilities, and (ii) using the Additive Rule of Probability.

18. Individuals with a particular medical condition were classified according to the presence (*T*) or absence (*N*) of a potential toxin in their blood and the onset of the condition (*E*: early, *M*: midrange, *L*: late). The breakdown according to this classification is shown in the two-way contingency table.

    ````````{list-table}
    :header-rows: 1

    - -
      - *E*
      - *M*
      - *L*
    - - *T*
      - 0.012
      - 0.124
      - 0.013
    - - *N*
      - 0.170
      - 0.638
      - 0.043

    ````````

    One of these individuals is selected at random. Find the probability of each of the following events.

    1.  The person experienced early onset of the condition.
    2.  The onset of the condition was either midrange or late, in two ways: (i) by adding numbers in the table, and (ii) using the answer to (a) and the Probability Rule for Complements.
    3.  The toxin is present in the person's blood.
    4.  The person experienced early onset of the condition and the toxin is present in the person's blood.
    5.  The person experienced early onset of the condition or the toxin is present in the person's blood, in two ways: (i) by finding the cells in the table that correspond to this event and adding their probabilities, and (ii) using the Additive Rule of Probability.

19. The breakdown of the students enrolled in a university course by class (*F*: freshman, $So$: sophomore, *J*: junior, $Se$: senior) and academic major (*S*: science, mathematics, or engineering, *L*: liberal arts, *O*: other) is shown in the two-way classification table.

    ````````{list-table}
    :header-rows: 2

    - - Major
      - Class
      - Class
      - Class
      - Class
    - - Major
      - *F*
      - *So*
      - *J*
      - *Se*
    - - *S*
      - 92
      - 42
      - 20
      - 13
    - - *L*
      - 368
      - 167
      - 80
      - 53
    - - *O*
      - 460
      - 209
      - 100
      - 67

    ````````

    A student enrolled in the course is selected at random. Adjoin the row and column totals to the table and use the expanded table to find the probability of each of the following events.

    1.  The student is a freshman.
    2.  The student is a liberal arts major.
    3.  The student is a freshman liberal arts major.
    4.  The student is either a freshman or a liberal arts major.
    5.  The student is not a liberal arts major.

20. The table relates the response to a fund-raising appeal by a college to its alumni to the number of years since graduation.

    ````````{list-table}
    :header-rows: 2

    - - Response
      - Years Since Graduation
      - Years Since Graduation
      - Years Since Graduation
      - Years Since Graduation
    - - Response
      - 0--5
      - 6--20
      - 21--35
      - Over 35
    - - Positive
      - 120
      - 440
      - 210
      - 90
    - - None
      - 1380
      - 3560
      - 3290
      - 910

    ````````

    An alumnus is selected at random. Adjoin the row and column totals to the table and use the expanded table to find the probability of each of the following events.

    1.  The alumnus responded.
    2.  The alumnus did not respond.
    3.  The alumnus graduated at least 21 years ago.
    4.  The alumnus graduated at least 21 years ago and responded.

### Additional Exercises

21. The sample space for tossing three coins is

    $$S = \left\{ {hhh,hht,hth,htt,thh,tht,tth,ttt} \right\}$$

    1.  List the outcomes that correspond to the statement "All the coins are heads."
    2.  List the outcomes that correspond to the statement "Not all the coins are heads."
    3.  List the outcomes that correspond to the statement "All the coins are not heads."

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\left\{ {b,c} \right\}$
    2.  $\left\{ a \right\}$
    3.  ∅
2. &nbsp;
3.  1.  $H = \left\{ {hhh,hht,hth,htt,thh,tht,tth} \right\}$, $M = \left\{ {hhh,hht,hth,thh} \right\}$
    2.  $H \cap M = \left\{ {hhh,hht,hth,thh} \right\}$, $H \cup M = H$, $H^{c} = \left\{ {ttt} \right\}$
    3.  $\left. P\left( {H \cap M} \right) = 4/ 8 \right.$, $\left. P\left( {H \cup M} \right) = 7/ 8 \right.$, $\left. P\left( H^{c} \right) = 1/ 8 \right.$
    4.  Mutually exclusive because they have no elements in common.
4. &nbsp;
5.  1.  $B = \left\{ {b1,b2,b3,b4} \right\}$, $R = \left\{ {r1,r2,r3,r4} \right\}$, $N = \left\{ {b1,b2,y1,y2,g1,g2,r1,r2} \right\}$
    2.  $B \cap R = \varnothing$, $B \cup R = \left\{ {b1,b2,b3,b4,r1,r2,r3,r4} \right\},$ $B \cap N = \left\{ {b1,b2} \right\}$, $R \cup N = \left\{ {b1,b2,y1,y2,g1,g2,r1,r2,r3,r4} \right\},$ $B^{c} = \left\{ {y1,y2,y3,y4,g1,g2,g3,g4,r1,r2,r3,r4} \right\},$ $\left( {B \cup R} \right)^{c} = \left\{ {y1,y2,y3,y4,g1,g2,g3,g4} \right\}$
    3.  $P\left( {B \cap R} \right) = 0$, $\left. P\left( {B \cup R} \right) = 8/ 16 \right.$, $\left. P\left( {B \cap N} \right) = 2/ 16 \right.$, $\left. P\left( {R \cup N} \right) = 10/ 16 \right.$, $\left. P\left( B^{c} \right) = 12/ 16 \right.$, $\left. P\left( \left( {B \cup R} \right)^{c} \right) = 8/ 16 \right.$
    4.  Not mutually exclusive because they have an element in common.
6. &nbsp;
7.  1.  0.36
    2.  0.78
    3.  0.64
    4.  0.27
    5.  0.87
8. &nbsp;
9.  1.  $P(A) = 0.38$, $P(B) = 0.62$, $P\left( {A \cap B} \right) = 0$
    2.  $P(U) = 0.37$, $P(W) = 0.33$, $P\left( {U \cap W} \right) = 0$
    3.  0.7
    4.  0.7
    5.  *A* and *U* are not mutually exclusive because $P\left( {A \cap U} \right)$ is the nonzero number 0.15. *A* and *V* are mutually exclusive because $P\left( {A \cap V} \right) = 0.$
10. &nbsp;

<!-- -->

11. 1.  "four or less"
    2.  "an odd number"
    3.  "no heads" or "all tails"
    4.  "a freshman"

12. &nbsp;

13. 1.  "All the children are boys."

        Event: $\left\{ {bbg,bgb,bgg,gbb,gbg,ggb,ggg} \right\}$,

        Complement: $\left\{ {bbb} \right\}$

    2.  "At least two of the children are girls" or "There are two or three girls."

        Event: $\left\{ {bbb,bbg,bgb,gbb} \right\}$,

        Complement: $\left\{ {bgg,gbg,ggb,ggg} \right\}$

    3.  "At least one child is a boy."

        Event: $\left\{ {ggg} \right\}$,

        Complement: $\left\{ {bbb,bbg,bgb,bgg,gbb,gbg,ggb} \right\}$

    4.  "There are either no girls, exactly one girl, or three girls."

        Event: $\left\{ {bgg,gbg,ggb} \right\}$,

        Complement: $\left\{ {bbb,bbg,bgb,gbb,ggg} \right\}$

    5.  "The first born is a boy."

        Event: $\left\{ {gbb,gbg,ggb,ggg} \right\}$,

        Complement: $\left\{ {bbb,bbg,bgb,bgg} \right\}$

14. &nbsp;

15. 0.47

16. &nbsp;

17. 1.  0.0023
    2.  0.9977
    3.  0.0009
    4.  0.3014

18. &nbsp;

19. 1.  920/1671
    2.  668/1671
    3.  368/1671
    4.  1220/1671
    5.  1003/1671

20. &nbsp;

<!-- -->

21. 1.  $\left\{ {hhh} \right\}$
    2.  $\left\{ {hht,hth,htt,thh,tht,tth,ttt} \right\}$
    3.  $\left\{ {ttt} \right\}$

`````````````

## 3.3 Conditional Probability and Independent Events

````````````{note} Learning Objectives

1.  To learn the concept of a conditional probability and how to compute it.
2.  To learn the concept of independence of events, and how to apply it.

````````````

### Conditional Probability

Suppose a fair die has been rolled and you are asked to give the probability that it was a five. There are six equally likely outcomes, so your answer is 1/6. But suppose that before you give your answer you are given the extra information that the number rolled was odd. Since there are only three odd numbers that are possible, one of which is five, you would certainly revise your estimate of the likelihood that a five was rolled from 1/6 to 1/3. In general, the *revised* probability that an event *A* has occurred, taking into account the additional information that another event *B* has definitely occurred on this trial of the experiment, is called the *conditional probability of* *A* *given* *B* and is denoted by $P\left( A \middle| B \right).$ The reasoning employed in this example can be generalized to yield the computational formula in the following definition.

````````````{important} Definition

*The* conditional probability[^stats-9] **of** *A* **given** *B*, *denoted* $P\left( A \middle| B \right)$, *is the probability that event* *A* *has occurred in a trial of a random experiment for which it is known that event* *B* *has definitely occurred. It may be computed by means of the following formula:*

Rule for Conditional Probability

$$P\left( A \middle| B \right) = \frac{P\left( {A \cap B} \right)}{P(B)}$$

````````````

### Example 20

A fair die is rolled.

1.  Find the probability that the number rolled is a five, given that it is odd.
2.  Find the probability that the number rolled is odd, given that it is a five.

Solution:

The sample space for this experiment is the set $S = \left\{ 1,2,3,4,5,6 \right\}$ consisting of six equally likely outcomes. Let *F* denote the event "a five is rolled" and let *O* denote the event "an odd number is rolled," so that

$$F = \left\{ 5 \right\}\quad\text{and}\quad O = \left\{ 1,3,5 \right\}$$

1.  This is the introductory example, so we already know that the answer is 1/3. To use the formula in the definition to confirm this we must replace *A* in the formula (the event whose likelihood we seek to estimate) by *F* and replace *B* (the event we know for certain has occurred) by *O*:

    $$P\left( F \middle| O \right) = \frac{P\left( {F \cap O} \right)}{P(O)}$$

    Since $F \cap O = \left\{ 5 \right\} \cap \left\{ 1,3,5 \right\} = \left\{ 5 \right\}$, $\left. P\left( {F \cap O} \right) = 1/ 6. \right.$

    Since $O = \left\{ 1,3,5 \right\}$, $\left. P(O) = 3/ 6. \right.$

    Thus

    $$P\left( F \middle| O \right) = \frac{P\left( {F \cap O} \right)}{P(O)} = \frac{\left. 1/ 6 \right.}{\left. 3/ 6 \right.} = \frac{1}{3}$$

2.  This is the same problem, but with the roles of *F* and *O* reversed. Since we are given that the number that was rolled is five, which is odd, the probability in question must be 1. To apply the formula to this case we must now replace *A* (the event whose likelihood we seek to estimate) by *O* and *B* (the event we know for certain has occurred) by *F*:

    $$P\left( O \middle| F \right) = \frac{P\left( {O \cap F} \right)}{P(F)}$$

    Obviously $\left. P(F) = 1/ 6. \right.$ In part (a) we found that $\left. P\left( {F \cap O} \right) = 1/ 6. \right.$ Thus

    $$P\left( O \middle| F \right) = \frac{P\left( {O \cap F} \right)}{P(F)} = \frac{\left. 1/ 6 \right.}{\left. 1/ 6 \right.} = 1$$

Just as we did not need the computational formula in this example, we do not need it when the information is presented in a two-way classification table, as in the next example.

(src-fwk-shafer-ch03-s03-s01-n04)=

### Example 21

In a sample of 902 individuals under 40 who were or had previously been married, each person was classified according to gender and age at first marriage. The results are summarized in the following two-way classification table, where the meaning of the labels is:

- *M*: male
- *F*: female
- *E*: a teenager when first married
- *W*: in one's twenties when first married
- *H*: in one's thirties when first married

````````{list-table}
:header-rows: 1

- -
  - *E*
  - *W*
  - *H*
  - Total
- - *M*
  - 43
  - 293
  - 114
  - 450
- - *F*
  - 82
  - 299
  - 71
  - 452
- - Total
  - 125
  - 592
  - 185
  - 902

````````

The numbers in the first row mean that 43 people in the sample were men who were first married in their teens, 293 were men who were first married in their twenties, 114 men who were first married in their thirties, and a total of 450 people in the sample were men. Similarly for the numbers in the second row. The numbers in the last row mean that, irrespective of gender, 125 people in the sample were married in their teens, 592 in their twenties, 185 in their thirties, and that there were 902 people in the sample in all. Suppose that the proportions in the sample accurately reflect those in the population of all individuals in the population who are under 40 and who are or have previously been married. Suppose such a person is selected at random.

1.  Find the probability that the individual selected was a teenager at first marriage.
2.  Find the probability that the individual selected was a teenager at first marriage, given that the person is male.

Solution:

It is natural to let *E* also denote the event that the person selected was a teenager at first marriage and to let *M* denote the event that the person selected is male.

1.  According to the table the proportion of individuals in the sample who were in their teens at their first marriage is 125/902. This is the relative frequency of such people in the population, hence $\left. P(E) = 125/ 902 \approx 0.139 \right.$ or about 14%.

2.  Since it is known that the person selected is male, all the females may be removed from consideration, so that only the row in the table corresponding to men in the sample applies:

    ````````{list-table}
    :header-rows: 1

    - -
      - *E*
      - *W*
      - *H*
      - Total
    - - *M*
      - 43
      - 293
      - 114
      - 450

    ````````

The proportion of males in the sample who were in their teens at their first marriage is 43/450. This is the relative frequency of such people in the population of males, hence $\left. P\left( E \middle| M \right) = 43/ 450 \approx 0.096 \right.$ or about 10%.

In the next example, the computational formula in the definition must be used.

### Example 22

Suppose that in an adult population the proportion of people who are both overweight and suffer hypertension is 0.09; the proportion of people who are not overweight but suffer hypertension is 0.11; the proportion of people who are overweight but do not suffer hypertension is 0.02; and the proportion of people who are neither overweight nor suffer hypertension is 0.78. An adult is randomly selected from this population.

1.  Find the probability that the person selected suffers hypertension given that he is overweight.
2.  Find the probability that the selected person suffers hypertension given that he is not overweight.
3.  Compare the two probabilities just found to give an answer to the question as to whether overweight people tend to suffer from hypertension.

Solution:

Let *H* denote the event "the person selected suffers hypertension." Let *O* denote the event "the person selected is overweight." The probability information given in the problem may be organized into the following contingency table:

````````{list-table}
:header-rows: 1

- -
  - *O*
  - *O<sup>c</sup>*
- - *H*
  - 0.09
  - 0.11
- - *H<sup>c</sup>*
  - 0.02
  - 0.78

````````

1.  Using the formula in the definition of conditional probability,

    $$P\left( H \middle| O \right) = \frac{P\left( {H \cap O} \right)}{P(O)} = \frac{0.09}{0.09 + 0.02} = 0.8182$$

2.  Using the formula in the definition of conditional probability,

    $$P\left( H \middle| O^{c} \right) = \frac{P\left( {H \cap O^{c}} \right)}{P\left( O^{c} \right)} = \frac{0.11}{0.11 + 0.78} = 0.1236$$

3.  $P\left( H \middle| O \right) = 0.8182$ is over six times as large as $P\left( H \middle| O^{c} \right) = 0.1236$, which indicates a much higher rate of hypertension among people who are overweight than among people who are not overweight. It might be interesting to note that a direct comparison of $P\left( {H \cap O} \right) = 0.09$ and $P\left( {H \cap O^{c}} \right) = 0.11$ does not answer the same question.

### Independent Events

Although typically we expect the conditional probability $P\left( A \middle| B \right)$ to be different from the probability $P(A)$ of *A*, it does not have to be different from $P(A).$ When $P\left( A \middle| B \right) = P(A)$, the occurrence of *B* has no effect on the likelihood of *A*. Whether or not the event *A* has occurred is *independent* of the event *B*.

Using algebra it can be shown that the equality $P\left( A \middle| B \right) = P(A)$ holds if and only if the equality $P\left( {A \cap B} \right) = P(A) \cdot P(B)$ holds, which in turn is true if and only if $P\left( B \middle| A \right) = P(B).$ This is the basis for the following definition.

````````````{important} Definition

*Events* *A* *and* *B* *are* independent[^stats-10] *if*

$$P\left( {A \cap B} \right) = P(A) \cdot P(B)$$

*If* *A* *and* *B* *are not independent then they are* **dependent**.

````````````

The formula in the definition has two practical but exactly opposite uses:

1.  In a situation in which we can compute all three probabilities $P(A)$, $P(B)$, and $P\left( {A \cap B} \right)$, it is used to check whether or not the events *A* and *B* are independent:

    - If $P\left( {A \cap B} \right) = P(A) \cdot P(B)$, then *A* and *B* are independent.
    - If $P\left( {A \cap B} \right) \neq P(A) \cdot P(B)$, then *A* and *B* are not independent.

2.  In a situation in which each of $P(A)$ and $P(B)$ can be computed and it is known that *A* and *B* are independent, then we can compute $P\left( {A \cap B} \right)$ by multiplying together $P(A)$ and $P(B)$: $P\left( {A \cap B} \right) = P(A) \cdot P(B).$

### Example 23

A single fair die is rolled. Let $A = \left\{ 3 \right\}$ and $B = \left\{ 1,3,5 \right\}.$ Are *A* and *B* independent?

Solution:

In this example we can compute all three probabilities $\left. P(A) = 1/ 6 \right.$, $\left. P(B) = 1/ 2 \right.$, and $\left. P\left( {A \cap B} \right) = P\left( \left\{ 3 \right\} \right) = 1/ 6. \right.$ Since the product $\left. P(A) \cdot P(B) = \left( 1/ 6 \right)\left( 1/ 2 \right) = 1/ 12 \right.$ is not the same number as $\left. P\left( {A \cap B} \right) = 1/ 6 \right.$, the events *A* and *B* are not independent.

### Example 24

The two-way classification of married or previously married adults under 40 according to gender and age at first marriage in [Note 3.48 \"Example 21\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s03-s01-n04) produced the table

````````{list-table}
:header-rows: 1

- -
  - *E*
  - *W*
  - *H*
  - Total
- - *M*
  - 43
  - 293
  - 114
  - 450
- - *F*
  - 82
  - 299
  - 71
  - 452
- - Total
  - 125
  - 592
  - 185
  - 902

````````

Determine whether or not the events *F*: "female" and *E*: "was a teenager at first marriage" are independent.

Solution:

The table shows that in the sample of 902 such adults, 452 were female, 125 were teenagers at their first marriage, and 82 were females who were teenagers at their first marriage, so that

$$P(F) = \frac{452}{902}\quad P(E) = \frac{125}{902}\quad P\left( {F \cap E} \right) = \frac{82}{902}$$

Since

$$P(F) \cdot P(E) = \frac{452}{902} \cdot \frac{125}{902} = 0.069$$

is not the same as

$$P\left( {F \cap E} \right) = \frac{82}{902} = 0.091$$

we conclude that the two events are not independent.

### Example 25

Many diagnostic tests for detecting diseases do not test for the disease directly but for a chemical or biological product of the disease, hence are not perfectly reliable. The *sensitivity* of a test is the probability that the test will be positive when administered to a person who has the disease. The higher the sensitivity, the greater the detection rate and the lower the false negative rate.

Suppose the sensitivity of a diagnostic procedure to test whether a person has a particular disease is 92%. A person who actually has the disease is tested for it using this procedure by two independent laboratories.

1.  What is the probability that both test results will be positive?
2.  What is the probability that at least one of the two test results will be positive?

Solution:

1.  Let *A*<sub>1</sub> denote the event "the test by the first laboratory is positive" and let *A*<sub>2</sub> denote the event "the test by the second laboratory is positive." Since *A*<sub>1</sub> and *A*<sub>2</sub> are independent,

    $$P\left( {A_{1} \cap A_{2}} \right) = P\left( A_{1} \right) \cdot P\left( A_{2} \right) = 0.92 \times 0.92 = 0.8464$$

2.  Using the Additive Rule for Probability and the probability just computed,

    $$P\left( {A_{1} \cup A_{2}} \right) = P\left( A_{1} \right) + P\left( A_{2} \right) - P\left( {A_{1} \cap A_{2}} \right) = 0.92 + 0.92 - 0.8464 = 0.9936$$

### Example 26

The *specificity* of a diagnostic test for a disease is the probability that the test will be negative when administered to a person who does not have the disease. The higher the specificity, the lower the false positive rate.

Suppose the specificity of a diagnostic procedure to test whether a person has a particular disease is 89%.

1.  A person who does not have the disease is tested for it using this procedure. What is the probability that the test result will be positive?
2.  A person who does not have the disease is tested for it by two independent laboratories using this procedure. What is the probability that both test results will be positive?

Solution:

1.  Let *B* denote the event "the test result is positive." The complement of *B* is that the test result is negative, and has probability the specificity of the test, 0.89. Thus

    $$P(B) = 1 - P\left( B^{c} \right) = 1 - 0.89 = 0.11.$$

2.  Let *B*<sub>1</sub> denote the event "the test by the first laboratory is positive" and let *B*<sub>2</sub> denote the event "the test by the second laboratory is positive." Since *B*<sub>1</sub> and *B*<sub>2</sub> are independent, by part (a) of the example

    $$P\left( {B_{1} \cap B_{2}} \right) = P\left( B_{1} \right) \cdot P\left( B_{2} \right) = 0.11 \times 0.11 = 0.0121.$$

The concept of independence applies to any number of events. For example, three events *A*, *B*, and *C* are independent if $P\left( {A \cap B \cap C} \right) = P(A) \cdot P(B) \cdot P(C).$ Note carefully that, as is the case with just two events, this is not a formula that is always valid, but holds precisely when the events in question are independent.

### Example 27

The reliability of a system can be enhanced by redundancy, which means building two or more independent devices to do the same job, such as two independent braking systems in an automobile.

Suppose a particular species of trained dogs has a 90% chance of detecting contraband in airline luggage. If the luggage is checked three times by three different dogs independently of one another, what is the probability that contraband will be detected?

Solution:

Let *D*<sub>1</sub> denote the event that the contraband is detected by the first dog, *D*<sub>2</sub> the event that it is detected by the second dog, and *D*<sub>3</sub> the event that it is detected by the third. Since each dog has a 90% of detecting the contraband, by the Probability Rule for Complements it has a 10% chance of failing. In symbols, $P\left( D_{1}^{c} \right) = 0.10,$ $P\left( D_{2}^{c} \right) = 0.10$, and $P\left( D_{3}^{c} \right) = 0.10.$

Let *D* denote the event that the contraband is detected. We seek $P(D).$ It is easier to find $P\left( D^{c} \right)$, because although there are several ways for the contraband to be detected, there is only one way for it to go undetected: all three dogs must fail. Thus $D^{c} = D_{1}^{c} \cap D_{2}^{c} \cap D_{3}^{c}$, and

$$P(D) = 1 - P\left( D^{c} \right) = 1 - P\left( {D_{1}^{c} \cap D_{2}^{c} \cap D_{3}^{c}} \right)$$

But the events *D*<sub>1</sub>, *D*<sub>2</sub>, and *D*<sub>3</sub> are independent, which implies that their complements are independent, so

$$P\left( {D_{1}^{c} \cap D_{2}^{c} \cap D_{3}^{c}} \right) = P\left( D_{1}^{c} \right) \cdot P\left( D_{2}^{c} \right) \cdot P\left( D_{3}^{c} \right) = 0.10 \times 0.10 \times 0.10 = 0.001$$

Using this number in the previous display we obtain

$$P(D) = 1 - 0.001 = 0.999$$

That is, although any one dog has only a 90% chance of detecting the contraband, three dogs working independently have a 99.9% chance of detecting it.

### Probabilities on Tree Diagrams

Some probability problems are made much simpler when approached using a tree diagram. The next example illustrates how to place probabilities on a tree diagram and use it to solve a problem.

### Example 28

A jar contains 10 marbles, 7 black and 3 white. Two marbles are drawn without replacement, which means that the first one is not put back before the second one is drawn.

1.  What is the probability that both marbles are black?
2.  What is the probability that exactly one marble is black?
3.  What is the probability that at least one marble is black?

Solution:

A tree diagram for the situation of drawing one marble after the other without replacement is shown in [Figure 3.6 \"Tree Diagram for Drawing Two Marbles\"](/chapters/ch-03-basic-concepts-of-probability.md#src-fwk-shafer-ch03-s03-s03-f01). The circle and rectangle will be explained later, and should be ignored for now.

``````{figure} /images/section_07/d49c86e68633de7735225880cc896d8b.jpg
:alt: Statistical diagram: Figure 3.6 Tree Diagram for Drawing Two Marbles
:name: src-fwk-shafer-ch03-s03-s03-f01

Figure 3.6 Tree Diagram for Drawing Two Marbles
``````

The numbers on the two leftmost branches are the probabilities of getting either a black marble, 7 out of 10, or a white marble, 3 out of 10, on the first draw. The number on each remaining branch is the probability of the event corresponding to the node on the right end of the branch occurring, given that the event corresponding to the node on the left end of the branch has occurred. Thus for the top branch, connecting the two Bs, it is $P\left( B_{2} \middle| B_{1} \right)$, where *B*<sub>1</sub> denotes the event "the first marble drawn is black" and *B*<sub>2</sub> denotes the event "the second marble drawn is black." Since after drawing a black marble out there are 9 marbles left, of which 6 are black, this probability is 6/9.

The number to the right of each final node is computed as shown, using the principle that if the formula in the Conditional Rule for Probability is multiplied by $P(B)$, then the result is

$$P\left( {B \cap A} \right) = P(B) \cdot P\left( A \middle| B \right)$$

1.  The event "both marbles are black" is $B_{1} \cap B_{2}$ and corresponds to the top right node in the tree, which has been circled. Thus as indicated there, it is 0.47.

2.  The event "exactly one marble is black" corresponds to the two nodes of the tree enclosed by the rectangle. The events that correspond to these two nodes are mutually exclusive: black followed by white is incompatible with white followed by black. Thus in accordance with the Additive Rule for Probability we merely add the two probabilities next to these nodes, since what would be subtracted from the sum is zero. Thus the probability of drawing exactly one black marble in two tries is $0.23 + 0.23 = 0.46.$

3.  The event "at least one marble is black" corresponds to the three nodes of the tree enclosed by either the circle or the rectangle. The events that correspond to these nodes are mutually exclusive, so as in part (b) we merely add the probabilities next to these nodes. Thus the probability of drawing at least one black marble in two tries is $0.47 + 0.23 + 0.23 = 0.93.$

    Of course, this answer could have been found more easily using the Probability Law for Complements, simply subtracting the probability of the complementary event, "two white marbles are drawn," from 1 to obtain $1 - 0.07 = 0.93.$

As this example shows, finding the probability for each branch is fairly straightforward, since we compute it knowing everything that has happened in the sequence of steps so far. Two principles that are true in general emerge from this example:

````````````{important} Probabilities on Tree Diagrams

1.  The probability of the event corresponding to any node on a tree is the product of the numbers on the unique path of branches that leads to that node from the start.
2.  If an event corresponds to several final nodes, then its probability is obtained by adding the numbers next to those nodes.

````````````

````````````{important} Key Takeaways

- A conditional probability is the probability that an event has occurred, taking into account additional information about the result of the experiment.
- A conditional probability can always be computed using the formula in the definition. Sometimes it can be computed by discarding part of the sample space.
- Two events *A* and *B* are independent if the probability $P\left( {A \cap B} \right)$ of their intersection *A* ∩ *B* is equal to the product $P(A) \cdot P(B)$ of their individual probabilities.

````````````

### Exercises

### Basic

1.  For two events *A* and *B*, $P(A) = 0.73$, $P(B) = 0.48$, and $P\left( {A \cap B} \right) = 0.29.$

    1.  Find $P\left( A \middle| B \right).$
    2.  Find $P\left( B \middle| A \right).$
    3.  Determine whether or not *A* and *B* are independent.

2.  For two events *A* and *B*, $P(A) = 0.26$, $P(B) = 0.37$, and $P\left( {A \cap B} \right) = 0.11.$

    1.  Find $P\left( A \middle| B \right).$
    2.  Find $P\left( B \middle| A \right).$
    3.  Determine whether or not *A* and *B* are independent.

3.  For independent events *A* and *B*, $P(A) = 0.81$ and $P(B) = 0.27.$

    1.  Find $P\left( {A \cap B} \right).$
    2.  Find $P\left( A \middle| B \right).$
    3.  Find $P\left( B \middle| A \right).$

4.  For independent events *A* and *B*, $P(A) = 0.68$ and $P(B) = 0.37.$

    1.  Find $P\left( {A \cap B} \right).$
    2.  Find $P\left( A \middle| B \right).$
    3.  Find $P\left( B \middle| A \right).$

5.  For mutually exclusive events *A* and *B*, $P(A) = 0.17$ and $P(B) = 0.32.$

    1.  Find $P\left( A \middle| B \right).$
    2.  Find $P\left( B \middle| A \right).$

6.  For mutually exclusive events *A* and *B*, $P(A) = 0.45$ and $P(B) = 0.09.$

    1.  Find $P\left( A \middle| B \right).$
    2.  Find $P\left( B \middle| A \right).$

7.  Compute the following probabilities in connection with the roll of a single fair die.

    1.  The probability that the roll is even.
    2.  The probability that the roll is even, given that it is not a two.
    3.  The probability that the roll is even, given that it is not a one.

8.  Compute the following probabilities in connection with two tosses of a fair coin.

    1.  The probability that the second toss is heads.
    2.  The probability that the second toss is heads, given that the first toss is heads.
    3.  The probability that the second toss is heads, given that at least one of the two tosses is heads.

9.  A special deck of 16 cards has 4 that are blue, 4 yellow, 4 green, and 4 red. The four cards of each color are numbered from one to four. A single card is drawn at random. Find the following probabilities.

    1.  The probability that the card drawn is red.
    2.  The probability that the card is red, given that it is not green.
    3.  The probability that the card is red, given that it is neither red nor yellow.
    4.  The probability that the card is red, given that it is not a four.

10. A special deck of 16 cards has 4 that are blue, 4 yellow, 4 green, and 4 red. The four cards of each color are numbered from one to four. A single card is drawn at random. Find the following probabilities.

    1.  The probability that the card drawn is a two or a four.
    2.  The probability that the card is a two or a four, given that it is not a one.
    3.  The probability that the card is a two or a four, given that it is either a two or a three.
    4.  The probability that the card is a two or a four, given that it is red or green.

11. A random experiment gave rise to the two-way contingency table shown. Use it to compute the probabilities indicated.

    ````````{list-table}
    :header-rows: 1

    - -
      - *R*
      - *S*
    - - *A*
      - 0.12
      - 0.18
    - - *B*
      - 0.28
      - 0.42

    ````````

    1.  $P(A)$, $P(R)$, $P\left( {A \cap R} \right).$
    2.  Based on the answer to (a), determine whether or not the events *A* and *R* are independent.
    3.  Based on the answer to (b), determine whether or not $P\left( A \middle| R \right)$ can be predicted without any computation. If so, make the prediction. In any case, compute $P\left( A \middle| R \right)$ using the Rule for Conditional Probability.

12. A random experiment gave rise to the two-way contingency table shown. Use it to compute the probabilities indicated.

    ````````{list-table}
    :header-rows: 1

    - -
      - *R*
      - *S*
    - - *A*
      - 0.13
      - 0.07
    - - *B*
      - 0.61
      - 0.19

    ````````

    1.  $P(A)$, $P(R)$, $P\left( {A \cap R} \right).$
    2.  Based on the answer to (a), determine whether or not the events *A* and *R* are independent.
    3.  Based on the answer to (b), determine whether or not $P\left( A \middle| R \right)$ can be predicted without any computation. If so, make the prediction. In any case, compute $P\left( A \middle| R \right)$ using the Rule for Conditional Probability.

13. Suppose for events *A* and *B* in a random experiment $P(A) = 0.70$ and $P(B) = 0.30.$ Compute the indicated probability, or explain why there is not enough information to do so.

    1.  $P\left( {A \cap B} \right).$
    2.  $P\left( {A \cap B} \right)$, with the extra information that *A* and *B* are independent.
    3.  $P\left( {A \cap B} \right)$, with the extra information that *A* and *B* are mutually exclusive.

14. Suppose for events *A* and *B* connected to some random experiment, $P(A) = 0.50$ and $P(B) = 0.50.$ Compute the indicated probability, or explain why there is not enough information to do so.

    1.  $P\left( {A \cap B} \right).$
    2.  $P\left( {A \cap B} \right)$, with the extra information that *A* and *B* are independent.
    3.  $P\left( {A \cap B} \right)$, with the extra information that *A* and *B* are mutually exclusive.

15. Suppose for events *A*, *B*, and *C* connected to some random experiment, *A*, *B*, and *C* are independent and $P(A) = 0.88$, $P(B) = 0.65$, and $P(C) = 0.44.$ Compute the indicated probability, or explain why there is not enough information to do so.

    1.  $P\left( {A \cap B \cap C} \right)$
    2.  $P\left( {A^{c} \cap B^{c} \cap C^{c}} \right)$

16. Suppose for events *A*, *B*, and *C* connected to some random experiment, *A*, *B*, and *C* are independent and $P(A) = 0.95$, $P(B) = 0.73$, and $P(C) = 0.62.$ Compute the indicated probability, or explain why there is not enough information to do so.

    1.  $P\left( {A \cap B \cap C} \right)$
    2.  $P\left( {A^{c} \cap B^{c} \cap C^{c}} \right)$

### Applications

17. The sample space that describes all three-child families according to the genders of the children with respect to birth order is

    $$S = \left\{ {bbb,bbg,bgb,bgg,gbb,gbg,ggb,ggg} \right\}$$

    In the experiment of selecting a three-child family at random, compute each of the following probabilities, assuming all outcomes are equally likely.

    1.  The probability that the family has at least two boys.
    2.  The probability that the family has at least two boys, given that not all of the children are girls.
    3.  The probability that at least one child is a boy.
    4.  The probability that at least one child is a boy, given that the first born is a girl.

18. The following two-way contingency table gives the breakdown of the population in a particular locale according to age and number of vehicular moving violations in the past three years:

    ````````{list-table}
    :header-rows: 2

    - - Age
      - Violations
      - Violations
      - Violations
    - - Age
      - 0
      - 1
      - 2+
    - - Under 21
      - 0.04
      - 0.06
      - 0.02
    - - 21--40
      - 0.25
      - 0.16
      - 0.01
    - - 41--60
      - 0.23
      - 0.10
      - 0.02
    - - 60+
      - 0.08
      - 0.03
      - 0.00

    ````````

    A person is selected at random. Find the following probabilities.

    1.  The person is under 21.
    2.  The person has had at least two violations in the past three years.
    3.  The person has had at least two violations in the past three years, given that he is under 21.
    4.  The person is under 21, given that he has had at least two violations in the past three years.
    5.  Determine whether the events "the person is under 21" and "the person has had at least two violations in the past three years" are independent or not.

19. The following two-way contingency table gives the breakdown of the population in a particular locale according to party affiliation (*A*, *B*, *C*, or *None*) and opinion on a bond issue:

    ````````{list-table}
    :header-rows: 2

    - - Affiliation
      - Opinion
      - Opinion
      - Opinion
    - - Affiliation
      - Favors
      - Opposes
      - Undecided
    - - *A*
      - 0.12
      - 0.09
      - 0.07
    - - *B*
      - 0.16
      - 0.12
      - 0.14
    - - *C*
      - 0.04
      - 0.03
      - 0.06
    - - *None*
      - 0.08
      - 0.06
      - 0.03

    ````````

    A person is selected at random. Find each of the following probabilities.

    1.  The person is in favor of the bond issue.
    2.  The person is in favor of the bond issue, given that he is affiliated with party *A*.
    3.  The person is in favor of the bond issue, given that he is affiliated with party *B*.

20. The following two-way contingency table gives the breakdown of the population of patrons at a grocery store according to the number of items purchased and whether or not the patron made an impulse purchase at the checkout counter:

    ````````{list-table}
    :header-rows: 2

    - - Number of Items
      - Impulse Purchase
      - Impulse Purchase
    - - Number of Items
      - Made
      - Not Made
    - - Few
      - 0.01
      - 0.19
    - - Many
      - 0.04
      - 0.76

    ````````

    A patron is selected at random. Find each of the following probabilities.

    1.  The patron made an impulse purchase.
    2.  The patron made an impulse purchase, given that the total number of items purchased was many.
    3.  Determine whether or not the events "few purchases" and "made an impulse purchase at the checkout counter" are independent.

21. The following two-way contingency table gives the breakdown of the population of adults in a particular locale according to employment type and level of life insurance:

    ````````{list-table}
    :header-rows: 2

    - - Employment Type
      - Level of Insurance
      - Level of Insurance
      - Level of Insurance
    - - Employment Type
      - Low
      - Medium
      - High
    - - Unskilled
      - 0.07
      - 0.19
      - 0.00
    - - Semi-skilled
      - 0.04
      - 0.28
      - 0.08
    - - Skilled
      - 0.03
      - 0.18
      - 0.05
    - - Professional
      - 0.01
      - 0.05
      - 0.02

    ````````

    An adult is selected at random. Find each of the following probabilities.

    1.  The person has a high level of life insurance.
    2.  The person has a high level of life insurance, given that he does not have a professional position.
    3.  The person has a high level of life insurance, given that he has a professional position.
    4.  Determine whether or not the events "has a high level of life insurance" and "has a professional position" are independent.

22. The sample space of equally likely outcomes for the experiment of rolling two fair dice is

    $$\begin{matrix}
    11 & 12 & 13 & 14 & 15 & 16 \\
    21 & 22 & 23 & 24 & 25 & 26 \\
    31 & 32 & 33 & 34 & 35 & 36 \\
    41 & 42 & 43 & 44 & 45 & 46 \\
    51 & 52 & 53 & 54 & 55 & 56 \\
    61 & 62 & 63 & 64 & 65 & 66
    \end{matrix}$$

    Identify the events *N*: the sum is at least nine, *T*: at least one of the dice is a two, and *F*: at least one of the dice is a five.

    1.  Find $P(N).$
    2.  Find $P\left( N \middle| F \right).$
    3.  Find $P\left( N \middle| T \right).$
    4.  Determine from the previous answers whether or not the events *N* and *F* are independent; whether or not *N* and *T* are.

23. The *sensitivity* of a drug test is the probability that the test will be positive when administered to a person who has actually taken the drug. Suppose that there are two independent tests to detect the presence of a certain type of banned drugs in athletes. One has sensitivity 0.75; the other has sensitivity 0.85. If both are applied to an athlete who has taken this type of drug, what is the chance that his usage will go undetected?

24. A man has two lights in his well house to keep the pipes from freezing in winter. He checks the lights daily. Each light has probability 0.002 of burning out before it is checked the next day (independently of the other light).

    1.  If the lights are wired in parallel one will continue to shine even if the other burns out. In this situation, compute the probability that at least one light will continue to shine for the full 24 hours. Note the greatly increased reliability of the system of two bulbs over that of a single bulb.
    2.  If the lights are wired in series neither one will continue to shine even if only one of them burns out. In this situation, compute the probability that at least one light will continue to shine for the full 24 hours. Note the slightly decreased reliability of the system of two bulbs over that of a single bulb.

25. An accountant has observed that 5% of all copies of a particular two-part form have an error in Part I, and 2% have an error in Part II. If the errors occur independently, find the probability that a randomly selected form will be error-free.

26. A box contains 20 screws which are identical in size, but 12 of which are zinc coated and 8 of which are not. Two screws are selected at random, without replacement.

    1.  Find the probability that both are zinc coated.
    2.  Find the probability that at least one is zinc coated.

### Additional Exercises

27. Events *A* and *B* are mutually exclusive. Find $P\left( A \middle| B \right).$

28. The city council of a particular city is composed of five members of party *A*, four members of party *B*, and three independents. Two council members are randomly selected to form an investigative committee.

    1.  Find the probability that both are from party *A*.
    2.  Find the probability that at least one is an independent.
    3.  Find the probability that the two have different party affiliations (that is, not both *A*, not both *B*, and not both independent).

29. A basketball player makes 60% of the free throws that he attempts, except that if he has just tried and missed a free throw then his chances of making a second one go down to only 30%. Suppose he has just been awarded two free throws.

    1.  Find the probability that he makes both.
    2.  Find the probability that he makes at least one. (A tree diagram could help.)

30. An economist wishes to ascertain the proportion *p* of the population of individual taxpayers who have purposely submitted fraudulent information on an income tax return. To truly guarantee anonymity of the taxpayers in a random survey, taxpayers questioned are given the following instructions.

    1.  Flip a coin.
    2.  If the coin lands heads, answer "Yes" to the question "Have you ever submitted fraudulent information on a tax return?" even if you have not.
    3.  If the coin lands tails, give a truthful "Yes" or "No" answer to the question "Have you ever submitted fraudulent information on a tax return?"

    The questioner is not told how the coin landed, so he does not know if a "Yes" answer is the truth or is given only because of the coin toss.

    1.  Using the Probability Rule for Complements and the independence of the coin toss and the taxpayers' status fill in the empty cells in the two-way contingency table shown. Assume that the coin is fair. Each cell except the two in the bottom row will contain the unknown proportion (or probability) *p*.

        ````````{list-table}
        :header-rows: 2

        - - Status
          - Coin
          - Coin
          - Probability
        - - Status
          - H
          - T
          - Probability
        - - Fraud
          -
          -
          - *p*
        - - No fraud
          -
          -
          -
        - - Probability
          -
          -
          - 1

        ````````

    2.  The only information that the economist sees are the entries in the following table:

        $$\begin{matrix}
        \text{Response} & {``\text{Yes}"} & {``\text{No}"} \\
        \text{Proportion} & r & s
        \end{matrix}$$

        Equate the entry in the one cell in the table in (a) that corresponds to the answer "No" to the number *s* to obtain the formula $p = 1 - 2s$ that expresses the unknown number *p* in terms of the known number *s*.

    3.  Equate the sum of the entries in the three cells in the table in (a) that together correspond to the answer "Yes" to the number *r* to obtain the formula $p = 2r\text{-}1$ that expresses the unknown number *p* in terms of the known number *r*.

    4.  Use the fact that $r + s = 1$ (since they are the probabilities of complementary events) to verify that the formulas in (b) and (c) give the same value for *p*. (For example, insert $s = 1 - r$ into the formula in (b) to obtain the formula in (c).)

    5.  Suppose a survey of 1,200 taxpayers is conducted and 690 respond "Yes" (truthfully or not) to the question "Have you ever submitted fraudulent information on a tax return?" Use the answer to either (b) or (c) to estimate the true proportion *p* of all individual taxpayers who have purposely submitted fraudulent information on an income tax return.

`````````````{admonition} Answers
:class: dropdown

1.  1.  0.6
    2.  0.4
    3.  not independent
2. &nbsp;
3.  1.  0.22
    2.  0.81
    3.  0.27
4. &nbsp;
5.  1.  0
    2.  0
6. &nbsp;
7.  1.  0.5
    2.  0.4
    3.  0.6
8. &nbsp;
9.  1.  0.25
    2.  0.33
    3.  0
    4.  0.25
10. &nbsp;
11. 1.  $P(A) = 0.3$, $P(R) = 0.4$, $P\left( {A \cap R} \right) = 0.12$
    2.  independent
    3.  without computation 0.3
12. &nbsp;
13. 1.  Insufficient information. The events *A* and *B* are not known to be either independent or mutually exclusive.
    2.  0.21
    3.  0
14. &nbsp;
15. 1.  0.25
    2.  0.02
16. &nbsp;

<!-- -->

17. 1.  0.5
    2.  0.57
    3.  0.875
    4.  0.75

18. &nbsp;

19. 1.  0.4
    2.  0.43
    3.  0.38

20. &nbsp;

21. 1.  0.15
    2.  0.14
    3.  0.25
    4.  not independent

22. &nbsp;

23. 0.0375

24. &nbsp;

25. 0.931

26. &nbsp;

<!-- -->

27. 0

28. &nbsp;

29. 1.  0.36
    2.  0.72

30. &nbsp;

`````````````

[^stats-1]: The set of all possible outcomes of a random experiment.

[^stats-2]: Any set of outcomes.

[^stats-3]: A number that measures the likelihood of the outcome.

[^stats-4]: A number that measures the likelihood of the event.

[^stats-5]: The event does not occur.

[^stats-6]: Both events occur.

[^stats-7]: Events that cannot both occur at once.

[^stats-8]: One or the other event occurs.

[^stats-9]: The probability of the event *A* taking into account the fact that event *B* is known to have occurred.

[^stats-10]: Events whose probability of occurring together is the product of their individual probabilities.
