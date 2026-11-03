"""Editorial prose corrections applied after HTML→MyST conversion.

Corrections are deliberate departures from the 2012 source archive and must stay
reproducible: import_source.py calls apply_content_corrections() on every page.
Document changes in SOURCES.md when this list grows.
"""
from __future__ import annotations

import re

# Exact substring replacements. Longer / more specific strings first where
# overlapping prefixes could bite.
EXACT_REPLACEMENTS: list[tuple[str, str]] = [
    # --- Spelling typos ---
    (r'\text{Probablity}', r'\text{Probability}'),
    ('Univeristy of Missouri-Columbia', 'University of Missouri-Columbia'),
    ('exercsises', 'exercises'),
    ("buyers's perception", "buyers' perception"),
    ('deciaml place', 'decimal place'),
    ('predominately rural', 'predominantly rural'),

    # --- Doubled words ---
    ('to to note', 'to note'),
    ('all all households', 'all households'),
    ('all all self-described', 'all self-described'),
    ('record the their test scores', 'record their test scores'),

    # --- Wrong word forms / morphology ---
    ('must first computed the', 'must first compute the'),
    ('are selected a random', 'are selected at random'),
    ('normally distributed normal random variable', 'normally distributed random variable'),
    ('The probability that *X* lie in', 'The probability that *X* lies in'),
    ('normally distributed random variable *X* with mean', 'normally distributed random variable with mean'),
    ('A investigator examines', 'An investigator examines'),
    ('A automotive tire manufacturer', 'An automotive tire manufacturer'),
    ('minimum samples size needed', 'minimum sample size needed'),
    ('degrees of freedoms', 'degrees of freedom'),
    ('predictions intervals', 'prediction intervals'),
    ('hypotheses testing procedure', 'hypothesis testing procedure'),
    ('outcomes of hypothesis testing procedure', 'outcomes of a hypothesis testing procedure'),
    ('hypotheses testing for', 'hypothesis testing for'),
    ('Hypotheses testing will', 'Hypothesis testing will'),
    ('the null hypotheses is', 'the null hypothesis is'),
    ('census of all freshman at', 'census of all freshmen at'),
    ('a local restaurants is', 'a local restaurant is'),
    ('the three dots indicates', 'the three dots indicate'),
    ('try to insure that', 'try to ensure that'),
    ('was insured by the Central Limit Theorem', 'was ensured by the Central Limit Theorem'),
    ('neither an upward or downward', 'neither an upward nor a downward'),
    ('hundreds of billion dollars', 'hundreds of billions of dollars'),
    ('Everyday at lunch time', 'Every day at lunchtime'),
    ('choose a text booklet', 'choose a test booklet'),
    ('To assess to the relative', 'To assess the relative'),
    ('using pair sampling', 'using paired sampling'),
    ('sleep got by healthy adults', 'sleep gotten by healthy adults'),
    ('The first column of numbers form a sample', 'The first column of numbers forms a sample'),
    ('the second column of numbers form a sample', 'the second column of numbers forms a sample'),

    # --- Missing words / broken phrases ---
    ('construct a 99% confidence for the mean', 'construct a 99% confidence interval for the mean'),
    ('construct a 95% confidence for the mean', 'construct a 95% confidence interval for the mean'),
    ('construct a 90% confidence for *p*', 'construct a 90% confidence interval for *p*'),
    ('construct a 90% confidence for $p_{1} - p_{2}.$',
     'construct a 90% confidence interval for $p_{1} - p_{2}.$'),
    ('Find percentage of all individuals', 'Find the percentage of all individuals'),
    ('average number monetary gifts', 'average number of monetary gifts'),
    ('top face of fair die that is rolled', 'top face of a fair die that is rolled'),
    ('in favor of proposed law in a sample 1,200',
     'in favor of the proposed law in a sample of 1,200'),
    ('*n* = 20 observations The values', '*n* = 20 observations. The values'),
    ('with variance with $\\mathit{\\sigma}_{2}^{2}.$',
     'with variance $\\mathit{\\sigma}_{2}^{2}.$'),
    ('is rejected at level of significance', 'is rejected at the level of significance'),
    ('procedure for test of hypotheses', 'procedure for a test of hypotheses'),
    ('Assume that population of differences', 'Assume that the population of differences'),
    ('the density function fit inside', 'the density function fits inside'),
    ('asked them if their opinion on', 'asked them their opinion on'),
    ('A list of all the formulas that appear anywhere in this chapter are collected',
     'A list of all the formulas that appear anywhere in this chapter is collected'),
    ('The set of assumptions in simple linear regression are a mathematical description',
     'The set of assumptions in simple linear regression is a mathematical description'),

    # --- Math / set notation typo ---
    (r'\left\{ {0.1.2} \right\}', r'\left\{ {0,1,2} \right\}'),

    # --- Subject-event label typo (event MF, not M) ---
    ('Since $MF = \\left\\{ {bf,hf,af,of} \\right\\}$, $P(M) =',
     'Since $MF = \\left\\{ {bf,hf,af,of} \\right\\}$, $P(MF) ='),

    # --- Content error: t_c described as normal instead of t ---
    ('so the symbol *t<sub>c</sub>* stands for the value that cuts off a right tail of area *c* in the standard normal distribution.',
     "so the symbol *t<sub>c</sub>* stands for the value that cuts off a right tail of area *c* in Student's *t*-distribution."),

    # --- Agency name ---
    ('National Institute of Health', 'National Institutes of Health'),
    ('supported by National Science Foundation, U.S. Environmental Protection Agency, Office of Naval Research, and National Institutes of Health',
     'supported by the National Science Foundation, the U.S. Environmental Protection Agency, the Office of Naval Research, and the National Institutes of Health'),

    # --- Coin-toss idiom ---
    ('at least one heads will appear', 'at least one head will appear'),
    ('"at least one heads."', '"at least one head."'),
    ('obtain at least one heads', 'obtain at least one head'),
    ('"at most one heads."', '"at most one head."'),

    # --- Missing sentence break after math ---
    ('$E(X) = \\text{-}0.0526$ In many bets',
     '$E(X) = \\text{-}0.0526$. In many bets'),
    ('with the symbol "≠" The following',
     'with the symbol "≠." The following'),

    # --- Truncated xref titles already broken in the 2012 HTML ---
    ('Figure 11.1 \\"Many \\"', 'Figure 11.1 \\"Many Chi-Square Distributions\\"'),
    ('Figure 11.7 \\"Many \\"', 'Figure 11.7 \\"Many F Distributions\\"'),
    ('Chapter 11 \\"Chi-Square Tests and \\"',
     'Chapter 11 \\"Chi-Square Tests and F-Tests\\"'),
    ('Figure 10.6 \\"Plot of the Five-Point Data and the Line \\"',
     'Figure 10.6 \\"Plot of the Five-Point Data and the Line\\"'),
    ('Figure 7.5 \\"Student\'s \\"',
     'Figure 7.5 \\"Student\'s t-Distribution\\"'),

    # --- Front-matter title ---
    ('# Acknowledgements\n', '# Acknowledgments\n'),
]


# British → American spelling (word-boundary). Case variants listed explicitly
# so Title Case headings convert cleanly.
AMERICAN_SPELLINGS: list[tuple[str, str]] = [
    ('Acknowledgements', 'Acknowledgments'),
    ('acknowledgements', 'acknowledgments'),
    ('Modelling', 'Modeling'),
    ('modelling', 'modeling'),
    ('travellers', 'travelers'),
    ('travelling', 'traveling'),
    ('judgement', 'judgment'),
    ('cancelling', 'canceling'),
    ('cancelled', 'canceled'),
    ('labelled', 'labeled'),
    ('labelling', 'labeling'),
]


def apply_content_corrections(text: str) -> str:
    """Apply documented editorial and American-spelling corrections."""
    for old, new in EXACT_REPLACEMENTS:
        text = text.replace(old, new)
    for british, american in AMERICAN_SPELLINGS:
        text = re.sub(rf'\b{re.escape(british)}\b', american, text)
    return text
