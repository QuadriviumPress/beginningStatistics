(src-fwk-shafer-ch11)=

# Chapter 11 Chi-Square Tests and *F*-Tests

In previous chapters you saw how to test hypotheses concerning population means and population proportions. The idea of testing hypotheses can be extended to many other situations that involve different parameters and use different test statistics. Whereas the standardized test statistics that appeared in earlier chapters followed either a normal or Student *t*-distribution, in this chapter the tests will involve two other very common and useful distributions, the chi-square and the *F*-distributions. The chi-square distribution[^stats-1] arises in tests of hypotheses concerning the independence of two random variables and concerning whether a discrete random variable follows a specified distribution. The *F*-distribution[^stats-2] arises in tests of hypotheses concerning whether or not two population variances are equal and concerning whether or not three or more population means are equal.

## 11.1 Chi-Square Tests for Independence

````````````{note} Learning Objectives

1.  To understand what chi-square distributions are.
2.  To understand how to use a chi-square test to judge whether two factors are independent.

````````````

### Chi-Square Distributions

As you know, there is a whole family of *t*-distributions, each one specified by a parameter called the *degrees of freedom*, denoted $df.$ Similarly, all the chi-square distributions form a family, and each of its members is also specified by a parameter $df$, the number of degrees of freedom. Chi is a Greek letter denoted by the symbol $\chi$ and chi-square is often denoted by $\chi^{2}.$ [Figure 11.1 \"Many Chi-Square Distributions\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s01-f01) shows several chi-square distributions for different degrees of freedom. A chi-square random variable[^stats-3] is a random variable that assumes only positive values and follows a chi-square distribution.

``````{figure} /images/redrawn/fig-11-01.svg
:alt: Chi-square density curves for 1, 2, 3, 5, and 10 degrees of freedom on a horizontal axis from 0 to 15. With 1 or 2 degrees of freedom the curve is highest at 0 and decreases; with more degrees of freedom it rises to a peak and has a long right tail, and the peak moves right and flattens as df grows.
:name: src-fwk-shafer-ch11-s01-s01-f01

Figure 11.1 Many $\chi^{2}$ Distributions
``````

````````````{important} Definition

*The value of the chi-square random variable* $\chi^{2}$ *with* $df = k$ *that cuts off a right tail of area* *c* *is denoted* $\chi_{c}^{2}$ *and is called a* **critical value**. *See [Figure 11.2](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s01-f02).*

``````{figure} /images/redrawn/fig-11-02.svg
:alt: A right-skewed chi-square density. The right tail beyond the point χ²_c is shaded and labeled c; the area to its left is labeled 1 − c.
:name: src-fwk-shafer-ch11-s01-s01-f02

Figure 11.2 $\chi_{c}^{2}$ Illustrated
``````

````````````

[Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04) gives values of $\chi_{c}^{2}$ for various values of *c* and under several chi-square distributions with various degrees of freedom.

### Tests for Independence

Hypotheses tests encountered earlier in the book had to do with how the numerical values of two population parameters compared. In this subsection we will investigate hypotheses that have to do with whether or not two random variables take their values independently, or whether the value of one has a relation to the value of the other. Thus the hypotheses will be expressed in words, not mathematical symbols. We build the discussion around the following example.

There is a theory that the gender of a baby in the womb is related to the baby's heart rate: baby girls tend to have higher heart rates. Suppose we wish to test this theory. We examine the heart rate records of 40 babies taken during their mothers' last prenatal checkups before delivery, and to each of these 40 randomly selected records we compute the values of two random measures: 1) gender and 2) heart rate. In this context these two random measures are often called factors[^stats-4]. Since the burden of proof is that heart rate and gender are related, not that they are unrelated, the problem of testing the theory on baby gender and heart rate can be formulated as a test of the following hypotheses:

$$\begin{array}{rcl}
H_{0} & : & {\text{Baby}\,\text{gender}\,\text{and}\,\text{baby}\,\text{heart}\,\text{rate}\,\text{are}\,\text{independent}} \\
{\text{vs}.\, H_{a}} & : & {\text{Baby}\,\text{gender}\,\text{and}\,\text{baby}\,\text{heart}\,\text{rate}\,\text{are}\, not\,\text{independent}}
\end{array}$$

The factor gender has two natural categories or levels: boy and girl. We divide the second factor, heart rate, into two levels, low and high, by choosing some heart rate, say 145 beats per minute, as the cutoff between them. A heart rate below 145 beats per minute will be considered low and 145 and above considered high. The 40 records give rise to a 2 × 2 *contingency table*. By adjoining row totals, column totals, and a grand total we obtain the table shown as [Table 11.1 \"Baby Gender and Heart Rate\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t01). The four entries in boldface type are counts of observations from the sample of *n* = 40. There were 11 girls with low heart rate, 17 boys with low heart rate, and so on. They form the *core* of the expanded table.

(src-fwk-shafer-ch11-s01-s02-t01)=

Table 11.1 Baby Gender and Heart Rate

````````{list-table}
:header-rows: 2

- -
  -
  - Heart Rate
  - Heart Rate
  -
  -
- -
  -
  - Low
  - High
  - Row Total
  -
- - Gender
  - Girl
  - **11**
  - **7**
  - 18
  -
- - Gender
  - Boy
  - **17**
  - **5**
  - 22
  -
- - Column Total
  - Column Total
  - 28
  - 12
  - Total = 40
  -

````````

In analogy with the fact that the probability of independent events is the product of the probabilities of each event, if heart rate and gender were independent then we would expect the number in each core cell to be close to the product of the row total *R* and column total *C* of the row and column containing it, divided by the sample size *n*. Denoting such an expected number of observations *E*, these four expected values are:

- 1st row and 1st column: $\left. E = \left( {R \times C} \right)/ n = 18 \times 28/ 40 = 12.6 \right.$
- 1st row and 2nd column: $\left. E = \left( {R \times C} \right)/ n = 18 \times 12/ 40 = 5.4 \right.$
- 2nd row and 1st column: $\left. E = \left( {R \times C} \right)/ n = 22 \times 28/ 40 = 15.4 \right.$
- 2nd row and 2nd column: $\left. E = \left( {R \times C} \right)/ n = 22 \times 12/ 40 = 6.6 \right.$

We update [Table 11.1 \"Baby Gender and Heart Rate\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t01) by placing each expected value in its corresponding core cell, right under the observed value in the cell. This gives the updated table [Table 11.2 \"Updated Baby Gender and Heart Rate\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t02).

(src-fwk-shafer-ch11-s01-s02-t02)=

Table 11.2 Updated Baby Gender and Heart Rate

````````{list-table}
:header-rows: 2

- -
  -
  - Heart Rate
  - Heart Rate
  -
  -
- -
  -
  - Low
  - High
  - Row Total
  -
- - Gender
  - Girl
  - $\begin{array}{l}
    {O = 11} \\
    {E = 12.6}
    \end{array}$
  - $\begin{array}{l}
    {O = 7} \\
    {E = 5.4}
    \end{array}$
  - *R* = 18
  -
- - Gender
  - Boy
  - $\begin{array}{l}
    {O = 17} \\
    {E = 15.4}
    \end{array}$
  - $\begin{array}{l}
    {O = 5} \\
    {E = 6.6}
    \end{array}$
  - *R* = 22
  -
- - Column Total
  - Column Total
  - *C* = 28
  - *C* = 12
  - *n* = 40
  -

````````

A measure of how much the data deviate from what we would expect to see if the factors really were independent is the sum of the squares of the difference of the numbers in each core cell, or, standardizing by dividing each square by the expected number in the cell, the sum $\left. \Sigma\left( {O - E} \right)^{2}/ E. \right.$ We would reject the null hypothesis that the factors are independent only if this number is large, so the test is right-tailed. In this example the random variable $\left. \Sigma\left( {O - E} \right)^{2}/ E \right.$ has the chi-square distribution with one degree of freedom. If we had decided at the outset to test at the 10% level of significance, the critical value defining the rejection region would be, reading from [Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04), $\chi_{\alpha}^{2} = \chi_{0.10}^{2} = 2.706$, so that the rejection region would be the interval $\left\lbrack {2.706,\infty} \right).$ When we compute the value of the standardized test statistic we obtain

$$\Sigma\frac{\left( {O - E} \right)^{2}}{E} = \frac{\left( {11 - 12.6} \right)^{2}}{12.6} + \frac{\left( {7 - 5.4} \right)^{2}}{5.4} + \frac{\left( {17 - 15.4} \right)^{2}}{15.4} + \frac{\left( {5 - 6.6} \right)^{2}}{6.6} = 1.231$$

Since 1.231 \< 2.706, the decision is not to reject *H*<sub>0</sub>. See [Figure 11.3 \"Baby Gender Prediction\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-f01). The data do not provide sufficient evidence, at the 10% level of significance, to conclude that heart rate and gender are related.

``````{figure} /images/redrawn/fig-11-03.svg
:alt: Chi-square density with 1 degree of freedom. The right tail of area α = 0.10 beyond the critical value χ²_α = 2.706 is shaded. On the number line below, the rejection region χ² ≥ 2.706 is red, and the test statistic χ² = 1.231, marked with a star, lies outside it.
:name: src-fwk-shafer-ch11-s01-s02-f01

Figure 11.3 Baby Gender Prediction
``````

With this specific example in mind, now turn to the general situation. In the general setting of testing the independence of two factors, call them *Factor 1* and *Factor 2*, the hypotheses to be tested are

$$\begin{array}{rcl}
H_{0} & : & {\text{The}\,\text{two}\,\text{factors}\,\text{are}\,\text{independent}} \\
{\text{vs}.\, H_{a}} & : & {\text{The}\,\text{two}\,\text{factors}\,\text{are}\, not\,\text{independent}}
\end{array}$$

As in the example each factor is divided into a number of categories or levels. These could arise naturally, as in the boy-girl division of gender, or somewhat arbitrarily, as in the high-low division of heart rate. Suppose Factor 1 has *I* levels and Factor 2 has *J* levels. Then the information from a random sample gives rise to a general *I* × *J* contingency table, which with row totals, column totals, and a grand total would appear as shown in [Table 11.3 \"General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t03). Each cell may be labeled by a pair of indices $\left( {i,j} \right).$ $O_{ij}$ stands for the observed count of observations in the cell in row *i* and column *j*, *R<sub>i</sub>* for the $i^{th}$ row total and *C<sub>j</sub>* for the $j^{th}$ column total. To simplify the notation we will drop the indices so [Table 11.3 \"General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t03) becomes [Table 11.4 \"Simplified General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t04). Nevertheless it is important to keep in mind that the *O*s, the *R*s and the *C*s, though denoted by the same symbols, are in fact different numbers.

(src-fwk-shafer-ch11-s01-s02-t03)=

Table 11.3 General Contingency Table

````````{list-table}
:header-rows: 2

- -
  -
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  -
  -
- -
  -
  - 1
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *j*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *J*
  - Row Total
  -
- - Factor 1 Levels
  - 1
  - *O*<sub>11</sub>
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{1j}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{1J}$
  - *R*<sub>1</sub>
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *i*
  - $O_{i1}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{ij}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{iJ}$
  - *R<sub>i</sub>*
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *I*
  - $O_{I1}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{Ij}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $O_{IJ}$
  - *R<sub>I</sub>*
  -
- - Column Total
  - Column Total
  - *C*<sub>1</sub>
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C<sub>j</sub>*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C<sub>J</sub>*
  - *n*
  -

````````

(src-fwk-shafer-ch11-s01-s02-t04)=

Table 11.4 Simplified General Contingency Table

````````{list-table}
:header-rows: 2

- -
  -
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  -
  -
- -
  -
  - 1
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *j*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *J*
  - Row Total
  -
- - Factor 1 Levels
  - 1
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - *R*
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *i*
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - *R*
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *I*
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *O*
  - *R*
  -
- - Column Total
  - Column Total
  - *C*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C*
  - *n*
  -

````````

As in the example, for each core cell in the table we compute what would be the *expected number* *E* of observations if the two factors were independent. *E* is computed for each core cell (each cell with an *O* in it) of [Table 11.4 \"Simplified General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t04) by the rule applied in the example:

$$E = \frac{R \times C}{n}$$

where *R* is the row total and *C* is the column total corresponding to the cell, and *n* is the sample size.

After the expected number is computed for every cell, [Table 11.4 \"Simplified General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t04) is updated to form [Table 11.5 \"Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t05) by inserting the computed value of *E* into each core cell.

(src-fwk-shafer-ch11-s01-s02-t05)=

Table 11.5 Updated General Contingency Table

````````{list-table}
:header-rows: 2

- -
  -
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  - Factor 2 Levels
  -
  -
- -
  -
  - 1
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *j*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *J*
  - Row Total
  -
- - Factor 1 Levels
  - 1
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - *R*
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *i*
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - *R*
  -
- - Factor 1 Levels
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  - ⋮
  -
- - Factor 1 Levels
  - *I*
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - $\begin{matrix}
    O \\
    E
    \end{matrix}$
  - *R*
  -
- - Column Total
  - Column Total
  - *C*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C*
  - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
  - *C*
  - *n*
  -

````````

Here is the test statistic for the general hypothesis based on [Table 11.5 \"Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t05), together with the conditions that it follow a chi-square distribution.

````````````{important} Test Statistic for Testing the Independence of Two Factors

$$\chi^{2} = \Sigma\frac{\left( {O - E} \right)^{2}}{E}$$

where the sum is over all core cells of the table.

If

1.  the two study factors are independent, and
2.  the observed count *O* of each cell in [Table 11.5 \"Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t05) is at least 5,

then $\chi^{2}$ approximately follows a chi-square distribution with $df = \left( {I\text{-}1} \right) \times \left( {J\text{-}1} \right)$ degrees of freedom.

````````````

The same five-step procedures, either the critical value approach or the *p*-value approach, that were introduced in [Section 8.1 \"The Elements of Hypothesis Testing\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08-s01) and [Section 8.3 \"The Observed Significance of a Test\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08-s03) of [Chapter 8 \"Testing Hypotheses\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08) are used to perform the test, which is always right-tailed.

(src-fwk-shafer-ch11-s01-s02-n03)=

### Example 1

A researcher wishes to investigate whether students' scores on a college entrance examination (CEE) have any indicative power for future college performance as measured by GPA. In other words, he wishes to investigate whether the factors CEE and GPA are independent or not. He randomly selects *n* = 100 students in a college and notes each student's score on the entrance examination and his grade point average at the end of the sophomore year. He divides entrance exam scores into two levels and grade point averages into three levels. Sorting the data according to these divisions, he forms the contingency table shown as [Table 11.6 \"CEE versus GPA Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t06), in which the row and column totals have already been computed.

(src-fwk-shafer-ch11-s01-s02-t06)=

Table 11.6 CEE versus GPA Contingency Table

````````{list-table}
:header-rows: 2

- -
  -
  - GPA
  - GPA
  - GPA
  -
  -
- -
  -
  - \<2.7
  - 2.7 to 3.2
  - \>3.2
  - Row Total
  -
- - CEE
  - $< 1800$
  - **35**
  - **12**
  - **5**
  - 52
  -
- - CEE
  - $\geq 1800$
  - **6**
  - **24**
  - **18**
  - 48
  -
- - Column Total
  - Column Total
  - 41
  - 36
  - 23
  - $\text{Total} = 100$
  -

````````

Test, at the 1% level of significance, whether these data provide sufficient evidence to conclude that CEE scores indicate future performance levels of incoming college freshmen as measured by GPA.

Solution:

We perform the test using the critical value approach, following the usual five-step method outlined at the end of [Section 8.1 \"The Elements of Hypothesis Testing\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08-s01) in [Chapter 8 \"Testing Hypotheses\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08).

- Step 1. The hypotheses are

  $$\begin{array}{rcl}
  H_{0} & : & \text{CEE and GPA are independent factors} \\
  {\text{vs}.\, H_{a}} & : & {\text{CEE and GPA are }{not}\text{ independent factors}}
  \end{array}$$

- Step 2. The distribution is chi-square.

- Step 3. To compute the value of the test statistic we must first compute the expected number for each of the six core cells (the ones whose entries are boldface):

  - 1st row and 1st column: $\left. E = \left( {R \times C} \right)/ n = 41 \times 52/ 100 = 21.32 \right.$
  - 1st row and 2nd column: $\left. E = \left( {R \times C} \right)/ n = 36 \times 52/ 100 = 18.72 \right.$
  - 1st row and 3rd column: $\left. E = \left( {R \times C} \right)/ n = 23 \times 52/ 100 = 11.96 \right.$
  - 2nd row and 1st column: $\left. E = \left( {R \times C} \right)/ n = 41 \times 48/ 100 = 19.68 \right.$
  - 2nd row and 2nd column: $\left. E = \left( {R \times C} \right)/ n = 36 \times 48/ 100 = 17.28 \right.$
  - 2nd row and 3rd column: $\left. E = \left( {R \times C} \right)/ n = 23 \times 48/ 100 = 11.04 \right.$

  [Table 11.6 \"CEE versus GPA Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t06) is updated to [Table 11.7 \"Updated CEE versus GPA Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-t07).

  (src-fwk-shafer-ch11-s01-s02-t07)=

  Table 11.7 Updated CEE versus GPA Contingency Table

  ````````{list-table}
  :header-rows: 2

  - -
    -
    - GPA
    - GPA
    - GPA
    -
    -
  - -
    -
    - \<2.7
    - 2.7 to 3.2
    - \>3.2
    - Row Total
    -
  - - CEE
    - $< 1800$
    - $\begin{array}{l}
      {O = 35} \\
      {E = 21.32}
      \end{array}$
    - $\begin{array}{l}
      {O = 12} \\
      {E = 18.72}
      \end{array}$
    - $\begin{array}{l}
      {O = 5} \\
      {E = 11.96}
      \end{array}$
    - *R* = 52
    -
  - - CEE
    - $\geq 1800$
    - $\begin{array}{l}
      {O = 6} \\
      {E = 19.68}
      \end{array}$
    - $\begin{array}{l}
      {O = 24} \\
      {E = 17.28}
      \end{array}$
    - $\begin{array}{l}
      {O = 18} \\
      {E = 11.04}
      \end{array}$
    - *R* = 48
    -
  - - Column Total
    - Column Total
    - *C* = 41
    - *C* = 36
    - *C* = 23
    - *n* = 100
    -

  ````````

  The test statistic is

  $$\begin{array}{lccc}
  \chi^{2} & = & {\Sigma^{}\frac{{(O - E)}^{2}}{E}} & \\
   & = & {\frac{{(35 - 21.32)}^{2}}{21.32} + \frac{{(12 - 18.72)}^{2}}{18.72} + \frac{{(5 - 11.96)}^{2}}{11.96}} & \\
   & & {+ \frac{{(6 - 19.68)}^{2}}{19.68} + \frac{{(24 - 17.28)}^{2}}{17.28} + \frac{{(18 - 11.04)}^{2}}{11.04}} & \\
   & = & 31.75 &
  \end{array}$$

- Step 4. Since the CEE factor has two levels and the GPA factor has three, *I* = 2 and *J* = 3. Thus the test statistic follows the chi-square distribution with $df = \left( {2 - 1} \right) \times \left( {3 - 1} \right) = 2$ degrees of freedom.

  Since the test is right-tailed, the critical value is $\chi_{0.01}^{2}.$ Reading from [Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04), $\chi_{0.01}^{2} = 9.210$, so the rejection region is $\left\lbrack {9.210,\infty} \right).$

- Step 5. Since 31.75 \> 9.21 the decision is to reject the null hypothesis. See [Figure 11.4](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-f02). The data provide sufficient evidence, at the 1% level of significance, to conclude that CEE score and GPA are not independent: the entrance exam score has predictive power.

``````{figure} /images/redrawn/fig-11-04.svg
:alt: Chi-square density with 2 degrees of freedom. The thin right tail of area α = 0.01 beyond the critical value χ²_α = 9.210 is shaded. On the number line below, the rejection region χ² ≥ 9.210 is red, and the test statistic χ² = 31.75, marked with a star near the right end, lies far inside it.
:name: src-fwk-shafer-ch11-s01-s02-f02

Figure 11.4 [Note 11.9 \"Example 1\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s01-s02-n03){.xref xrefstyle="select: title"}
``````

````````````{important} Key Takeaways

- Critical values of a chi-square distribution with degrees of freedom $df$ are found in [Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04).
- A chi-square test[^stats-5] can be used to evaluate the hypothesis that two random variables or factors are independent.

````````````

### Exercises

### Basic

1.  Find $\chi_{0.01}^{2}$ for each of the following number of degrees of freedom.

    1.  $df = 5$
    2.  $df = 11$
    3.  $df = 25$

2.  Find $\chi_{0.05}^{2}$ for each of the following number of degrees of freedom.

    1.  $df = 6$
    2.  $df = 12$
    3.  $df = 30$

3.  Find $\chi_{0.10}^{2}$ for each of the following number of degrees of freedom.

    1.  $df = 6$
    2.  $df = 12$
    3.  $df = 30$

4.  Find $\chi_{0.01}^{2}$ for each of the following number of degrees of freedom.

    1.  $df = 7$
    2.  $df = 10$
    3.  $df = 20$

5.  For $df = 7$ and $\alpha = 0.05$, find

    1.  $\chi_{\alpha}^{2}$
    2.  $\chi_{\frac{\alpha}{2}}^{2}$

6.  For $df = 17$ and $\alpha = 0.01$, find

    1.  $\chi_{\alpha}^{2}$
    2.  $\chi_{\frac{\alpha}{2}}^{2}$

7.  A data sample is sorted into a 2 × 2 contingency table based on two factors, each of which has two levels.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Factor 1
      - Factor 1
      -
      -
    - -
      -
      - Level 1
      - Level 2
      - Row Total
      -
    - - Factor 2
      - Level 1
      - $\begin{array}{l}
        20
        \end{array}$
      - $\begin{array}{l}
        10
        \end{array}$
      - *R*
      -
    - - Factor 2
      - Level 2
      - $\begin{array}{l}
        15
        \end{array}$
      - $\begin{array}{l}
        5
        \end{array}$
      - *R*
      -
    - - Column Total
      - Column Total
      - *C*
      - *C*
      - *n*
      -

    ````````

    1.  Find the column totals, the row totals, and the grand total, *n*, of the table.
    2.  Find the expected number *E* of observations for each cell based on the assumption that the two factors are independent (that is, just use the formula $\left. E = \left( {R \times C} \right)/ n \right.$).
    3.  Find the value of the chi-square test statistic $\chi^{2}.$
    4.  Find the number of degrees of freedom of the chi-square test statistic.

8.  A data sample is sorted into a 3 × 2 contingency table based on two factors, one of which has three levels and the other of which has two levels.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Factor 1
      - Factor 1
      -
      -
    - -
      -
      - Level 1
      - Level 2
      - Row Total
      -
    - - Factor 2
      - Level 1
      - $\begin{array}{l}
        20
        \end{array}$
      - $\begin{array}{l}
        10
        \end{array}$
      - *R*
      -
    - - Factor 2
      - Level 2
      - $\begin{array}{l}
        15
        \end{array}$
      - $\begin{array}{l}
        5
        \end{array}$
      - *R*
      -
    - - Factor 2
      - Level 3
      - $\begin{array}{l}
        10
        \end{array}$
      - $\begin{array}{l}
        20
        \end{array}$
      - *R*
      -
    - - Column Total
      - Column Total
      - *C*
      - *C*
      - *n*
      -

    ````````

    1.  Find the column totals, the row totals, and the grand total, *n*, of the table.
    2.  Find the expected number *E* of observations for each cell based on the assumption that the two factors are independent (that is, just use the formula $\left. E = \left( {R \times C} \right)/ n \right.$).
    3.  Find the value of the chi-square test statistic $\chi^{2}.$
    4.  Find the number of degrees of freedom of the chi-square test statistic.

### Applications

9.  A child psychologist believes that children perform better on tests when they are given perceived freedom of choice. To test this belief, the psychologist carried out an experiment in which 200 third graders were randomly assigned to two groups, *A* and *B*. Each child was given the same simple logic test. However in group *B*, each child was given the freedom to choose a test booklet from many with various drawings on the covers. The performance of each child was rated as Very Good, Good, and Fair. The results are summarized in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to support the psychologist's belief.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Group
      - Group
      -
    - -
      -
      - *A*
      - *B*
      -
    - - Performance
      - Very Good
      - 32
      - 29
      -
    - - Performance
      - Good
      - 55
      - 61
      -
    - - Performance
      - Fair
      - 10
      - 13
      -

    ````````

10. In regard to wine tasting competitions, many experts claim that the first glass of wine served sets a reference taste and that a different reference wine may alter the relative ranking of the other wines in competition. To test this claim, three wines, *A*, *B* and *C*, were served at a wine tasting event. Each person was served a single glass of each wine, but in different orders for different guests. At the close, each person was asked to name the best of the three. One hundred seventy-two people were at the event and their top picks are given in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to support the claim that wine experts' preference is dependent on the first served wine.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Top Pick
      - Top Pick
      - Top Pick
      -
    - -
      -
      - *A*
      - *B*
      - *C*
      -
    - - First Glass
      - *A*
      - 12
      - 31
      - 27
      -
    - - First Glass
      - *B*
      - 15
      - 40
      - 21
      -
    - - First Glass
      - *C*
      - 10
      - 9
      - 7
      -

    ````````

11. Is being left-handed hereditary? To answer this question, 250 adults are randomly selected and their handedness and their parents' handedness are noted. The results are summarized in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to conclude that there is a hereditary element in handedness.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Number of Parents Left-Handed
      - Number of Parents Left-Handed
      - Number of Parents Left-Handed
      -
    - -
      -
      - 0
      - 1
      - 2
      -
    - - Handedness
      - Left
      - 8
      - 10
      - 12
      -
    - - Handedness
      - Right
      - 178
      - 21
      - 21
      -

    ````````

12. Some geneticists claim that the genes that determine left-handedness also govern development of the language centers of the brain. If this claim is true, then it would be reasonable to expect that left-handed people tend to have stronger language abilities. A study designed to text this claim randomly selected 807 students who took the Graduate Record Examination (GRE). Their scores on the language portion of the examination were classified into three categories: *low*, *average*, and *high*, and their handedness was also noted. The results are given in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that left-handed people tend to have stronger language abilities.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - GRE English Scores
      - GRE English Scores
      - GRE English Scores
      -
    - -
      -
      - Low
      - Average
      - High
      -
    - - Handedness
      - Left
      - 18
      - 40
      - 22
      -
    - - Handedness
      - Right
      - 201
      - 360
      - 166
      -

    ````````

13. It is generally believed that children brought up in stable families tend to do well in school. To verify such a belief, a social scientist examined 290 randomly selected students' records in a public high school and noted each student's family structure and academic status four years after entering high school. The data were then sorted into a 2 × 3 contingency table with two factors. Factor 1 has two levels: *graduated* and *did not graduate*. Factor 2 has three levels: *no parent*, *one parent*, and *two parents*. The results are given in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to conclude that family structure matters in school performance of the students.

    ````````{list-table}
    :header-rows: 2

    - -
      -
      - Academic Status
      - Academic Status
      -
    - -
      -
      - Graduated
      - Did Not Graduate
      -
    - - Family
      - No parent
      - 18
      - 31
      -
    - - Family
      - One parent
      - 101
      - 44
      -
    - - Family
      - Two parents
      - 70
      - 26
      -

    ````````

14. A large middle school administrator wishes to use celebrity influence to encourage students to make healthier choices in the school cafeteria. The cafeteria is situated at the center of an open space. Every day at lunchtime students get their lunch and a drink in three separate lines leading to three separate serving stations. As an experiment, the school administrator displayed a poster of a popular teen pop star drinking milk at each of the three areas where drinks are provided, except the milk in the poster is different at each location: one shows white milk, one shows strawberry-flavored pink milk, and one shows chocolate milk. After the first day of the experiment the administrator noted the students' milk choices separately for the three lines. The data are given in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to conclude that the posters had some impact on the students' drink choices.

    ````````{list-table}
    :header-rows: 2

    - -
      - Student Choice
      - Student Choice
      - Student Choice
    - -
      - Regular
      - Strawberry
      - Chocolate
    - - Poster Choice
      - Poster Choice
      - Poster Choice
      - Poster Choice
    - - Regular
      - 38
      - 28
      - 40
    - - Strawberry
      - 18
      - 51
      - 24
    - - Chocolate
      - 32
      - 32
      - 53

    ````````

### Large Data Set Exercise

15. Large Data Set 8 records the result of a survey of 300 randomly selected adults who go to movie theaters regularly. For each person the gender and preferred type of movie were recorded. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that the factors "gender" and "preferred type of movie" are dependent.

    <http://www.flatworldknowledge.com/sites/all/files/data8.xls>

`````````````{admonition} Answers
:class: dropdown

1.  1.  15.09,
    2.  24.72,
    3.  44.31
2. &nbsp;
3.  1.  10.64,
    2.  18.55,
    3.  40.26
4. &nbsp;
5.  1.  14.07,
    2.  16.01
6. &nbsp;
7.  1.  $C_{1} = 35$, $C_{2} = 15$, $R_{1} = 30$, $R_{2} = 20$, *n* = 50,
    2.  $E_{11} = 21$, $E_{12} = 9$, $E_{21} = 14$, $E_{22} = 6$,
    3.  $\chi^{2} = 0.3968$,
    4.  $df = 1$
8. &nbsp;

<!-- -->

9.  $\chi^{2} = 0.6698$, $\chi_{0.05}^{2} = 5.99$, do not reject *H*<sub>0</sub>

10. &nbsp;

11. $\chi^{2} = 72.35$, $\chi_{0.01}^{2} = 9.21$, reject *H*<sub>0</sub>

12. &nbsp;

13. $\chi^{2} = 21.2784$, $\chi_{0.01}^{2} = 9.21$, reject *H*<sub>0</sub>

14. &nbsp;

<!-- -->

15. $\chi^{2} = 28.4539.$ $df = 3.$ Rejection Region: $\left\lbrack {7.815,\infty} \right).$ Decision: Reject *H*<sub>0</sub> of independence.

`````````````

## 11.2 Chi-Square One-Sample Goodness-of-Fit Tests

````````````{note} Learning Objective

1.  To understand how to use a chi-square test to judge whether a sample fits a particular population well.

````````````

Suppose we wish to determine if an ordinary-looking six-sided die is fair, or balanced, meaning that every face has probability 1/6 of landing on top when the die is tossed. We could toss the die dozens, maybe hundreds, of times and compare the actual number of times each face landed on top to the expected number, which would be 1/6 of the total number of tosses. We wouldn't expect each number to be exactly 1/6 of the total, but it should be close. To be specific, suppose the die is tossed *n* = 60 times with the results summarized in [Table 11.8 \"Die Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t01). For ease of reference we add a column of expected frequencies, which in this simple example is simply a column of 10s. The result is shown as [Table 11.9 \"Updated Die Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t02). In analogy with the previous section we call this an "updated" table. A measure of how much the data deviate from what we would expect to see if the die really were fair is the sum of the squares of the differences between the observed frequency *O* and the expected frequency *E* in each row, or, standardizing by dividing each square by the expected number, the sum $\left. \Sigma\left( {O - E} \right)^{2}/ E. \right.$ If we formulate the investigation as a test of hypotheses, the test is

$$\begin{array}{rcl}
H_{0} & : & \text{The die is fair} \\
{\text{\quad vs.}\, H_{a}} & : & {\text{The die is }not\text{ fair}}
\end{array}$$

(src-fwk-shafer-ch11-s02-t01)=

Table 11.8 Die Contingency Table

````````{list-table}
:header-rows: 1

- - Die Value
  - Assumed Distribution
  - Observed Frequency
- - 1
  - 1/6
  - 9
- - 2
  - 1/6
  - 15
- - 3
  - 1/6
  - 9
- - 4
  - 1/6
  - 8
- - 5
  - 1/6
  - 6
- - 6
  - 1/6
  - 13

````````

(src-fwk-shafer-ch11-s02-t02)=

Table 11.9 Updated Die Contingency Table

````````{list-table}
:header-rows: 1

- - Die Value
  - Assumed Distribution
  - Observed Freq.
  - Expected Freq.
- - 1
  - 1/6
  - 9
  - 10
- - 2
  - 1/6
  - 15
  - 10
- - 3
  - 1/6
  - 9
  - 10
- - 4
  - 1/6
  - 8
  - 10
- - 5
  - 1/6
  - 6
  - 10
- - 6
  - 1/6
  - 13
  - 10

````````

We would reject the null hypothesis that the die is fair only if the number $\left. \Sigma\left( {O - E} \right)^{2}/ E \right.$ is large, so the test is right-tailed. In this example the random variable $\left. \Sigma\left( {O - E} \right)^{2}/ E \right.$ has the chi-square distribution with five degrees of freedom. If we had decided at the outset to test at the 10% level of significance, the critical value defining the rejection region would be, reading from [Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04), $\chi_{\alpha}^{2} = \chi_{0.10}^{2} = 9.236$, so that the rejection region would be the interval $\left\lbrack {9.236,\infty} \right).$ When we compute the value of the standardized test statistic using the numbers in the last two columns of [Table 11.9 \"Updated Die Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t02), we obtain

$$\begin{array}{l}
{\Sigma\frac{\left( {O - E} \right)^{2}}{E}} \\
{= \frac{\left( {\text{-}1} \right)^{2}}{10} + \frac{5^{2}}{10} + \frac{\left( {\text{-}1} \right)^{2}}{10} + \frac{\left( {\text{-}2} \right)^{2}}{10} + \frac{\left( {\text{-}4} \right)^{2}}{10} + \frac{3^{2}}{10}} \\
{= 0.1 + 2.5 + 0.1 + 0.4 + 1.6 + 0.9} \\
{= 5.6}
\end{array}$$

Since 5.6 \< 9.236 the decision is not to reject *H*<sub>0</sub>. See [Figure 11.5 \"Balanced Die\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-f01). The data do not provide sufficient evidence, at the 10% level of significance, to conclude that the die is loaded.

``````{figure} /images/redrawn/fig-11-05.svg
:alt: Chi-square density with 5 degrees of freedom. The right tail of area α = 0.10 beyond the critical value χ²_α = 9.236 is shaded. On the number line below, the rejection region χ² ≥ 9.236 is red, and the test statistic χ² = 5.6, marked with a star, lies outside it.
:name: src-fwk-shafer-ch11-s02-f01

Figure 11.5 Balanced Die
``````

In the general situation we consider a discrete random variable that can take *I* different values, $x_{1},x_{2},\ldots,x_{I}$, for which the default assumption is that the probability distribution is

$$\begin{matrix}
x & x_{1} & x_{2} & \ldots & x_{I} \\
{P(x)} & p_{1} & p_{2} & \ldots & p_{I}
\end{matrix}$$

We wish to test the hypotheses

$$\begin{array}{rcl}
H_{0} & : & {\text{The assumed probability distribution for }X\text{ is valid}} \\
{\text{\quad vs.}\, H_{a}} & : & {\text{The assumed probability distribution for }X\text{ is }not\text{ valid}}
\end{array}$$

We take a sample of size *n* and obtain a list of observed frequencies. This is shown in [Table 11.10 \"General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t03). Based on the assumed probability distribution we also have a list of assumed frequencies, each of which is defined and computed by the formula

$$E_{i} = n \times p_{i}$$

(src-fwk-shafer-ch11-s02-t03)=

Table 11.10 General Contingency Table

````````{list-table}
:header-rows: 1

- - Factor Levels
  - Assumed Distribution
  - Observed Frequency
- - 1
  - *p*<sub>1</sub>
  - *O*<sub>1</sub>
- - 2
  - *p*<sub>2</sub>
  - *O*<sub>2</sub>
- - ⋮
  - ⋮
  - ⋮
- - *I*
  - *p<sub>I</sub>*
  - *O<sub>I</sub>*

````````

[Table 11.10 \"General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t03) is updated to [Table 11.11 \"Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t04) by adding the expected frequency for each value of *X*. To simplify the notation we drop indices for the observed and expected frequencies and represent [Table 11.11 \"Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t04) by [Table 11.12 \"Simplified Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t05).

(src-fwk-shafer-ch11-s02-t04)=

Table 11.11 Updated General Contingency Table

````````{list-table}
:header-rows: 1

- - Factor Levels
  - Assumed Distribution
  - Observed Freq.
  - Expected Freq.
- - 1
  - *p*<sub>1</sub>
  - *O*<sub>1</sub>
  - *E*<sub>1</sub>
- - 2
  - *p*<sub>2</sub>
  - *O*<sub>2</sub>
  - *E*<sub>2</sub>
- - ⋮
  - ⋮
  - ⋮
  - ⋮
- - *I*
  - *p<sub>I</sub>*
  - *O<sub>I</sub>*
  - *E<sub>I</sub>*

````````

(src-fwk-shafer-ch11-s02-t05)=

Table 11.12 Simplified Updated General Contingency Table

````````{list-table}
:header-rows: 1

- - Factor Levels
  - Assumed Distribution
  - Observed Freq.
  - Expected Freq.
- - 1
  - *p*<sub>1</sub>
  - *O*
  - *E*
- - 2
  - *p*<sub>2</sub>
  - *O*
  - *E*
- - ⋮
  - ⋮
  - ⋮
  - ⋮
- - *I*
  - *p<sub>I</sub>*
  - *O*
  - *E*

````````

Here is the test statistic for the general hypothesis based on [Table 11.12 \"Simplified Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t05), together with the conditions that it follow a chi-square distribution.

````````````{important} Test Statistic for Testing Goodness of Fit to a Discrete Probability Distribution

$$\chi^{2} = \Sigma\frac{\left( {O - E} \right)^{2}}{E}$$

where the sum is over all the rows of the table (one for each value of *X*).

If

1.  the true probability distribution of *X* is as assumed, and
2.  the observed count *O* of each cell in [Table 11.12 \"Simplified Updated General Contingency Table\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t05) is at least 5,

then $\chi^{2}$ approximately follows a chi-square distribution with $df = I\text{-}1$ degrees of freedom.

````````````

The test is known as a *goodness-of-fit* $\chi^{2}$ test since it tests the null hypothesis that the sample fits the assumed probability distribution well. It is always right-tailed, since deviation from the assumed probability distribution corresponds to large values of $\chi^{2}.$

Testing is done using either of the usual five-step procedures.

(src-fwk-shafer-ch11-s02-n04)=

### Example 2

[Table 11.13 \"Ethnic Groups in the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t06) shows the distribution of various ethnic groups in the population of a particular state based on a decennial U.S. census. Five years later a random sample of 2,500 residents of the state was taken, with the results given in [Table 11.14 \"Sample Data Five Years After the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t07) (along with the probability distribution from the census year). Test, at the 1% level of significance, whether there is sufficient evidence in the sample to conclude that the distribution of ethnic groups in this state five years after the census had changed from that in the census year.

(src-fwk-shafer-ch11-s02-t06)=

Table 11.13 Ethnic Groups in the Census Year

````````{list-table}
:header-rows: 1

- - Ethnicity
  - White
  - Black
  - Amer.-Indian
  - Hispanic
  - Asian
  - Others
- - Proportion
  - 0.743
  - 0.216
  - 0.012
  - 0.012
  - 0.008
  - 0.009

````````

(src-fwk-shafer-ch11-s02-t07)=

Table 11.14 Sample Data Five Years After the Census Year

````````{list-table}
:header-rows: 1

- - Ethnicity
  - Assumed Distribution
  - Observed Frequency
- - White
  - 0.743
  - 1732
- - Black
  - 0.216
  - 538
- - American-Indian
  - 0.012
  - 32
- - Hispanic
  - 0.012
  - 42
- - Asian
  - 0.008
  - 133
- - Others
  - 0.009
  - 23

````````

Solution:

We test using the critical value approach.

- Step 1. The hypotheses of interest in this case can be expressed as

  $$\begin{array}{rcl}
  H_{0} & : & \text{The distribution of ethnic groups has not changed} \\
  {\text{\quad vs.}\, H_{a}} & : & {\text{The distribution of ethnic groups }has\text{ changed}}
  \end{array}$$

- Step 2. The distribution is chi-square.

- Step 3. To compute the value of the test statistic we must first compute the expected number for each row of [Table 11.14 \"Sample Data Five Years After the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t07). Since *n* = 2500, using the formula $E_{i} = n \times p_{i}$ and the values of *p<sub>i</sub>* from either [Table 11.13 \"Ethnic Groups in the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t06) or [Table 11.14 \"Sample Data Five Years After the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t07),

  $$\begin{array}{rcl}
  E_{1} & = & {2500 \times 0.743 = 1857.5} \\
  E_{2} & = & {2500 \times 0.216 = 540} \\
  E_{3} & = & {2500 \times 0.012 = 30} \\
  E_{4} & = & {2500 \times 0.012 = 30} \\
  E_{5} & = & {2500 \times 0.008 = 20} \\
  E_{6} & = & {2500 \times 0.009 = 22.5}
  \end{array}$$

  [Table 11.14 \"Sample Data Five Years After the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t07) is updated to [Table 11.15 \"Observed and Expected Frequencies Five Years After the Census Year\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-t08).

  (src-fwk-shafer-ch11-s02-t08)=

  Table 11.15 Observed and Expected Frequencies Five Years After the Census Year

  ````````{list-table}
  :header-rows: 1

  - - Ethnicity
    - Assumed Dist.
    - Observed Freq.
    - Expected Freq.
  - - White
    - 0.743
    - 1732
    - 1857.5
  - - Black
    - 0.216
    - 538
    - 540
  - - American-Indian
    - 0.012
    - 32
    - 30
  - - Hispanic
    - 0.012
    - 42
    - 30
  - - Asian
    - 0.008
    - 133
    - 20
  - - Others
    - 0.009
    - 23
    - 22.5

  ````````

  The value of the test statistic is

  $$\begin{array}{rcc}
  \chi^{2} & = & {\Sigma\frac{\left( {O - E} \right)^{2}}{E}} \\
   & = & {\frac{\left( {1732 - 1857.5} \right)^{2}}{1857.5} + \frac{\left( {538 - 540} \right)^{2}}{540} + \frac{\left( {32 - 30} \right)^{2}}{30} + \frac{\left( {42 - 30} \right)^{2}}{30}} \\
   & & {+ \frac{\left( {133 - 20} \right)^{2}}{20} + \frac{\left( {23 - 22.5} \right)^{2}}{22.5}} \\
   & = & 651.881
  \end{array}$$

- Since the random variable takes six values, *I* = 6. Thus the test statistic follows the chi-square distribution with $df = 6 - 1 = 5$ degrees of freedom.

  Since the test is right-tailed, the critical value is $\chi_{0.01}^{2}.$ Reading from [Figure 12.4 \"Critical Values of Chi-Square Distributions\"](/appendices/appendix.md#src-fwk-shafer-ch12-f04), $\chi_{0.01}^{2} = 15.086$, so the rejection region is $\left\lbrack {15.086,\infty} \right).$

- Since 651.881 \> 15.086 the decision is to reject the null hypothesis. See [Figure 11.6](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-f02). The data provide sufficient evidence, at the 1% level of significance, to conclude that the ethnic distribution in this state has changed in the five years since the U.S. census.

``````{figure} /images/redrawn/fig-11-06.svg
:alt: Chi-square density with 5 degrees of freedom. The thin right tail of area α = 0.01 beyond the critical value χ²_α = 15.086 is shaded. On the number line below, the rejection region χ² ≥ 15.086 is red, and the test statistic χ² = 651.881, marked with a star near the right end, lies far inside it.
:name: src-fwk-shafer-ch11-s02-f02

Figure 11.6 [Note 11.15 \"Example 2\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s02-n04){.xref xrefstyle="select: title"}
``````

````````````{important} Key Takeaway

- The chi-square goodness-of-fit test[^stats-6] can be used to evaluate the hypothesis that a sample is taken from a population with an assumed specific probability distribution.

````````````

### Exercises

### Basic

1.  A data sample is sorted into five categories with an assumed probability distribution.

    ````````{list-table}
    :header-rows: 1

    - - Factor Levels
      - Assumed Distribution
      - Observed Frequency
    - - 1
      - $p_{1} = 0.1$
      - 10
    - - 2
      - $p_{2} = 0.4$
      - 35
    - - 3
      - $p_{3} = 0.4$
      - 45
    - - 4
      - $p_{4} = 0.1$
      - 10

    ````````

    1.  Find the size *n* of the sample.
    2.  Find the expected number *E* of observations for each level, if the sampled population has a probability distribution as assumed (that is, just use the formula $E_{i} = n \times p_{i}$).
    3.  Find the chi-square test statistic $\chi^{2}.$
    4.  Find the number of degrees of freedom of the chi-square test statistic.

2.  A data sample is sorted into five categories with an assumed probability distribution.

    ````````{list-table}
    :header-rows: 1

    - - Factor Levels
      - Assumed Distribution
      - Observed Frequency
    - - 1
      - $p_{1} = 0.3$
      - 23
    - - 2
      - $p_{2} = 0.3$
      - 30
    - - 3
      - $p_{3} = 0.2$
      - 19
    - - 4
      - $p_{4} = 0.1$
      - 8
    - - 5
      - $p_{5} = 0.1$
      - 10

    ````````

    1.  Find the size *n* of the sample.
    2.  Find the expected number *E* of observations for each level, if the sampled population has a probability distribution as assumed (that is, just use the formula $E_{i} = n \times p_{i}$).
    3.  Find the chi-square test statistic $\chi^{2}.$
    4.  Find the number of degrees of freedom of the chi-square test statistic.

### Applications

3.  Retailers of collectible postage stamps often buy their stamps in large quantities by weight at auctions. The prices the retailers are willing to pay depend on how old the postage stamps are. Many collectible postage stamps at auctions are described by the proportions of stamps issued at various periods in the past. Generally the older the stamps the higher the value. At one particular auction, a lot of collectible stamps is advertised to have the age distribution given in the table provided. A retail buyer took a sample of 73 stamps from the lot and sorted them by age. The results are given in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that the age distribution of the lot is different from what was claimed by the seller.

    ````````{list-table}
    :header-rows: 1

    - - Year
      - Claimed Distribution
      - Observed Frequency
    - - Before 1940
      - 0.10
      - 6
    - - 1940 to 1959
      - 0.25
      - 15
    - - 1960 to 1979
      - 0.45
      - 30
    - - After 1979
      - 0.20
      - 22

    ````````

4.  The litter size of Bengal tigers is typically two or three cubs, but it can vary between one and four. Based on long-term observations, the litter size of Bengal tigers in the wild has the distribution given in the table provided. A zoologist believes that Bengal tigers in captivity tend to have different (possibly smaller) litter sizes from those in the wild. To verify this belief, the zoologist searched all data sources and found 316 litter size records of Bengal tigers in captivity. The results are given in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that the distribution of litter sizes in captivity differs from that in the wild.

    ````````{list-table}
    :header-rows: 1

    - - Litter Size
      - Wild Litter Distribution
      - Observed Frequency
    - - 1
      - 0.11
      - 41
    - - 2
      - 0.69
      - 243
    - - 3
      - 0.18
      - 27
    - - 4
      - 0.02
      - 5

    ````````

5.  An online shoe retailer sells men's shoes in sizes 8 to 13. In the past orders for the different shoe sizes have followed the distribution given in the table provided. The management believes that recent marketing efforts may have expanded their customer base and, as a result, there may be a shift in the size distribution for future orders. To have a better understanding of its future sales, the shoe seller examined 1,040 sales records of recent orders and noted the sizes of the shoes ordered. The results are given in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to conclude that the shoe size distribution of future sales will differ from the historic one.

    ````````{list-table}
    :header-rows: 1

    - - Shoe Size
      - Past Size Distribution
      - Recent Size Frequency
    - - 8.0
      - 0.03
      - 25
    - - 8.5
      - 0.06
      - 43
    - - 9.0
      - 0.09
      - 88
    - - 9.5
      - 0.19
      - 221
    - - 10.0
      - 0.23
      - 272
    - - 10.5
      - 0.14
      - 150
    - - 11.0
      - 0.10
      - 107
    - - 11.5
      - 0.06
      - 51
    - - 12.0
      - 0.05
      - 37
    - - 12.5
      - 0.03
      - 35
    - - 13.0
      - 0.02
      - 11

    ````````

6.  An online shoe retailer sells women's shoes in sizes 5 to 10. In the past orders for the different shoe sizes have followed the distribution given in the table provided. The management believes that recent marketing efforts may have expanded their customer base and, as a result, there may be a shift in the size distribution for future orders. To have a better understanding of its future sales, the shoe seller examined 1,174 sales records of recent orders and noted the sizes of the shoes ordered. The results are given in the table provided. Test, at the 1% level of significance, whether there is sufficient evidence in the data to conclude that the shoe size distribution of future sales will differ from the historic one.

    ````````{list-table}
    :header-rows: 1

    - - Shoe Size
      - Past Size Distribution
      - Recent Size Frequency
    - - 5.0
      - 0.02
      - 20
    - - 5.5
      - 0.03
      - 23
    - - 6.0
      - 0.07
      - 88
    - - 6.5
      - 0.08
      - 90
    - - 7.0
      - 0.20
      - 222
    - - 7.5
      - 0.20
      - 258
    - - 8.0
      - 0.15
      - 177
    - - 8.5
      - 0.11
      - 121
    - - 9.0
      - 0.08
      - 91
    - - 9.5
      - 0.04
      - 53
    - - 10.0
      - 0.02
      - 31

    ````````

7.  A chess opening is a sequence of moves at the beginning of a chess game. There are many well-studied named openings in chess literature. French Defense is one of the most popular openings for black, although it is considered a relatively weak opening since it gives black probability 0.344 of winning, probability 0.405 of losing, and probability 0.251 of drawing. A chess master believes that he has discovered a new variation of French Defense that may alter the probability distribution of the outcome of the game. In his many Internet chess games in the last two years, he was able to apply the new variation in 77 games. The wins, losses, and draws in the 77 games are given in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that the newly discovered variation of French Defense alters the probability distribution of the result of the game.

    ````````{list-table}
    :header-rows: 1

    - - Result for Black
      - Probability Distribution
      - New Variation Wins
    - - Win
      - 0.344
      - 31
    - - Loss
      - 0.405
      - 25
    - - Draw
      - 0.251
      - 21

    ````````

8.  The Department of Parks and Wildlife stocks a large lake with fish every six years. It is determined that a healthy diversity of fish in the lake should consist of 10% largemouth bass, 15% smallmouth bass, 10% striped bass, 10% trout, and 20% catfish. Therefore each time the lake is stocked, the fish population in the lake is restored to maintain that particular distribution. Every three years, the department conducts a study to see whether the distribution of the fish in the lake has shifted away from the target proportions. In one particular year, a research group from the department observed a sample of 292 fish from the lake with the results given in the table provided. Test, at the 5% level of significance, whether there is sufficient evidence in the data to conclude that the fish population distribution has shifted since the last stocking.

    ````````{list-table}
    :header-rows: 1

    - - Fish
      - Target Distribution
      - Fish in Sample
    - - Largemouth Bass
      - 0.10
      - 14
    - - Smallmouth Bass
      - 0.15
      - 49
    - - Striped Bass
      - 0.10
      - 21
    - - Trout
      - 0.10
      - 22
    - - Catfish
      - 0.20
      - 75
    - - Other
      - 0.35
      - 111

    ````````

### Large Data Set Exercise

9.  Large Data Set 4 records the result of 500 tosses of six-sided die. Test, at the 10% level of significance, whether there is sufficient evidence in the data to conclude that the die is not "fair" (or "balanced"), that is, that the probability distribution differs from probability 1/6 for each of the six faces on the die.

    <http://www.flatworldknowledge.com/sites/all/files/data4.xls>

`````````````{admonition} Answers
:class: dropdown

1.  1.  *n* = 100,
    2.  *E* = 10, *E* = 40, *E* = 40, *E* = 10;
    3.  $\chi^{2} = 1.25$,
    4.  $df = 3$
2. &nbsp;

<!-- -->

3.  $\chi^{2} = 4.8082$, $\chi_{0.05}^{2} = 7.81$, do not reject *H*<sub>0</sub>

4. &nbsp;

5.  $\chi^{2} = 26.5765$, $\chi_{0.01}^{2} = 23.21$, reject *H*<sub>0</sub>

6. &nbsp;

7.  $\chi^{2} = 2.1401$, $\chi_{0.05}^{2} = 5.99$, do not reject *H*<sub>0</sub>

8. &nbsp;

<!-- -->

9.  $\chi^{2} = 2.944.$ $df = 5.$ Rejection Region: $\left\lbrack {9.236,\infty} \right).$ Decision: Fail to reject *H*<sub>0</sub> of balance.

`````````````

## 11.3 *F*-tests for Equality of Two Variances

````````````{note} Learning Objectives

1.  To understand what *F*-distributions are.
2.  To understand how to use an *F*-test to judge whether two population variances are equal.

````````````

### *F*-Distributions

Another important and useful family of distributions in statistics is the family of *F*-distributions. Each member of the *F*-distribution family is specified by a pair of parameters called *degrees of freedom* and denoted $df_{1}$ and $df_{2}.$ [Figure 11.7 \"Many F Distributions\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s01-f01) shows several *F*-distributions for different pairs of degrees of freedom. An $\mathbf{F}$ random variable[^stats-7] is a random variable that assumes only positive values and follows an *F*-distribution.

``````{figure} /images/redrawn/fig-11-07.svg
:alt: F density curves for degrees of freedom (1, 1), (10, 20), and (5, 4) on a horizontal axis from 0 to 5. The (1, 1) curve is highest at 0 and decreases slowly; the (10, 20) curve has a tall peak near 1; the (5, 4) curve peaks lower, closer to 0, and has a heavier right tail.
:name: src-fwk-shafer-ch11-s03-s01-f01

Figure 11.7 Many *F*-Distributions
``````

The parameter $df_{1}$ is often referred to as the *numerator* degrees of freedom and the parameter $df_{2}$ as the *denominator* degrees of freedom. It is important to keep in mind that they are not interchangeable. For example, the *F*-distribution with degrees of freedom $df_{1} = 3$ and $df_{2} = 8$ is a different distribution from the *F*-distribution with degrees of freedom $df_{1} = 8$ and $df_{2} = 3.$

````````````{important} Definition

*The value of the* *F* *random variable* *F* *with degrees of freedom* $df_{1}$ *and* $df_{2}$ *that cuts off a right tail of area* *c* *is denoted* *F<sub>c</sub>* *and is called a* **critical value**. *See [Figure 11.8](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s01-f02).*

``````{figure} /images/redrawn/fig-11-08.svg
:alt: A right-skewed F density. The right tail beyond the point F_c is shaded and labeled c; the area to its left is labeled 1 − c.
:name: src-fwk-shafer-ch11-s03-s01-f02

Figure 11.8 *F<sub>c</sub>* Illustrated
``````

````````````

Tables containing the values of *F<sub>c</sub>* are given in [Chapter 11 \"Chi-Square Tests and F-Tests\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11). Each of the tables is for a fixed collection of values of *c*, either 0.900, 0.950, 0.975, 0.990, and 0.995 (yielding what are called "lower" critical values), or 0.005, 0.010, 0.025, 0.050, and 0.100 (yielding what are called "upper" critical values). In each table critical values are given for various pairs $\left( {df_{1},df_{2}} \right).$ We illustrate the use of the tables with several examples.

### Example 3

Suppose *F* is an *F* random variable with degrees of freedom $df_{1} = 5$ and $df_{2} = 4.$ Use the tables to find

1.  *F*<sub>0.10</sub>
2.  *F*<sub>0.95</sub>

Solution:

1.  The column headings of all the tables contain $df_{1} = 5.$ Look for the table for which 0.10 is one of the entries on the extreme left (a table of upper critical values) and that has a row heading $df_{2} = 4$ in the left margin of the table. A portion of the relevant table is provided. The entry in the intersection of the column with heading $df_{1} = 5$ and the row with the headings 0.10 and $df_{2} = 4$, which is shaded in the table provided, is the answer, $F_{0.10} = 4.05.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.005
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 22.5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.01
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 15.5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.025
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 9.36
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.05
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 6.26
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.10
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $4.05$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

2.  Look for the table for which 0.95 is one of the entries on the extreme left (a table of lower critical values) and that has a row heading $df_{2} = 4$ in the left margin of the table. A portion of the relevant table is provided. The entry in the intersection of the column with heading $df_{1} = 5$ and the row with the headings 0.95 and $df_{2} = 4$, which is shaded in the table provided, is the answer, $F_{0.95} = 0.19.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.90
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.28
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.95
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $0.19$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.975
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.14
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.99
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.09
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.995
      - 4
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.06
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

### Example 4

Suppose $\mathbf{F}$ is an *F* random variable with degrees of freedom $df_{1} = 2$ and $df_{2} = 20.$ Let $\alpha = 0.05.$ Use the tables to find

1.  $F_{\alpha}$
2.  $F_{\alpha / 2}$
3.  $F_{1 - \alpha}$
4.  $F_{1 - \alpha / 2}$

Solution:

1.  The column headings of all the tables contain $df_{1} = 2.$ Look for the table for which $\alpha = 0.05$ is one of the entries on the extreme left (a table of upper critical values) and that has a row heading $df_{2} = 20$ in the left margin of the table. A portion of the relevant table is provided. The shaded entry, in the intersection of the column with heading $df_{1} = 2$ and the row with the headings 0.05 and $df_{2} = 20$ is the answer, $F_{0.05} = 3.49.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.005
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 6.99
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.01
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5.85
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.025
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 4.46
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.05
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $3.49$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.10
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 2.59
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

2.  Look for the table for which $\left. \alpha/ 2 = 0.025 \right.$ is one of the entries on the extreme left (a table of upper critical values) and that has a row heading $df_{2} = 20$ in the left margin of the table. A portion of the relevant table is provided. The shaded entry, in the intersection of the column with heading $df_{1} = 2$ and the row with the headings 0.025 and $df_{2} = 20$ is the answer, $F_{0.025} = 4.46.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.005
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 6.99
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.01
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 5.85
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.025
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $4.46$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.05
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 3.49
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.10
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 2.59
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

3.  Look for the table for which $1 - \alpha = 0.95$ is one of the entries on the extreme left (a table of lower critical values) and that has a row heading $df_{2} = 20$ in the left margin of the table. A portion of the relevant table is provided. The shaded entry, in the intersection of the column with heading $df_{1} = 2$ and the row with the headings 0.95 and $df_{2} = 20$ is the answer, $F_{0.95} = 0.05.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.90
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.11
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.95
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $0.05$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.975
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.03
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.99
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.01
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.995
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.01
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

4.  Look for the table for which $\left. 1 - \alpha/ 2 = 0.975 \right.$ is one of the entries on the extreme left (a table of lower critical values) and that has a row heading $df_{2} = 20$ in the left margin of the table. A portion of the relevant table is provided. The shaded entry, in the intersection of the column with heading $df_{1} = 2$ and the row with the headings 0.975 and $df_{2} = 20$ is the answer, $F_{0.975} = 0.03.$

    ````````{list-table}
    :header-rows: 2

    - - *F* Tail Area
      - $df_{1}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - *F* Tail Area
      - $df_{2}$
      - 1
      - 2
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮
    - - 0.90
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.11
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.95
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.05
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.975
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - $0.03$
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.99
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.01
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - 0.995
      - 20
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
      - 0.01
      - $\text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ }$
    - - ⋮
      - ⋮
      - ⋮
      - ⋮
      - ⋮

    ````````

A fact that sometimes allows us to find a critical value from a table that we could not read otherwise is:

If $F_{u}\left( {r,s} \right)$ denotes the value of the *F*-distribution with degrees of freedom $df_{1} = r$ and $df_{2} = s$ that cuts off a right tail of area *u*, then

$$F_{c}\left( {k,\ell} \right) = \frac{1}{F_{1 - c}\left( {\ell,k} \right)}$$

### Example 5

Use the tables to find

1.  *F*<sub>0.01</sub> for an *F* random variable with $df_{1} = 13$ and $df_{2} = 8$
2.  *F*<sub>0.975</sub> for an *F* random variable with $df_{1} = 40$ and $df_{2} = 10$

Solution:

1.  There is no table with $df_{1} = 13$, but there is one with $df_{1} = 8.$ Thus we use the fact that

    $$F_{0.01}(13,8) = \frac{1}{F_{0.99}(8,13)}$$

    Using the relevant table we find that $F_{0.99}(8,13) = 0.18$, hence $F_{0.01}(13,8) = 0.18^{\text{-}1} = 5.556.$

2.  There is no table with $df_{1} = 40$, but there is one with $df_{1} = 10.$ Thus we use the fact that

    $$F_{0.975}(40,10) = \frac{1}{F_{0.025}(10,40)}$$

    Using the relevant table we find that $F_{0.025}(10,40) = 3.31$, hence $F_{0.975}(40,10) = 3.31^{\text{-}1} = 0.302.$

### *F*-Tests for Equality of Two Variances

[^stats-8]In [Chapter 9 \"Two-Sample Problems\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09) we saw how to test hypotheses about the difference between two population means $\mathit{\mu}_{1}$ and $\mathit{\mu}_{2}.$ In some practical situations the difference between the population standard deviations $\mathit{\sigma}_{1}$ and $\mathit{\sigma}_{2}$ is also of interest. Standard deviation measures the variability of a random variable. For example, if the random variable measures the size of a machined part in a manufacturing process, the size of standard deviation is one indicator of product quality. A smaller standard deviation among items produced in the manufacturing process is desirable since it indicates consistency in product quality.

For theoretical reasons it is easier to compare the squares of the population standard deviations, the population variances $\mathit{\sigma}_{1}^{2}$ and $\mathit{\sigma}_{2}^{2}.$ This is not a problem, since $\mathit{\sigma}_{1} = \mathit{\sigma}_{2}$ precisely when $\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$, $\mathit{\sigma}_{1} < \mathit{\sigma}_{2}$ precisely when $\mathit{\sigma}_{1}^{2} < \mathit{\sigma}_{2}^{2}$, and $\mathit{\sigma}_{1} > \mathit{\sigma}_{2}$ precisely when $\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}.$

The null hypothesis always has the form $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}.$ The three forms of the alternative hypothesis, with the terminology for each case, are:

````````{list-table}
:header-rows: 1

- - Form of *H<sub>a</sub>*
  - Terminology
- - $H_{a}:\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}$
  - Right-tailed
- - $H_{a}:\mathit{\sigma}_{1}^{2} < \mathit{\sigma}_{2}^{2}$
  - Left-tailed
- - $H_{a}:\mathit{\sigma}_{1}^{2} \neq \mathit{\sigma}_{2}^{2}$
  - Two-tailed

````````

Just as when we test hypotheses concerning two population means, we take a random sample from each population, of sizes *n*<sub>1</sub> and *n*<sub>2</sub>, and compute the sample standard deviations *s*<sub>1</sub> and *s*<sub>2</sub>. In this context the samples are always independent. The populations themselves must be normally distributed.

````````````{important} Test Statistic for Hypothesis Tests Concerning the Difference Between Two Population Variances

$$F = \frac{s_{1}^{2}}{s_{2}^{2}}$$

If the two populations are normally distributed and if $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ is true then under independent sampling *F* approximately follows an *F*-distribution with degrees of freedom $df_{1} = n_{1}\text{-}1$ and $df_{2} = n_{2}\text{-}1.$

````````````

A test based on the test statistic $\mathbf{F}$ is called an *F*-test.

A most important point is that while the rejection region for a right-tailed test is exactly as in every other situation that we have encountered, because of the asymmetry in the *F*-distribution the critical value for a left-tailed test and the lower critical value for a two-tailed test have the special forms shown in the following table:

````````{list-table}
:header-rows: 1

- - Terminology
  - Alternative Hypothesis
  - Rejection Region
- - Right-tailed
  - $H_{a}:\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}$
  - $\mathbf{F} \geq F_{\alpha}$
- - Left-tailed
  - $H_{a}:\mathit{\sigma}_{1}^{2} < \mathit{\sigma}_{2}^{2}$
  - $\mathbf{F} \leq F_{1 - \alpha}$
- - Two-tailed
  - $H_{a}:\mathit{\sigma}_{1}^{2} \neq \mathit{\sigma}_{2}^{2}$
  - $\mathbf{F} \leq F_{1 - \alpha / 2}$ or $\mathbf{F} \geq F_{\alpha / 2}$

````````

[Figure 11.9 \"Rejection Regions: (a) Right-Tailed; (b) Left-Tailed; (c) Two-Tailed\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-f01) illustrates these rejection regions.

``````{figure} /images/redrawn/fig-11-09.svg
:alt: Three F density curves. (a) For Hₐ: σ₁² > σ₂², the right tail of area α above F_α is shaded, and the rejection region is F ≥ F_α. (b) For Hₐ: σ₁² < σ₂², the left tail of area α below F₁₋α is shaded, and the rejection region runs from 0 to F₁₋α. (c) For Hₐ: σ₁² ≠ σ₂², both tails, each of area α/2, are shaded, below F₁₋α/2 and above F_α/2, and the rejection region is both intervals.
:name: src-fwk-shafer-ch11-s03-s02-f01

Figure 11.9 Rejection Regions: (a) Right-Tailed; (b) Left-Tailed; (c) Two-Tailed
``````

The test is performed using the usual five-step procedure described at the end of [Section 8.1 \"The Elements of Hypothesis Testing\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08-s01) in [Chapter 8 \"Testing Hypotheses\"](/chapters/ch-08-testing-hypotheses.md#src-fwk-shafer-ch08).

(src-fwk-shafer-ch11-s03-s02-n02)=

### Example 6

One of the quality measures of blood glucose meter strips is the consistency of the test results on the same sample of blood. The consistency is measured by the variance of the readings in repeated testing. Suppose two types of strips, *A* and *B*, are compared for their respective consistencies. We arbitrarily label the population of Type *A* strips Population 1 and the population of Type *B* strips Population 2. Suppose 15 Type *A* strips were tested with blood drops from a well-shaken vial and 20 Type *B* strips were tested with the blood from the same vial. The results are summarized in [Table 11.16 \"Two Types of Test Strips\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-t01). Assume the glucose readings using Type *A* strips follow a normal distribution with variance $\mathit{\sigma}_{1}^{2}$ and those using Type *B* strips follow a normal distribution with variance $\mathit{\sigma}_{2}^{2}.$ Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that the consistencies of the two types of strips are different.

(src-fwk-shafer-ch11-s03-s02-t01)=

Table 11.16 Two Types of Test Strips

````````{list-table}
:header-rows: 1

- - Strip Type
  - Sample Size
  - Sample Variance
- - *A*
  - $n_{1} = 16$
  - $s_{1}^{2} = 2.09$
- - *B*
  - $n_{2} = 21$
  - $s_{2}^{2} = 1.10$

````````

Solution:

- Step 1. The test of hypotheses is

  $$\begin{array}{rll}
  H_{0} & : & {\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}} \\
  {\text{\quad vs.}\, H_{a}} & : & {\mathit{\sigma}_{1}^{2} \neq \mathit{\sigma}_{2}^{2}\,\,\quad @\,\alpha = 0.10}
  \end{array}$$

- Step 2. The distribution is the *F*-distribution with degrees of freedom $df_{1} = 16 - 1 = 15$ and $df_{2} = 21 - 1 = 20.$

- Step 3. The test is two-tailed. The left or lower critical value is $F_{1 - \alpha / 2} = F_{0.95} = 0.43.$ The right or upper critical value is $F_{\alpha / 2} = F_{0.05} = 2.20.$ Thus the rejection region is $\left\lbrack {0,\text{-}0.43} \right\rbrack \cup \left\lbrack {2.20,\infty} \right)$, as illustrated in [Figure 11.10 \"Rejection Region and Test Statistic for \"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-f02).

``````{figure} /images/redrawn/fig-11-10.svg
:alt: F density with 15 and 20 degrees of freedom. Both tails, each of area α/2 = 0.05, are shaded: below F₁₋α/2 = 0.43 and above F_α/2 = 2.20. On the number line below, the rejection intervals from 0 to 0.43 and from 2.20 on are red, and the test statistic F = 1.90, marked with a star, lies between them.
:name: src-fwk-shafer-ch11-s03-s02-f02

Figure 11.10 Rejection Region and Test Statistic for [Note 11.27 \"Example 6\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-n02){.xref xrefstyle="select: title"}
``````

- Step 4. The value of the test statistic is

  $$\mathbf{F} = \frac{s_{1}^{2}}{s_{2}^{2}} = \frac{2.09}{1.10} = 1.90$$

- Step 5. As shown in [Figure 11.10 \"Rejection Region and Test Statistic for \"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-f02), the test statistic 1.90 does not lie in the rejection region, so the decision is not to reject *H*<sub>0</sub>. The data do not provide sufficient evidence, at the 10% level of significance, to conclude that there is a difference in the consistency, as measured by the variance, of the two types of test strips.

(src-fwk-shafer-ch11-s03-s02-n03)=

### Example 7

In the context of [Note 11.27 \"Example 6\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-n02), suppose Type *A* test strips are the current market leader and Type *B* test strips are a newly improved version of Type *A*. Test, at the 10% level of significance, whether the data given in [Table 11.16 \"Two Types of Test Strips\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-t01) provide sufficient evidence to conclude that Type *B* test strips have better consistency (lower variance) than Type *A* test strips.

Solution:

- Step 1. The test of hypotheses is now

  $$\begin{array}{rll}
  H_{0} & : & {\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}} \\
  {\text{\quad vs.}\, H_{a}} & : & {\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}\quad\,@\,\alpha = 0.10}
  \end{array}$$

- Step 2. The distribution is the *F*-distribution with degrees of freedom $df_{1} = 16 - 1 = 15$ and $df_{2} = 21 - 1 = 20.$

- Step 3. The value of the test statistic is

  $$\mathbf{F} = \frac{s_{1}^{2}}{s_{2}^{2}} = \frac{2.09}{1.10} = 1.90$$

- Step 4. The test is right-tailed. The single critical value is $F_{\alpha} = F_{0.10} = 1.84.$ Thus the rejection region is $\left\lbrack {1.84,\infty} \right)$, as illustrated in [Figure 11.11 \"Rejection Region and Test Statistic for \"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-f03).

``````{figure} /images/redrawn/fig-11-11.svg
:alt: F density with 15 and 20 degrees of freedom. The right tail of area α = 0.10 beyond the critical value F_α = 1.84 is shaded. On the number line below, the rejection region F ≥ 1.84 is red, and the test statistic F = 1.90, marked with a star, lies just inside it.
:name: src-fwk-shafer-ch11-s03-s02-f03

Figure 11.11 Rejection Region and Test Statistic for [Note 11.28 \"Example 7\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-n03){.xref xrefstyle="select: title"}
``````

- Step 5. As shown in [Figure 11.11 \"Rejection Region and Test Statistic for \"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s03-s02-f03), the test statistic 1.90 lies in the rejection region, so the decision is to reject *H*<sub>0</sub>. The data provide sufficient evidence, at the 10% level of significance, to conclude that Type *B* test strips have better consistency (lower variance) than Type *A* test strips do.

````````````{important} Key Takeaways

- Critical values of an *F*-distribution with degrees of freedom $df_{1}$ and $df_{2}$ are found in tables in [Chapter 12 \"Appendix\"](/appendices/appendix.md#src-fwk-shafer-ch12).
- An *F*-test can be used to evaluate the hypothesis of two identical normal population variances.

````````````

### Exercises

### Basic

1.  Find *F*<sub>0.01</sub> for each of the following degrees of freedom.

    1.  $df_{1} = 5$ and $df_{2} = 5$
    2.  $df_{1} = 5$ and $df_{2} = 12$
    3.  $df_{1} = 12$ and $df_{2} = 20$

2.  Find *F*<sub>0.05</sub> for each of the following degrees of freedom.

    1.  $df_{1} = 6$ and $df_{2} = 6$
    2.  $df_{1} = 6$ and $df_{2} = 12$
    3.  $df_{1} = 12$ and $df_{2} = 30$

3.  Find *F*<sub>0.95</sub> for each of the following degrees of freedom.

    1.  $df_{1} = 6$ and $df_{2} = 6$
    2.  $df_{1} = 6$ and $df_{2} = 12$
    3.  $df_{1} = 12$ and $df_{2} = 30$

4.  Find *F*<sub>0.90</sub> for each of the following degrees of freedom.

    1.  $df_{1} = 5$ and $df_{2} = 5$
    2.  $df_{1} = 5$ and $df_{2} = 12$
    3.  $df_{1} = 12$ and $df_{2} = 20$

5.  For $df_{1} = 7$, $df_{2} = 10$ and $\alpha = 0.05$, find

    1.  $F_{\alpha}$
    2.  $F_{1 - \alpha}$
    3.  $F_{\alpha / 2}$
    4.  $F_{1 - \alpha / 2}$

6.  For $df_{1} = 15$, $df_{2} = 8$, and $\alpha = 0.01$, find

    1.  $F_{\alpha}$
    2.  $F_{1 - \alpha}$
    3.  $F_{\alpha / 2}$
    4.  $F_{1 - \alpha / 2}$

7.  For each of the two samples

    $$\begin{aligned}
    {\text{Sample 1}:} & \left\{ {8,2,11,0,\text{-}2,} \right\} \\
    {\text{Sample 2}:} & \left\{ {\text{-}2,0,0,0,2,4,\text{-}1} \right\}
    \end{aligned}$$

    find

    1.  the sample size,
    2.  the sample mean,
    3.  the sample variance.

8.  For each of the two samples

    $$\begin{aligned}
    {\text{Sample 1}:} & \left\{ {0.8,1.2,1.1,0.8,\text{-}2.0} \right\} \\
    {\text{Sample 2}:} & \left\{ {\text{-}2.0,0.0,0.7,0.8,2.2,4.1,\text{-}1.9} \right\}
    \end{aligned}$$

    find

    1.  the sample size,
    2.  the sample mean,
    3.  the sample variance.

9.  Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 16$
      - $s_{1}^{2} = 53$
    - - 2
      - $n_{2} = 21$
      - $s_{2}^{2} = 32$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  Find *F*<sub>0.05</sub> using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

10. Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 11$
      - $s_{1}^{2} = 61$
    - - 2
      - $n_{2} = 8$
      - $s_{2}^{2} = 44$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  Find *F*<sub>0.05</sub> using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} > \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

11. Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 10$
      - $s_{1}^{2} = 12$
    - - 2
      - $n_{2} = 13$
      - $s_{2}^{2} = 23$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  For $\alpha = 0.05$ find $F_{1 - \alpha}$ using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} < \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

12. Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 8$
      - $s_{1}^{2} = 102$
    - - 2
      - $n_{2} = 8$
      - $s_{2}^{2} = 603$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  For $\alpha = 0.05$ find $F_{1 - \alpha}$ using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} < \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

13. Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 9$
      - $s_{1}^{2} = 123$
    - - 2
      - $n_{2} = 31$
      - $s_{2}^{2} = 543$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  For $\alpha = 0.05$ find $F_{1 - \alpha / 2}$ and $F_{\alpha / 2}$ using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} \neq \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

14. Two random samples taken from two normal populations yielded the following information:

    ````````{list-table}
    :header-rows: 1

    - - Sample
      - Sample Size
      - Sample Variance
    - - 1
      - $n_{1} = 21$
      - $s_{1}^{2} = 199$
    - - 2
      - $n_{2} = 21$
      - $s_{2}^{2} = 66$

    ````````

    1.  Find the statistic $\left. F = s_{1}^{2}/ s_{2}^{2}. \right.$
    2.  Find the degrees of freedom $df_{1}$ and $df_{2}.$
    3.  For $\alpha = 0.05$ find $F_{1 - \alpha / 2}$ and $F_{\alpha / 2}$ using $df_{1}$ and $df_{2}$ computed above.
    4.  Perform the test the hypotheses $H_{0}:\mathit{\sigma}_{1}^{2} = \mathit{\sigma}_{2}^{2}$ vs. $H_{a}:\mathit{\sigma}_{1}^{2} \neq \mathit{\sigma}_{2}^{2}$ at the 5% level of significance.

### Applications

15. Japanese sturgeon is a subspecies of the sturgeon family indigenous to Japan and the Northwest Pacific. In a particular fish hatchery newly hatched baby Japanese sturgeon are kept in tanks for several weeks before being transferred to larger ponds. Dissolved oxygen in tank water is very tightly monitored by an electronic system and rigorously maintained at a target level of 6.5 milligrams per liter (mg/l). The fish hatchery looks to upgrade their water monitoring systems for tighter control of dissolved oxygen. A new system is evaluated against the old one currently being used in terms of the variance in measured dissolved oxygen. Thirty-one water samples from a tank operated with the new system were collected and 16 water samples from a tank operated with the old system were collected, all during the course of a day. The samples yield the following information:

    $$\begin{array}{llll}
    \text{New} & \text{Sample 1:} & {n_{1} = 31} & {s_{1}^{2} = 0.0121} \\
    \text{Old} & \text{Sample 2:} & {n_{2} = 16} & {s_{2}^{2} = 0.0319} \\
     & & &
    \end{array}$$

    Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that the new system will provide a tighter control of dissolved oxygen in the tanks.

16. The risk of investing in a stock is measured by the volatility, or the variance, in changes in the price of that stock. Mutual funds are baskets of stocks and offer generally lower risk to investors. Different mutual funds have different focuses and offer different levels of risk. Hippolyta is deciding between two mutual funds, *A* and *B*, with similar expected returns. To make a final decision, she examined the annual returns of the two funds during the last ten years and obtained the following information:

    $$\begin{array}{lll}
    {\text{Mutual Fund }A} & & \\
    {\text{Sample }1:} & {n_{1} = 10} & {s_{1}^{2} = 0.012} \\
    {\text{Mutual Fund }B} & & \\
    {\text{Sample }2:} & {n_{2} = 10} & {s_{2}^{2} = 0.005}
    \end{array}$$

    Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that the two mutual funds offer different levels of risk.

17. It is commonly acknowledged that grading of the writing part of a college entrance examination is subject to inconsistency. Every year a large number of potential graders are put through a rigorous training program before being given grading assignments. In order to gauge whether such a training program really enhances consistency in grading, a statistician conducted an experiment in which a reference essay was given to 61 trained graders and 31 untrained graders. Information on the scores given by these graders is summarized below:

    $$\begin{array}{llll}
    \text{Trained} & \text{Sample 1:} & {n_{1} = 61} & {s_{1}^{2} = 2.15} \\
    \text{Untrained} & \text{Sample 2:} & {n_{2} = 31} & {s_{2}^{2} = 3.91} \\
     & & &
    \end{array}$$

    Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that the training program enhances the consistency in essay grading.

18. A common problem encountered by many classical music radio stations is that their listeners belong to an increasingly narrow band of ages in the population. The new general manager of a classical music radio station believed that a new playlist offered by a professional programming agency would attract listeners from a wider range of ages. The new list was used for a year. Two random samples were taken before and after the new playlist was adopted. Information on the ages of the listeners in the sample are summarized below:

    $$\begin{array}{llll}
    \text{Before} & \text{Sample 1:} & {n_{1} = 21} & {s_{1}^{2} = 56.25} \\
    \text{After} & \text{Sample 2:} & {n_{2} = 16} & {s_{2}^{2} = 76.56} \\
     & & &
    \end{array}$$

    Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that the new playlist has expanded the range of listener ages.

19. A laptop computer maker uses battery packs supplied by two companies, *A* and *B*. While both brands have the same average battery life between charges (LBC), the computer maker seems to receive more complaints about shorter LBC than expected for battery packs supplied by company *B*. The computer maker suspects that this could be caused by higher variance in LBC for Brand *B*. To check that, ten new battery packs from each brand are selected, installed on the same models of laptops, and the laptops are allowed to run until the battery packs are completely discharged. The following are the observed LBCs in hours.

    $$\begin{matrix}
    {\text{Brand }A} & {\text{Brand }B} \\
    3.2 & 3.0 \\
    3.4 & 3.5 \\
    2.8 & 2.9 \\
    3.0 & 3.1 \\
    3.0 & 2.3 \\
    3.0 & 2.0 \\
    2.8 & 3.0 \\
    2.9 & 2.9 \\
    3.0 & 3.0 \\
    3.0 & 4.1
    \end{matrix}$$

    Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that the LBCs of Brand *B* have a larger variance that those of Brand *A*.

20. A manufacturer of a blood-pressure measuring device for home use claims that its device is more consistent than that produced by a leading competitor. During a visit to a medical store a potential buyer tried both devices on himself repeatedly during a short period of time. The following are readings of systolic pressure.

    $$\begin{matrix}
    \text{Manufacturer} & \text{Competitor} \\
    132 & 129 \\
    134 & 132 \\
    129 & 129 \\
    129 & 138 \\
    130 & \\
    132 &
    \end{matrix}$$

    1.  Test, at the 5% level of significance, whether the data provide sufficient evidence to conclude that the manufacturer's claim is true.
    2.  Repeat the test at the 10% level of significance. Quote as many computations from part (a) as possible.

### Large Data Set Exercises

21. Large Data Sets 1A and 1B record SAT scores for 419 male and 581 female students. Test, at the 1% level of significance, whether the data provide sufficient evidence to conclude that the variances of scores of male and female students differ.

    <http://www.flatworldknowledge.com/sites/all/files/data1A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data1B.xls>

22. Large Data Sets 7, 7A, and 7B record the survival times of 140 laboratory mice with thymic leukemia. Test, at the 10% level of significance, whether the data provide sufficient evidence to conclude that the variances of survival times of male mice and female mice differ.

    <http://www.flatworldknowledge.com/sites/all/files/data7.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data7A.xls>

    <http://www.flatworldknowledge.com/sites/all/files/data7B.xls>

`````````````{admonition} Answers
:class: dropdown

1.  1.  11.0,
    2.  5.06,
    3.  3.23

2. &nbsp;

3.  1.  0.23,
    2.  0.25,
    3.  0.40

4. &nbsp;

5.  1.  3.14,
    2.  0.27,
    3.  3.95,
    4.  0.21

6. &nbsp;

7.  Sample 1:

    1.  $n_{1} = 5$,
    2.  ${\overset{-}{x}}_{1} = 3.8$,
    3.  $s_{1}^{2} = 30.2.$

    Sample 2:

    1.  $n_{2} = 7$,
    2.  ${\overset{-}{x}}_{2} = 0.4286$,
    3.  $s_{2}^{2} = 3.95$

8. &nbsp;

9.  1.  1.6563,
    2.  $df_{1} = 15$, $df_{2} = 20$,
    3.  $F_{0.05} = 2.2$
    4.  do not reject *H*<sub>0</sub>

10. &nbsp;

11. 1.  0.5217
    2.  $df_{1} = 9$, $df_{2} = 12$,
    3.  $F_{0.95} = 0.3254$,
    4.  do not reject *H*<sub>0</sub>

12. &nbsp;

13. 1.  0.1692
    2.  $df_{1} = 8$, $df_{2} = 30$
    3.  $F_{0.975} = 0.26$, $F_{0.025} = 2.65$,
    4.  reject *H*<sub>0</sub>

14. &nbsp;

<!-- -->

15. *F* = 0.3793, $F_{0.90} = 0.58$, reject *H*<sub>0</sub>

16. &nbsp;

17. *F* = 0.5499, $F_{0.95} = 0.61$, reject *H*<sub>0</sub>

18. &nbsp;

19. *F* = 0.0971, $F_{0.95} = 0.31$, reject *H*<sub>0</sub>

20. &nbsp;

<!-- -->

21. *F* = 0.893131. $df_{1} = 418$ and $df_{2} = 580.$ Rejection Region: $\left( {0,0.7897} \right\rbrack \cup \left\lbrack {1.2614,\infty} \right).$ Decision: Fail to reject *H*<sub>0</sub> of equal variances.

22. &nbsp;

`````````````

## 11.4 *F*-Tests in One-Way ANOVA

````````````{note} Learning Objective

1.  To understand how to use an *F*-test to judge whether several population means are all equal.

````````````

In [Chapter 9 \"Two-Sample Problems\"](/chapters/ch-09-two-sample-problems.md#src-fwk-shafer-ch09) we saw how to compare two population means $\mathit{\mu}_{1}$ and $\mathit{\mu}_{2}.$ In this section we will learn to compare three or more population means at the same time, which is often of interest in practical applications. For example, an administrator at a university may be interested in knowing whether student grade point averages are the same for different majors. In another example, an oncologist may be interested in knowing whether patients with the same type of cancer have the same average survival times under several different competing cancer treatments.

In general, suppose there are *K* normal populations with possibly different means, $\mathit{\mu}_{1},\mathit{\mu}_{2},\ldots,\mathit{\mu}_{K}$, but all with the same variance $\mathit{\sigma}^{2}.$ The study question is whether all the *K* population means are the same. We formulate this question as the test of hypotheses

$$\begin{array}{rll}
H_{0} & : & {\mathit{\mu}_{1} = \mathit{\mu}_{2} = \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } = \mathit{\mu}_{K}} \\
{\text{\quad vs.}\, H_{a}} & : & {\text{ not all }K\text{ population means are equal}}
\end{array}$$

To perform the test *K* independent random samples are taken from the *K* normal populations. The *K* sample means, the *K* sample variances, and the *K* sample sizes are summarized in the table:

````````{list-table}
:header-rows: 1

- - Population
  - Sample Size
  - Sample Mean
  - Sample Variance
- - 1
  - $n_{1}$
  - ${\overset{-}{x}}_{1}$
  - $s_{1}^{2}$
- - 2
  - $n_{2}$
  - ${\overset{-}{x}}_{2}$
  - $s_{2}^{2}$
- - ⋮
  - ⋮
  - ⋮
  - ⋮
- - *K*
  - $n_{K}$
  - ${\overset{-}{x}}_{K}$
  - $s_{K}^{2}$

````````

Define the following quantities:

The **combined sample size**:

$$n = n_{1} + n_{2} + \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } + n_{K}$$

The **mean of the combined sample** of all *n* observations:

$$\overset{-}{x} = \frac{\Sigma x}{n} = \frac{n_{1}{\overset{-}{x}}_{1} + n_{2}{\overset{-}{x}}_{2} + \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } + n_{K}{\overset{-}{x}}_{K}}{n}$$

The **mean square for treatment**:

$$MST = \frac{n_{1}\left( {{\overset{-}{x}}_{1} - \overset{-}{x}} \right)^{2} + n_{2}\left( {{\overset{-}{x}}_{2} - \overset{-}{x}} \right)^{2} + \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } + n_{K}\left( {{\overset{-}{x}}_{K} - \overset{-}{x}} \right)^{2}}{K\text{-}1}$$

The **mean square for error**:

$$MSE = \frac{\left( {n_{1}\text{-}1} \right)s_{1}^{2} + \left( {n_{2}\text{-}1} \right)s_{2}^{2} + \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } + \left( {n_{K}\text{-}1} \right)s_{K}^{2}}{n - K}$$

MST[^stats-9] can be thought of as the variance between the *K* individual independent random samples and MSE[^stats-10] as the variance within the samples. This is the reason for the name "analysis of variance," universally abbreviated ANOVA[^stats-11]. The adjective "one-way" has to do with the fact that the sampling scheme is the simplest possible, that of taking one random sample from each population under consideration. If the means of the *K* populations are all the same then the two quantities MST and MSE should be close to the same, so the null hypothesis will be rejected if the ratio of these two quantities is significantly greater than 1. This yields the following test statistic and methods and conditions for its use.

````````````{important} Test Statistic for Testing the Null Hypothesis that K Population Means Are Equal

$$F = \frac{MST}{MSE}$$

If the *K* populations are normally distributed with a common variance and if $H_{0}:\mathit{\mu}_{1} = \text{ }\cdot \text{ }\cdot \text{ }\cdot \text{ } = \mathit{\mu}_{K}$ is true then under independent random sampling *F* approximately follows an *F*-distribution with degrees of freedom $df_{1} = K\text{-}1$ and $df_{2} = n - K.$

The test is right-tailed: *H*<sub>0</sub> is rejected at the level of significance $\alpha$ if $\mathbf{F} \geq F_{\alpha}.$

````````````

As always the test is performed using the usual five-step procedure.

(src-fwk-shafer-ch11-s04-n04)=

### Example 8

The average of grade point averages (GPAs) of college courses in a specific major is a measure of difficulty of the major. An educator wishes to conduct a study to find out whether the difficulty levels of different majors are the same. For such a study, a random sample of major grade point averages (GPA) of 11 graduating seniors at a large university is selected for each of the four majors mathematics, English, education, and biology. The data are given in [Table 11.17 \"Difficulty Levels of College Majors\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-t01). Test, at the 5% level of significance, whether the data contain sufficient evidence to conclude that there are differences among the average major GPAs of these four majors.

(src-fwk-shafer-ch11-s04-t01)=

Table 11.17 Difficulty Levels of College Majors

````````{list-table}
:header-rows: 1

- - Mathematics
  - English
  - Education
  - Biology
- - 2.59
  - 3.64
  - 4.00
  - 2.78
- - 3.13
  - 3.19
  - 3.59
  - 3.51
- - 2.97
  - 3.15
  - 2.80
  - 2.65
- - 2.50
  - 3.78
  - 2.39
  - 3.16
- - 2.53
  - 3.03
  - 3.47
  - 2.94
- - 3.29
  - 2.61
  - 3.59
  - 2.32
- - 2.53
  - 3.20
  - 3.74
  - 2.58
- - 3.17
  - 3.30
  - 3.77
  - 3.21
- - 2.70
  - 3.54
  - 3.13
  - 3.23
- - 3.88
  - 3.25
  - 3.00
  - 3.57
- - 2.64
  - 4.00
  - 3.47
  - 3.22

````````

Solution:

- Step 1. The test of hypotheses is

  $$\begin{array}{rll}
  H_{0} & : & {\mathit{\mu}_{1} = \mathit{\mu}_{2} = \mathit{\mu}_{3} = \mathit{\mu}_{4}} \\
  {\text{\quad vs.}\,\, H_{a}} & : & {\text{ not all four population means are equal}\quad\,@\,\alpha = 0.05}
  \end{array}$$

- Step 2. The test statistic is $\left. \mathbf{F} = MST/ MSE \right.$ with (since *n* = 44 and *K* = 4) degrees of freedom $df_{1} = K\text{-}1 = 4 - 1 = 3$ and $df_{2} = n - K = 44 - 4 = 40.$

- Step 3. If we index the population of mathematics majors by 1, English majors by 2, education majors by 3, and biology majors by 4, then the sample sizes, sample means, and sample variances of the four samples in [Table 11.17 \"Difficulty Levels of College Majors\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-t01) are summarized (after rounding for simplicity) by:

  ````````{list-table}
  :header-rows: 1

  - - Major
    - Sample Size
    - Sample Mean
    - Sample Variance
  - - Mathematics
    - $n{}_{1} = 11$
    - ${\overset{-}{x}}_{1} = 2.90$
    - $s_{1}^{2} = 0.188$
  - - English
    - $n{}_{2} = 11$
    - ${\overset{-}{x}}_{2} = 3.34$
    - $s_{2}^{2} = 0.148$
  - - Education
    - $n{}_{3} = 11$
    - ${\overset{-}{x}}_{3} = 3.36$
    - $s_{3}^{2} = 0.229$
  - - Biology
    - $n{}_{4} = 11$
    - ${\overset{-}{x}}_{4} = 3.02$
    - $s_{4}^{2} = 0.157$

  ````````

  The average of all 44 observations is (after rounding for simplicity) $\overset{-}{x} = 3.15.$ We compute (rounding for simplicity)

  $$\begin{aligned}
  {MST} & {= \frac{11\left( {2.90 - 3.15} \right)^{2} + 11\left( {3.34 - 3.15} \right)^{2} + 11\left( {3.36 - 3.15} \right)^{2} + 11\left( {3.02 - 3.15} \right)^{2}}{4 - 1}} & & \\
   & {= \frac{1.7556}{3}} & & \\
   & {= 0.585} & &
  \end{aligned}$$

  and

  $$\begin{array}{lll}
  {MSE} & = & \frac{\left( {11 - 1} \right)(0.188) + \left( {11 - 1} \right)(0.148) + \left( {11 - 1} \right)(0.229) + \left( {11 - 1} \right)(0.157)}{44 - 4} \\
   & = & \frac{7.22}{40} \\
   & = & 0.181
  \end{array}$$

  so that

  $$\mathbf{F} = \frac{MST}{MSE} = \frac{0.585}{0.181} = 3.232$$

- Step 4. The test is right-tailed. The single critical value is (since $df_{1} = 3$ and $df_{2} = 40$) $F_{\alpha} = F_{0.05} = 2.84.$ Thus the rejection region is $\left\lbrack {2.84,\infty} \right)$, as illustrated in [Figure 11.12](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-f01).

``````{figure} /images/redrawn/fig-11-12.svg
:alt: F density with 3 and 40 degrees of freedom. The right tail of area α = 0.05 beyond the critical value F_α = 2.84 is shaded. On the number line below, the rejection region F ≥ 2.84 is red, and the test statistic F = 3.232, marked with a star, lies inside it.
:name: src-fwk-shafer-ch11-s04-f01

Figure 11.12 [Note 11.36 \"Example 8\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-n04){.xref xrefstyle="select: title"} Rejection Region
``````

- Step 5. Since $F = 3.232 > 2.84$, we reject *H*<sub>0</sub>. The data provide sufficient evidence, at the 5% level of significance, to conclude that the averages of major GPAs for the four majors considered are not all equal.

(src-fwk-shafer-ch11-s04-n05)=

### Example 9

A research laboratory developed two treatments which are believed to have the potential of prolonging the survival times of patients with an acute form of thymic leukemia. To evaluate the potential treatment effects 33 laboratory mice with thymic leukemia were randomly divided into three groups. One group received Treatment 1, one received Treatment 2, and the third was observed as a control group. The survival times of these mice are given in [Table 11.18 \"Mice Survival Times in Days\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-t02). Test, at the 1% level of significance, whether these data provide sufficient evidence to confirm the belief that at least one of the two treatments affects the average survival time of mice with thymic leukemia.

(src-fwk-shafer-ch11-s04-t02)=

Table 11.18 Mice Survival Times in Days

````````{list-table}
:header-rows: 1

- - Treatment 1
  - Treatment 1
  - Treatment 2
  - Control
- - 71
  - 75
  - 77
  - 81
- - 72
  - 73
  - 67
  - 79
- - 75
  - 72
  - 79
  - 73
- - 80
  - 65
  - 78
  - 71
- - 60
  - 63
  - 81
  - 75
- - 65
  - 69
  - 72
  - 84
- - 63
  - 64
  - 71
  - 77
- - 78
  - 71
  - 84
  - 67
- -
  -
  - 91
  -

````````

Solution:

- Step 1. The test of hypotheses is

  $$\begin{array}{rll}
  H_{0} & : & {\mathit{\mu}_{1} = \mathit{\mu}_{2} = \mathit{\mu}_{3}} \\
  {\text{\quad vs.}\,\, H_{a}} & : & {\text{not all three population means are equal}\,\quad @\,\alpha = 0.01}
  \end{array}$$

- Step 2. The test statistic is $\left. \mathbf{F} = MST/ MSE \right.$ with (since *n* = 33 and *K* = 3) degrees of freedom $df_{1} = K\text{-}1 = 3 - 1 = 2$ and $df_{2} = n - K = 33 - 3 = 30.$

- Step 3. If we index the population of mice receiving Treatment 1 by 1, Treatment 2 by 2, and no treatment by 3, then the sample sizes, sample means, and sample variances of the three samples in [Table 11.18 \"Mice Survival Times in Days\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-t02) are summarized (after rounding for simplicity) by:

  ````````{list-table}
  :header-rows: 1

  - - Group
    - Sample Size
    - Sample Mean
    - Sample Variance
  - - Treatment 1
    - $n_{1} = 16$
    - ${\overset{-}{x}}_{1} = 69.75$
    - $s_{1}^{2} = 34.47$
  - - Treatment 2
    - $n_{2} = 9$
    - ${\overset{-}{x}}_{2} = 77.78$
    - $s_{2}^{2} = 52.69$
  - - Control
    - $n_{3} = 8$
    - ${\overset{-}{x}}_{3} = 75.88$
    - $s_{3}^{2} = 30.69$

  ````````

  The average of all 33 observations is (after rounding for simplicity) $\overset{-}{x} = 73.42.$ We compute (rounding for simplicity)

  $$MST = \frac{16\left( {69.75 - 73.42} \right)^{2} + 9\left( {77.78 - 73.42} \right)^{2} + 8\left( {75.88 - 73.42} \right)^{2}}{3 - 1} = \frac{434.63}{2} = 217.50$$

  and

  $$MSE = \frac{\left( {16 - 1} \right)(34.47) + \left( {9 - 1} \right)(52.69) + \left( {8 - 1} \right)(30.69)}{33 - 3} = \frac{1153.4}{30} = 38.45$$

  so that

  $$\mathbf{F} = \frac{MST}{MSE} = \frac{217.50}{38.45} = 5.65$$

- Step 4. The test is right-tailed. The single critical value is $F_{\alpha} = F_{0.01} = 5.39.$ Thus the rejection region is $\left\lbrack {5.39,\infty} \right)$, as illustrated in [Figure 11.13](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-f02).

``````{figure} /images/redrawn/fig-11-13.svg
:alt: F density with 2 and 30 degrees of freedom, highest at 0 and decreasing. The thin right tail of area α = 0.01 beyond the critical value F_α = 5.39 is shaded. On the number line below, the rejection region F ≥ 5.39 is red, and the test statistic F = 5.65, marked with a star, lies just inside it.
:name: src-fwk-shafer-ch11-s04-f02

Figure 11.13 [Note 11.37 \"Example 9\"](/chapters/ch-11-chi-square-tests-and-f-tests.md#src-fwk-shafer-ch11-s04-n05){.xref xrefstyle="select: title"} Rejection Region
``````

- Step 5. Since $F = 5.65 > 5.39$, we reject *H*<sub>0</sub>. The data provide sufficient evidence, at the 1% level of significance, to conclude that a treatment effect exists at least for one of the two treatments in increasing the mean survival time of mice with thymic leukemia.

It is important to note that, if the null hypothesis of equal population means is rejected, the statistical implication is that not all population means are equal. It does not however tell which population mean is different from which. The inference about where the suggested difference lies is most frequently made by a follow-up study.

````````````{important} Key Takeaway

- An *F*-test can be used to evaluate the hypothesis that the means of several normal populations, all with the same standard deviation, are identical.

````````````

### Exercises

### Basic

1.  The following three random samples are taken from three normal populations with respective means $\mathit{\mu}_{1}$, $\mathit{\mu}_{2}$, and $\mathit{\mu}_{3}$, and the same variance $\mathit{\sigma}^{2}.$

    ````````{list-table}
    :header-rows: 1

    - - Sample 1
      - Sample 2
      - Sample 3
    - - 2
      - 3
      - 0
    - - 2
      - 5
      - 1
    - - 3
      - 7
      - 2
    - - 5
      -
      - 1
    - - 3
      -
      -

    ````````

    1.  Find the combined sample size *n*.
    2.  Find the combined sample mean $\overset{-}{x}.$
    3.  Find the sample mean for each of the three samples.
    4.  Find the sample variance for each of the three samples.
    5.  Find $MST.$
    6.  Find $MSE.$
    7.  Find $\left. F = MST/ MSE. \right.$

2.  The following three random samples are taken from three normal populations with respective means $\mathit{\mu}_{1}$, $\mathit{\mu}_{2}$, and $\mathit{\mu}_{3}$, and a same variance $\mathit{\sigma}^{2}.$

    ````````{list-table}
    :header-rows: 1

    - - Sample 1
      - Sample 2
      - Sample 3
    - - 0.0
      - 1.3
      - 0.2
    - - 0.1
      - 1.5
      - 0.2
    - - 0.2
      - 1.7
      - 0.3
    - - 0.1
      -
      - 0.5
    - -
      -
      - 0.0

    ````````

    1.  Find the combined sample size *n*.
    2.  Find the combined sample mean $\overset{-}{x}.$
    3.  Find the sample mean for each of the three samples.
    4.  Find the sample variance for each of the three samples.
    5.  Find $MST.$
    6.  Find $MSE.$
    7.  Find $\left. F = MST/ MSE. \right.$

3.  Refer to Exercise 1.

    1.  Find the number of populations under consideration *K*.

    2.  Find the degrees of freedom $df_{1} = K\text{-}1$ and $df_{2} = n - K.$

    3.  For $\alpha = 0.05$, find $F_{\alpha}$ with the degrees of freedom computed above.

    4.  At $\alpha = 0.05$, test hypotheses

        $$\begin{array}{ccl}
        H_{0} & : & {\mathit{\mu}_{1} = \mathit{\mu}_{2} = \mathit{\mu}_{3}} \\
        {\text{vs. }H_{a}} & : & \text{at least one pair of the} \\
         & & \text{ population means are not equal}
        \end{array}$$

4.  Refer to Exercise 2.

    1.  Find the number of populations under consideration *K*.

    2.  Find the degrees of freedom $df_{1} = K\text{-}1$ and $df_{2} = n - K.$

    3.  For $\alpha = 0.01$, find $F_{\alpha}$ with the degrees of freedom computed above.

    4.  At $\alpha = 0.01$, test hypotheses

        $$\begin{array}{ccl}
        H_{0} & : & {\mathit{\mu}_{1} = \mathit{\mu}_{2} = \mathit{\mu}_{3}} \\
        {\text{vs. }H_{a}} & : & \text{at least one pair of the } \\
         & & \text{population means are not equal}
        \end{array}$$

### Applications

5.  The Mozart effect refers to a boost of average performance on tests for elementary school students if the students listen to Mozart's chamber music for a period of time immediately before the test. In order to attempt to test whether the Mozart effect actually exists, an elementary school teacher conducted an experiment by dividing her third-grade class of 15 students into three groups of 5. The first group was given an end-of-grade test without music; the second group listened to Mozart's chamber music for 10 minutes; and the third groups listened to Mozart's chamber music for 20 minutes before the test. The scores of the 15 students are given below:

    ````````{list-table}
    :header-rows: 1

    - - Group 1
      - Group 2
      - Group 3
    - - 80
      - 79
      - 73
    - - 63
      - 73
      - 82
    - - 74
      - 74
      - 79
    - - 71
      - 77
      - 82
    - - 70
      - 81
      - 84

    ````````

    Using the ANOVA *F*-test[^stats-12] at $\alpha = 0.10$, is there sufficient evidence in the data to suggest that the Mozart effect exists?

6.  The Mozart effect refers to a boost of average performance on tests for elementary school students if the students listen to Mozart's chamber music for a period of time immediately before the test. Many educators believe that such an effect is not necessarily due to Mozart's music per se but rather a relaxation period before the test. To support this belief, an elementary school teacher conducted an experiment by dividing her third-grade class of 15 students into three groups of 5. Students in the first group were asked to give themselves a self-administered facial massage; students in the second group listened to Mozart's chamber music for 15 minutes; students in the third group listened to Schubert's chamber music for 15 minutes before the test. The scores of the 15 students are given below:

    ````````{list-table}
    :header-rows: 1

    - - Group 1
      - Group 2
      - Group 3
    - - 79
      - 82
      - 80
    - - 81
      - 84
      - 81
    - - 80
      - 86
      - 71
    - - 89
      - 91
      - 90
    - - 86
      - 82
      - 86

    ````````

    Test, using the ANOVA *F*-test at the 10% level of significance, whether the data provide sufficient evidence to conclude that any of the three relaxation method does better than the others.

7.  Precision weighing devices are sensitive to environmental conditions. Temperature and humidity in a laboratory room where such a device is installed are tightly controlled to ensure high precision in weighing. A newly designed weighing device is claimed to be more robust against small variations of temperature and humidity. To verify such a claim, a laboratory tests the new device under four settings of temperature-humidity conditions. First, two levels of *high* and *low* temperature and two levels of *high* and *low* humidity are identified. Let *T* stand for temperature and *H* for humidity. The four experimental settings are defined and noted as (*T*, *H*): (high, high), (high, low), (low, high), and (low, low). A pre-calibrated standard weight of 1 kg was weighed by the new device four times in each setting. The results in terms of error (in micrograms mcg) are given below:

    ````````{list-table}
    :header-rows: 1

    - - (high, high)
      - (high, low)
      - (low, high)
      - (low, low)
    - - −1.50
      - 11.47
      - −14.29
      - 5.54
    - - −6.73
      - 9.28
      - −18.11
      - 10.34
    - - 11.69
      - 5.58
      - −11.16
      - 15.23
    - - −5.72
      - 10.80
      - −10.41
      - −5.69

    ````````

    Test, using the ANOVA *F*-test at the 1% level of significance, whether the data provide sufficient evidence to conclude that the mean weight readings by the newly designed device vary among the four settings.

8.  To investigate the real cost of owning different makes and models of new automobiles, a consumer protection agency followed 16 owners of new vehicles of four popular makes and models, call them $TC$, $HA$, $NA$, and $FT$, and kept a record of each of the owner's real cost in dollars for the first five years. The five-year costs of the 16 car owners are given below:

    ````````{list-table}
    :header-rows: 1

    - - TC
      - HA
      - NA
      - FT
    - - 8423
      - 7776
      - 8907
      - 10333
    - - 7889
      - 7211
      - 9077
      - 9217
    - - 8665
      - 6870
      - 8732
      - 10540
    - -
      - 7129
      - 9747
      -
    - -
      - 7359
      - 8677
      -

    ````````

    Test, using the ANOVA *F*-test at the 5% level of significance, whether the data provide sufficient evidence to conclude that there are differences among the mean real costs of ownership for these four models.

9.  Helping people to lose weight has become a huge industry in the United States, with annual revenue in the hundreds of billions of dollars. Recently each of the three market-leading weight reducing programs claimed to be the most effective. A consumer research company recruited 33 people who wished to lose weight and sent them to the three leading programs. After six months their weight losses were recorded. The results are summarized below:

    ````````{list-table}
    :header-rows: 1

    - - Statistic
      - Prog. 1
      - Prog. 2
      - Prog. 3
    - - Sample Mean
      - ${\overset{-}{x}}_{1} = 10.65$
      - ${\overset{-}{x}}_{2} = 8.90$
      - ${\overset{-}{x}}_{3} = 9.33$
    - - Sample Variance
      - $s_{1}^{2} = 27.20$
      - $s_{2}^{2} = 16.86$
      - $s_{3}^{2} = 32.40$
    - - Sample Size
      - $n_{1} = 11$
      - $n_{2} = 11$
      - $n_{3} = 11$

    ````````

    The mean weight loss of the combined sample of all 33 people was $\overset{-}{x} = 9.63.$ Test, using the ANOVA *F*-test at the 5% level of significance, whether the data provide sufficient evidence to conclude that some program is more effective than the others.

10. A leading pharmaceutical company in the disposable contact lenses market has always taken for granted that the sales of certain peripheral products such as contact lens solutions would automatically go with the established brands. The long-standing culture in the company has been that lens solutions would not make a significant difference in user experience. Recent market research surveys, however, suggest otherwise. To gain a better understanding of the effects of contact lens solutions on user experience, the company conducted a comparative study in which 63 contact lens users were randomly divided into three groups, each of which received one of three top selling lens solutions on the market, including one of the company's own. After using the assigned solution for two weeks, each participant was asked to rate the solution on the scale of 1 to 5 for satisfaction, with 5 being the highest level of satisfaction. The results of the study are summarized below:

    ````````{list-table}
    :header-rows: 1

    - - Statistics
      - Sol. 1
      - Sol. 2
      - Sol. 3
    - - Sample Mean
      - ${\overset{-}{x}}_{1} = 3.28$
      - ${\overset{-}{x}}_{2} = 3.96$
      - ${\overset{-}{x}}_{3} = 4.10$
    - - Sample Variance
      - $s_{1}^{2} = 0.15$
      - $s_{2}^{2} = 0.32$
      - $s_{3}^{2} = 0.36$
    - - Sample Size
      - $n_{1} = 18$
      - $n_{2} = 23$
      - $n_{3} = 22$

    ````````

    The mean satisfaction level of the combined sample of all 63 participants was $\overset{-}{x} = 3.81.$ Test, using the ANOVA *F*-test at the 5% level of significance, whether the data provide sufficient evidence to conclude that not all three average satisfaction levels are the same.

### Large Data Set Exercise

11. Large Data Set 9 records the costs of materials (textbook, solution manual, laboratory fees, and so on) in each of ten different courses in each of three different subjects, chemistry, computer science, and mathematics. Test, at the 1% level of significance, whether the data provide sufficient evidence to conclude that the mean costs in the three disciplines are not all the same.

    <http://www.flatworldknowledge.com/sites/all/files/data9.xls>

`````````````{admonition} Answers
:class: dropdown

1.  1.  *n* = 12,
    2.  $\overset{-}{x} = 2.8333$,
    3.  ${\overset{-}{x}}_{1} = 3$, ${\overset{-}{x}}_{2} = 5$, ${\overset{-}{x}}_{3} = 1$,
    4.  $s_{1}^{2} = 1.5$, $s_{2}^{2} = 4$, $s_{3}^{2} = 0.6667$,
    5.  $MST = 13.83$,
    6.  $MSE = 1.78$,
    7.  *F* = 7.7812
2. &nbsp;
3.  1.  *K* = 3;
    2.  $df_{1} = 2$, $df_{2} = 9$;
    3.  $F_{0.05} = 4.26$;
    4.  *F* = 5.53, reject *H*<sub>0</sub>
4. &nbsp;

<!-- -->

5.  *F* = 3.9647, $F_{0.10} = 2.81$, reject *H*<sub>0</sub>

6. &nbsp;

7.  *F* = 9.6018, $F_{0.01} = 5.95$, reject *H*<sub>0</sub>

8. &nbsp;

9.  *F* = 0.3589, $F_{0.05} = 3.32$, do not reject *H*<sub>0</sub>

10. &nbsp;

<!-- -->

11. *F* = 1.418. $df_{1} = 2$ and $df_{2} = 27.$ Rejection Region: $\left\lbrack {5.4881,\infty} \right).$ Decision: Fail to reject *H*<sub>0</sub> of equal means.

`````````````

[^stats-1]: A particular probability distribution specified by a number of degrees of freedom, $df$.

[^stats-2]: A particular probability distribution specified by two degrees of freedom, $df_{1}$ and $df_{2}.$

[^stats-3]: A random variable that follows a chi-square distribution.

[^stats-4]: A variable with several qualitative levels.

[^stats-5]: A test based on a chi-square statistic to check whether two factors are independent.

[^stats-6]: A test based on a chi-square statistic to check whether a sample is taken from a population with a hypothesized probability distribution.

[^stats-7]: A random variable following an *F*-distribution.

[^stats-8]: A test based on an *F* statistic to check whether two population variances are equal.

[^stats-9]: Mean square for treatment.

[^stats-10]: Mean square for error.

[^stats-11]: Analysis of variance.

[^stats-12]: a test based on an *F* statistic to check whether several population means are equal.
