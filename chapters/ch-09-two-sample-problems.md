(src-fwk-shafer-ch09)=

# Chapter 9 Two-Sample Problems

The previous two chapters treated the questions of estimating and making inferences about a parameter of a single population. In this chapter we consider a comparison of parameters that belong to two different populations. For example, we might wish to compare the average income of all adults in one region of the country with the average income of those in another region, or we might wish to compare the proportion of all men who are vegetarians with the proportion of all women who are vegetarians.

We will study construction of confidence intervals and tests of hypotheses in four situations, depending on the parameter of interest, the sizes of the samples drawn from each of the populations, and the method of sampling. We also examine sample size considerations.

## 9.1 Comparison of Two Population Means: Large, Independent Samples

````````````{note} Learning Objectives

1.  To understand the logical framework for estimating the difference between the means of two distinct populations and performing tests of hypotheses concerning those means.
2.  To learn how to construct a confidence interval for the difference in the means of two distinct populations using large, independent samples.
3.  To learn how to perform a test of hypotheses concerning the difference between the means of two distinct populations using large, independent samples.

````````````

Suppose we wish to compare the means of two distinct populations. [Figure 9.1 \"Independent Sampling from Two Populations\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-f01) illustrates the conceptual framework of our investigation in this and the next section. Each population has a mean and a standard deviation. We arbitrarily label one population as Population 1 and the other as Population 2, and subscript the parameters with the numbers 1 and 2 to tell them apart. We draw a random sample from Population 1 and label the sample statistics it yields with the subscript 1. Without reference to the first sample we draw a sample from Population 2 and label its sample statistics with the subscript 2.

``````{figure} /images/redrawn/fig-09-01.svg
:alt: Two boxes labeled Population 1 and Population 2, with means μ₁ and μ₂ and standard deviations σ₁ and σ₂. An arrow from each leads to a box for its sample, Sample 1 or Sample 2, with size n₁ or n₂, mean x̄₁ or x̄₂, and standard deviation s₁ or s₂.
:name: src-fwk-shafer-ch09-s01-f01

Figure 9.1 Independent Sampling from Two Populations
``````

````````````{important} Definition

*Samples from two distinct populations are* **independent** *if each one is drawn without reference to the other, and has no connection with the other.*

````````````

Our goal is to use the information in the *samples* to estimate the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ in the means of the two *populations* and to make statistically valid inferences about it.

### Confidence Intervals

Since the mean ${\overset{-}{x}}_{1}$ of the sample drawn from Population 1 is a good estimator of $\mathit{\mu}_{1}$ and the mean ${\overset{-}{x}}_{2}$ of the sample drawn from Population 2 is a good estimator of $\mathit{\mu}_{2}$, a reasonable point estimate of the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ is ${\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}.$ In order to widen this point estimate into a confidence interval, we first suppose that both samples are large, that is, that both $n_{1} \geq 30$ and $n_{2} \geq 30.$ If so, then the following formula for a confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ is valid. The symbols $s_{1}^{2}$ and $s_{2}^{2}$ denote the squares of *s*<sub>1</sub> and *s*<sub>2</sub>. (In the relatively rare case that both population standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ are known they would be used instead of the sample standard deviations.)

````````````{important} $100\left( {1 - \alpha} \right)\%$ Confidence Interval for the Difference Between Two Population Means: Large, Independent Samples

$$\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) \pm z_{\alpha / 2}\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}$$

The samples must be independent, and *each* sample must be large: $n_{1} \geq 30$ and $n_{2} \geq 30.$

````````````

(src-fwk-shafer-ch09-s01-s01-n02)=

### Example 1

To compare customer satisfaction levels of two competing cable television companies, 174 customers of Company 1 and 355 customers of Company 2 were randomly selected and were asked to rate their cable companies on a five-point scale, with 1 being least satisfied and 5 most satisfied. The survey results are summarized in the following table:

````````{list-table}
:header-rows: 1

- - Company 1
  - Company 2
- - $n_{1} = 174$
  - $n_{2} = 355$
- - ${\overset{-}{x}}_{1} = 3.51$
  - ${\overset{-}{x}}_{2} = 3.24$
- - $s_{1} = 0.51$
  - $s_{2} = 0.52$

````````

Construct a point estimate and a 99% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$, the difference in average satisfaction levels of customers of the two companies as measured on this five-point scale.

Solution:

The point estimate of $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ is

$${\overset{-}{x}}_{1} - {\overset{-}{x}}_{2} = 3.51 - 3.24 = 0.27.$$

In words, we estimate that the average customer satisfaction level for Company 1 is 0.27 points higher on this five-point scale than it is for Company 2.

To apply the formula for the confidence interval, proceed exactly as was done in [Chapter 7 \"Estimation\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07). The 99% confidence level means that $\alpha = 1 - 0.99 = 0.01$ so that $z_{\alpha / 2} = z_{0.005}.$ From [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we read directly that $z_{0.005} = 2.576.$ Thus

$$\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) \pm z_{\alpha / 2}\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}} = 0.27 \pm 2.576\sqrt{\frac{0.51^{2}}{174} + \frac{0.52^{2}}{355}} = 0.27 \pm 0.12$$

We are 99% confident that the difference in the population means lies in the interval $\left\lbrack {0.15,0.39} \right\rbrack$, in the sense that in repeated sampling 99% of all intervals constructed from the sample data in this manner will contain $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$ In the context of the problem we say we are 99% confident that the average level of customer satisfaction for Company 1 is between 0.15 and 0.39 points higher, on this five-point scale, than that for Company 2.

### Hypothesis Testing

Hypotheses concerning the relative sizes of the means of two populations are tested using the same critical value and *p*-value procedures that were used in the case of a single population. All that is needed is to know how to express the null and alternative hypotheses and to know the formula for the standardized test statistic and the distribution that it follows.

The null and alternative hypotheses will always be expressed in terms of the difference of the two population means. Thus the null hypothesis will always be written

$$H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = D_{0}$$

where *D*<sub>0</sub> is a number that is deduced from the statement of the situation. As was the case with a single population the alternative hypothesis can take one of the three forms, with the same terminology:

````````{list-table}
:header-rows: 1

- - Form of $H_{a}$
  - Terminology
- - $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < D_{0}$
  - Left-tailed
- - $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > D_{0}$
  - Right-tailed
- - $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq D_{0}$
  - Two-tailed

````````

As long as the samples are independent and both are large the following formula for the standardized test statistic is valid, and it has the standard normal distribution. (In the relatively rare case that both population standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ are known they would be used instead of the sample standard deviations.)

````````````{important} Standardized Test Statistic for Hypothesis Tests Concerning the Difference Between Two Population Means: Large, Independent Samples

$$Z = \frac{\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) - D_{0}}{\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}}$$

The test statistic has the standard normal distribution.

The samples must be independent, and *each* sample must be large: $n_{1} \geq 30$ and $n_{2} \geq 30.$

````````````

(src-fwk-shafer-ch09-s01-s02-n02)=

### Example 2

Refer to [Note 9.4 \"Example 1\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s01-n02) concerning the mean satisfaction levels of customers of two competing cable television companies. Test at the 1% level of significance whether the data provide sufficient evidence to conclude that Company 1 has a higher mean satisfaction rating than does Company 2. Use the critical value approach.

Solution:

- Step 1. If the mean satisfaction levels $\mathit{\mu}_{1}$ and $\mathit{\mu}_{2}$ are the same then $\mathit{\mu}_{1} = \mathit{\mu}_{2}$, but we always express the null hypothesis in terms of the difference between $\mathit{\mu}_{1}$ and $\mathit{\mu}_{2}$, hence *H*<sub>0</sub> is $\mathit{\mu}_{1} - \mathit{\mu}_{2} = 0.$ To say that the mean customer satisfaction for Company 1 is higher than that for Company 2 means that $\mathit{\mu}_{1} > \mathit{\mu}_{2}$, which in terms of their difference is $\mathit{\mu}_{1} - \mathit{\mu}_{2} > 0.$ The test is therefore

  $$\begin{array}{rccc}
  {H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2}} & = & 0 & \\
  {\text{ vs. }\, H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2}} & > & 0 & {@\,\alpha = 0.01}
  \end{array}$$

- Step 2. Since the samples are independent and both are large the test statistic is

  $$Z = \frac{\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) - D_{0}}{\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}}$$

- Step 3. Inserting the data into the formula for the test statistic gives

  $$Z = \frac{\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) - D_{0}}{\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}} = \frac{\left( {3.51 - 3.24} \right)\text{-}0}{\sqrt{\frac{0.51^{2}}{174} + \frac{0.52^{2}}{355}}} = 5.684$$

- Step 4. Since the symbol in *H<sub>a</sub>* is "\>" this is a right-tailed test, so there is a single critical value, $z_{\alpha} = z_{0.01}$, which from the last line in [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we read off as 2.326. The rejection region is $\left\lbrack {2.326,\infty} \right).$

  ``````{figure} /images/redrawn/fig-09-02.svg
  :alt: Standard normal curve for Hₐ: μ₁ − μ₂ > 0. The right tail of area α = 0.01 is shaded above the critical value z_α = 2.326. On the number line below, the rejection region z ≥ 2.326 is red, and the test statistic Z = 5.684, marked with a star near the right end, lies far inside it.
  :name: src-fwk-shafer-ch09-s01-s02-f01

  Figure 9.2 Rejection Region and Test Statistic for [Note 9.6 \"Example 2\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-n02){.xref xrefstyle="select: title"}
  ``````

- Step 5. As shown in [Figure 9.2 \"Rejection Region and Test Statistic for \"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-f01) the test statistic falls in the rejection region. The decision is to reject *H*<sub>0</sub>. In the context of the problem our conclusion is:

  The data provide sufficient evidence, at the 1% level of significance, to conclude that the mean customer satisfaction for Company 1 is higher than that for Company 2.

(src-fwk-shafer-ch09-s01-s02-n03)=

### Example 3

Perform the test of [Note 9.6 \"Example 2\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-n02) using the *p*-value approach.

Solution:

The first three steps are identical to those in [Note 9.6 \"Example 2\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-n02).

- Step 4. The observed significance or *p*-value of the test is the area of the right tail of the standard normal distribution that is cut off by the test statistic *Z* = 5.684. The number 5.684 is too large to appear in [Figure 12.2 \"Cumulative Normal Probability\"](/appendices/appendix.md#src-fwk-shafer-ch12-f02), which means that the area of the *left* tail that it cuts off is 1.0000 to four decimal places. The area that we seek, the area of the *right* tail, is therefore $1 - 1.0000 = 0.0000$ to four decimal places. See [Figure 9.3](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-f02). That is, $p\text{ -value} = 0.0000$ to four decimal places. (The actual value is approximately $0.000\, 000\, 007.$)

``````{figure} /images/redrawn/fig-09-03.svg
:alt: Standard normal curve with the test statistic Z = 5.684 marked near the right end of the z axis. The area to its left is labeled area ≈ 1.0000; the vanishing tail to its right is labeled area = p-value ≈ 0.000.
:name: src-fwk-shafer-ch09-s01-s02-f02

Figure 9.3 *P*-Value for [Note 9.7 \"Example 3\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s01-s02-n03){.xref xrefstyle="select: title"}
``````

- Step 5. Since 0.0000 \< 0.01, $p\text{ -value} < \alpha$ so the decision is to reject the null hypothesis:

  The data provide sufficient evidence, at the 1% level of significance, to conclude that the mean customer satisfaction for Company 1 is higher than that for Company 2.

````````````{important} Key Takeaways

- A point estimate for the difference in two population means is simply the difference in the corresponding sample means.
- In the context of estimating or testing hypotheses concerning two population means, "large" samples means that *both* samples are large.
- A confidence interval for the difference in two population means is computed using a formula in the same fashion as was done for a single population mean.
- The same five-step procedure used to test hypotheses concerning a single population mean is used to test hypotheses concerning the difference between two population means. The only difference is in the formula for the standardized test statistic.

````````````

### Exercises

### Basic

1.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  90% confidence,

        $n_{1} = 45$, ${\overset{-}{x}}_{1} = 27$, $s_{1} = 2$

        $n_{2} = 60$, ${\overset{-}{x}}_{2} = 22$, $s_{2} = 3$

    2.  99% confidence,

        $n_{1} = 30$, ${\overset{-}{x}}_{1} = \text{-}112$, $s_{1} = 9$

        $n_{2} = 40$, ${\overset{-}{x}}_{2} = \text{-}98$, $s_{2} = 4$

2.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  95% confidence,

        $n_{1} = 110$, ${\overset{-}{x}}_{1} = 77$, $s_{1} = 15$

        $n_{2} = 85$, ${\overset{-}{x}}_{2} = 79$, $s_{2} = 21$

    2.  90% confidence,

        $n_{1} = 65$, ${\overset{-}{x}}_{1} = \text{-}83$, $s_{1} = 12$

        $n_{2} = 65$, ${\overset{-}{x}}_{2} = \text{-}74$, $s_{2} = 8$

3.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  99.5% confidence,

        $n_{1} = 130$, ${\overset{-}{x}}_{1} = 27.2$, $s_{1} = 2.5$

        $n_{2} = 155$, ${\overset{-}{x}}_{2} = 38.8$, $s_{2} = 4.6$

    2.  95% confidence,

        $n_{1} = 68$, ${\overset{-}{x}}_{1} = 215.5$, $s_{1} = 12.3$

        $n_{2} = 84$, ${\overset{-}{x}}_{2} = 287.8$, $s_{2} = 14.1$

4.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  99.9% confidence,

        $n_{1} = 275$, ${\overset{-}{x}}_{1} = 70.2$, $s_{1} = 1.5$

        $n_{2} = 325$, ${\overset{-}{x}}_{2} = 63.4$, $s_{2} = 1.1$

    2.  90% confidence,

        $n_{1} = 120$, ${\overset{-}{x}}_{1} = 35.5$, $s_{1} = 0.75$

        $n_{2} = 146$, ${\overset{-}{x}}_{2} = 29.6$, $s_{2} = 0.80$

5.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach. Compute the *p*-value of the test as well.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 3$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 3$ @ $\alpha = 0.05$,

        $n_{1} = 35$, ${\overset{-}{x}}_{1} = 25$, $s_{1} = 1$

        $n_{2} = 45$, ${\overset{-}{x}}_{2} = 19$, $s_{2} = 2$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}25$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < \text{-}25$ @ $\alpha = 0.10$,

        $n_{1} = 85$, ${\overset{-}{x}}_{1} = 188$, $s_{1} = 15$

        $n_{2} = 62$, ${\overset{-}{x}}_{2} = 215$, $s_{2} = 19$

6.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach. Compute the *p*-value of the test as well.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 45$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 45$ @ $\alpha = 0.001$,

        $n_{1} = 200$, ${\overset{-}{x}}_{1} = 1312$, $s_{1} = 35$

        $n_{2} = 225$, ${\overset{-}{x}}_{2} = 1256$, $s_{2} = 28$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}12$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}12$ @ $\alpha = 0.10$,

        $n_{1} = 35$, ${\overset{-}{x}}_{1} = 121$, $s_{1} = 6$

        $n_{2} = 40$, ${\overset{-}{x}}_{2} = 135$, $s_{2} = 7$

7.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach. Compute the *p*-value of the test as well.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 0$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 0$ @ $\alpha = 0.01$,

        $n_{1} = 125$, ${\overset{-}{x}}_{1} = \text{-}46$, $s_{1} = 10$

        $n_{2} = 90$, ${\overset{-}{x}}_{2} = \text{-}50$, $s_{2} = 13$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 20$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 20$ @ $\alpha = 0.05$,

        $n_{1} = 40$, ${\overset{-}{x}}_{1} = 142$, $s_{1} = 11$

        $n_{2} = 40$, ${\overset{-}{x}}_{2} = 118$, $s_{2} = 10$

8.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach. Compute the *p*-value of the test as well.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 13$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < 13$ @ $\alpha = 0.01$,

        $n_{1} = 35$, ${\overset{-}{x}}_{1} = 100$, $s_{1} = 2$

        $n_{2} = 35$, ${\overset{-}{x}}_{2} = 88$, $s_{2} = 2$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}10$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}10$ @ $\alpha = 0.10$,

        $n_{1} = 146$, ${\overset{-}{x}}_{1} = 62$, $s_{1} = 4$

        $n_{2} = 120$, ${\overset{-}{x}}_{2} = 73$, $s_{2} = 7$

9.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 57$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < 57$ @ $\alpha = 0.10$,

        $n_{1} = 117$, ${\overset{-}{x}}_{1} = 1309$, $s_{1} = 42$

        $n_{2} = 133$, ${\overset{-}{x}}_{2} = 1258$, $s_{2} = 37$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}1.5$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}1.5$ @ $\alpha = 0.20$,

        $n_{1} = 65$, ${\overset{-}{x}}_{1} = 16.9$, $s_{1} = 1.3$

        $n_{2} = 57$, ${\overset{-}{x}}_{2} = 18.6$, $s_{2} = 1.1$

10. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}10.5$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > \text{-}10.5$ @ $\alpha = 0.01$,

        $n_{1} = 64$, ${\overset{-}{x}}_{1} = 85.6$, $s_{1} = 2.4$

        $n_{2} = 50$, ${\overset{-}{x}}_{2} = 95.3$, $s_{2} = 3.1$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 110$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 110$ @ $\alpha = 0.02$,

        $n_{1} = 176$, ${\overset{-}{x}}_{1} = 1918$, $s_{1} = 68$

        $n_{2} = 241$, ${\overset{-}{x}}_{2} = 1782$, $s_{2} = 146$

11. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 50$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 50$ @ $\alpha = 0.005$,

        $n_{1} = 72$, ${\overset{-}{x}}_{1} = 272$, $s_{1} = 26$

        $n_{2} = 103$, ${\overset{-}{x}}_{2} = 213$, $s_{2} = 14$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 7.5$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 7.5$ @ $\alpha = 0.10$,

        $n_{1} = 52$, ${\overset{-}{x}}_{1} = 94.3$, $s_{1} = 2.6$

        $n_{2} = 38$, ${\overset{-}{x}}_{2} = 88.6$, $s_{2} = 8.0$

12. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 23$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < 23$ @ $\alpha = 0.20$,

        $n_{1} = 314$, ${\overset{-}{x}}_{1} = 198$, $s_{1} = 12.2$

        $n_{2} = 220$, ${\overset{-}{x}}_{2} = 176$, $s_{2} = 11.5$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 4.4$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 4.4$ @ $\alpha = 0.05$,

        $n_{1} = 32$, ${\overset{-}{x}}_{1} = 40.3$, $s_{1} = 0.5$

        $n_{2} = 30$, ${\overset{-}{x}}_{2} = 35.5$, $s_{2} = 0.7$

### Applications

13. In order to investigate the relationship between mean job tenure in years among workers who have a bachelor's degree or higher and those who do not, random samples of each type of worker were taken, with the following results.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Bachelor's degree or higher
      - 155
      - 5.2
      - 1.3
    - - No degree
      - 210
      - 5.0
      - 1.5

    ````````

    1.  Construct the 99% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 1% level of significance, the claim that mean job tenure among those with higher education is greater than among those without, against the default that there is no difference in the means.
    3.  Compute the observed significance of the test.

14. Records of 40 used passenger cars and 40 used pickup trucks (none used commercially) were randomly selected to investigate whether there was any difference in the mean time in years that they were kept by the original owner before being sold. For cars the mean was 5.3 years with standard deviation 2.2 years. For pickup trucks the mean was 7.1 years with standard deviation 3.0 years.

    1.  Construct the 95% confidence interval for the difference in the means based on these data.
    2.  Test the hypothesis that there is a difference in the means against the null hypothesis that there is no difference. Use the 1% level of significance.
    3.  Compute the observed significance of the test in part (b).

15. In previous years the average number of patients per hour at a hospital emergency room on weekends exceeded the average on weekdays by 6.3 visits per hour. A hospital administrator believes that the current weekend mean exceeds the weekday mean by fewer than 6.3 hours.

    1.  Construct the 99% confidence interval for the difference in the population means based on the following data, derived from a study in which 30 weekend and 30 weekday one-hour periods were randomly selected and the number of new patients in each recorded.

        ````````{list-table}
        :header-rows: 1

        - -
          - *n*
          - $\overset{-}{x}$
          - *s*
        - - Weekends
          - 30
          - 13.8
          - 3.1
        - - Weekdays
          - 30
          - 8.6
          - 2.7

        ````````

    2.  Test at the 5% level of significance whether the current weekend mean exceeds the weekday mean by fewer than 6.3 patients per hour.

    3.  Compute the observed significance of the test.

16. A sociologist surveys 50 randomly selected citizens in each of two countries to compare the mean number of hours of volunteer work done by adults in each. Among the 50 inhabitants of Lilliput, the mean hours of volunteer work per year was 52, with standard deviation 11.8. Among the 50 inhabitants of Blefuscu, the mean number of hours of volunteer work per year was 37, with standard deviation 7.2.

    1.  Construct the 99% confidence interval for the difference in mean number of hours volunteered by all residents of Lilliput and the mean number of hours volunteered by all residents of Blefuscu.
    2.  Test, at the 1% level of significance, the claim that the mean number of hours volunteered by all residents of Lilliput is more than ten hours greater than the mean number of hours volunteered by all residents of Blefuscu.
    3.  Compute the observed significance of the test in part (b).

17. A university administrator asserted that upperclassmen spend more time studying than underclassmen.

    1.  Test this claim against the default that the average number of hours of study per week by the two groups is the same, using the following information based on random samples from each group of students. Test at the 1% level of significance.

        ````````{list-table}
        :header-rows: 1

        - -
          - *n*
          - $\overset{-}{x}$
          - *s*
        - - Upperclassmen
          - 35
          - 15.6
          - 2.9
        - - Underclassmen
          - 35
          - 12.3
          - 4.1

        ````````

    2.  Compute the observed significance of the test.

18. An kinesiologist claims that the resting heart rate of men aged 18 to 25 who exercise regularly is more than five beats per minute less than that of men who do not exercise regularly. Men in each category were selected at random and their resting heart rates were measured, with the results shown.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Regular exercise
      - 40
      - 63
      - 1.0
    - - No regular exercise
      - 30
      - 71
      - 1.2

    ````````

    1.  Perform the relevant test of hypotheses at the 1% level of significance.
    2.  Compute the observed significance of the test.

19. Children in two elementary school classrooms were given two versions of the same test, but with the order of questions arranged from easier to more difficult in Version *A* and in reverse order in Version *B*. Randomly selected students from each class were given Version *A* and the rest Version *B*. The results are shown in the table.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Version *A*
      - 31
      - 83
      - 4.6
    - - Version *B*
      - 32
      - 78
      - 4.3

    ````````

    1.  Construct the 90% confidence interval for the difference in the means of the populations of all children taking Version *A* of such a test and of all children taking Version *B* of such a test.
    2.  Test at the 1% level of significance the hypothesis that the *A* version of the test is easier than the *B* version (even though the questions are the same).
    3.  Compute the observed significance of the test.

20. The Municipal Transit Authority wants to know if, on weekdays, more passengers ride the northbound blue line train towards the city center that departs at 8:15 a.m. or the one that departs at 8:30 a.m. The following sample statistics are assembled by the Transit Authority.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - 8:15 a.m. train
      - 30
      - 323
      - 41
    - - 8:30 a.m. train
      - 45
      - 356
      - 45

    ````````

    1.  Construct the 90% confidence interval for the difference in the mean number of daily travelers on the 8:15 train and the mean number of daily travelers on the 8:30 train.
    2.  Test at the 5% level of significance whether the data provide sufficient evidence to conclude that more passengers ride the 8:30 train.
    3.  Compute the observed significance of the test.

21. In comparing the academic performance of college students who are affiliated with fraternities and those male students who are unaffiliated, a random sample of students was drawn from each of the two populations on a university campus. Summary statistics on the student GPAs are given below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Fraternity
      - 645
      - 2.90
      - 0.47
    - - Unaffiliated
      - 450
      - 2.88
      - 0.42

    ````````

    Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that there is a difference in average GPA between the population of fraternity students and the population of unaffiliated male students on this university campus.

22. In comparing the academic performance of college students who are affiliated with sororities and those female students who are unaffiliated, a random sample of students was drawn from each of the two populations on a university campus. Summary statistics on the student GPAs are given below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Sorority
      - 330
      - 3.18
      - 0.37
    - - Unaffiliated
      - 550
      - 3.12
      - 0.41

    ````````

    Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that there is a difference in average GPA between the population of sorority students and the population of unaffiliated female students on this university campus.

23. The owner of a professional football team believes that the league has become more offense oriented since five years ago. To check his belief, 32 randomly selected games from one year's schedule were compared to 32 randomly selected games from the schedule five years later. Since more offense produces more points per game, the owner analyzed the following information on points per game (ppg).

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - ppg previously
      - 32
      - 20.62
      - 4.17
    - - ppg recently
      - 32
      - 22.05
      - 4.01

    ````````

    Test, at the 10% level of significance, whether the data on points per game provide sufficient evidence to conclude that the game has become more offense oriented.

24. The owner of a professional football team believes that the league has become more offense oriented since five years ago. To check his belief, 32 randomly selected games from one year's schedule were compared to 32 randomly selected games from the schedule five years later. Since more offense produces more offensive yards per game, the owner analyzed the following information on offensive yards per game (oypg).

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - oypg previously
      - 32
      - 316
      - 40
    - - oypg recently
      - 32
      - 336
      - 35

    ````````

    Test, at the 10% level of significance, whether the data on offensive yards per game provide sufficient evidence to conclude that the game has become more offense oriented.

### Large Data Set Exercises

25. Large Data Sets 1A and 1B list the SAT scores for 1,000 randomly selected students. Denote the population of all male students as Population 1 and the population of all female students as Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data1A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data1B.xls>

    1.  Restricting attention to just the males, find *n*<sub>1</sub>, ${\overset{-}{x}}_{1}$, and *s*<sub>1</sub>. Restricting attention to just the females, find *n*<sub>2</sub>, ${\overset{-}{x}}_{2}$, and *s*<sub>2</sub>.
    2.  Let $\mathit{\mu}_{1}$ denote the mean SAT score for all males and $\mathit{\mu}_{2}$ the mean SAT score for all females. Use the results of part (a) to construct a 90% confidence interval for the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$
    3.  Test, at the 5% level of significance, the hypothesis that the mean SAT scores among males exceeds that of females.

26. Large Data Sets 1A and 1B list the GPAs for 1,000 randomly selected students. Denote the population of all male students as Population 1 and the population of all female students as Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data1A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data1B.xls>

    1.  Restricting attention to just the males, find *n*<sub>1</sub>, ${\overset{-}{x}}_{1}$, and *s*<sub>1</sub>. Restricting attention to just the females, find *n*<sub>2</sub>, ${\overset{-}{x}}_{2}$, and *s*<sub>2</sub>.
    2.  Let $\mathit{\mu}_{1}$ denote the mean GPA for all males and $\mathit{\mu}_{2}$ the mean GPA for all females. Use the results of part (a) to construct a 95% confidence interval for the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$
    3.  Test, at the 10% level of significance, the hypothesis that the mean GPAs among males and females differ.

27. Large Data Sets 7A and 7B list the survival times for 65 male and 75 female laboratory mice with thymic leukemia. Denote the population of all such male mice as Population 1 and the population of all such female mice as Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data7A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data7B.xls>

    1.  Restricting attention to just the males, find *n*<sub>1</sub>, ${\overset{-}{x}}_{1}$, and *s*<sub>1</sub>. Restricting attention to just the females, find *n*<sub>2</sub>, ${\overset{-}{x}}_{2}$, and *s*<sub>2</sub>.
    2.  Let $\mathit{\mu}_{1}$ denote the mean survival for all males and $\mathit{\mu}_{2}$ the mean survival time for all females. Use the results of part (a) to construct a 99% confidence interval for the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$
    3.  Test, at the 1% level of significance, the hypothesis that the mean survival time for males exceeds that for females by more than 182 days (half a year).
    4.  Compute the observed significance of the test in part (c).

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\left( {4.20,5.80} \right)$,
    2.  $\left( {\text{-}18.54,\text{-}9.46} \right)$
2. &nbsp;
3.  1.  $\left( {\text{-}12.81,\text{-}10.39} \right)$,
    2.  $\left( {\text{-}76.50,\text{-}68.10} \right)$
4. &nbsp;
5.  1.  *Z* = 8.753, $\pm z_{0.025} = \pm 1.960$, reject *H*<sub>0</sub>, *p*-value = 0.0000;
    2.  $Z = \text{-}0.687$, $\text{-}z_{0.10} = \text{-}1.282$, do not reject *H*<sub>0</sub>, *p*-value = 0.2451
6. &nbsp;
7.  1.  *Z* = 2.444, $\pm z_{0.005} = \pm 2.576$, do not reject *H*<sub>0</sub>, *p*-value = 0.0146.
    2.  *Z* = 1.702, $z_{0.05} = 1.645$, reject *H*<sub>0</sub>, *p*-value = 0.0446
8. &nbsp;
9.  1.  $Z = \text{-}1.19$, *p*-value = 0.1170, do not reject *H*<sub>0</sub>;
    2.  $Z = \text{-}0.92$, *p*-value = 0.3576, do not reject *H*<sub>0</sub>
10. &nbsp;
11. 1.  *Z* = 2.68, *p*-value = 0.0037, reject *H*<sub>0</sub>;
    2.  $Z = \text{-}1.34$, *p*-value = 0.1802, do not reject *H*<sub>0</sub>
12. &nbsp;

<!-- -->

13. 1.  $0.2 \pm 0.4$,
    2.  *Z* = 1.360, $z_{0.01} = 2.326$, do not reject *H*<sub>0</sub> (not greater)
    3.  *p*-value = 0.0869

14. &nbsp;

15. 1.  $5.2 \pm 1.9$,
    2.  $Z = \text{-}1.466$, $\text{-}z_{0.050} = \text{-}1.645$, do not reject *H*<sub>0</sub> (exceeds by 6.3 or more)
    3.  *p*-value = 0.0708

16. &nbsp;

17. 1.  *Z* = 3.888, $z_{0.01} = 2.326$, reject *H*<sub>0</sub> (upperclassmen study more)
    2.  *p*-value = 0.0001

18. &nbsp;

19. 1.  $5 \pm 1.8$,
    2.  *Z* = 4.454, $z_{0.01} = 2.326$, reject *H*<sub>0</sub> (Test A is easier)
    3.  *p*-value = 0.0000

20. &nbsp;

21. *Z* = 0.738, $\pm z_{0.025} = \pm 1.960$, do not reject *H*<sub>0</sub> (no difference)

22. &nbsp;

23. $Z = \text{-}1.398$, $\text{-}z_{0.10} = \text{-}1.282$, reject *H*<sub>0</sub> (more offense oriented)

24. &nbsp;

<!-- -->

25. 1.  $n_{1} = 419$, ${\overset{-}{x}}_{1} = 1540.33$, $s_{1} = 205.40$, $n_{2} = 581$, ${\overset{-}{x}}_{2} = 1520.38$, and $s_{2} = 217.34.$
    2.  $\left( {\text{-}2.24,42.15} \right)$
    3.  $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 0$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 0.$ Test Statistic: *Z* = 1.48. Rejection Region: $\left\lbrack {1.645,\infty} \right).$ Decision: Fail to reject *H*<sub>0</sub>.
26. &nbsp;
27. 1.  $n_{1} = 65$, ${\overset{-}{x}}_{1} = 665.97$, $s_{1} = 41.60$, $n_{2} = 75$, ${\overset{-}{x}}_{2} = 455.89$, and $s_{2} = 63.22.$
    2.  $\left( {187.06,233.09} \right)$
    3.  $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 182$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 182.$ Test Statistic: *Z* = 3.14. Rejection Region: $\left\lbrack {2.33,\infty} \right).$ Decision: Reject *H*<sub>0</sub>.
    4.  $p - value = 0.0008$

`````````````

## 9.2 Comparison of Two Population Means: Small, Independent Samples

````````````{note} Learning Objectives

1.  To learn how to construct a confidence interval for the difference in the means of two distinct populations using small, independent samples.
2.  To learn how to perform a test of hypotheses concerning the difference between the means of two distinct populations using small, independent samples.

````````````

When one or the other of the sample sizes is small, as is often the case in practice, the Central Limit Theorem does not apply. We must then impose conditions on the population to give statistical validity to the test procedure. We will assume that both populations from which the samples are taken have a normal probability distribution and that their standard deviations are equal.

### Confidence Intervals

When the two populations are normally distributed and have equal standard deviations, the following formula for a confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ is valid.

````````````{important} $100\left( {1 - \alpha} \right)\%$ Confidence Interval for the Difference Between Two Population Means: Small, Independent Samples

$$\begin{matrix}
{({\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}) \pm t_{\alpha / 2}\sqrt{s_{p}^{2}\left( {\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)}} & \text{where} & {s_{p}^{2} = \frac{(n_{1}\text{-}1)s_{1}^{2} + (n_{2}\text{-}1)s_{2}^{2}}{n_{1} + n_{2}\text{-}2}}
\end{matrix}$$

The number of degrees of freedom is $df = n_{1} + n_{2}\text{-}2.$

The samples must be independent, the populations must be normal, and the population standard deviations must be equal. "Small" samples means that either $n_{1} < 30$ or $n_{2} < 30.$

````````````

The quantity $s_{p}^{2}$ is called the **pooled sample variance**. It is a weighted average of the two estimates $s_{1}^{2}$ and $s_{2}^{2}$ of the common variance $\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ of the two populations.

(src-fwk-shafer-ch09-s02-s01-n02)=

### Example 4

A software company markets a new computer game with two experimental packaging designs. Design 1 is sent to 11 stores; their average sales the first month is 52 units with sample standard deviation 12 units. Design 2 is sent to 6 stores; their average sales the first month is 46 units with sample standard deviation 10 units. Construct a point estimate and a 95% confidence interval for the difference in average monthly sales between the two package designs.

Solution:

The point estimate of $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ is

$${\overset{-}{x}}_{1} - {\overset{-}{x}}_{2} = 52 - 46 = 6$$

In words, we estimate that the average monthly sales for Design 1 is 6 units more per month than the average monthly sales for Design 2.

To apply the formula for the confidence interval, we must find $t_{\alpha / 2}.$ The 95% confidence level means that *α* = 1 − 0.95 = 0.05 so that $t_{\alpha / 2} = t_{0.025}.$ From [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03), in the row with the heading *df* = 11 + 6 − 2 = 15 we read that $t_{0.025} = 2.131.$ From the formula for the pooled sample variance we compute

$$s_{p}^{2} = \frac{\left( {n_{1}\text{-}1} \right)s_{1}^{2} + \left( {n_{2}\text{-}1} \right)s_{2}^{2}}{n_{1} + n_{2}\text{-}2} = \frac{(10)(12)^{2} + (5)(10)^{2}}{15} = 129.\overset{-}{3}$$

Thus

$$({\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}) \pm t_{\alpha / 2}\sqrt{s_{p}^{2}\left( {\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)} = 6 \pm (2.131)\sqrt{129.\overset{-}{3}\left( {\frac{1}{11} + \frac{1}{6}} \right)} \approx 6 \pm 12.3$$

We are 95% confident that the difference in the population means lies in the interval $\left\lbrack {\text{-}6.3,18.3} \right\rbrack$, in the sense that in repeated sampling 95% of all intervals constructed from the sample data in this manner will contain $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$ Because the interval contains both positive and negative values the statement in the context of the problem is that we are 95% confident that the average monthly sales for Design 1 is between 18.3 units higher and 6.3 units lower than the average monthly sales for Design 2.

### Hypothesis Testing

Testing hypotheses concerning the difference of two population means using small samples is done precisely as it is done for large samples, using the following standardized test statistic. The same conditions on the populations that were required for constructing a confidence interval for the difference of the means must also be met when hypotheses are tested.

````````````{important} Standardized Test Statistic for Hypothesis Tests Concerning the Difference Between Two Population Means: Small, Independent Samples

$$\begin{matrix}
{T = \frac{({\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}) - D_{0}}{\sqrt{s_{p}^{2}\left( {\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)}}} & \text{where} & {s_{p}^{2} = \frac{(n_{1}\text{-}1)s_{1}^{2} + (n_{2}\text{-}1)s_{2}^{2}}{n_{1} + n_{2}\text{-}2}}
\end{matrix}$$

The test statistic has Student's *t*-distribution with $df = n_{1} + n_{2}\text{-}2$ degrees of freedom.

The samples must be independent, the populations must be normal, and the population standard deviations must be equal. "Small" samples means that either $n_{1} < 30$ or $n_{2} < 30.$

````````````

(src-fwk-shafer-ch09-s02-s02-n02)=

### Example 5

Refer to [Note 9.11 \"Example 4\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s02-s01-n02) concerning the mean sales per month for the same computer game but sold with two package designs. Test at the 1% level of significance whether the data provide sufficient evidence to conclude that the mean sales per month of the two designs are different. Use the critical value approach.

Solution:

- Step 1. The relevant test is

  $$\begin{array}{rccc}
  {H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2}} & = & 0 & \\
  {\text{ vs. }\, H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2}} & \neq & 0 & {@\,\alpha = 0.01}
  \end{array}$$

- Step 2. Since the samples are independent and at least one is less than 30 the test statistic is

  $$T = \frac{({\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}) - D_{0}}{\sqrt{s_{p}^{2}\left( {\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)}}$$

  which has Student's *t*-distribution with $df = 11 + 6 - 2 = 15$ degrees of freedom.

- Step 3. Inserting the data and the value $D_{0} = 0$ into the formula for the test statistic gives

  $$T = \frac{({\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}) - D_{0}}{\sqrt{s_{p}^{2}\left( {\frac{1}{n_{1}} + \frac{1}{n_{2}}} \right)}} = \frac{(52 - 46)\text{-}0}{\sqrt{129.\overset{-}{3}\left( {\frac{1}{11} + \frac{1}{6}} \right)}} = 1.040$$

- Step 4. Since the symbol in *H<sub>a</sub>* is "≠" this is a two-tailed test, so there are two critical values, $\pm t_{\alpha / 2} = \pm t_{0.005}.$ From the row in [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) with the heading $df = 15$ we read off $t_{0.005} = 2.947.$ The rejection region is $\left( {\text{-}\infty,\text{-}2.947} \right\rbrack \cup \left\lbrack {2.947,\infty} \right).$

  ``````{figure} /images/redrawn/fig-09-04.svg
  :alt: Student t curve with 15 degrees of freedom. Both tails, each of area α/2 = 0.005, are shaded beyond the critical values −t_α/2 = −2.947 and t_α/2 = 2.947. On the number line below, the two rejection intervals are red, and the test statistic T = 1.040, marked with a star, lies outside the rejection region.
  :name: src-fwk-shafer-ch09-s02-s02-f01

  Figure 9.4 Rejection Region and Test Statistic for [Note 9.13 \"Example 5\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s02-s02-n02){.xref xrefstyle="select: title"}
  ``````

- Step 5. As shown in [Figure 9.4 \"Rejection Region and Test Statistic for \"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s02-s02-f01) the test statistic does not fall in the rejection region. The decision is not to reject *H*<sub>0</sub>. In the context of the problem our conclusion is:

  The data do not provide sufficient evidence, at the 1% level of significance, to conclude that the mean sales per month of the two designs are different.

### Example 6

Perform the test of [Note 9.13 \"Example 5\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s02-s02-n02) using the *p*-value approach.

Solution:

The first three steps are identical to those in [Note 9.13 \"Example 5\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s02-s02-n02).

- Step 4. Because the test is two-tailed the observed significance or *p*-value of the test is the double of the area of the right tail of Student's *t*-distribution, with 15 degrees of freedom, that is cut off by the test statistic *T* = 1.040. We can only approximate this number. Looking in the row of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) headed $df = 15$, the number 1.040 is between the numbers 0.866 and 1.341, corresponding to *t*<sub>0.200</sub> and *t*<sub>0.100</sub>.

  The area cut off by *t* = 0.866 is 0.200 and the area cut off by *t* = 1.341 is 0.100. Since 1.040 is between 0.866 and 1.341 the area it cuts off is between 0.200 and 0.100. Thus the *p*-value (since the area must be doubled) is between 0.400 and 0.200.

- Step 5. Since $p > 0.200 > 0.01$, $p > \alpha$, so the decision is not to reject the null hypothesis:

  The data do not provide sufficient evidence, at the 1% level of significance, to conclude that the mean sales per month of the two designs are different.

````````````{important} Key Takeaways

- In the context of estimating or testing hypotheses concerning two population means, "small" samples means that *at least one* sample is small. In particular, even if one sample is of size 30 or more, if the other is of size less than 30 the formulas of this section must be used.
- A confidence interval for the difference in two population means is computed using a formula in the same fashion as was done for a single population mean.

````````````

### Exercises

### Basic

In all exercises for this section assume that the populations are normal and have equal standard deviations.

1.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  95% confidence,

        $n_{1} = 10$, ${\overset{-}{x}}_{1} = 120$, $s_{1} = 2$

        $n_{2} = 15$, ${\overset{-}{x}}_{2} = 101$, $s_{2} = 4$

    2.  99% confidence,

        $n_{1} = 6$, ${\overset{-}{x}}_{1} = 25$, $s_{1} = 1$

        $n_{2} = 12$, ${\overset{-}{x}}_{2} = 17$, $s_{2} = 3$

2.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  90% confidence,

        $n_{1} = 28$, ${\overset{-}{x}}_{1} = 212$, $s_{1} = 6$

        $n_{2} = 23$, ${\overset{-}{x}}_{2} = 198$, $s_{2} = 5$

    2.  99% confidence,

        $n_{1} = 14$, ${\overset{-}{x}}_{1} = 68$, $s_{1} = 8$

        $n_{2} = 20$, ${\overset{-}{x}}_{2} = 43$, $s_{2} = 3$

3.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  99.9% confidence,

        $n_{1} = 35$, ${\overset{-}{x}}_{1} = 6.5$, $s_{1} = 0.2$

        $n_{2} = 20$, ${\overset{-}{x}}_{2} = 6.2$, $s_{2} = 0.1$

    2.  99% confidence,

        $n_{1} = 18$, ${\overset{-}{x}}_{1} = 77.3$, $s_{1} = 1.2$

        $n_{2} = 32$, ${\overset{-}{x}}_{2} = 75.0$, $s_{2} = 1.6$

4.  Construct the confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ for the level of confidence and the data from independent samples given.

    1.  99.5% confidence,

        $n_{1} = 40$, ${\overset{-}{x}}_{1} = 85.6$, $s_{1} = 2.8$

        $n_{2} = 20$, ${\overset{-}{x}}_{2} = 73.1$, $s_{2} = 2.1$

    2.  99.9% confidence,

        $n_{1} = 25$, ${\overset{-}{x}}_{1} = 215$, $s_{1} = 7$

        $n_{2} = 35$, ${\overset{-}{x}}_{2} = 185$, $s_{2} = 12$

5.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 11$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 11$ @ $\alpha = 0.025$,

        $n_{1} = 6$, ${\overset{-}{x}}_{1} = 32$, $s_{1} = 2$

        $n_{2} = 11$, ${\overset{-}{x}}_{2} = 19$, $s_{2} = 1$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 26$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 26$ @ $\alpha = 0.05$,

        $n_{1} = 17$, ${\overset{-}{x}}_{1} = 166$, $s_{1} = 4$

        $n_{2} = 24$, ${\overset{-}{x}}_{2} = 138$, $s_{2} = 3$

6.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 40$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < 40$ @ $\alpha = 0.10$,

        $n_{1} = 14$, ${\overset{-}{x}}_{1} = 289$, $s_{1} = 11$

        $n_{2} = 12$, ${\overset{-}{x}}_{2} = 254$, $s_{2} = 9$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 21$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 21$ @ $\alpha = 0.05$,

        $n_{1} = 23$, ${\overset{-}{x}}_{1} = 130$, $s_{1} = 6$

        $n_{2} = 27$, ${\overset{-}{x}}_{2} = 113$, $s_{2} = 8$

7.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}15$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < \text{-}15$ @ $\alpha = 0.10$,

        $n_{1} = 30$, ${\overset{-}{x}}_{1} = 42$, $s_{1} = 7$

        $n_{2} = 12$, ${\overset{-}{x}}_{2} = 60$, $s_{2} = 5$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 103$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 103$ @ $\alpha = 0.10$,

        $n_{1} = 17$, ${\overset{-}{x}}_{1} = 711$, $s_{1} = 28$

        $n_{2} = 32$, ${\overset{-}{x}}_{2} = 598$, $s_{2} = 21$

8.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the critical value approach.

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 75$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 75$ @ $\alpha = 0.025$,

        $n_{1} = 45$, ${\overset{-}{x}}_{1} = 674$, $s_{1} = 18$

        $n_{2} = 29$, ${\overset{-}{x}}_{2} = 591$, $s_{2} = 13$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}20$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}20$ @ $\alpha = 0.005$,

        $n_{1} = 30$, ${\overset{-}{x}}_{1} = 137$, $s_{1} = 8$

        $n_{2} = 19$, ${\overset{-}{x}}_{2} = 166$, $s_{2} = 11$

9.  Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach. (The *p*-value can be only approximated.)

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 12$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 12$ @ $\alpha = 0.01$,

        $n_{1} = 20$, ${\overset{-}{x}}_{1} = 133$, $s_{1} = 7$

        $n_{2} = 10$, ${\overset{-}{x}}_{2} = 115$, $s_{2} = 5$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 46$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 46$ @ $\alpha = 0.10$,

        $n_{1} = 24$, ${\overset{-}{x}}_{1} = 586$, $s_{1} = 11$

        $n_{2} = 27$, ${\overset{-}{x}}_{2} = 535$, $s_{2} = 13$

10. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach. (The *p*-value can be only approximated.)

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 38$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < 38$ @ $\alpha = 0.01$,

        $n_{1} = 12$, ${\overset{-}{x}}_{1} = 464$, $s_{1} = 5$

        $n_{2} = 10$, ${\overset{-}{x}}_{2} = 432$, $s_{2} = 6$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 4$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 4$ @ $\alpha = 0.005$,

        $n_{1} = 14$, ${\overset{-}{x}}_{1} = 68$, $s_{1} = 2$

        $n_{2} = 17$, ${\overset{-}{x}}_{2} = 67$, $s_{2} = 3$

11. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach. (The *p*-value can be only approximated.)

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 50$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 50$ @ $\alpha = 0.01$,

        $n_{1} = 30$, ${\overset{-}{x}}_{1} = 681$, $s_{1} = 8$

        $n_{2} = 27$, ${\overset{-}{x}}_{2} = 625$, $s_{2} = 8$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 35$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 35$ @ $\alpha = 0.10$,

        $n_{1} = 36$, ${\overset{-}{x}}_{1} = 325$, $s_{1} = 11$

        $n_{2} = 29$, ${\overset{-}{x}}_{2} = 286$, $s_{2} = 7$

12. Perform the test of hypotheses indicated, using the data from independent samples given. Use the *p*-value approach. (The *p*-value can be only approximated.)

    1.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}4$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} < \text{-}4$ @ $\alpha = 0.05$,

        $n_{1} = 40$, ${\overset{-}{x}}_{1} = 80$, $s_{1} = 5$

        $n_{2} = 25$, ${\overset{-}{x}}_{2} = 87$, $s_{2} = 5$

    2.  Test $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 21$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq 21$ @ $\alpha = 0.01$,

        $n_{1} = 15$, ${\overset{-}{x}}_{1} = 192$, $s_{1} = 12$

        $n_{2} = 34$, ${\overset{-}{x}}_{2} = 180$, $s_{2} = 8$

### Applications

13. A county environmental agency suspects that the fish in a particular polluted lake have elevated mercury level. To confirm that suspicion, five striped bass in that lake were caught and their tissues were tested for mercury. For the purpose of comparison, four striped bass in an unpolluted lake were also caught and tested. The fish tissue mercury levels in mg/kg are given below.

    $$\begin{matrix}
    {\text{Sample}\,\text{1}\,} & {\text{Sample}\,\text{2}} \\
    {\text{(from}\,\text{polluted}\,\text{lake)}} & {\text{(from}\,\text{unpolluted}\,\text{lake)}} \\
    0.580 & 0.382 \\
    0.711 & 0.276 \\
    0.571 & 0.570 \\
    0.666 & 0.366 \\
    0.598 &
    \end{matrix}$$

    1.  Construct the 95% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that fish in the polluted lake have elevated levels of mercury in their tissue.

14. A genetic engineering company claims that it has developed a genetically modified tomato plant that yields on average more tomatoes than other varieties. A farmer wants to test the claim on a small scale before committing to a full-scale planting. Ten genetically modified tomato plants are grown from seeds along with ten other tomato plants. At the season's end, the resulting yields in pound are recorded as below.

    $$\begin{matrix}
    {\text{Sample}\,\text{1}} & {\text{Sample}\,\text{2}} \\
    {\text{(genetically}\,\text{modified)}} & \text{(regular)} \\
    20 & 21 \\
    23 & 21 \\
    27 & 22 \\
    25 & 18 \\
    25 & 20 \\
    25 & 20 \\
    27 & 18 \\
    23 & 25 \\
    24 & 23 \\
    22 & 20
    \end{matrix}$$

    1.  Construct the 99% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 1% level of significance, whether the data provide sufficient evidence to conclude that the mean yield of the genetically modified variety is greater than that for the standard variety.

15. The coaching staff of a professional football team believes that the rushing offense has become increasingly potent in recent years. To investigate this belief, 20 randomly selected games from one year's schedule were compared to 11 randomly selected games from the schedule five years later. The sample information on rushing yards per game (rypg) is summarized below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - rypg previously
      - 20
      - 112
      - 24
    - - rypg recently
      - 11
      - 114
      - 21

    ````````

    1.  Construct the 95% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 5% level of significance, whether the data on rushing yards per game provide sufficient evidence to conclude that the rushing offense has become more potent in recent years.

16. The coaching staff of professional football team believes that the rushing offense has become increasingly potent in recent years. To investigate this belief, 20 randomly selected games from one year's schedule were compared to 11 randomly selected games from the schedule five years later. The sample information on passing yards per game (pypg) is summarized below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - pypg previously
      - 20
      - 203
      - 38
    - - pypg recently
      - 11
      - 232
      - 33

    ````````

    1.  Construct the 95% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 5% level of significance, whether the data on passing yards per game provide sufficient evidence to conclude that the passing offense has become more potent in recent years.

17. A university administrator wishes to know if there is a difference in average starting salary for graduates with master's degrees in engineering and those with master's degrees in business. Fifteen recent graduates with master's degree in engineering and 11 with master's degrees in business are surveyed and the results are summarized below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - Engineering
      - 15
      - 68,535
      - 1627
    - - Business
      - 11
      - 63,230
      - 2033

    ````````

    1.  Construct the 90% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that the average starting salaries are different.

18. A gardener sets up a flower stand in a busy business district and sells bouquets of assorted fresh flowers on weekdays. To find a more profitable pricing, she sells bouquets for 15 dollars each for ten days, then for 10 dollars each for five days. Her average daily profit for the two different prices are given below.

    ````````{list-table}
    :header-rows: 1

    - -
      - *n*
      - $\overset{-}{x}$
      - *s*
    - - \$15
      - 10
      - 171
      - 26
    - - \$10
      - 5
      - 198
      - 29

    ````````

    1.  Construct the 90% confidence interval for the difference in the population means based on these data.
    2.  Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude the gardener's average daily profit will be higher if the bouquets are sold at \$10 each.

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\left( {16.16,21.84} \right)$,
    2.  $\left( {4.28,11.72} \right)$
2. &nbsp;
3.  1.  $\left( {0.13,0.47} \right)$,
    2.  $\left( {1.14,3.46} \right)$
4. &nbsp;
5.  1.  *T* = 2.787, $t_{0.025} = 2.131$, reject *H*<sub>0</sub>,
    2.  *T* = 1.831, $\pm t_{0.025} = \pm 2.023$, do not reject *H*<sub>0</sub>
6. &nbsp;
7.  1.  $T = \text{-}1.349$, $\text{-}t_{0.10} = \text{-}1.303$, reject *H*<sub>0</sub>,
    2.  *T* = 1.411, $\pm t_{0.05} = \pm 1.678$, do not reject *H*<sub>0</sub>
8. &nbsp;
9.  1.  *T* = 2.411, $df = 28$, $p\text{ -value} > 0.01$, do not reject *H*<sub>0</sub>,
    2.  *T* = 1.473, $df = 49$, $p\text{ -value} < 0.10$, reject *H*<sub>0</sub>
10. &nbsp;
11. 1.  *T* = 2.827, $df = 55$, $p\text{ -value} < 0.01$, reject *H*<sub>0</sub>.
    2.  *T* = 1.699, $df = 63$, $p\text{ -value } < 0.10$, reject *H*<sub>0</sub>
12. &nbsp;

<!-- -->

13. 1.  $0.2267 \pm 0.2182$,
    2.  *T* = 3.635, $df = 7$, $t_{0.05} = 1.895$, reject *H*<sub>0</sub> (elevated levels)
14. &nbsp;
15. 1.  $\text{-}2 \pm 17.7$,
    2.  $T = \text{-}0.232$, $df = 29$, $\text{-}t_{0.05} = \text{-}1.699$, do not reject *H*<sub>0</sub> (not more potent)
16. &nbsp;
17. 1.  $5305 \pm 1227$,
    2.  *T* = 7.395, $df = 24$, $\pm t_{0.05} = \pm 1.711$, reject *H*<sub>0</sub> (different)
18. &nbsp;

`````````````

(src-fwk-shafer-ch09-s03)=

## 9.3 Comparison of Two Population Means: Paired Samples

````````````{note} Learning Objectives

1.  To learn the distinction between independent samples and paired samples.
2.  To learn how to construct a confidence interval for the difference in the means of two distinct populations using paired samples.
3.  To learn how to perform a test of hypotheses concerning the difference in the means of two distinct populations using paired samples.

````````````

Suppose chemical engineers wish to compare the fuel economy obtained by two different formulations of gasoline. Since fuel economy varies widely from car to car, if the mean fuel economy of two independent samples of vehicles run on the two types of fuel were compared, even if one formulation were better than the other the large variability from vehicle to vehicle might make any difference arising from difference in fuel difficult to detect. Just imagine one random sample having many more large vehicles than the other. Instead of independent random samples, it would make more sense to select pairs of cars of the same make and model and driven under similar circumstances, and compare the fuel economy of the two cars in each pair. Thus the data would look something like [Table 9.1 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t01), where the first car in each pair is operated on one formulation of the fuel (call it Type 1 gasoline) and the second car is operated on the second (call it Type 2 gasoline).

(src-fwk-shafer-ch09-s03-t01)=

Table 9.1 Fuel Economy of Pairs of Vehicles

````````{list-table}
:header-rows: 1

- - Make and Model
  - Car 1
  - Car 2
- - Buick LaCrosse
  - 17.0
  - 17.0
- - Dodge Viper
  - 13.2
  - 12.9
- - Honda CR-Z
  - 35.3
  - 35.4
- - Hummer H 3
  - 13.6
  - 13.2
- - Lexus RX
  - 32.7
  - 32.5
- - Mazda CX-9
  - 18.4
  - 18.1
- - Saab 9-3
  - 22.5
  - 22.5
- - Toyota Corolla
  - 26.8
  - 26.7
- - Volvo XC 90
  - 15.1
  - 15.0

````````

The first column of numbers forms a sample from Population 1, the population of all cars operated on Type 1 gasoline; the second column of numbers forms a sample from Population 2, the population of all cars operated on Type 2 gasoline. It would be incorrect to analyze the data using the formulas from the previous section, however, since the samples were not drawn independently. What *is* correct is to compute the difference in the numbers in each pair (subtracting in the same order each time) to obtain the third column of numbers as shown in [Table 9.2 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t02) and treat the differences as the data. At this point, the new sample of differences $d_{1} = 0.0,\ldots,d_{9} = 0.1$ in the third column of [Table 9.2 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t02) may be considered as a random sample of size *n* = 9 selected from a population with mean $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}.$ This approach essentially transforms the paired two-sample problem into a one-sample problem as discussed in the previous two chapters.

(src-fwk-shafer-ch09-s03-t02)=

Table 9.2 Fuel Economy of Pairs of Vehicles

````````{list-table}
:header-rows: 1

- - Make and Model
  - Car 1
  - Car 2
  - Difference
- - Buick LaCrosse
  - 17.0
  - 17.0
  - 0.0
- - Dodge Viper
  - 13.2
  - 12.9
  - 0.3
- - Honda CR-Z
  - 35.3
  - 35.4
  - −0.1
- - Hummer H 3
  - 13.6
  - 13.2
  - 0.4
- - Lexus RX
  - 32.7
  - 32.5
  - 0.2
- - Mazda CX-9
  - 18.4
  - 18.1
  - 0.3
- - Saab 9-3
  - 22.5
  - 22.5
  - 0.0
- - Toyota Corolla
  - 26.8
  - 26.7
  - 0.1
- - Volvo XC 90
  - 15.1
  - 15.0
  - 0.1

````````

Note carefully that although it does not matter what order the subtraction is done, it must be done in the *same* order for all pairs. This is why there are both positive and negative quantities in the third column of numbers in [Table 9.2 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t02).

### Confidence Intervals

When the population of differences is normally distributed the following formula for a confidence interval for $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ is valid.

````````````{important} $100\left( {1 - \alpha} \right)\%$ Confidence Interval for the Difference Between Two Population Means: Paired Difference Samples

$$\overset{-}{d} \pm t_{\alpha / 2}\frac{s_{d}}{\sqrt{n}}$$

where there are *n* pairs, $\overset{-}{d}$ is the mean and *s<sub>d</sub>* is the standard deviation of their differences.

The number of degrees of freedom is $df = n\text{-}1.$

The population of differences must be normally distributed.

````````````

### Example 7

Using the data in [Table 9.1 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t01) construct a point estimate and a 95% confidence interval for the difference in average fuel economy between cars operated on Type 1 gasoline and cars operated on Type 2 gasoline.

Solution:

We have referred to the data in [Table 9.1 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t01) because that is the way that the data are typically presented, but we emphasize that with paired sampling one immediately computes the differences, as given in [Table 9.2 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t02), and uses the differences as the data.

The mean and standard deviation of the differences are

$$\begin{matrix}
{\overset{-}{d} = \frac{\Sigma d}{n} = \frac{1.3}{9} = 0.1\overset{-}{4}} & \text{and} & {s_{d} = \sqrt{\frac{\Sigma d^{2} - \frac{1}{n}\left( {\Sigma d} \right)^{2}}{n\text{-}1}} = \sqrt{\frac{0.41 - \frac{1}{9}(1.3)^{2}}{8}} = 0.1\overset{-}{6}}
\end{matrix}$$

The point estimate of $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ is

$$\overset{-}{d} = 0.14$$

In words, we estimate that the average fuel economy of cars using Type 1 gasoline is 0.14 mpg greater than the average fuel economy of cars using Type 2 gasoline.

To apply the formula for the confidence interval, we must find $t_{\alpha / 2}.$ The 95% confidence level means that $\alpha = 1 - 0.95 = 0.05$ so that $t_{\alpha / 2} = t_{0.025}.$ From [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03), in the row with the heading $df = 9 - 1 = 8$ we read that $t_{0.025} = 2.306.$ Thus

$$\overset{-}{d} \pm t_{\alpha / 2}\frac{s_{d}}{\sqrt{n}} = 0.14 \pm 2.306\left( \frac{0.1\overset{-}{6}}{\sqrt{9}} \right) \approx 0.14 \pm 0.13$$

We are 95% confident that the difference in the population means lies in the interval $\left\lbrack {0.01,0.27} \right\rbrack$, in the sense that in repeated sampling 95% of all intervals constructed from the sample data in this manner will contain $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}.$ Stated differently, we are 95% confident that mean fuel economy is between 0.01 and 0.27 mpg greater with Type 1 gasoline than with Type 2 gasoline.

### Hypothesis Testing

Testing hypotheses concerning the difference of two population means using paired difference samples is done precisely as it is done for independent samples, although now the null and alternative hypotheses are expressed in terms of $\mathit{\mu}_{d}$ instead of $\mathit{\mu}_{1} - \mathit{\mu}_{2}.$ Thus the null hypothesis will always be written

$$H_{0}:\mathit{\mu}_{d} = D_{0}$$

The three forms of the alternative hypothesis, with the terminology for each case, are:

````````{list-table}
:header-rows: 1

- - Form of $H_{a}$
  - Terminology
- - $H_{a}:\mathit{\mu}_{d} < D_{0}$
  - Left-tailed
- - $H_{a}:\mathit{\mu}_{d} > D_{0}$
  - Right-tailed
- - $H_{a}:\mathit{\mu}_{d} \neq D_{0}$
  - Two-tailed

````````

The same conditions on the population of differences that was required for constructing a confidence interval for the difference of the means must also be met when hypotheses are tested. Here is the standardized test statistic that is used in the test.

````````````{important} Standardized Test Statistic for Hypothesis Tests Concerning the Difference Between Two Population Means: Paired Difference Samples

$$T = \frac{\overset{-}{d} - D_{0}}{\left. s_{d}/\sqrt{n} \right.}$$

where there are *n* pairs, $\overset{-}{d}$ is the mean and *s<sub>d</sub>* is the standard deviation of their differences.

The test statistic has Student's *t*-distribution with $df = n\text{-}1$ degrees of freedom.

The population of differences must be normally distributed.

````````````

(src-fwk-shafer-ch09-s03-s02-n02)=

### Example 8

Using the data of [Table 9.2 \"Fuel Economy of Pairs of Vehicles\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-t02) test the hypothesis that mean fuel economy for Type 1 gasoline is greater than that for Type 2 gasoline against the null hypothesis that the two formulations of gasoline yield the same mean fuel economy. Test at the 5% level of significance using the critical value approach.

Solution:

The only part of the table that we use is the third column, the differences.

- Step 1. Since the differences were computed in the order $\text{ Type 1 mpg} - \text{ Type 2 mpg}$, better fuel economy with Type 1 fuel corresponds to $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2} > 0.$ Thus the test is

  $$\begin{array}{rccc}
  {H_{0}:\mathit{\mu}_{d}} & = & 0 & \\
  {\text{\quad vs.}\, H_{a}:\mathit{\mu}_{d}} & > & 0 & {@\,\alpha = 0.05}
  \end{array}$$

  (If the differences had been computed in the opposite order then the alternative hypotheses would have been $H_{a}:\mathit{\mu}_{d} < 0.$)

- Step 2. Since the sampling is in pairs the test statistic is

  $$T = \frac{\overset{-}{d} - D_{0}}{\left. s_{d}/\sqrt{n} \right.}$$

- Step 3. We have already computed $\overset{-}{d}$ and *s<sub>d</sub>* in the previous example. Inserting their values and $D_{0} = 0$ into the formula for the test statistic gives

  $$T = \frac{\overset{-}{d} - D_{0}}{\left. s_{d}/\sqrt{n} \right.} = \frac{0.1\overset{-}{4}}{\left. 0.1\overset{-}{6}/ 3 \right.} = 2.600$$

- Step 4. Since the symbol in *H<sub>a</sub>* is "\>" this is a right-tailed test, so there is a single critical value, $t_{\alpha} = t_{0.05}$ with 8 degrees of freedom, which from the row labeled $df = 8$ in [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we read off as 1.860. The rejection region is $\left\lbrack {1.860,\infty} \right).$

- Step 5. As shown in [Figure 9.5 \"Rejection Region and Test Statistic for \"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-f01) the test statistic falls in the rejection region. The decision is to reject *H*<sub>0</sub>. In the context of the problem our conclusion is:

  ``````{figure} /images/redrawn/fig-09-05.svg
  :alt: Student t curve with 8 degrees of freedom for Hₐ: μ_d > 0. The right tail of area α = 0.05 is shaded above the critical value t₀.₀₅ = 1.860. On the number line below, the rejection region t ≥ 1.860 is red, and the test statistic T = 2.600, marked with a star, lies inside it.
  :name: src-fwk-shafer-ch09-s03-s02-f01

  Figure 9.5 Rejection Region and Test Statistic for [Note 9.20 \"Example 8\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-n02){.xref xrefstyle="select: title"}
  ``````

  The data provide sufficient evidence, at the 5% level of significance, to conclude that the mean fuel economy provided by Type 1 gasoline is greater than that for Type 2 gasoline.

(src-fwk-shafer-ch09-s03-s02-n03)=

### Example 9

Perform the test of [Note 9.20 \"Example 8\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-n02) using the *p*-value approach.

Solution:

The first three steps are identical to those in [Note 9.20 \"Example 8\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-n02).

- Step 4. Because the test is one-tailed the observed significance or *p*-value of the test is just the area of the right tail of Student's *t*-distribution, with 8 degrees of freedom, that is cut off by the test statistic *T* = 2.600. We can only approximate this number. Looking in the row of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) headed $df = 8$, the number 2.600 is between the numbers 2.306 and 2.896, corresponding to *t*<sub>0.025</sub> and *t*<sub>0.010</sub>.

  The area cut off by *t* = 2.306 is 0.025 and the area cut off by *t* = 2.896 is 0.010. Since 2.600 is between 2.306 and 2.896 the area it cuts off is between 0.025 and 0.010. Thus the *p*-value is between 0.025 and 0.010. In particular it is less than 0.025. See [Figure 9.6](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-f02).

``````{figure} /images/redrawn/fig-09-06.svg
:alt: Student t curve with 8 degrees of freedom. Vertical lines at 2.306, at the test statistic T = 2.6 (red), and at 2.896 mark right tails of area 0.025, the p-value, and 0.010, so the p-value lies between 0.010 and 0.025.
:name: src-fwk-shafer-ch09-s03-s02-f02

Figure 9.6 *P*-Value for [Note 9.21 \"Example 9\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03-s02-n03){.xref xrefstyle="select: title"}
``````

- Step 5. Since 0.025 \< 0.05, $p < \alpha$ so the decision is to reject the null hypothesis:

  The data provide sufficient evidence, at the 5% level of significance, to conclude that the mean fuel economy provided by Type 1 gasoline is greater than that for Type 2 gasoline.

The paired two-sample experiment is a very powerful study design. It bypasses many unwanted sources of "statistical noise" that might otherwise influence the outcome of the experiment, and focuses on the possible difference that might arise from the one factor of interest.

If the sample is large (meaning that *n* ≥ 30) then in the formula for the confidence interval we may replace $t_{\alpha / 2}$ by $z_{\alpha / 2}.$ For hypothesis testing when the number of pairs is at least 30, we may use the same statistic as for small samples for hypothesis testing, except now it follows a standard normal distribution, so we use the last line of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) to compute critical values, and *p*-values can be computed exactly with [Figure 12.2 \"Cumulative Normal Probability\"](/appendices/appendix.md#src-fwk-shafer-ch12-f02), not merely estimated using [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03).

````````````{important} Key Takeaways

- When the data are collected in pairs, the differences computed for each pair are the data that are used in the formulas.
- A confidence interval for the difference in two population means using paired sampling is computed using a formula in the same fashion as was done for a single population mean.
- The same five-step procedure used to test hypotheses concerning a single population mean is used to test hypotheses concerning the difference between two population means using paired sampling. The only difference is in the formula for the standardized test statistic.

````````````

### Exercises

### Basic

In all exercises for this section assume that the population of differences is normal.

1.  Use the following paired sample data for this exercise.

    $$\begin{array}{lccccccc}
    {\text{Population}\, 1} & 35 & 32 & 35 & 35 & 36 & 35 & 36 \\
    {\text{Population}\, 2} & 28 & 26 & 27 & 26 & 29 & 27 & 29
    \end{array}$$

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 95% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 10% level of significance, the hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} > 7$ as an alternative to the null hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} = 7.$

2.  Use the following paired sample data for this exercise.

    $$\begin{array}{lcccc}
    {\text{Population}\, 1} & 103 & 127 & 96 & 110 \\
    {\text{Population}\, 2} & 81 & 106 & 73 & 88
    \end{array}$$

    $$\begin{array}{lcccc}
    {\text{Population}\, 1} & 90 & 118 & 130 & 106 \\
    {\text{Population}\, 2} & 70 & 95 & 109 & 83
    \end{array}$$

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 90% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 1% level of significance, the hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} < 24$ as an alternative to the null hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} = 24.$

3.  Use the following paired sample data for this exercise.

    $$\begin{array}{lcccc}
    {\text{Population}\, 1} & 40 & 27 & 55 & 34 \\
    {\text{Population}\, 2} & 53 & 42 & 68 & 50
    \end{array}$$

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 99% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 10% level of significance, the hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}12$ as an alternative to the null hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}12.$

4.  Use the following paired sample data for this exercise.

    $$\begin{array}{lccccc}
    {\text{Population}\, 1} & 196 & 165 & 181 & 201 & 190 \\
    {\text{Population}\, 2} & 212 & 182 & 199 & 210 & 205
    \end{array}$$

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 98% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 2% level of significance, the hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} \neq \text{-}20$ as an alternative to the null hypothesis that $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \text{-}20.$

### Applications

5.  Each of five laboratory mice was released into a maze twice. The five pairs of times to escape were:

    ````````{list-table}
    :header-rows: 1

    - - Mouse
      - 1
      - 2
      - 3
      - 4
      - 5
    - - First release
      - 129
      - 89
      - 136
      - 163
      - 118
    - - Second release
      - 113
      - 97
      - 139
      - 85
      - 75

    ````````

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 90% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 10% level of significance, the hypothesis that it takes mice less time to run the maze on the second trial, on average.

6.  Eight golfers were asked to submit their latest scores on their favorite golf courses. These golfers were each given a set of newly designed clubs. After playing with the new clubs for a few months, the golfers were again asked to submit their latest scores on the same golf courses. The results are summarized below.

    ````````{list-table}
    :header-rows: 1

    - - Golfer
      - 1
      - 2
      - 3
      - 4
      - 5
      - 6
      - 7
      - 8
    - - Own clubs
      - 77
      - 80
      - 69
      - 73
      - 73
      - 72
      - 75
      - 77
    - - New clubs
      - 72
      - 81
      - 68
      - 73
      - 75
      - 70
      - 73
      - 75

    ````````

    1.  Compute $\overset{-}{d}$ and *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}.$
    3.  Construct the 99% confidence interval for $\mathit{\mu}_{1} - \mathit{\mu}_{2} = \mathit{\mu}_{d}$ from these data.
    4.  Test, at the 1% level of significance, the hypothesis that on average golf scores are lower with the new clubs.

7.  A neighborhood home owners association suspects that the recent appraisal values of the houses in the neighborhood conducted by the county government for taxation purposes is too high. It hired a private company to appraise the values of ten houses in the neighborhood. The results, in thousands of dollars, are

    ````````{list-table}
    :header-rows: 1

    - - House
      - County Government
      - Private Company
    - - 1
      - 217
      - 219
    - - 2
      - 350
      - 338
    - - 3
      - 296
      - 291
    - - 4
      - 237
      - 237
    - - 5
      - 237
      - 235
    - - 6
      - 272
      - 269
    - - 7
      - 257
      - 239
    - - 8
      - 277
      - 275
    - - 9
      - 312
      - 320
    - - 10
      - 335
      - 335

    ````````

    1.  Give a point estimate for the difference between the mean private appraisal of all such homes and the government appraisal of all such homes.
    2.  Construct the 99% confidence interval based on these data for the difference.
    3.  Test, at the 1% level of significance, the hypothesis that appraised values by the county government of all such houses is greater than the appraised values by the private appraisal company.

8.  In order to cut costs a wine producer is considering using duo or 1 + 1 corks in place of full natural wood corks, but is concerned that it could affect buyers' perception of the quality of the wine. The wine producer shipped eight pairs of bottles of its best young wines to eight wine experts. Each pair includes one bottle with a natural wood cork and one with a duo cork. The experts are asked to rate the wines on a one to ten scale, higher numbers corresponding to higher quality. The results are:

    ````````{list-table}
    :header-rows: 1

    - - Wine Expert
      - Duo Cork
      - Wood Cork
    - - 1
      - 8.5
      - 8.5
    - - 2
      - 8.0
      - 8.5
    - - 3
      - 6.5
      - 8.0
    - - 4
      - 7.5
      - 8.5
    - - 5
      - 8.0
      - 7.5
    - - 6
      - 8.0
      - 8.0
    - - 7
      - 9.0
      - 9.0
    - - 8
      - 7.0
      - 7.5

    ````````

    1.  Give a point estimate for the difference between the mean ratings of the wine when bottled are sealed with different kinds of corks.
    2.  Construct the 90% confidence interval based on these data for the difference.
    3.  Test, at the 10% level of significance, the hypothesis that on the average duo corks decrease the rating of the wine.

9.  Engineers at a tire manufacturing corporation wish to test a new tire material for increased durability. To test the tires under realistic road conditions, new front tires are mounted on each of 11 company cars, one tire made with a production material and the other with the experimental material. After a fixed period the 11 pairs were measured for wear. The amount of wear for each tire (in mm) is shown in the table:

    ````````{list-table}
    :header-rows: 1

    - - Car
      - Production
      - Experimental
    - - 1
      - 5.1
      - 5.0
    - - 2
      - 6.5
      - 6.5
    - - 3
      - 3.6
      - 3.1
    - - 4
      - 3.5
      - 3.7
    - - 5
      - 5.7
      - 4.5
    - - 6
      - 5.0
      - 4.1
    - - 7
      - 6.4
      - 5.3
    - - 8
      - 4.7
      - 2.6
    - - 9
      - 3.2
      - 3.0
    - - 10
      - 3.5
      - 3.5
    - - 11
      - 6.4
      - 5.1

    ````````

    1.  Give a point estimate for the difference in mean wear.
    2.  Construct the 99% confidence interval for the difference based on these data.
    3.  Test, at the 1% level of significance, the hypothesis that the mean wear with the experimental material is less than that for the production material.

10. A marriage counselor administered a test designed to measure overall contentment to 30 randomly selected married couples. The scores for each couple are given below. A higher number corresponds to greater contentment or happiness.

    ````````{list-table}
    :header-rows: 1

    - - Couple
      - Husband
      - Wife
    - - 1
      - 47
      - 44
    - - 2
      - 44
      - 46
    - - 3
      - 49
      - 44
    - - 4
      - 53
      - 44
    - - 5
      - 42
      - 43
    - - 6
      - 45
      - 45
    - - 7
      - 48
      - 47
    - - 8
      - 45
      - 44
    - - 9
      - 52
      - 44
    - - 10
      - 47
      - 42
    - - 11
      - 40
      - 34
    - - 12
      - 45
      - 42
    - - 13
      - 40
      - 43
    - - 14
      - 46
      - 41
    - - 15
      - 47
      - 45
    - - 16
      - 46
      - 45
    - - 17
      - 46
      - 41
    - - 18
      - 46
      - 41
    - - 19
      - 44
      - 45
    - - 20
      - 45
      - 43
    - - 21
      - 48
      - 38
    - - 22
      - 42
      - 46
    - - 23
      - 50
      - 44
    - - 24
      - 46
      - 51
    - - 25
      - 43
      - 45
    - - 26
      - 50
      - 40
    - - 27
      - 46
      - 46
    - - 28
      - 42
      - 41
    - - 29
      - 51
      - 41
    - - 30
      - 46
      - 47

    ````````

    1.  Test, at the 1% level of significance, the hypothesis that on average men and women are not equally happy in marriage.
    2.  Test, at the 1% level of significance, the hypothesis that on average men are happier than women in marriage.

### Large Data Set Exercises

11. Large Data Set 5 lists the scores for 25 randomly selected students on practice SAT reading tests before and after taking a two-week SAT preparation course. Denote the population of all students who have taken the course as Population 1 and the population of all students who have not taken the course as Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data5.xls>

    1.  Compute the 25 differences in the order $\text{ after} - \text{ before}$, their mean $\overset{-}{d}$, and their sample standard deviation *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$, the difference in the mean score of all students who have taken the course and the mean score of all who have not.
    3.  Construct a 98% confidence interval for $\mathit{\mu}_{d}.$
    4.  Test, at the 1% level of significance, the hypothesis that the mean SAT score increases by at least ten points by taking the two-week preparation course.

12. Large Data Set 12 lists the scores on one round for 75 randomly selected members at a golf course, first using their own original clubs, then two months later after using new clubs with an experimental design. Denote the population of all golfers using their own original clubs as Population 1 and the population of all golfers using the new style clubs as Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data12.xls>

    1.  Compute the 75 differences in the order $\text{ original clubs} - \text{ new clubs}$, their mean $\overset{-}{d}$, and their sample standard deviation *s<sub>d</sub>*.
    2.  Give a point estimate for $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$, the difference in the mean score of all golfers using their original clubs and the mean score of all golfers using the new kind of clubs.
    3.  Construct a 90% confidence interval for $\mathit{\mu}_{d}.$
    4.  Test, at the 1% level of significance, the hypothesis that the mean golf score decreases by at least one stroke by using the new kind of clubs.

13. Consider the previous problem again. Since the data set is so large, it is reasonable to use the standard normal distribution instead of Student's *t*-distribution with 74 degrees of freedom.

    1.  Construct a 90% confidence interval for $\mathit{\mu}_{d}$ using the standard normal distribution, meaning that the formula is $\overset{-}{d} \pm z_{\alpha / 2}\frac{s_{d}}{\sqrt{n}}.$ (The computations done in part (a) of the previous problem still apply and need not be redone.) How does the result obtained here compare to the result obtained in part (c) of the previous problem?
    2.  Test, at the 1% level of significance, the hypothesis that the mean golf score decreases by at least one stroke by using the new kind of clubs, using the standard normal distribution. (All the work done in part (d) of the previous problem applies, except the critical value is now $z_{\alpha}$ instead of $t_{\alpha}$ (or the *p*-value can be computed exactly instead of only approximated, if you used the *p*-value approach).) How does the result obtained here compare to the result obtained in part (c) of the previous problem?
    3.  Construct the 99% confidence intervals for $\mathit{\mu}_{d}$ using both the $t-$ and $z-$distributions. How much difference is there in the results now?

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\overset{-}{d} = 7.4286$, $s_{d} = 0.9759$,
    2.  $\overset{-}{d} = 7.4286$,
    3.  $\left( {6.53,8.33} \right)$,
    4.  *T* = 1.162, $df = 6$, $t_{0.10} = 1.44$, do not reject *H*<sub>0</sub>
2. &nbsp;
3.  1.  $\overset{-}{d} = \text{-}14.25$, $s_{d} = 1.5$,
    2.  $\overset{-}{d} = \text{-}14.25$,
    3.  $\left( {\text{-}18.63,\text{-}9.87} \right)$,
    4.  $T = \text{-}3.000$, $df = 3$, $\pm t_{0.05} = \pm 2.353$, reject *H*<sub>0</sub>
4. &nbsp;

<!-- -->

5.  1.  $\overset{-}{d} = 25.2$, $s_{d} = 35.6609$,
    2.  25.2,
    3.  $25.2 \pm 34.0$
    4.  *T* = 1.580, $df = 4$, $t_{0.10} = 1.533$, reject *H*<sub>0</sub> (takes less time)
6. &nbsp;
7.  1.  3.2,
    2.  $3.2 \pm 7.5$
    3.  *T* = 1.392, $df = 9$, $t_{0.10} = 2.821$, do not reject *H*<sub>0</sub> (government appraisals not higher)
8. &nbsp;
9.  1.  0.65,
    2.  $0.65 \pm 0.69$,
    3.  *T* = 3.014, $df = 10$, $t_{0.01} = 2.764$, reject *H*<sub>0</sub> (experimental material wears less)
10. &nbsp;

<!-- -->

11. 1.  $\overset{-}{d} = 16.68$ and $s_{d} = 10.77$
    2.  $\overset{-}{d} = 16.68$
    3.  $\left( {11.31,22.05} \right)$
    4.  $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 10$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 10.$ Test Statistic: *T* = 3.1014. $d.f. = 24.$ Rejection Region: $\left\lbrack {2.492,\infty} \right).$ Decision: Reject *H*<sub>0</sub>.
12. &nbsp;
13. 1.  $\left( {1.6266,2.6401} \right).$ Endpoints change in the third decimal place.
    2.  $H_{0}:\mathit{\mu}_{1} - \mathit{\mu}_{2} = 1$ vs. $H_{a}:\mathit{\mu}_{1} - \mathit{\mu}_{2} > 1.$ Test Statistic: *Z* = 3.6791. Rejection Region: $\left\lbrack {2.33,\infty} \right).$ Decision: Reject *H*<sub>0</sub>. The decision is the same as in the previous problem.
    3.  Using the $t -$distribution, $\left( {1.3188,2.9478} \right).$ Using the $z -$distribution, $\left( {1.3401,2.9266} \right).$ There is a difference.

`````````````

## 9.4 Comparison of Two Population Proportions

````````````{note} Learning Objectives

1.  To learn how to construct a confidence interval for the difference in the proportions of two distinct populations that have a particular characteristic of interest.
2.  To learn how to perform a test of hypotheses concerning the difference in the proportions of two distinct populations that have a particular characteristic of interest.

````````````

Suppose we wish to compare the proportions of two populations that have a specific characteristic, such as the proportion of men who are left-handed compared to the proportion of women who are left-handed. [Figure 9.7 \"Independent Sampling from Two Populations In Order to Compare Proportions\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-f01) illustrates the conceptual framework of our investigation. Each population is divided into two groups, the group of elements that have the characteristic of interest (for example, being left-handed) and the group of elements that do not. We arbitrarily label one population as Population 1 and the other as Population 2, and subscript the proportion of each population that possesses the characteristic with the number 1 or 2 to tell them apart. We draw a random sample from Population 1 and label the sample statistic it yields with the subscript 1. Without reference to the first sample we draw a sample from Population 2 and label its sample statistic with the subscript 2.

``````{figure} /images/redrawn/fig-09-07.svg
:alt: Two boxes labeled Population 1 and Population 2, with proportions p₁ and p₂. An arrow from each leads to a box for its sample, Sample 1 or Sample 2, with size n₁ or n₂, number of successes x₁ or x₂, and sample proportion p̂₁ or p̂₂.
:name: src-fwk-shafer-ch09-s04-f01

Figure 9.7 Independent Sampling from Two Populations In Order to Compare Proportions
``````

Our goal is to use the information in the *samples* to estimate the difference $p_{1} - p_{2}$ in the two *population* proportions and to make statistically valid inferences about it.

### Confidence Intervals

Since the sample proportion ${\hat{p}}_{1}$ computed using the sample drawn from Population 1 is a good estimator of population proportion *p*<sub>1</sub> of Population 1 and the sample proportion ${\hat{p}}_{2}$ computed using the sample drawn from Population 2 is a good estimator of population proportion *p*<sub>2</sub> of Population 2, a reasonable point estimate of the difference $p_{1} - p_{2}$ is ${\hat{p}}_{1} - {\hat{p}}_{2}.$ In order to widen this point estimate into a confidence interval we suppose that both samples are large, as described in [Section 7.3 \"Large Sample Estimation of a Population Proportion\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07-s03) in [Chapter 7 \"Estimation\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07) and repeated below. If so, then the following formula for a confidence interval for $p_{1} - p_{2}$ is valid.

````````````{important} $100\left( {1 - \alpha} \right)\%$ Confidence Interval for the Difference Between Two Population Proportions

$$\left( {{\hat{p}}_{1} - {\hat{p}}_{2}} \right) \pm z_{\alpha / 2}\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}$$

The samples must be independent, and *each* sample must be large: each of the intervals

$$\left\lbrack {\hat{p}}_{1} - 3\,\sqrt{\frac{{\hat{p}}_{1}(1 - {\hat{p}}_{1})}{n_{1}}},\,{\hat{p}}_{1} + 3\,\sqrt{\frac{{\hat{p}}_{1}(1 - {\hat{p}}_{1})}{n_{1}}}\, \right\rbrack$$

and

$$\left\lbrack {\hat{p}}_{2} - 3\,\sqrt{\frac{{\hat{p}}_{2}(1 - {\hat{p}}_{2})}{n_{2}}},\,{\hat{p}}_{2} + 3\,\sqrt{\frac{{\hat{p}}_{2}(1 - {\hat{p}}_{2})}{n_{2}}}\, \right\rbrack$$

must lie wholly within the interval $\lbrack 0,1\,\rbrack.$

````````````

(src-fwk-shafer-ch09-s04-s01-n02)=

### Example 10

The department of code enforcement of a county government issues permits to general contractors to work on residential projects. For each permit issued, the department inspects the result of the project and gives a "pass" or "fail" rating. A failed project must be re-inspected until it receives a pass rating. The department had been frustrated by the high cost of re-inspection and decided to publish the inspection records of all contractors on the web. It was hoped that public access to the records would lower the re-inspection rate. A year after the web access was made public, two samples of records were randomly selected. One sample was selected from the pool of records before the web publication and one after. The proportion of projects that passed on the first inspection was noted for each sample. The results are summarized below. Construct a point estimate and a 90% confidence interval for the difference in the passing rate on first inspection between the two time periods.

$$\begin{array}{lll}
{\text{No}\,\text{public}\,\text{web}\,\text{access}} & {n_{1} = 500} & {{\hat{p}}_{1} = 0.67} \\
{\text{Public}\,\text{web}\,\text{access}} & {n_{2} = 100} & {{\hat{p}}_{2} = 0.80}
\end{array}$$

Solution:

The point estimate of $p_{1} - p_{2}$ is

$${\hat{p}}_{1} - {\hat{p}}_{2} = 0.67 - 0.80 = \text{-}0.13$$

Because the "No public web access" population was labeled as Population 1 and the "Public web access" population was labeled as Population 2, in words this means that we estimate that the proportion of projects that passed on the first inspection increased by 13 percentage points after records were posted on the web.

The sample sizes are sufficiently large for constructing a confidence interval since for sample 1:

$$3\,\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}}} = 3\,\sqrt{\frac{(0.67)(0.33)}{500}} = 0.06$$

so that

$$\begin{array}{l}
\left\lbrack {{\hat{p}}_{1}\text{-}3\,\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}}},\,{\hat{p}}_{1} + 3\,\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}}}} \right\rbrack \\
{= \left\lbrack {0.67 - 0.06,0.67 + 0.06}\, \right\rbrack = \left\lbrack {0.61,0.73}\, \right\rbrack \subset \lbrack 0,1\,\rbrack}
\end{array}$$

and for sample 2:

$$3\,\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}}} = 3\,\sqrt{\frac{(0.8)(0.2)}{100}} = 0.12$$

so that

$$\begin{array}{l}
\left\lbrack {{\hat{p}}_{2}\text{-}3\,\sqrt{\frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}},\,{\hat{p}}_{2} + 3\,\sqrt{\frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}} \right\rbrack \\
{= \left\lbrack {0.8 - 0.12,0.8 + 0.12}\, \right\rbrack = \left\lbrack {0.68,0.92}\, \right\rbrack \subset \lbrack 0,1\,\rbrack}
\end{array}$$

To apply the formula for the confidence interval, we first observe that the 90% confidence level means that $\alpha = 1 - 0.90 = 0.10$ so that $z_{\alpha / 2} = z_{0.05}.$ From [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we read directly that $z_{0.05} = 1.645.$ Thus the desired confidence interval is

$$\begin{array}{rcc}
\left( {{\hat{p}}_{1} - {\hat{p}}_{2}} \right) & \pm & {z_{\alpha / 2}\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}} \\
 & = & {\text{-}0.13 \pm 1.645\sqrt{\frac{(0.67)(0.33)}{500} + \frac{(0.8)(0.2)}{100}}\,} \\
 & = & {\text{-}0.13 \pm 0.07\,}
\end{array}$$

The 90% confidence interval is $\left\lbrack {\text{-}0.20,\text{-}0.06}\, \right\rbrack.$ We are 90% confident that the difference in the population proportions lies in the interval $\left\lbrack {\text{-}0.20,\text{-}0.06}\, \right\rbrack$, in the sense that in repeated sampling 90% of all intervals constructed from the sample data in this manner will contain $p_{1} - p_{2}.$ Taking into account the labeling of the two populations, this means that we are 90% confident that the proportion of projects that pass on the first inspection is between 6 and 20 percentage points higher after public access to the records than before.

### Hypothesis Testing

In hypothesis tests concerning the relative sizes of the proportions *p*<sub>1</sub> and *p*<sub>2</sub> of two populations that possess a particular characteristic, the null and alternative hypotheses will always be expressed in terms of the difference of the two population proportions. Hence the null hypothesis is always written

$$H_{0}:p_{1} - p_{2} = D_{0}$$

The three forms of the alternative hypothesis, with the terminology for each case, are:

````````{list-table}
:header-rows: 1

- - Form of $H_{a}$
  - Terminology
- - $H_{a}:p_{1} - p_{2} < D_{0}$
  - Left-tailed
- - $H_{a}:p_{1} - p_{2} > D_{0}$
  - Right-tailed
- - $H_{a}:p_{1} - p_{2} \neq D_{0}$
  - Two-tailed

````````

As long as the samples are independent and both are large the following formula for the standardized test statistic is valid, and it has the standard normal distribution.

````````````{important} Standardized Test Statistic for Hypothesis Tests Concerning the Difference Between Two Population Proportions

$$Z = \frac{\left( {{\hat{p}}_{1} - {\hat{p}}_{2}} \right) - D_{0}}{\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}}$$

The test statistic has the standard normal distribution.

The samples must be independent, and *each* sample must be large: each of the intervals

$$\left\lbrack {\hat{p}}_{1} - 3\,\sqrt{\frac{{\hat{p}}_{1}(1 - {\hat{p}}_{1})}{n_{1}}},\,{\hat{p}}_{1} + 3\,\sqrt{\frac{{\hat{p}}_{1}(1 - {\hat{p}}_{1})}{n_{1}}}\, \right\rbrack$$

and

$$\left\lbrack {\hat{p}}_{2} - 3\,\sqrt{\frac{{\hat{p}}_{2}(1 - {\hat{p}}_{2})}{n_{2}}},\,\,\,{\hat{p}}_{2} + 3\,\sqrt{\frac{{\hat{p}}_{2}(1 - {\hat{p}}_{2})}{n_{2}}}\, \right\rbrack$$

must lie wholly within the interval $\lbrack 0,1\,\rbrack.$

````````````

(src-fwk-shafer-ch09-s04-s02-n02)=

### Example 11

Using the data of [Note 9.25 \"Example 10\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s01-n02), test whether there is sufficient evidence to conclude that public web access to the inspection records has increased the proportion of projects that passed on the first inspection by more than 5 percentage points. Use the critical value approach at the 10% level of significance.

Solution:

- Step 1. Taking into account the labeling of the populations an increase in passing rate at the first inspection by more than 5 percentage points after public access on the web may be expressed as $p_{2} > p_{1} + 0.05$, which by algebra is the same as $p_{1} - p_{2} < \text{-}0.05.$ This is the alternative hypothesis. Since the null hypothesis is always expressed as an equality, with the same number on the right as is in the alternative hypothesis, the test is

  $$\begin{array}{rccc}
  {H_{0}:p_{1} - p_{2}} & = & {\text{-}0.05} & \\
  {\,\text{\quad vs.}\, H_{a}:p_{1} - p_{2}} & < & {\text{-}0.05} & {@\,\,\alpha = 0.10}
  \end{array}$$

- Step 2. Since the test is with respect to a difference in population proportions the test statistic is

  $$Z = \frac{\left( {{\hat{p}}_{1} - {\hat{p}}_{2}} \right) - D_{0}}{\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}}$$

- Step 3. Inserting the values given in [Note 9.25 \"Example 10\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s01-n02) and the value $D_{0} = \text{-}0.05$ into the formula for the test statistic gives

  $$Z = \frac{\left( {{\hat{p}}_{1} - {\hat{p}}_{2}} \right) - D_{0}}{\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}} = \frac{\left( {\text{-}0.13} \right) - \left( {\text{-}0.05} \right)}{\sqrt{\frac{(0.67)(0.33)}{500} + \frac{(0.8)(0.2)}{100}}} = \text{-}1.770$$

- Step 4. Since the symbol in *H<sub>a</sub>* is "\<" this is a left-tailed test, so there is a single critical value, $z_{\alpha} = \text{-}z_{0.10}.$ From the last row in [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) $z_{0.10} = 1.282$, so $\text{-}z_{0.10} = \text{-}1.282.$ The rejection region is $\left( {\text{-}\infty,\text{-}1.282}\, \right\rbrack.$

- Step 5. As shown in [Figure 9.8 \"Rejection Region and Test Statistic for \"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s02-f01) the test statistic falls in the rejection region. The decision is to reject *H*<sub>0</sub>. In the context of the problem our conclusion is:

  The data provide sufficient evidence, at the 10% level of significance, to conclude that the rate of passing on the first inspection has increased by more than 5 percentage points since records were publicly posted on the web.

``````{figure} /images/redrawn/fig-09-08.svg
:alt: Standard normal curve for Hₐ: p₁ − p₂ < −0.05. The left tail of area α = 0.10 is shaded below the critical value −z₀.₁₀ = −1.282. On the number line below, the rejection region z ≤ −1.282 is red, and the test statistic Z = −1.770, marked with a star, lies inside it.
:name: src-fwk-shafer-ch09-s04-s02-f01

Figure 9.8 Rejection Region and Test Statistic for [Note 9.27 \"Example 11\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s02-n02){.xref xrefstyle="select: title"}
``````

### Example 12

Perform the test of [Note 9.27 \"Example 11\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s02-n02) using the *p*-value approach.

Solution:

The first three steps are identical to those in [Note 9.27 \"Example 11\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s04-s02-n02).

- Step 4. Because the test is left-tailed the observed significance or *p*-value of the test is just the area of the left tail of the standard normal distribution that is cut off by the test statistic $Z = \text{-}1.770.$ From [Figure 12.2 \"Cumulative Normal Probability\"](/appendices/appendix.md#src-fwk-shafer-ch12-f02) the area of the left tail determined by −1.77 is 0.0384. The *p*-value is 0.0384.
- Step 5. Since the *p*-value 0.0384 is less than $\alpha = 0.10$, the decision is to reject the null hypothesis: The data provide sufficient evidence, at the 10% level of significance, to conclude that the rate of passing on the first inspection has increased by more than 5 percentage points since records were publicly posted on the web.

Finally a common misuse of the formulas given in this section must be mentioned. Suppose a large pre-election survey of potential voters is conducted. Each person surveyed is asked to express a preference between, say, Candidate A and Candidate B. (Perhaps "no preference" or "other" are also choices, but that is not important.) In such a survey, estimators ${\hat{p}}_{A}$ and ${\hat{p}}_{B}$ of *p<sub>A</sub>* and *p<sub>B</sub>* can be calculated. It is important to realize, however, that these two estimators were not calculated from two independent samples. While ${\hat{p}}_{A} - {\hat{p}}_{B}$ may be a reasonable estimator of $p_{A} - p_{B}$, the formulas for confidence intervals and for the standardized test statistic given in this section are not valid for data obtained in this manner.

````````````{important} Key Takeaways

- A confidence interval for the difference in two population proportions is computed using a formula in the same fashion as was done for a single population mean.
- The same five-step procedure used to test hypotheses concerning a single population proportion is used to test hypotheses concerning the difference between two population proportions. The only difference is in the formula for the standardized test statistic.

````````````

### Exercises

### Basic

1.  Construct the confidence interval for $p_{1} - p_{2}$ for the level of confidence and the data given. (The samples are sufficiently large.)

    1.  90% confidence,

        $n_{1} = 1670$, ${\hat{p}}_{1} = 0.42$

        $n_{2} = 900$, ${\hat{p}}_{2} = 0.38$

    2.  95% confidence,

        $n_{1} = 600$, ${\hat{p}}_{1} = 0.84$

        $n_{2} = 420$, ${\hat{p}}_{2} = 0.67$

2.  Construct the confidence interval for $p_{1} - p_{2}$ for the level of confidence and the data given. (The samples are sufficiently large.)

    1.  98% confidence,

        $n_{1} = 750$, ${\hat{p}}_{1} = 0.64$

        $n_{2} = 800$, ${\hat{p}}_{2} = 0.51$

    2.  99.5% confidence,

        $n_{1} = 250$, ${\hat{p}}_{1} = 0.78$

        $n_{2} = 250$, ${\hat{p}}_{2} = 0.51$

3.  Construct the confidence interval for $p_{1} - p_{2}$ for the level of confidence and the data given. (The samples are sufficiently large.)

    1.  80% confidence,

        $n_{1} = 300$, ${\hat{p}}_{1} = 0.255$

        $n_{2} = 400$, ${\hat{p}}_{2} = 0.193$

    2.  95% confidence,

        $n_{1} = 3500$, ${\hat{p}}_{1} = 0.147$

        $n_{2} = 3750$, ${\hat{p}}_{2} = 0.131$

4.  Construct the confidence interval for $p_{1} - p_{2}$ for the level of confidence and the data given. (The samples are sufficiently large.)

    1.  99% confidence,

        $n_{1} = 2250$, ${\hat{p}}_{1} = 0.915$

        $n_{2} = 2525$, ${\hat{p}}_{2} = 0.858$

    2.  95% confidence,

        $n_{1} = 120$, ${\hat{p}}_{1} = 0.650$

        $n_{2} = 200$, ${\hat{p}}_{2} = 0.505$

5.  Perform the test of hypotheses indicated, using the data given. Use the critical value approach. Compute the *p*-value of the test as well. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} > 0$ @ $\alpha = 0.10$,

        $n_{1} = 1200$, ${\hat{p}}_{1} = 0.42$

        $n_{2} = 1200$, ${\hat{p}}_{2} = 0.40$

    2.  Test $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} \neq 0$ @ $\alpha = 0.05$,

        $n_{1} = 550$, ${\hat{p}}_{1} = 0.61$

        $n_{2} = 600$, ${\hat{p}}_{2} = 0.67$

6.  Perform the test of hypotheses indicated, using the data given. Use the critical value approach. Compute the *p*-value of the test as well. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.05$ vs. $H_{a}:p_{1} - p_{2} > 0.05$ @ $\alpha = 0.05$,

        $n_{1} = 1100$, ${\hat{p}}_{1} = 0.57$

        $n_{2} = 1100$, ${\hat{p}}_{2} = 0.48$

    2.  Test $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} \neq 0$ @ $\alpha = 0.05$,

        $n_{1} = 800$, ${\hat{p}}_{1} = 0.39$

        $n_{2} = 900$, ${\hat{p}}_{2} = 0.43$

7.  Perform the test of hypotheses indicated, using the data given. Use the critical value approach. Compute the *p*-value of the test as well. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.25$ vs. $H_{a}:p_{1} - p_{2} < 0.25$ @ $\alpha = 0.005$,

        $n_{1} = 1400$, ${\hat{p}}_{1} = 0.57$

        $n_{2} = 1200$, ${\hat{p}}_{2} = 0.37$

    2.  Test $H_{0}:p_{1} - p_{2} = 0.16$ vs. $H_{a}:p_{1} - p_{2} \neq 0.16$ @ $\alpha = 0.02$,

        $n_{1} = 750$, ${\hat{p}}_{1} = 0.43$

        $n_{2} = 600$, ${\hat{p}}_{2} = 0.22$

8.  Perform the test of hypotheses indicated, using the data given. Use the critical value approach. Compute the *p*-value of the test as well. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.08$ vs. $H_{a}:p_{1} - p_{2} > 0.08$ @ $\alpha = 0.025$,

        $n_{1} = 450$, ${\hat{p}}_{1} = 0.67$

        $n_{2} = 200$, ${\hat{p}}_{2} = 0.52$

    2.  Test $H_{0}:p_{1} - p_{2} = 0.02$ vs. $H_{a}:p_{1} - p_{2} \neq 0.02$ @ $\alpha = 0.001$,

        $n_{1} = 2700$, ${\hat{p}}_{1} = 0.837$

        $n_{2} = 2900$, ${\hat{p}}_{2} = 0.854$

9.  Perform the test of hypotheses indicated, using the data given. Use the *p*-value approach. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} < 0$ @ $\alpha = 0.005$,

        $n_{1} = 1100$, ${\hat{p}}_{1} = 0.22$

        $n_{2} = 1300$, ${\hat{p}}_{2} = 0.27$

    2.  Test $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} \neq 0$ @ $\alpha = 0.01$,

        $n_{1} = 650$, ${\hat{p}}_{1} = 0.35$

        $n_{2} = 650$, ${\hat{p}}_{2} = 0.41$

10. Perform the test of hypotheses indicated, using the data given. Use the *p*-value approach. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.15$ vs. $H_{a}:p_{1} - p_{2} > 0.15$ @ $\alpha = 0.10$,

        $n_{1} = 950$, ${\hat{p}}_{1} = 0.41$

        $n_{2} = 500$, ${\hat{p}}_{2} = 0.23$

    2.  Test $H_{0}:p_{1} - p_{2} = 0.10$ vs. $H_{a}:p_{1} - p_{2} \neq 0.10$ @ $\alpha = 0.10$,

        $n_{1} = 220$, ${\hat{p}}_{1} = 0.92$

        $n_{2} = 160$, ${\hat{p}}_{2} = 0.78$

11. Perform the test of hypotheses indicated, using the data given. Use the *p*-value approach. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.22$ vs. $H_{a}:p_{1} - p_{2} > 0.22$ @ $\alpha = 0.05$,

        $n_{1} = 90$, ${\hat{p}}_{1} = 0.72$

        $n_{2} = 75$, ${\hat{p}}_{2} = 0.40$

    2.  Test $H_{0}:p_{1} - p_{2} = 0.37$ vs. $H_{a}:p_{1} - p_{2} \neq 0.37$ @ $\alpha = 0.02$,

        $n_{1} = 425$, ${\hat{p}}_{1} = 0.772$

        $n_{2} = 425$, ${\hat{p}}_{2} = 0.331$

12. Perform the test of hypotheses indicated, using the data given. Use the *p*-value approach. (The samples are sufficiently large.)

    1.  Test $H_{0}:p_{1} - p_{2} = 0.50$ vs. $H_{a}:p_{1} - p_{2} < 0.50$ @ $\alpha = 0.10$,

        $n_{1} = 40$, ${\hat{p}}_{1} = 0.65$

        $n_{2} = 55$, ${\hat{p}}_{2} = 0.24$

    2.  Test $H_{0}:p_{1} - p_{2} = 0.30$ vs. $H_{a}:p_{1} - p_{2} \neq 0.30$ @ $\alpha = 0.10$,

        $n_{1} = 7500$, ${\hat{p}}_{1} = 0.664$

        $n_{2} = 1000$, ${\hat{p}}_{2} = 0.319$

### Applications

In all the remaining exercises the samples are sufficiently large (so this need not be checked).

13. Voters in a particular city who identify themselves with one or the other of two political parties were randomly selected and asked if they favor a proposal to allow citizens with proper license to carry a concealed handgun in city parks. The results are:

    ````````{list-table}
    :header-rows: 1

    - -
      - Party A
      - Party B
    - - Sample size, *n*
      - 150
      - 200
    - - Number in favor, *x*
      - 90
      - 140

    ````````

    1.  Give a point estimate for the difference in the proportion of all members of Party A and all members of Party B who favor the proposal.
    2.  Construct the 95% confidence interval for the difference, based on these data.
    3.  Test, at the 5% level of significance, the hypothesis that the proportion of all members of Party A who favor the proposal is less than the proportion of all members of Party B who do.
    4.  Compute the *p*-value of the test.

14. To investigate a possible relation between gender and handedness, a random sample of 320 adults was taken, with the following results:

    ````````{list-table}
    :header-rows: 1

    - -
      - Men
      - Women
    - - Sample size, *n*
      - 168
      - 152
    - - Number of left-handed, *x*
      - 24
      - 9

    ````````

    1.  Give a point estimate for the difference in the proportion of all men who are left-handed and the proportion of all women who are left-handed.
    2.  Construct the 95% confidence interval for the difference, based on these data.
    3.  Test, at the 5% level of significance, the hypothesis that the proportion of men who are left-handed is greater than the proportion of women who are.
    4.  Compute the *p*-value of the test.

15. A local school board member randomly sampled private and public high school teachers in his district to compare the proportions of National Board Certified (NBC) teachers in the faculty. The results were:

    ````````{list-table}
    :header-rows: 1

    - -
      - Private Schools
      - Public Schools
    - - Sample size, *n*
      - 80
      - 520
    - - Proportion of NBC teachers, $\hat{p}$
      - 0.175
      - 0.150

    ````````

    1.  Give a point estimate for the difference in the proportion of all teachers in area public schools and the proportion of all teachers in private schools who are National Board Certified.
    2.  Construct the 90% confidence interval for the difference, based on these data.
    3.  Test, at the 10% level of significance, the hypothesis that the proportion of all public school teachers who are National Board Certified is less than the proportion of private school teachers who are.
    4.  Compute the *p*-value of the test.

16. In professional basketball games, the fans of the home team always try to distract free throw shooters on the visiting team. To investigate whether this tactic is actually effective, the free throw statistics of a professional basketball player with a high free throw percentage were examined. During the entire last season, this player had 656 free throws, 420 in home games and 236 in away games. The results are summarized below.

    ````````{list-table}
    :header-rows: 1

    - -
      - Home
      - Away
    - - Sample size, *n*
      - 420
      - 236
    - - Free throw percent, $\hat{p}$
      - 81.5%
      - 78.8%

    ````````

    1.  Give a point estimate for the difference in the proportion of free throws made at home and away.
    2.  Construct the 90% confidence interval for the difference, based on these data.
    3.  Test, at the 10% level of significance, the hypothesis that there exists a home advantage in free throws.
    4.  Compute the *p*-value of the test.

17. Randomly selected middle-aged people in both China and the United States were asked if they believed that adults have an obligation to financially support their aged parents. The results are summarized below.

    ````````{list-table}
    :header-rows: 1

    - -
      - China
      - USA
    - - Sample size, *n*
      - 1300
      - 150
    - - Number of yes, *x*
      - 1170
      - 110

    ````````

    Test, at the 1% level of significance, whether the data provide sufficient evidence to conclude that there exists a cultural difference in attitude regarding this question.

18. A manufacturer of walk-behind push mowers receives refurbished small engines from two new suppliers, *A* and *B*. It is not uncommon that some of the refurbished engines need to be lightly serviced before they can be fitted into mowers. The mower manufacturer recently received 100 engines from each supplier. In the shipment from *A*, 13 needed further service. In the shipment from *B*, 10 needed further service. Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that there exists a difference in the proportions of engines from the two suppliers needing service.

### Large Data Set Exercises

19. Large Data Sets 6A and 6B record results of a random survey of 200 voters in each of two regions, in which they were asked to express whether they prefer Candidate *A* for a U.S. Senate seat or prefer some other candidate. Let the population of all voters in region 1 be denoted Population 1 and the population of all voters in region 2 be denoted Population 2. Let *p*<sub>1</sub> be the proportion of voters in Population 1 who prefer Candidate *A*, and *p*<sub>2</sub> the proportion in Population 2 who do.

    <http://www.flatworldknowledge.com/sites/all/files/data6A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data6B.xls>

    1.  Find the relevant sample proportions ${\hat{p}}_{1}$ and ${\hat{p}}_{2}.$
    2.  Construct a point estimate for $p_{1} - p_{2}.$
    3.  Construct a 95% confidence interval for $p_{1} - p_{2}.$
    4.  Test, at the 5% level of significance, the hypothesis that the same proportion of voters in the two regions favor Candidate *A*, against the alternative that a larger proportion in Population 2 do.

20. Large Data Set 11 records the results of samples of real estate sales in a certain region in the year 2008 (lines 2 through 536) and in the year 2010 (lines 537 through 1106). Foreclosure sales are identified with a 1 in the second column. Let all real estate sales in the region in 2008 be Population 1 and all real estate sales in the region in 2010 be Population 2.

    <http://www.flatworldknowledge.com/sites/all/files/data11.xls>

    1.  Use the sample data to construct point estimates ${\hat{p}}_{1}$ and ${\hat{p}}_{2}$ of the proportions *p*<sub>1</sub> and *p*<sub>2</sub> of all real estate sales in this region in 2008 and 2010 that were foreclosure sales. Construct a point estimate of $p_{1} - p_{2}.$
    2.  Use the sample data to construct a 90% confidence interval for $p_{1} - p_{2}.$
    3.  Test, at the 10% level of significance, the hypothesis that the proportion of real estate sales in the region in 2010 that were foreclosure sales was greater than the proportion of real estate sales in the region in 2008 that were foreclosure sales. (The default is that the proportions were the same.)

`````````````{admonition} Answers
:class: dropdown

1.  1.  $\left( {0.0068,0.0732} \right)$,
    2.  $\left( {0.1163,0.2237} \right)$
2. &nbsp;
3.  1.  $\left( {0.0210,0.1030} \right)$,
    2.  $\left( {0.0001,0.0319} \right)$
4. &nbsp;
5.  1.  *Z* = 0.996, $z_{0.10} = 1.282$, $p\,\text{-value} = 0.1587$, do not reject *H*<sub>0</sub>,
    2.  $Z = \text{-}2.120$, $\pm z_{0.025} = \pm 1.960$, $p\,\text{-value} = 0.0340$, reject *H*<sub>0</sub>
6. &nbsp;
7.  1.  $Z = \text{-}2.602$, $\text{-}z_{0.005} = \text{-}2.576$, $p\,\text{-value} = 0.0047$, reject *H*<sub>0</sub>,
    2.  *Z* = 2.020, $\pm z_{0.01} = \pm 2.326$, $p\,\text{-value} = 0.0434$, do not reject *H*<sub>0</sub>
8. &nbsp;
9.  1.  $Z = \text{-}2.85$, $p\,\text{-value} = 0.0022$, reject *H*<sub>0</sub>,
    2.  $Z = \text{-}2.23$, $p\,\text{-value} = 0.0258$, do not reject *H*<sub>0</sub>
10. &nbsp;
11. 1.  *Z* = 1.36, $p\,\text{-value} = 0.0869$, do not reject *H*<sub>0</sub>,
    2.  *Z* = 2.32, $p\,\text{-value} = 0.0204$, do not reject *H*<sub>0</sub>
12. &nbsp;

<!-- -->

13. 1.  −0.10,
    2.  $\text{-}0.10 \pm 0.101$,
    3.  $Z = \text{-}1.943$, $\text{-}z_{0.05} = \text{-}1.645$, reject *H*<sub>0</sub> (fewer in Party A favor),
    4.  *p*-value = 0.0262

14. &nbsp;

15. 1.  0.025,
    2.  $0.025 \pm 0.0745$,
    3.  *Z* = 0.552, $z_{0.10} = 1.282$, do not reject *H*<sub>0</sub> (as many public school teachers are certified),
    4.  *p*-value = 0.2912

16. &nbsp;

17. *Z* = 4.498, $\pm z_{0.005} = \pm 2.576$, reject *H*<sub>0</sub> (different)

18. &nbsp;

<!-- -->

19. 1.  ${\hat{p}}_{1} = 0.355$ and ${\hat{p}}_{2} = 0.41$
    2.  ${\hat{p}}_{1} - {\hat{p}}_{2} = \text{-}0.055$
    3.  $\left( {\text{-}0.1501,0.0401} \right)$
    4.  $H_{0}:p_{1} - p_{2} = 0$ vs. $H_{a}:p_{1} - p_{2} < 0.$ Test Statistic: $Z = \text{-}1.1335.$ Rejection Region: $\left( {\text{-}\infty,\text{-}1.645}\, \right\rbrack.$ Decision: Fail to reject *H*<sub>0</sub>.
20. &nbsp;

`````````````

## 9.5 Sample Size Considerations

````````````{note} Learning Objective

1.  To learn how to apply formulas for estimating the size samples that will be needed in order to construct a confidence interval for the difference in two population means or proportions that meets given criteria.

````````````

As was pointed out at the beginning of [Section 7.4 \"Sample Size Considerations\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07-s04) in [Chapter 7 \"Estimation\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07), sampling is typically done with definite objectives in mind. For example, a physician might wish to estimate the difference in the average amount of sleep gotten by patients suffering a certain condition with the average amount of sleep gotten by healthy adults, at 90% confidence and to within half an hour. Since sampling costs time, effort, and money, it would be useful to be able to estimate the smallest size samples that are likely to meet these criteria.

### Estimating $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ with Independent Samples

Assuming that large samples will be required, the confidence interval formula for estimating the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ between two population means using independent samples is $\left( {{\overset{-}{x}}_{1} - {\overset{-}{x}}_{2}} \right) \pm E$, where

$$E = z_{\alpha / 2}\sqrt{\frac{s_{1}^{2}}{n_{1}} + \frac{s_{2}^{2}}{n_{2}}}$$

To say that we wish to estimate the mean to within a certain number of units means that we want the margin of error *E* to be no larger than that number. The number $z_{\alpha / 2}$ is determined by the desired level of confidence.

The numbers *s*<sub>1</sub> and *s*<sub>2</sub> are estimates of the standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ of the two populations. In analogy with what we did in [Section 7.4 \"Sample Size Considerations\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07-s04) in [Chapter 7 \"Estimation\"](/chapters/ch-07-estimation.md#src-fwk-shafer-ch07) we will assume that we either know or can reasonably approximate $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}.$

We cannot solve for both *n*<sub>1</sub> and *n*<sub>2</sub>, so we have to make an assumption about their relative sizes. We will specify that they be equal. With these assumptions we obtain the minimum sample sizes needed by solving the equation displayed just above for $n_{1} = n_{2}.$

````````````{important} Minimum Equal Sample Sizes for Estimating the Difference in the Means of Two Populations Using Independent Samples

The estimated minimum equal sample sizes $n_{1} = n_{2}$ needed to estimate the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ in two population means to within *E* units at $100\left( {1 - \alpha} \right)$% confidence is

$$\begin{matrix}
{n_{1} = n_{2} = \frac{{(z_{\alpha / 2})}^{2}(\mathit{\sigma}_{1}^{2} + \mathit{\sigma}_{2}^{2})}{E^{2}}} & {(\text{rounded}\,\text{up})}
\end{matrix}$$

````````````

In all the examples and exercises the population standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ will be given.

### Example 13

A law firm wishes to estimate the difference in the mean delivery time of documents sent between two of its offices by two different courier companies, to within half an hour and with 99.5% confidence. From their records it will randomly sample the same number *n* of documents as delivered by each courier company. Determine how large *n* must be if the estimated standard deviations of the delivery times are 0.75 hour for one company and 1.15 hours for the other.

Solution:

Confidence level 99.5% means that $\alpha = 1 - 0.995 = 0.005$ so $\left. \alpha/ 2 = 0.0025. \right.$ From the last line of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we obtain $z_{0.0025} = 2.807.$

To say that the estimate is to be "to within half an hour" means that *E* = 0.5. Thus

$$n = \frac{\left( z_{\alpha / 2} \right)^{2}\left( {\mathit{\sigma}_{1}^{2} + \mathit{\sigma}_{2}^{2}} \right)}{E^{2}} = \frac{(2.807)^{2}\left( {0.75^{2} + 1.15^{2}} \right)}{0.5^{2}} = 59.40953746$$

which we round up to 60, since it is impossible to take a fractional observation. The law firm must sample 60 document deliveries by each company.

### Estimating $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ with Paired Samples

As we mentioned at the end of [Section 9.3 \"Comparison of Two Population Means: Paired Samples\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09-s03), if the sample is large (meaning that *n* ≥ 30) then in the formula for the confidence interval we may replace $t_{\alpha / 2}$ by $z_{\alpha / 2}$, so that the confidence interval formula becomes $\overset{-}{d} \pm E$ for

$$E = z_{\alpha / 2}\frac{s_{d}}{\sqrt{n}}$$

The number *s<sub>d</sub>* is an estimate of the standard deviations $\mathit{\sigma}_{d}$ of the population of differences. We must assume that we either know or can reasonably approximate $\mathit{\sigma}_{d}.$ Thus, assuming that large samples will be required to meet the criteria given, we can solve the displayed equation for *n* to obtain an estimate of the number of pairs needed in the sample.

````````````{important} Minimum Sample Size for Estimating the Difference in the Means of Two Populations Using Paired Difference Samples

The estimated minimum number of pairs *n* needed to estimate the difference $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ in two population means to within *E* units at $100\left( {1 - \alpha} \right)$% confidence using paired difference samples is

$$\begin{matrix}
{n = \frac{\left( z_{\alpha / 2} \right)^{2}\mathit{\sigma}_{d}^{2}}{E^{2}}} & {(\text{rounded}\,\text{up})}
\end{matrix}$$

````````````

In all the examples and exercises the population standard deviation of the differences $\mathit{\sigma}_{d}$ will be given.

### Example 14

An automotive tire manufacturer wishes to compare the mean lifetime of two tread designs under actual driving conditions. They will mount one of each type of tire on *n* vehicles (both on the front or both on the back) and measure the difference in remaining tread after 20,000 miles of driving. If the standard deviation of the differences is assumed to be 0.025 inch, find the minimum sample size needed to estimate the difference in mean depth (at 20,000 miles use) to within 0.01 inch at 99.9% confidence.

Solution:

Confidence level 99.9% means that $\alpha = 1 - 0.999 = 0.001$ so $\left. \alpha/ 2 = 0.0005. \right.$ From the last line of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we obtain $z_{0.0005} = 3.291.$

To say that the estimate is to be "to within 0.01 inch" means that *E* = 0.01. Thus

$$n = \frac{\left( z_{\alpha / 2} \right)^{2}\mathit{\sigma}_{d}^{2}}{E^{2}} = \frac{(3.291)^{2}(0.025)^{2}}{(0.01)^{2}} = 67.69175625$$

which we round up to 68. The manufacturer must test 68 pairs of tires.

### Estimating $p_{1} - p_{2}$

The confidence interval formula for estimating the difference $p_{1} - p_{2}$ between two population proportions is ${\hat{p}}_{1} - {\hat{p}}_{2} \pm E$, where

$$E = z_{\alpha / 2}\sqrt{\frac{{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right)}{n_{1}} + \frac{{\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)}{n_{2}}}$$

To say that we wish to estimate the mean to within a certain number of units means that we want the margin of error *E* to be no larger than that number. The number $z_{\alpha / 2}$ is determined by the desired level of confidence.

We cannot solve for both *n*<sub>1</sub> and *n*<sub>2</sub>, so we have to make an assumption about their relative sizes. We will specify that they be equal. With these assumptions we obtain the minimum sample sizes needed by solving the displayed equation for $n_{1} = n_{2}.$

````````````{important} Minimum Equal Sample Sizes for Estimating the Difference in Two Population Proportions

The estimated minimum equal sample sizes $n_{1} = n_{2}$ needed to estimate the difference $p_{1} - p_{2}$ in two population proportions to within *E* percentage points at $100\left( {1 - \alpha} \right)$% confidence is

$$\begin{matrix}
{n_{1} = n_{2} = \frac{\left( z_{\alpha / 2} \right)^{2}\left( {{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right) + {\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)} \right)}{E^{2}}} & {(\text{rounded}\,\text{up})}
\end{matrix}$$

````````````

Here we face the same dilemma that we encountered in the case of a single population proportion: the formula for estimating how large a sample to take contains the numbers ${\hat{p}}_{1}$ and ${\hat{p}}_{2}$, which we know only after we have taken the sample. There are two ways out of this dilemma. Typically the researcher will have some idea as to the values of the population proportions *p*<sub>1</sub> and *p*<sub>2</sub>, hence of what the sample proportions ${\hat{p}}_{1}$ and ${\hat{p}}_{2}$ are likely to be. If so, those estimates can be used in the formula.

The second approach to resolving the dilemma is simply to replace each of ${\hat{p}}_{1}$ and ${\hat{p}}_{2}$ in the formula by 0.5. As in the one-population case, this is the **most conservative estimate**, since it gives the largest possible estimate of *n*. If we have an estimate of only one of *p*<sub>1</sub> and *p*<sub>2</sub> we can use that estimate for it, and use the conservative estimate 0.5 for the other.

### Example 15

Find the minimum equal sample sizes necessary to construct a 98% confidence interval for the difference $p_{1} - p_{2}$ with a margin of error *E* = 0.05,

1.  assuming that no prior knowledge about *p*<sub>1</sub> or *p*<sub>2</sub> is available; and
2.  assuming that prior studies suggest that $p_{1} \approx 0.2$ and $p_{2} \approx 0.3.$

Solution:

Confidence level 98% means that $\alpha = 1 - 0.98 = 0.02$ so $\left. \alpha/ 2 = 0.01. \right.$ From the last line of [Figure 12.3 \"Critical Values of \"](/appendices/appendix.md#src-fwk-shafer-ch12-f03) we obtain $z_{0.01} = 2.326.$

1.  Since there is no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> we make the most conservative estimate that ${\hat{p}}_{1} = 0.5$ and ${\hat{p}}_{2} = 0.5.$ Then

    $$\begin{array}{l}
    {n_{1} = n_{2} = \frac{\left( z_{\alpha / 2} \right)^{2}\left( {{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right) + {\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)} \right)}{E^{2}}} \\
    {= \frac{(2.326)^{2}\left( {(0.5)(0.5) + (0.5)(0.5)} \right)}{0.05^{2}}} \\
    {= 1082.0552}
    \end{array}$$

    which we round up to 1,083. We must take a sample of size 1,083 from each population.

2.  Since $p_{1} \approx 0.2$ we estimate ${\hat{p}}_{1}$ by 0.2, and since $p_{2} \approx 0.3$ we estimate ${\hat{p}}_{2}$ by 0.3. Thus we obtain

    $$\begin{array}{l}
    {n_{1} = n_{2} = \frac{\left( z_{\alpha / 2} \right)^{2}\left( {{\hat{p}}_{1}\left( {1 - {\hat{p}}_{1}} \right) + {\hat{p}}_{2}\left( {1 - {\hat{p}}_{2}} \right)} \right)}{E^{2}}} \\
    {= \frac{(2.326)^{2}\left( {(0.2)(0.8) + (0.3)(0.7)} \right)}{0.05^{2}}} \\
    {= 800.720848}
    \end{array}$$

    which we round up to 801. We must take a sample of size 801 from each population.

````````````{important} Key Takeaways

- If the population standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ are known or can be estimated, then the minimum equal sizes of independent samples needed to obtain a confidence interval for the difference $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ in two population means with a given maximum error of the estimate *E* and a given level of confidence can be estimated.
- If the standard deviation $\mathit{\sigma}_{d}$ of the population of differences in pairs drawn from two populations is known or can be estimated, then the minimum number of sample pairs needed under paired difference sampling to obtain a confidence interval for the difference $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ in two population means with a given maximum error of the estimate *E* and a given level of confidence can be estimated.
- The minimum equal sample sizes needed to obtain a confidence interval for the difference in two population proportions with a given maximum error of the estimate and a given level of confidence can always be estimated. If there is prior knowledge of the population proportions *p*<sub>1</sub> and *p*<sub>2</sub> then the estimate can be sharpened.

````````````

### Exercises

### Basic

1.  Estimate the common sample size *n* of equally sized independent samples needed to estimate $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ as specified when the population standard deviations are as shown.

    1.  90% confidence, to within 3 units, $\mathit{\sigma}_{1} = 10$ and $\mathit{\sigma}_{2} = 7$
    2.  99% confidence, to within 4 units, $\mathit{\sigma}_{1} = 6.8$ and $\mathit{\sigma}_{2} = 9.3$
    3.  95% confidence, to within 5 units, $\mathit{\sigma}_{1} = 22.6$ and $\mathit{\sigma}_{2} = 31.8$

2.  Estimate the common sample size *n* of equally sized independent samples needed to estimate $\mathit{\mu}_{1} - \mathit{\mu}_{2}$ as specified when the population standard deviations are as shown.

    1.  80% confidence, to within 2 units, $\mathit{\sigma}_{1} = 14$ and $\mathit{\sigma}_{2} = 23$
    2.  90% confidence, to within 0.3 units, $\mathit{\sigma}_{1} = 1.3$ and $\mathit{\sigma}_{2} = 0.8$
    3.  99% confidence, to within 11 units, $\mathit{\sigma}_{1} = 42$ and $\mathit{\sigma}_{2} = 37$

3.  Estimate the number *n* of pairs that must be sampled in order to estimate $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ as specified when the standard deviation *s<sub>d</sub>* of the population of differences is as shown.

    1.  80% confidence, to within 6 units, $\mathit{\sigma}_{d} = 26.5$
    2.  95% confidence, to within 4 units, $\mathit{\sigma}_{d} = 12$
    3.  90% confidence, to within 5.2 units, $\mathit{\sigma}_{d} = 11.3$

4.  Estimate the number *n* of pairs that must be sampled in order to estimate $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ as specified when the standard deviation *s<sub>d</sub>* of the population of differences is as shown.

    1.  90% confidence, to within 20 units, $\mathit{\sigma}_{d} = 75.5$
    2.  95% confidence, to within 11 units, $\mathit{\sigma}_{d} = 31.4$
    3.  99% confidence, to within 1.8 units, $\mathit{\sigma}_{d} = 4$

5.  Estimate the minimum equal sample sizes $n_{1} = n_{2}$ necessary in order to estimate $p_{1} - p_{2}$ as specified.

    1.  80% confidence, to within 0.05 (five percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.20$ and $p_{2} \approx 0.65$

    2.  90% confidence, to within 0.02 (two percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.75$ and $p_{2} \approx 0.63$

    3.  95% confidence, to within 0.10 (ten percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.11$ and $p_{2} \approx 0.37$

6.  Estimate the minimum equal sample sizes $n_{1} = n_{2}$ necessary in order to estimate $p_{1} - p_{2}$ as specified.

    1.  80% confidence, to within 0.02 (two percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.78$ and $p_{2} \approx 0.65$

    2.  90% confidence, to within 0.05 (two percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.12$ and $p_{2} \approx 0.24$

    3.  95% confidence, to within 0.10 (ten percentage points)

        1.  when no prior knowledge of *p*<sub>1</sub> or *p*<sub>2</sub> is available
        2.  when prior studies indicate that $p_{1} \approx 0.14$ and $p_{2} \approx 0.21$

### Applications

7.  An educational researcher wishes to estimate the difference in average scores of elementary school children on two versions of a 100-point standardized test, at 99% confidence and to within two points. Estimate the minimum equal sample sizes necessary if it is known that the standard deviation of scores on different versions of such tests is 4.9.

8.  A university administrator wishes to estimate the difference in mean grade point averages among all men affiliated with fraternities and all unaffiliated men, with 95% confidence and to within 0.15. It is known from prior studies that the standard deviations of grade point averages in the two groups have common value 0.4. Estimate the minimum equal sample sizes necessary to meet these criteria.

9.  An automotive tire manufacturer wishes to estimate the difference in mean wear of tires manufactured with an experimental material and ordinary production tire, with 90% confidence and to within 0.5 mm. To eliminate extraneous factors arising from different driving conditions the tires will be tested in pairs on the same vehicles. It is known from prior studies that the standard deviations of the differences of wear of tires constructed with the two kinds of materials is 1.75 mm. Estimate the minimum number of pairs in the sample necessary to meet these criteria.

10. To assess the relative happiness of men and women in their marriages, a marriage counselor plans to administer a test measuring happiness in marriage to *n* randomly selected married couples, record their test scores, find the differences, and then draw inferences on the possible difference. Let $\mathit{\mu}_{1}$ and $\mathit{\mu}_{2}$ be the true average levels of happiness in marriage for men and women respectively as measured by this test. Suppose it is desired to find a 90% confidence interval for estimating $\mathit{\mu}_{d} = \mathit{\mu}_{1} - \mathit{\mu}_{2}$ to within two test points. Suppose further that, from prior studies, it is known that the standard deviation of the differences in test scores is $\mathit{\sigma}_{d} \approx 10.$ What is the minimum number of married couples that must be included in this study?

11. A journalist plans to interview an equal number of members of two political parties to compare the proportions in each party who favor a proposal to allow citizens with a proper license to carry a concealed handgun in public parks. Let *p*<sub>1</sub> and *p*<sub>2</sub> be the true proportions of members of the two parties who are in favor of the proposal. Suppose it is desired to find a 95% confidence interval for estimating $p_{1} - p_{2}$ to within 0.05. Estimate the minimum equal number of members of each party that must be sampled to meet these criteria.

12. A member of the state board of education wants to compare the proportions of National Board Certified (NBC) teachers in private high schools and in public high schools in the state. His study plan calls for an equal number of private school teachers and public school teachers to be included in the study. Let *p*<sub>1</sub> and *p*<sub>2</sub> be these proportions. Suppose it is desired to find a 99% confidence interval that estimates $p_{1} - p_{2}$ to within 0.05.

    1.  Supposing that both proportions are known, from a prior study, to be approximately 0.15, compute the minimum common sample size needed.
    2.  Compute the minimum common sample size needed on the supposition that nothing is known about the values of *p*<sub>1</sub> and *p*<sub>2</sub>.

`````````````{admonition} Answers
:class: dropdown

1.  1.  $n_{1} = n_{2} = 45$,
    2.  $n_{1} = n_{2} = 56.$
    3.  $n_{1} = n_{2} = 234$
2. &nbsp;
3.  1.  $n_{1} = n_{2} = 33.$
    2.  $n_{1} = n_{2} = 35.$
    3.  $n_{1} = n_{2} = 13$
4. &nbsp;
5.  1.  1.  $n_{1} = n_{2} = 329$,
        2.  $n_{1} = n_{2} = 255.$
    2.  1.  $n_{1} = n_{2} = 3383$,
        2.  $n_{1} = n_{2} = 2846.$
    3.  1.  $n_{1} = n_{2} = 193$,
        2.  $n_{1} = n_{2} = 128$
6. &nbsp;

<!-- -->

7.  $n_{1} = n_{2} \approx 80$

8. &nbsp;

9.  $n_{1} = n_{2} \approx 34$

10. &nbsp;

11. $n_{1} = n_{2} \approx 769$

12. &nbsp;

`````````````
