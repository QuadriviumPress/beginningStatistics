(src-fwk-shafer-ch06)=

# Chapter 6 Sampling Distributions

A statistic, such as the sample mean or the sample standard deviation, is a number computed from a sample. Since a sample is random, every statistic is a random variable: it varies from sample to sample in a way that cannot be predicted with certainty. As a random variable it has a mean, a standard deviation, and a probability distribution. The probability distribution of a statistic is called its sampling distribution[^stats-1]. Typically sample statistics are not ends in themselves, but are computed in order to estimate the corresponding population parameters, as illustrated in the grand picture of statistics presented in [Figure 1.1 \"The Grand Picture of Statistics\"](/chapters/ch-01-introduction.md#src-fwk-shafer-ch01-s01-f01) in [Chapter 1 \"Introduction\"](/chapters/ch-01-introduction.md#src-fwk-shafer-ch01).

This chapter introduces the concepts of the mean, the standard deviation, and the sampling distribution of a sample statistic, with an emphasis on the sample mean $\overset{-}{\mathit{x}}.$

(src-fwk-shafer-ch06-s01)=

## 6.1 The Mean and Standard Deviation of the Sample Mean

````````````{note} Learning Objectives

1.  To become familiar with the concept of the probability distribution of the sample mean.
2.  To understand the meaning of the formulas for the mean and standard deviation of the sample mean.

````````````

Suppose we wish to estimate the mean *μ* of a population. In actual practice we would typically take just one sample. Imagine however that we take sample after sample, all of the same size *n*, and compute the sample mean $\overset{-}{\mathit{x}}$ of each one. We will likely get a different value of $\overset{-}{\mathit{x}}$ each time. The sample mean $\overset{-}{\mathit{x}}$ is a random variable: it varies from sample to sample in a way that cannot be predicted with certainty. We will write $\overset{-}{\mathit{X}}$ when the sample mean is thought of as a random variable, and write $\overset{-}{\mathit{x}}$ for the values that it takes. The random variable $\overset{-}{\mathit{X}}$ has a mean[^stats-2], denoted $\mathit{\mu}_{\overset{-}{\mathit{X}}}$, and a standard deviation[^stats-3], denoted $\mathit{\sigma}_{\overset{-}{\mathit{X}}}.$ Here is an example with such a small population and small sample size that we can actually write down every single sample.

(src-fwk-shafer-ch06-s01-n02)=

### Example 1

A rowing team consists of four rowers who weigh 152, 156, 160, and 164 pounds. Find all possible random samples with replacement of size two and compute the sample mean for each one. Use them to find the probability distribution, the mean, and the standard deviation of the sample mean $\overset{-}{\mathit{X}}.$

Solution

The following table shows all possible samples with replacement of size two, along with the mean of each:

````````{list-table}
:header-rows: 1

- - Sample
  - Mean
  -
  - Sample
  - Mean
  -
  - Sample
  - Mean
  -
  - Sample
  - Mean
- - 152, 152
  - 152
  -
  - 156, 152
  - 154
  -
  - 160, 152
  - 156
  -
  - 164, 152
  - 158
- - 152, 156
  - 154
  -
  - 156, 156
  - 156
  -
  - 160, 156
  - 158
  -
  - 164, 156
  - 160
- - 152, 160
  - 156
  -
  - 156, 160
  - 158
  -
  - 160, 160
  - 160
  -
  - 164, 160
  - 162
- - 152, 164
  - 158
  -
  - 156, 164
  - 160
  -
  - 160, 164
  - 162
  -
  - 164, 164
  - 164

````````

The table shows that there are seven possible values of the sample mean $\overset{-}{\mathit{X}}.$ The value $\overset{-}{\mathit{x}} = 152$ happens only one way (the rower weighing 152 pounds must be selected both times), as does the value $\overset{-}{\mathit{x}} = 164$, but the other values happen more than one way, hence are more likely to be observed than 152 and 164 are. Since the 16 samples are equally likely, we obtain the probability distribution of the sample mean just by counting:

$$\begin{matrix}
\overset{-}{\mathit{x}} & 152 & 154 & 156 & 158 & 160 & 162 & 164 \\
{P\left( \overset{-}{\mathit{x}} \right)} & \frac{1}{16} & \frac{2}{16} & \frac{3}{16} & \frac{4}{16} & \frac{3}{16} & \frac{2}{16} & \frac{1}{16}
\end{matrix}$$

Now we apply the formulas from [Section 4.2.2 \"The Mean and Standard Deviation of a Discrete Random Variable\"](/chapters/ch-04-discrete-random-variables.md#src-fwk-shafer-ch04-s02-s02) in [Chapter 4 \"Discrete Random Variables\"](/chapters/ch-04-discrete-random-variables.md#src-fwk-shafer-ch04) for the mean and standard deviation of a discrete random variable to $\overset{-}{\mathit{X}}.$ For $\mathit{\mu}_{\overset{-}{\mathit{X}}}$ we obtain.

$$\begin{array}{cl}
\mathit{\mu}_{\overset{-}{\mathit{X}}} & {= {\Sigma{\overset{-}{\mathit{x}}\, P\left( \overset{-}{\mathit{x}} \right)}}} \\
 & {= 152\left( \frac{1}{16} \right) + 154\left( \frac{2}{16} \right) + 156\left( \frac{3}{16} \right) + 158\left( \frac{4}{16} \right) + 160\left( \frac{3}{16} \right) + 162\left( \frac{2}{16} \right) + 164\left( \frac{1}{16} \right)} \\
 & {= 158}
\end{array}$$

For $\mathit{\sigma}_{\overset{-}{\mathit{X}}}$ we first compute $\Sigma{{\overset{-}{\mathit{x}}}^{2}P\left( \overset{-}{\mathit{x}} \right)}$:

$$152^{2}\left( \frac{1}{16} \right) + 154^{2}\left( \frac{2}{16} \right) + 156^{2}\left( \frac{3}{16} \right) + 158^{2}\left( \frac{4}{16} \right) + 160^{2}\left( \frac{3}{16} \right) + 162^{2}\left( \frac{2}{16} \right) + 164^{2}\left( \frac{1}{16} \right)$$

which is 24,974, so that

$$\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \sqrt{\Sigma{{\overset{-}{\mathit{x}}}^{2}P\left( \overset{-}{\mathit{x}} \right) - \mathit{\mu}_{\overset{-}{\mathit{x}}}^{2}}} = \sqrt{24,974 - 158^{2}} = \sqrt{10}$$

The mean and standard deviation of the population {152,156,160,164} in the example are *μ* = 158 and $\mathit{\sigma} = \sqrt{20}.$ The mean of the sample mean $\overset{-}{\mathit{X}}$ that we have just computed is exactly the mean of the population. The standard deviation of the sample mean $\overset{-}{\mathit{X}}$ that we have just computed is the standard deviation of the population divided by the square root of the sample size: $\sqrt{10} = \sqrt{20}/\sqrt{2}.$ These relationships are not coincidences, but are illustrations of the following formulas.

Suppose random samples of size *n* are drawn from a population with mean *μ* and standard deviation *σ*. The mean $\mathit{\mu}_{\overset{-}{\mathit{X}}}$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}}$ of the sample mean $\overset{-}{\mathit{X}}$ satisfy

$$\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu}\quad\quad\text{and}\quad\quad\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \frac{\mathit{\sigma}}{\sqrt{n}}$$

The first formula says that if we could take every possible sample from the population and compute the corresponding sample mean, then those numbers would center at the number we wish to estimate, the population mean *μ*.

The second formula says that averages computed from samples vary less than individual measurements on the population do, and quantifies the relationship.

### Example 2

The mean and standard deviation of the tax value of all vehicles registered in a certain state are $\mathit{\mu} = \$ 13,525$ and $\mathit{\sigma} = \$ 4,180.$ Suppose random samples of size 100 are drawn from the population of vehicles. What are the mean $\mathit{\mu}_{\overset{-}{\mathit{X}}}$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}}$ of the sample mean $\overset{-}{\mathit{X}}$?

Solution

Since *n* = 100, the formulas yield

$$\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu} = \$ 13,525\quad\text{and}\quad\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \frac{\mathit{\sigma}}{\sqrt{n}} = \frac{\$ 4180}{\sqrt{100}} = \$ 418$$

````````````{important} Key Takeaways

- The sample mean is a random variable; as such it is written $\overset{-}{\mathit{X}}$, and $\overset{-}{\mathit{x}}$ stands for individual values it takes.
- As a random variable the sample mean has a probability distribution, a mean $\mathit{\mu}_{\overset{-}{\mathit{X}}}$, and a standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}}.$
- There are formulas that relate the mean and standard deviation of the sample mean to the mean and standard deviation of the population from which the sample is drawn.

````````````

### Exercises

1.  Random samples of size 225 are drawn from a population with mean 100 and standard deviation 20. Find the mean and standard deviation of the sample mean.

2.  Random samples of size 64 are drawn from a population with mean 32 and standard deviation 5. Find the mean and standard deviation of the sample mean.

3.  A population has mean 75 and standard deviation 12.

    1.  Random samples of size 121 are taken. Find the mean and standard deviation of the sample mean.
    2.  How would the answers to part (a) change if the size of the samples were 400 instead of 121?

4.  A population has mean 5.75 and standard deviation 1.02.

    1.  Random samples of size 81 are taken. Find the mean and standard deviation of the sample mean.
    2.  How would the answers to part (a) change if the size of the samples were 25 instead of 81?

`````````````{admonition} Answers
:class: dropdown

1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 100$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 1.33$

2. &nbsp;

3.  1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 75$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 1.09$
    2.  $\mathit{\mu}_{\overset{-}{\mathit{X}}}$ stays the same but $\mathit{\sigma}_{\overset{-}{\mathit{X}}}$ decreases to 0.6

4. &nbsp;

`````````````

## 6.2 The Sampling Distribution of the Sample Mean

````````````{note} Learning Objectives

1.  To learn what the sampling distribution of $\overset{-}{\mathit{X}}$ is when the sample size is large.
2.  To learn what the sampling distribution of $\overset{-}{\mathit{X}}$ is when the population is normal.

````````````

### The Central Limit Theorem

In [Note 6.5 \"Example 1\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s01-n02) in [Section 6.1 \"The Mean and Standard Deviation of the Sample Mean\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s01) we constructed the probability distribution of the sample mean for samples of size two drawn from the population of four rowers. The probability distribution is:

$$\begin{matrix}
\overset{-}{\mathit{x}} & 152 & 154 & 156 & 158 & 160 & 162 & 164 \\
{P\left( \overset{-}{\mathit{x}} \right)} & \frac{1}{16} & \frac{2}{16} & \frac{3}{16} & \frac{4}{16} & \frac{3}{16} & \frac{2}{16} & \frac{1}{16}
\end{matrix}$$

[Figure 6.1 \"Distribution of a Population and a Sample Mean\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s02-s01-f01) shows a side-by-side comparison of a histogram for the original population and a histogram for this distribution. Whereas the distribution of the population is uniform, the sampling distribution of the mean has a shape approaching the shape of the familiar bell curve. This phenomenon of the sampling distribution of the mean taking on a bell shape even though the population distribution is not bell-shaped happens in general. Here is a somewhat more realistic example.

``````{figure} /images/redrawn/fig-06-01.svg
:alt: (a) Population: probability 0.25 at each of 152, 156, 160, and 164. (b) Sample mean of two draws: probabilities 1/16, 2/16, 3/16, 4/16, 3/16, 2/16, and 1/16 at 152, 154, 156, 158, 160, 162, and 164.
:name: src-fwk-shafer-ch06-s02-s01-f01

Figure 6.1 Distribution of a Population and a Sample Mean
``````

Suppose we take samples of size 1, 5, 10, or 20 from a population that consists entirely of the numbers 0 and 1, half the population 0, half 1, so that the population mean is 0.5. The sampling distributions are:

*n* = 1:

$$\begin{array}{lcc}
\overset{-}{\mathit{x}} & 0 & 1 \\
{P\left( \overset{-}{\mathit{x}} \right)} & 0.5 & 0.5
\end{array}$$

*n* = 5:

$$\begin{array}{lcccccc}
\overset{-}{\mathit{x}} & 0 & 0.2 & 0.4 & 0.6 & 0.8 & 1 \\
{P\left( \overset{-}{\mathit{x}} \right)} & 0.03 & 0.16 & 0.31 & 0.31 & 0.16 & 0.03
\end{array}$$

*n* = 10:

$$\begin{array}{lccccccccccc}
\overset{-}{\mathit{x}} & 0 & 0.1 & 0.2 & 0.3 & 0.4 & 0.5 & 0.6 & 0.7 & 0.8 & 0.9 & 1 \\
{P\left( \overset{-}{\mathit{x}} \right)} & 0.00 & 0.01 & 0.04 & 0.12 & 0.21 & 0.25 & 0.21 & 0.12 & 0.04 & 0.01 & 0.00
\end{array}$$

*n* = 20:

$$\begin{array}{lccccccccccc}
\overset{-}{\mathit{x}} & 0 & 0.05 & 0.10 & 0.15 & 0.20 & 0.25 & 0.30 & 0.35 & 0.40 & 0.45 & 0.50 \\
{P\left( \overset{-}{\mathit{x}} \right)} & 0.00 & 0.00 & 0.00 & 0.00 & 0.00 & 0.01 & 0.04 & 0.07 & 0.12 & 0.16 & 0.18
\end{array}$$

$$\begin{array}{lcccccccccc}
\overset{-}{\mathit{x}} & 0.55 & 0.60 & 0.65 & 0.70 & 0.75 & 0.80 & 0.85 & 0.90 & 0.95 & 1 \\
{P\left( \overset{-}{\mathit{x}} \right)} & 0.16 & 0.12 & 0.07 & 0.04 & 0.01 & 0.00 & 0.00 & 0.00 & 0.00 & 0.00
\end{array}$$

Histograms illustrating these distributions are shown in [Figure 6.2 \"Distributions of the Sample Mean\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s02-s01-f02).

``````{figure} /images/redrawn/fig-06-02.svg
:alt: Probability histograms of the sample mean of n draws from a population of 0s and 1s in equal proportion, each on its own scale from 0 to 1, for n = 1, 5, 10, and 20. For n = 1 there are two equal bars; as n grows the histogram becomes a narrower, taller bell centered at 0.5.
:name: src-fwk-shafer-ch06-s02-s01-f02

Figure 6.2 Distributions of the Sample Mean
``````

As *n* increases the sampling distribution of $\overset{-}{\mathit{X}}$ evolves in an interesting way: the probabilities on the lower and the upper ends shrink and the probabilities in the middle become larger in relation to them. If we were to continue to increase *n* then the shape of the sampling distribution would become smoother and more bell-shaped.

What we are seeing in these examples does not depend on the particular population distributions involved. In general, one may start with any distribution and the sampling distribution of the sample mean will increasingly resemble the bell-shaped normal curve as the sample size increases. This is the content of the Central Limit Theorem.

````````````{important} The Central Limit Theorem

For samples of size 30 or more, the sample mean is approximately normally distributed, with mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu}$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n}$, where *n* is the sample size. The larger the sample size, the better the approximation.

````````````

The Central Limit Theorem is illustrated for several common population distributions in [Figure 6.3 \"Distribution of Populations and Sample Means\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s02-s01-f03).

``````{figure} /images/redrawn/fig-06-03.svg
:alt: A three-by-three grid. The top row shows three populations: uniform, two-humped, and skewed right. Below each are the distributions of the sample mean for n = 5, already more bell-shaped, and for n = 30, a narrow bell centered at the population mean in every case.
:name: src-fwk-shafer-ch06-s02-s01-f03

Figure 6.3 Distribution of Populations and Sample Means
``````

The dashed vertical lines in the figures locate the population mean. Regardless of the distribution of the population, as the sample size is increased the shape of the sampling distribution of the sample mean becomes increasingly bell-shaped, centered on the population mean. Typically by the time the sample size is 30 the distribution of the sample mean is practically the same as a normal distribution.

The importance of the Central Limit Theorem is that it allows us to make probability statements about the sample mean, specifically in relation to its value in comparison to the population mean, as we will see in the examples. But to use the result properly we must first realize that there are two separate random variables (and therefore two probability distributions) at play:

1.  *X*, the measurement of a single element selected at random from the population; the distribution of *X* is the distribution of the population, with mean the population mean *μ* and standard deviation the population standard deviation *σ*;
2.  $\overset{-}{\mathit{X}}$, the mean of the measurements in a sample of size *n*; the distribution of $\overset{-}{\mathit{X}}$ is its sampling distribution, with mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu}$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n}.$

(src-fwk-shafer-ch06-s02-s01-n02)=

### Example 3

Let $\overset{-}{\mathit{X}}$ be the mean of a random sample of size 50 drawn from a population with mean 112 and standard deviation 40.

1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}.$
2.  Find the probability that $\overset{-}{\mathit{X}}$ assumes a value between 110 and 114.
3.  Find the probability that $\overset{-}{\mathit{X}}$ assumes a value greater than 113.

Solution

1.  By the formulas in the previous section

    $$\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu} = 112{\quad\text{and}}\quad\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \frac{\mathit{\sigma}}{\sqrt{n}} = \frac{40}{\sqrt{50}} = 5.65685$$

2.  Since the sample size is at least 30, the Central Limit Theorem applies: $\overset{-}{\mathit{X}}$ is approximately normally distributed. We compute probabilities using [Figure 12.2 \"Cumulative Normal Probability\"](/appendices/appendix.md#src-fwk-shafer-ch12-f02) in the usual way, just being careful to use $\mathit{\sigma}_{\overset{-}{\mathit{X}}}$ and not *σ* when we standardize:

    $$\begin{array}{ll}
    {P\left( 110 < \overset{-}{\mathit{X}} < 114 \right)} & {= P\left( {\frac{110 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}} < Z < \frac{114 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}}} \right)} \\
     & {= P\left( {\frac{110 - 112}{5.65685} < Z < \frac{114 - 112}{5.65685}} \right)} \\
     & {= P\left( {\text{-}0.35 < Z < 0.35} \right) = 0.6368 - 0.3632 = 0.2736}
    \end{array}$$

3.  Similarly

    $$\begin{array}{ll}
    {P\left( \overset{-}{\mathit{X}} > 113 \right)} & {= P\left( {Z > \frac{113 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}}} \right)} \\
     & {= P\left( {Z > \frac{113 - 112}{5.65685}} \right)} \\
     & {= P\left( {Z > 0.18} \right)} \\
     & {= 1 - P(Z < 0.18) = 1 - 0.5714 = 0.4286}
    \end{array}$$

Note that if in [Note 6.11 \"Example 3\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s02-s01-n02) we had been asked to compute the probability that the value of a single randomly selected element of the population exceeds 113, that is, to compute the number *P*(*X* \> 113), we would not have been able to do so, since we do not know the distribution of *X*, but only that its mean is 112 and its standard deviation is 40. By contrast we could compute $P\left( {\overset{-}{\mathit{X}} > 113} \right)$ even without complete knowledge of the distribution of *X* because the Central Limit Theorem guarantees that $\overset{-}{\mathit{X}}$ is approximately normal.

### Example 4

The numerical population of grade point averages at a college has mean 2.61 and standard deviation 0.5. If a random sample of size 100 is taken from the population, what is the probability that the sample mean will be between 2.51 and 2.71?

Solution

The sample mean $\overset{-}{\mathit{X}}$ has mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu} = 2.61$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n} = 0.5/10 = 0.05$, so

$$\begin{array}{ll}
{P\left( 2.51 < \overset{-}{\mathit{X}} < 2.71 \right)} & {= P\left( {\frac{2.51 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}} < Z < \frac{2.71 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}}} \right)} \\
 & {= P\left( {\frac{2.51 - 2.61}{0.05} < Z < \frac{2.71 - 2.61}{0.05}} \right)} \\
 & {= P\left( {\text{-}2 < Z < 2} \right)} \\
 & {= P\left( {Z < 2} \right) - P\left( {Z < \text{-}2} \right)} \\
 & {= 0.9772 - 0.0228 = 0.9544}
\end{array}$$

### Normally Distributed Populations

The Central Limit Theorem says that no matter what the distribution of the population is, as long as the sample is "large," meaning of size 30 or more, the sample mean is approximately normally distributed. If the population is normal to begin with then the sample mean also has a normal distribution, regardless of the sample size.

For samples of *any* size drawn from a normally distributed population, the sample mean is normally distributed, with mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu}$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n}$, where *n* is the sample size.

The effect of increasing the sample size is shown in [Figure 6.4 \"Distribution of Sample Means for a Normal Population\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s02-s02-f04).

``````{figure} /images/redrawn/fig-06-04.svg
:alt: A normal population centered at μ, then the distributions of the sample mean for n = 5 and n = 30, which are normal, centered at μ, and progressively narrower and taller, and finally all three superimposed.
:name: src-fwk-shafer-ch06-s02-s02-f04

Figure 6.4 Distribution of Sample Means for a Normal Population
``````

### Example 5

A prototype automotive tire has a design life of 38,500 miles with a standard deviation of 2,500 miles. Five such tires are manufactured and tested. On the assumption that the actual population mean is 38,500 miles and the actual population standard deviation is 2,500 miles, find the probability that the sample mean will be less than 36,000 miles. Assume that the distribution of lifetimes of such tires is normal.

Solution

For simplicity we use units of thousands of miles. Then the sample mean $\overset{-}{\mathit{X}}$ has mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu} = 38.5$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n} = 2.5/\sqrt{5} = 1.11803.$ Since the population is normally distributed, so is $\overset{-}{\mathit{X}}$, hence

$$\begin{array}{ll}
{P\left( \overset{-}{\mathit{X}} < 36 \right)} & {= P\left( {Z < \frac{36 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}}} \right)} \\
 & {= P\left( {Z < \frac{36 - 38.5}{1.11803}} \right)} \\
 & {= P\left( {Z < \text{-}2.24} \right) = 0.0125}
\end{array}$$

That is, if the tires perform as designed, there is only about a 1.25% chance that the average of a sample of this size would be so low.

### Example 6

An automobile battery manufacturer claims that its midgrade battery has a mean life of 50 months with a standard deviation of 6 months. Suppose the distribution of battery lives of this particular brand is approximately normal.

1.  On the assumption that the manufacturer's claims are true, find the probability that a randomly selected battery of this type will last less than 48 months.
2.  On the same assumption, find the probability that the mean of a random sample of 36 such batteries will be less than 48 months.

Solution

1.  Since the population is known to have a normal distribution

    $$\begin{array}{ll}
    {P\left( {X < 48} \right)} & {= P\left( {Z < \frac{48 - \mathit{\mu}}{\mathit{\sigma}}} \right) = P\left( {Z < \frac{48 - 50}{6}} \right)} \\
     & {= P\left( {Z < \text{-}0.33} \right) = 0.3707}
    \end{array}$$

2.  The sample mean has mean $\mathit{\mu}_{\overset{-}{\mathit{X}}} = \mathit{\mu} = 50$ and standard deviation $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = \mathit{\sigma}/\sqrt{n} = 6/\sqrt{36} = 1.$ Thus

    $$\begin{array}{ll}
    {P\left( {\overset{-}{\mathit{X}} < 48} \right)} & {= P\left( {Z < \frac{48 - \mathit{\mu}_{\overset{-}{\mathit{X}}}}{\mathit{\sigma}_{\overset{-}{\mathit{X}}}}} \right)} \\
     & {= P\left( {Z < \frac{48 - 50}{1}} \right)} \\
     & {= P\left( {Z < \text{-}2} \right) = 0.0228}
    \end{array}$$

````````````{important} Key Takeaways

- When the sample size is at least 30 the sample mean is normally distributed.
- When the population is normal the sample mean is normally distributed regardless of the sample size.

````````````

### Exercises

### Basic

1.  A population has mean 128 and standard deviation 22.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 36.
    2.  Find the probability that the mean of a sample of size 36 will be within 10 units of the population mean, that is, between 118 and 138.

2.  A population has mean 1,542 and standard deviation 246.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 100.
    2.  Find the probability that the mean of a sample of size 100 will be within 100 units of the population mean, that is, between 1,442 and 1,642.

3.  A population has mean 73.5 and standard deviation 2.5.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 30.
    2.  Find the probability that the mean of a sample of size 30 will be less than 72.

4.  A population has mean 48.4 and standard deviation 6.3.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 64.
    2.  Find the probability that the mean of a sample of size 64 will be less than 46.7.

5.  A normally distributed population has mean 25.6 and standard deviation 3.3.

    1.  Find the probability that a single randomly selected element *X* of the population exceeds 30.
    2.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 9.
    3.  Find the probability that the mean of a sample of size 9 drawn from this population exceeds 30.

6.  A normally distributed population has mean 57.7 and standard deviation 12.1.

    1.  Find the probability that a single randomly selected element *X* of the population is less than 45.
    2.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 16.
    3.  Find the probability that the mean of a sample of size 16 drawn from this population is less than 45.

7.  A population has mean 557 and standard deviation 35.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 50.
    2.  Find the probability that the mean of a sample of size 50 will be more than 570.

8.  A population has mean 16 and standard deviation 1.7.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 80.
    2.  Find the probability that the mean of a sample of size 80 will be more than 16.4.

9.  A normally distributed population has mean 1,214 and standard deviation 122.

    1.  Find the probability that a single randomly selected element *X* of the population is between 1,100 and 1,300.
    2.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 25.
    3.  Find the probability that the mean of a sample of size 25 drawn from this population is between 1,100 and 1,300.

10. A normally distributed population has mean 57,800 and standard deviation 750.

    1.  Find the probability that a single randomly selected element *X* of the population is between 57,000 and 58,000.
    2.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 100.
    3.  Find the probability that the mean of a sample of size 100 drawn from this population is between 57,000 and 58,000.

11. A population has mean 72 and standard deviation 6.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 45.
    2.  Find the probability that the mean of a sample of size 45 will differ from the population mean 72 by at least 2 units, that is, is either less than 70 or more than 74. (Hint: One way to solve the problem is to first find the probability of the complementary event.)

12. A population has mean 12 and standard deviation 1.5.

    1.  Find the mean and standard deviation of $\overset{-}{\mathit{X}}$ for samples of size 90.
    2.  Find the probability that the mean of a sample of size 90 will differ from the population mean 12 by at least 0.3 unit, that is, is either less than 11.7 or more than 12.3. (Hint: One way to solve the problem is to first find the probability of the complementary event.)

### Applications

13. Suppose the mean number of days to germination of a variety of seed is 22, with standard deviation 2.3 days. Find the probability that the mean germination time of a sample of 160 seeds will be within 0.5 day of the population mean.

14. Suppose the mean length of time that a caller is placed on hold when telephoning a customer service center is 23.8 seconds, with standard deviation 4.6 seconds. Find the probability that the mean length of time on hold in a sample of 1,200 calls will be within 0.5 second of the population mean.

15. Suppose the mean amount of cholesterol in eggs labeled "large" is 186 milligrams, with standard deviation 7 milligrams. Find the probability that the mean amount of cholesterol in a sample of 144 eggs will be within 2 milligrams of the population mean.

16. Suppose that in one region of the country the mean amount of credit card debt per household in households having credit card debt is \$15,250, with standard deviation \$7,125. Find the probability that the mean amount of credit card debt in a sample of 1,600 such households will be within \$300 of the population mean.

17. Suppose speeds of vehicles on a particular stretch of roadway are normally distributed with mean 36.6 mph and standard deviation 1.7 mph.

    1.  Find the probability that the speed *X* of a randomly selected vehicle is between 35 and 40 mph.
    2.  Find the probability that the mean speed $\overset{-}{\mathit{X}}$ of 20 randomly selected vehicles is between 35 and 40 mph.

18. Many sharks enter a state of tonic immobility when inverted. Suppose that in a particular species of sharks the time a shark remains in a state of tonic immobility when inverted is normally distributed with mean 11.2 minutes and standard deviation 1.1 minutes.

    1.  If a biologist induces a state of tonic immobility in such a shark in order to study it, find the probability that the shark will remain in this state for between 10 and 13 minutes.
    2.  When a biologist wishes to estimate the mean time that such sharks stay immobile by inducing tonic immobility in each of a sample of 12 sharks, find the probability that mean time of immobility in the sample will be between 10 and 13 minutes.

19. Suppose the mean cost across the country of a 30-day supply of a generic drug is \$46.58, with standard deviation \$4.84. Find the probability that the mean of a sample of 100 prices of 30-day supplies of this drug will be between \$45 and \$50.

20. Suppose the mean length of time between submission of a state tax return requesting a refund and the issuance of the refund is 47 days, with standard deviation 6 days. Find the probability that in a sample of 50 returns requesting a refund, the mean such time will be more than 50 days.

21. Scores on a common final exam in a large enrollment, multiple-section freshman course are normally distributed with mean 72.7 and standard deviation 13.1.

    1.  Find the probability that the score *X* on a randomly selected exam paper is between 70 and 80.
    2.  Find the probability that the mean score $\overset{-}{\mathit{X}}$ of 38 randomly selected exam papers is between 70 and 80.

22. Suppose the mean weight of school children's bookbags is 17.4 pounds, with standard deviation 2.2 pounds. Find the probability that the mean weight of a sample of 30 bookbags will exceed 17 pounds.

23. Suppose that in a certain region of the country the mean duration of first marriages that end in divorce is 7.8 years, standard deviation 1.2 years. Find the probability that in a sample of 75 divorces, the mean age of the marriages is at most 8 years.

24. Borachio eats at the same fast food restaurant every day. Suppose the time *X* between the moment Borachio enters the restaurant and the moment he is served his food is normally distributed with mean 4.2 minutes and standard deviation 1.3 minutes.

    1.  Find the probability that when he enters the restaurant today it will be at least 5 minutes until he is served.
    2.  Find the probability that average time until he is served in eight randomly selected visits to the restaurant will be at least 5 minutes.

### Additional Exercises

25. A high-speed packing machine can be set to deliver between 11 and 13 ounces of a liquid. For any delivery setting in this range the amount delivered is normally distributed with mean some amount *μ* and with standard deviation 0.08 ounce. To calibrate the machine it is set to deliver a particular amount, many containers are filled, and 25 containers are randomly selected and the amount they contain is measured. Find the probability that the sample mean will be within 0.05 ounce of the actual mean amount being delivered to all containers.

26. A tire manufacturer states that a certain type of tire has a mean lifetime of 60,000 miles. Suppose lifetimes are normally distributed with standard deviation $\mathit{\sigma} = {\,\text{3,500}}$ miles.

    1.  Find the probability that if you buy one such tire, it will last only 57,000 or fewer miles. If you had this experience, is it particularly strong evidence that the tire is not as good as claimed?
    2.  A consumer group buys five such tires and tests them. Find the probability that average lifetime of the five tires will be 57,000 miles or less. If the mean is so low, is that particularly strong evidence that the tire is not as good as claimed?

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 128$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 3.67$
    2.  0.9936
2. &nbsp;
3.  1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 73.5$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 0.456$
    2.  0.0005
4. &nbsp;
5.  1.  0.0918
    2.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 25.6$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 1.1$
    3.  0.0000
6. &nbsp;
7.  1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 557$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 4.9497$
    2.  0.0043
8. &nbsp;
9.  1.  0.5818
    2.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 1214$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 24.4$
    3.  0.9998
10. &nbsp;
11. 1.  $\mathit{\mu}_{\overset{-}{\mathit{X}}} = 72$, $\mathit{\sigma}_{\overset{-}{\mathit{X}}} = 0.8944$
    2.  0.0250
12. &nbsp;

<!-- -->

13. 0.9940

14. &nbsp;

15. 0.9994

16. &nbsp;

17. 1.  0.8036
    2.  1.0000

18. &nbsp;

19. 0.9994

20. &nbsp;

21. 1.  0.2955
    2.  0.8977

22. &nbsp;

23. 0.9251

24. &nbsp;

<!-- -->

25. 0.9982

26. &nbsp;

`````````````

(src-fwk-shafer-ch06-s03)=

## 6.3 The Sample Proportion

````````````{note} Learning Objectives

1.  To recognize that the sample proportion $\hat{P}$ is a random variable.
2.  To understand the meaning of the formulas for the mean and standard deviation of the sample proportion.
3.  To learn what the sampling distribution of $\hat{P}$ is when the sample size is large.

````````````

Often sampling is done in order to estimate the proportion of a population that has a specific characteristic, such as the proportion of all items coming off an assembly line that are defective or the proportion of all people entering a retail store who make a purchase before leaving. The population proportion is denoted *p* and the sample proportion is denoted $\hat{p}.$ Thus if in reality 43% of people entering a store make a purchase before leaving, *p* = 0.43; if in a sample of 200 people entering the store, 78 make a purchase, $\hat{p} = 78/200 = 0.39.$

The sample proportion is a random variable: it varies from sample to sample in a way that cannot be predicted with certainty. Viewed as a random variable it will be written $\hat{P}.$ It has a mean[^stats-4] $\mathit{\mu}_{\hat{P}}$ and a standard deviation[^stats-5] $\mathit{\sigma}_{\hat{P}}.$ Here are formulas for their values.

Suppose random samples of size *n* are drawn from a population in which the proportion with a characteristic of interest is *p*. The mean $\mathit{\mu}_{\hat{P}}$ and standard deviation $\mathit{\sigma}_{\hat{P}}$ of the sample proportion $\hat{P}$ satisfy

$$\mathit{\mu}_{\hat{P}} = p\quad\quad\text{and}\quad\quad\mathit{\sigma}_{\hat{P}} = \sqrt{\frac{pq}{n}}$$

where $q = 1 - p.$

The Central Limit Theorem has an analogue for the population proportion $\hat{P}.$ To see how, imagine that every element of the population that has the characteristic of interest is labeled with a 1, and that every element that does not is labeled with a 0. This gives a numerical population consisting entirely of zeros and ones. Clearly the proportion of the population with the special characteristic is the proportion of the numerical population that are ones; in symbols,

$$p = \frac{\text{number}\,\text{of}\, 1\text{s}}{N}$$

But of course the sum of all the zeros and ones is simply the number of ones, so the mean *μ* of the numerical population is

$$\mathit{\mu} = \frac{\Sigma x}{N} = \frac{\text{number}\,\text{of}\, 1\text{s}}{N}$$

Thus the population proportion *p* is the same as the mean *μ* of the corresponding population of zeros and ones. In the same way the sample proportion $\hat{p}$ is the same as the sample mean $\overset{-}{\mathit{x}}.$ Thus the Central Limit Theorem applies to $\hat{P}.$ However, the condition that the sample be large is a little more complicated than just being of size at least 30.

````````````{important} The Sampling Distribution of the Sample Proportion

For large samples, the sample proportion is approximately normally distributed, with mean $\mathit{\mu}_{\hat{P}} = p$ and standard deviation $\mathit{\sigma}_{\hat{P}} = \sqrt{pq/n}.$

A sample is large if the interval $\left\lbrack {p\text{-}3\,\mathit{\sigma}_{\hat{P}},\, p + 3\,\mathit{\sigma}_{\hat{P}}} \right\rbrack$ lies wholly within the interval $\lbrack 0,1\rbrack.$

````````````

In actual practice *p* is not known, hence neither is $\mathit{\sigma}_{\hat{P}}.$ In that case in order to check that the sample is sufficiently large we substitute the known quantity $\hat{p}$ for *p*. This means checking that the interval

$$\left\lbrack {\hat{p}\text{-}3\,\sqrt{\frac{\hat{p}\left( 1 - \hat{p} \right)}{n}},\,\hat{p} + 3\,\sqrt{\frac{\hat{p}\left( 1 - \hat{p} \right)}{n}}}\, \right\rbrack$$

lies wholly within the interval $\lbrack 0,1\rbrack.$ This is illustrated in the examples.

[Figure 6.5 \"Distribution of Sample Proportions\"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s03-f05) shows that when *p* = 0.1 a sample of size 15 is too small but a sample of size 100 is acceptable. [Figure 6.6 \"Distribution of Sample Proportions for \"](/chapters/ch-06-sampling-distributions.md#src-fwk-shafer-ch06-s03-f06) shows that when *p* = 0.5 a sample of size 15 is acceptable.

``````{figure} /images/redrawn/fig-06-05.svg
:alt: Histograms of the sample proportion with normal curves overlaid, for p = 0.1. (a) For n = 15 the histogram is skewed right and the interval p ± 3√(p(1 − p)/n), from −0.13 to 0.33, extends below 0. (b) For n = 100 the histogram is nearly bell-shaped and the interval, from 0.01 to 0.19, lies within [0, 1].
:name: src-fwk-shafer-ch06-s03-f05

Figure 6.5 Distribution of Sample Proportions
``````

``````{figure} /images/redrawn/fig-06-06.svg
:alt: Histogram of the sample proportion for p = 0.5 and n = 15, symmetric about 0.5, with a normal curve overlaid; the interval p ± 3√(p(1 − p)/n), from 0.11 to 0.89, lies within [0, 1].
:name: src-fwk-shafer-ch06-s03-f06

Figure 6.6 Distribution of Sample Proportions for *p* = 0.5 and *n* = 15
``````

### Example 7

Suppose that in a population of voters in a certain region 38% are in favor of particular bond issue. Nine hundred randomly selected voters are asked if they favor the bond issue.

1.  Verify that the sample proportion $\hat{P}$ computed from samples of size 900 meets the condition that its sampling distribution be approximately normal.
2.  Find the probability that the sample proportion computed from a sample of size 900 will be within 5 percentage points of the true population proportion.

Solution

1.  The information given is that *p* = 0.38, hence $q = 1 - p = 0.62.$ First we use the formulas to compute the mean and standard deviation of $\hat{P}$:

    $$\mathit{\mu}_{\hat{P}} = p = 0.38\quad\text{and}\quad\mathit{\sigma}_{\hat{P}} = \sqrt{\frac{pq}{n}} = \sqrt{\frac{(0.38)(0.62)}{900}} = 0.01618$$

    Then $3\mathit{\sigma}_{\hat{P}} = 3(0.01618) = 0.04854 \approx 0.05$ so

    $$\left\lbrack {p\text{-}3\mathit{\sigma}_{\hat{P}},p + 3\mathit{\sigma}_{\hat{P}}} \right\rbrack = \left\lbrack {0.38 - 0.05,0.38 + 0.05} \right\rbrack = \left\lbrack {0.33,0.43} \right\rbrack$$

    which lies wholly within the interval $\lbrack 0,1\rbrack$, so it is safe to assume that $\hat{P}$ is approximately normally distributed.

2.  To be within 5 percentage points of the true population proportion 0.38 means to be between $0.38 - 0.05 = 0.33$ and $0.38 + 0.05 = 0.43.$ Thus

    $$\begin{array}{ll}
    {P\left( 0.33 < \hat{P} < 0.43 \right)} & {= P\left( {\frac{0.33 - \mathit{\mu}_{\hat{P}}}{\mathit{\sigma}_{\hat{P}}} < Z < \frac{0.43 - \mathit{\mu}_{\hat{P}}}{\mathit{\sigma}_{\hat{P}}}} \right)} \\
     & {= P\left( {\frac{0.33 - 0.38}{0.01618} < Z < \frac{0.43 - 0.38}{0.01618}} \right)} \\
     & {= P\left( {\text{-}3.09 < Z < 3.09} \right)} \\
     & {= P(3.09) - P\left( {\text{-}3.09} \right)} \\
     & {= 0.9990 - 0.0010 = 0.9980}
    \end{array}$$

### Example 8

An online retailer claims that 90% of all orders are shipped within 12 hours of being received. A consumer group placed 121 orders of different sizes and at different times of day; 102 orders were shipped within 12 hours.

1.  Compute the sample proportion of items shipped within 12 hours.
2.  Confirm that the sample is large enough to assume that the sample proportion is normally distributed. Use *p* = 0.90, corresponding to the assumption that the retailer's claim is valid.
3.  Assuming the retailer's claim is true, find the probability that a sample of size 121 would produce a sample proportion so low as was observed in this sample.
4.  Based on the answer to part (c), draw a conclusion about the retailer's claim.

Solution

1.  The sample proportion is the number *x* of orders that are shipped within 12 hours divided by the number *n* of orders in the sample:

    $$\hat{p} = \frac{x}{n} = \frac{102}{121} = 0.84$$

2.  Since *p* = 0.90, $q = 1 - p = 0.10$, and *n* = 121,

    $$\mathit{\sigma}_{\hat{P}} = \sqrt{\frac{(0.90)(0.10)}{121}} = 0.0\overset{-}{27}$$

    hence

    $$\left\lbrack {p\text{-}3\mathit{\sigma}_{\hat{P}},p + 3\mathit{\sigma}_{\hat{P}}} \right\rbrack = \left\lbrack {0.90 - 0.08,0.90 + 0.08} \right\rbrack = \left\lbrack {0.82,0.98} \right\rbrack$$

    Because

    $$\left\lbrack {0.82,\, 0.98} \right\rbrack \subset \lbrack 0,1\rbrack,$$

    it is appropriate to use the normal distribution to compute probabilities related to the sample proportion $\hat{P}.$

3.  Using the value of $\hat{P}$ from part (a) and the computation in part (b),

    $$\begin{array}{ll}
    {P\left( \hat{P} \leq 0.84 \right)} & {= P\left( {Z \leq \frac{0.84 - \mathit{\mu}_{\hat{P}}}{\mathit{\sigma}_{\hat{P}}}} \right)} \\
     & {= P\left( {Z \leq \frac{0.84 - 0.90}{0.0\overset{-}{27}}} \right)} \\
     & {= P\left( {Z \leq \text{-}2.20} \right) = 0.0139}
    \end{array}$$

4.  The computation shows that a random sample of size 121 has only about a 1.4% chance of producing a sample proportion as the one that was observed, $\hat{p} = 0.84$, when taken from a population in which the actual proportion is 0.90. This is so unlikely that it is reasonable to conclude that the actual value of *p* is less than the 90% claimed.

````````````{important} Key Takeaways

- The sample proportion is a random variable $\hat{P}.$
- There are formulas for the mean $\mathit{\mu}_{\hat{P}}$ and standard deviation $\mathit{\sigma}_{\hat{P}}$ of the sample proportion.
- When the sample size is large the sample proportion is normally distributed.

````````````

### Exercises

### Basic

1.  The proportion of a population with a characteristic of interest is *p* = 0.37. Find the mean and standard deviation of the sample proportion $\hat{P}$ obtained from random samples of size 1,600.

2.  The proportion of a population with a characteristic of interest is *p* = 0.82. Find the mean and standard deviation of the sample proportion $\hat{P}$ obtained from random samples of size 900.

3.  The proportion of a population with a characteristic of interest is *p* = 0.76. Find the mean and standard deviation of the sample proportion $\hat{P}$ obtained from random samples of size 1,200.

4.  The proportion of a population with a characteristic of interest is *p* = 0.37. Find the mean and standard deviation of the sample proportion $\hat{P}$ obtained from random samples of size 125.

5.  Random samples of size 225 are drawn from a population in which the proportion with the characteristic of interest is 0.25. Decide whether or not the sample size is large enough to assume that the sample proportion $\hat{P}$ is normally distributed.

6.  Random samples of size 1,600 are drawn from a population in which the proportion with the characteristic of interest is 0.05. Decide whether or not the sample size is large enough to assume that the sample proportion $\hat{P}$ is normally distributed.

7.  Random samples of size *n* produced sample proportions $\hat{p}$ as shown. In each case decide whether or not the sample size is large enough to assume that the sample proportion $\hat{P}$ is normally distributed.

    1.  *n* = 50, $\hat{p} = 0.48$
    2.  *n* = 50, $\hat{p} = 0.12$
    3.  *n* = 100, $\hat{p} = 0.12$

8.  Samples of size *n* produced sample proportions $\hat{p}$ as shown. In each case decide whether or not the sample size is large enough to assume that the sample proportion $\hat{P}$ is normally distributed.

    1.  *n* = 30, $\hat{p} = 0.72$
    2.  *n* = 30, $\hat{p} = 0.84$
    3.  *n* = 75, $\hat{p} = 0.84$

9.  A random sample of size 121 is taken from a population in which the proportion with the characteristic of interest is *p* = 0.47. Find the indicated probabilities.

    1.  $P\left( {0.45 \leq \hat{P} \leq 0.50} \right)$
    2.  $P\left( {\hat{P} \geq 0.50} \right)$

10. A random sample of size 225 is taken from a population in which the proportion with the characteristic of interest is *p* = 0.34. Find the indicated probabilities.

    1.  $P\left( {0.25 \leq \hat{P} \leq 0.40} \right)$
    2.  $P\left( {\hat{P} \leq 0.35} \right)$

11. A random sample of size 900 is taken from a population in which the proportion with the characteristic of interest is *p* = 0.62. Find the indicated probabilities.

    1.  $P\left( {0.60 \leq \hat{P} \leq 0.64} \right)$
    2.  $P\left( {0.57 \leq \hat{P} \leq 0.67} \right)$

12. A random sample of size 1,100 is taken from a population in which the proportion with the characteristic of interest is *p* = 0.28. Find the indicated probabilities.

    1.  $P\left( {0.27 \leq \hat{P} \leq 0.29} \right)$
    2.  $P\left( {0.23 \leq \hat{P} \leq 0.33} \right)$

### Applications

13. Suppose that 8% of all males suffer some form of color blindness. Find the probability that in a random sample of 250 men at least 10% will suffer some form of color blindness. First verify that the sample is sufficiently large to use the normal distribution.

14. Suppose that 29% of all residents of a community favor annexation by a nearby municipality. Find the probability that in a random sample of 50 residents at least 35% will favor annexation. First verify that the sample is sufficiently large to use the normal distribution.

15. Suppose that 2% of all cell phone connections by a certain provider are dropped. Find the probability that in a random sample of 1,500 calls at most 40 will be dropped. First verify that the sample is sufficiently large to use the normal distribution.

16. Suppose that in 20% of all traffic accidents involving an injury, driver distraction in some form (for example, changing a radio station or texting) is a factor. Find the probability that in a random sample of 275 such accidents between 15% and 25% involve driver distraction in some form. First verify that the sample is sufficiently large to use the normal distribution.

17. An airline claims that 72% of all its flights to a certain region arrive on time. In a random sample of 30 recent arrivals, 19 were on time. You may assume that the normal distribution applies.

    1.  Compute the sample proportion.
    2.  Assuming the airline's claim is true, find the probability of a sample of size 30 producing a sample proportion so low as was observed in this sample.

18. A humane society reports that 19% of all pet dogs were adopted from an animal shelter. Assuming the truth of this assertion, find the probability that in a random sample of 80 pet dogs, between 15% and 20% were adopted from a shelter. You may assume that the normal distribution applies.

19. In one study it was found that 86% of all homes have a functional smoke detector. Suppose this proportion is valid for all homes. Find the probability that in a random sample of 600 homes, between 80% and 90% will have a functional smoke detector. You may assume that the normal distribution applies.

20. A state insurance commission estimates that 13% of all motorists in its state are uninsured. Suppose this proportion is valid. Find the probability that in a random sample of 50 motorists, at least 5 will be uninsured. You may assume that the normal distribution applies.

21. An outside financial auditor has observed that about 4% of all documents he examines contain an error of some sort. Assuming this proportion to be accurate, find the probability that a random sample of 700 documents will contain at least 30 with some sort of error. You may assume that the normal distribution applies.

22. Suppose 7% of all households have no home telephone but depend completely on cell phones. Find the probability that in a random sample of 450 households, between 25 and 35 will have no home telephone. You may assume that the normal distribution applies.

### Additional Exercises

23. Some countries allow individual packages of prepackaged goods to weigh less than what is stated on the package, subject to certain conditions, such as the average of all packages being the stated weight or greater. Suppose that one requirement is that at most 4% of all packages marked 500 grams can weigh less than 490 grams. Assuming that a product actually meets this requirement, find the probability that in a random sample of 150 such packages the proportion weighing less than 490 grams is at least 3%. You may assume that the normal distribution applies.

24. An economist wishes to investigate whether people are keeping cars longer now than in the past. He knows that five years ago, 38% of all passenger vehicles in operation were at least ten years old. He commissions a study in which 325 automobiles are randomly sampled. Of them, 132 are ten years old or older.

    1.  Find the sample proportion.
    2.  Find the probability that, when a sample of size 325 is drawn from a population in which the true proportion is 0.38, the sample proportion will be as large as the value you computed in part (a). You may assume that the normal distribution applies.
    3.  Give an interpretation of the result in part (b). Is there strong evidence that people are keeping their cars longer than was the case five years ago?

25. A state public health department wishes to investigate the effectiveness of a campaign against smoking. Historically 22% of all adults in the state regularly smoked cigars or cigarettes. In a survey commissioned by the public health department, 279 of 1,500 randomly selected adults stated that they smoke regularly.

    1.  Find the sample proportion.
    2.  Find the probability that, when a sample of size 1,500 is drawn from a population in which the true proportion is 0.22, the sample proportion will be no larger than the value you computed in part (a). You may assume that the normal distribution applies.
    3.  Give an interpretation of the result in part (b). How strong is the evidence that the campaign to reduce smoking has been effective?

26. In an effort to reduce the population of unwanted cats and dogs, a group of veterinarians set up a low-cost spay/neuter clinic. At the inception of the clinic a survey of pet owners indicated that 78% of all pet dogs and cats in the community were spayed or neutered. After the low-cost clinic had been in operation for three years, that figure had risen to 86%.

    1.  What information is missing that you would need to compute the probability that a sample drawn from a population in which the proportion is 78% (corresponding to the assumption that the low-cost clinic had had no effect) is as high as 86%?
    2.  Knowing that the size of the original sample three years ago was 150 and that the size of the recent sample was 125, compute the probability mentioned in part (a). You may assume that the normal distribution applies.
    3.  Give an interpretation of the result in part (b). How strong is the evidence that the presence of the low-cost clinic has increased the proportion of pet dogs and cats that have been spayed or neutered?

27. An ordinary die is "fair" or "balanced" if each face has an equal chance of landing on top when the die is rolled. Thus the proportion of times a three is observed in a large number of tosses is expected to be close to 1/6 or $0.1\overset{-}{6}.$ Suppose a die is rolled 240 times and shows three on top 36 times, for a sample proportion of 0.15.

    1.  Find the probability that a fair die would produce a proportion of 0.15 or less. You may assume that the normal distribution applies.
    2.  Give an interpretation of the result in part (b). How strong is the evidence that the die is not fair?
    3.  Suppose the sample proportion 0.15 came from rolling the die 2,400 times instead of only 240 times. Rework part (a) under these circumstances.
    4.  Give an interpretation of the result in part (c). How strong is the evidence that the die is not fair?

`````````````{admonition} Answers
:class: dropdown

1.  $\mathit{\mu}_{\hat{P}} = 0.37$, $\mathit{\sigma}_{\hat{P}} = 0.012$

2. &nbsp;

3.  $\mathit{\mu}_{\hat{P}} = 0.76$, $\mathit{\sigma}_{\hat{P}} = 0.012$

4. &nbsp;

5.  $p \pm 3\sqrt{\frac{pq}{n}} = 0.25 \pm 0.087$, yes

6. &nbsp;

7.  1.  $\hat{p} \pm 3\sqrt{\frac{\hat{p}\hat{q}}{n}} = 0.48 \pm 0.21$, yes
    2.  $\hat{p} \pm 3\sqrt{\frac{\hat{p}\hat{q}}{n}} = 0.12 \pm 0.14$, no
    3.  $\hat{p} \pm 3\sqrt{\frac{\hat{p}\hat{q}}{n}} = 0.12 \pm 0.10$, yes

8. &nbsp;

9.  1.  0.4154
    2.  0.2546

10. &nbsp;

11. 1.  0.7850
    2.  0.9980

12. &nbsp;

<!-- -->

13. $p \pm 3\sqrt{\frac{pq}{n}} = 0.08 \pm 0.05$

    and

    $\left\lbrack {0.03,0.13} \right\rbrack \subset {\lbrack 0,1\rbrack,0.1210}$

14. &nbsp;

15. $p \pm 3\sqrt{\frac{pq}{n}} = 0.02 \pm 0.01$

    and

    $\left\lbrack {0.01,0.03} \right\rbrack \subset {\lbrack 0,1\rbrack,0.9671}$

16. &nbsp;

17. 1.  0.63
    2.  0.1446

18. &nbsp;

19. 0.9977

20. &nbsp;

21. 0.3483

22. &nbsp;

<!-- -->

23. 0.7357

24. &nbsp;

25. 1.  0.186
    2.  0.0007
    3.  In a population in which the true proportion is 22% the chance that a random sample of size 1500 would produce a sample proportion of 18.6% or less is only 7/100 of 1%. This is strong evidence that currently a smaller proportion than 22% smoke.

26. &nbsp;

27. 1.  0.2451
    2.  We would expect a sample proportion of 0.15 or less in about 24.5% of all samples of size 240, so this is practically no evidence at all that the die is not fair.
    3.  0.0139
    4.  We would expect a sample proportion of 0.15 or less in only about 1.4% of all samples of size 2400, so this is strong evidence that the die is not fair.

`````````````

[^stats-1]: The probability distribution of a sample statistic when the statistic is viewed as a random variable.

[^stats-2]: The number about which means computed from samples of the same size center.

[^stats-3]: A measure of the variability of means computed from samples of the same size.

[^stats-4]: The number about which proportions computed from samples of the same size center.

[^stats-5]: A measure of the variability of proportions computed from samples of the same size.
