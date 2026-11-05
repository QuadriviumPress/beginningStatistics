#!/usr/bin/env python3
"""Redraw source statistical diagrams as accessible SVG (standard library only).

``FIGURES`` maps a source image key (the stem of its upstream filename) to a
specification. Every curve is computed from the distribution it depicts, and
every z position is the true standard-normal value. Student t figures are
schematic, as in the source: each t value is drawn where the bell curve
encloses the same tail area as the t distribution with the stated degrees of
freedom, so shaded areas keep their meaning.

Labels use a small markup: text inside ``$...$`` is math, where letters are
italic, ``-`` is a minus sign, ``_x`` or ``_{...}`` is a subscript, and
``\\bar{x}`` and ``\\hat{p}`` are accents.

Run ``python3 scripts/render_figures.py`` to regenerate every SVG. The importer
calls ``render`` through ``figure_replacements.prepare_figures``.
"""
import hashlib
import math
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'images' / 'redrawn'

INK = '#1a1a1a'
CURVE = '#1f56a8'
FILL = '#dde2f3'
REJECT = '#d9262c'
GREEN = '#169447'
BROWN = '#a8692b'
GRAY = '#8c8c8c'
SERIF = "'STIX Two Text','Times New Roman',Times,'Liberation Serif',serif"
FONT = 30
SPAN = 3.6  # half-width of every bell-curve panel, in standard deviations


# --- distributions ---------------------------------------------------------

def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def Phi_inv(p):
    lo, hi = -10.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if Phi(mid) < p else (lo, mid)
    return (lo + hi) / 2


def betainc(a, b, x):
    """Regularized incomplete beta function I_x(a, b) (continued fraction)."""
    if x <= 0 or x >= 1:
        return 0.0 if x <= 0 else 1.0
    if x > (a + 1) / (a + b + 2):
        return 1 - betainc(b, a, 1 - x)
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                     + a * math.log(x) + b * math.log(1 - x)) / a
    c, d, f = 1.0, 0.0, 1.0
    for i in range(400):
        m = i // 2
        if i == 0:
            num = 1.0
        elif i % 2 == 0:
            num = m * (b - m) * x / ((a + 2 * m - 1) * (a + 2 * m))
        else:
            num = -(a + m) * (a + b + m) * x / ((a + 2 * m) * (a + 2 * m + 1))
        d = 1 + num * d
        d = 1 / (d if abs(d) > 1e-30 else 1e-30)
        c = 1 + num / c
        c = c if abs(c) > 1e-30 else 1e-30
        f *= c * d
        if abs(c * d - 1) < 1e-14:
            break
    return front * (f - 1)


def t_cdf(t, df):
    tail = 0.5 * betainc(df / 2, 0.5, df / (df + t * t))
    return 1 - tail if t > 0 else tail


def gammainc(a, x):
    """Regularized lower incomplete gamma function P(a, x)."""
    if x <= 0:
        return 0.0
    if x < a + 1:
        term = total = 1 / a
        for n in range(1, 500):
            term *= x / (a + n)
            total += term
            if abs(term) < abs(total) * 1e-15:
                break
        return total * math.exp(-x + a * math.log(x) - math.lgamma(a))
    b, c, d = x + 1 - a, 1e300, 1 / (x + 1 - a)
    h = d
    for i in range(1, 500):
        an = -i * (i - a)
        b += 2
        d = 1 / (an * d + b)
        c = b + an / c
        h *= d * c
        if abs(d * c - 1) < 1e-15:
            break
    return 1 - math.exp(-x + a * math.log(x) - math.lgamma(a)) * h


def chi2_cdf(x, k):
    return gammainc(k / 2, x / 2)


def f_cdf(x, d1, d2):
    return betainc(d1 / 2, d2 / 2, d1 * x / (d1 * x + d2)) if x > 0 else 0.0


def quantile(cdf, p, lo=0.0, hi=1000.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if cdf(mid) < p else (lo, mid)
    return (lo + hi) / 2


def t_position(t, df):
    """Where a t value sits on the drawn bell curve (equal tail area)."""
    return Phi_inv(t_cdf(t, df))


# --- label markup ------------------------------------------------------------

ACCENTS = {'bar': '\u0304', 'hat': '\u0302', 'tilde': '\u0303'}
GREEK = set('αβγδεθλμνπρστφχψω')


def runs(markup):
    """Split label markup into (text, italic, level) runs."""
    out = []
    for i, part in enumerate(re.split(r'\$', markup)):
        if i % 2 == 0:
            if part:
                out.append((part, False, 0))
        else:
            out.extend(math_runs(part, 0))
    return out


def math_runs(src, level):
    out, i = [], 0
    while i < len(src):
        ch = src[i]
        accent = next((a for a in ACCENTS if src.startswith(f'\\{a}{{', i)), None)
        if src.startswith('\\text{', i):
            j = src.index('}', i)
            out.append((src[i + 6:j], False, level))
            i = j + 1
        elif accent:
            j = src.index('}', i)
            out.append((src[i + len(accent) + 2:j] + ACCENTS[accent], True, level))
            i = j + 1
        elif ch in '_^':
            shift = -1 if ch == '_' else 1
            if src[i + 1] == '{':
                j, depth = i + 2, 1
                while depth:
                    depth += {'{': 1, '}': -1}.get(src[j], 0)
                    j += 1
                out.extend(math_runs(src[i + 2:j - 1], level + shift))
                i = j
            else:
                out.extend(math_runs(src[i + 1], level + shift))
                i += 2
        else:
            italic = ch.isascii() and ch.isalpha() or ch in GREEK
            out.append(({'-': '−', "'": '′'}.get(ch, ch), italic, level))
            i += 1
    return out


def merged(markup):
    out = []
    for run in runs(markup):
        if out and out[-1][1:] == run[1:]:
            out[-1] = (out[-1][0] + run[0],) + run[1:]
        else:
            out.append(run)
    return out


def width(markup, size):
    """Rough advance width of a label, for placing leaders and avoiding overlaps."""
    return sum(len(t) * size * (0.36 if level else 0.5) for t, _, level in runs(markup))


def tspans(markup, size):
    # Relative dy only, so the whole label stays one anchored text chunk.
    def offset(level):  # a subscript drops, a superscript rises
        return -level * size * (0.3 if level < 0 else 0.38)

    parts, level, previous = [], 0, ''
    for text, italic, new in merged(markup):
        attrs = ''
        if level < 0 < new:
            attrs += f' dx="{-len(previous) * size * 0.7 * 0.5:.1f}"'
        if new != level:
            attrs += f' dy="{offset(new) - offset(level):.1f}"'
            level = new
        previous = text
        attrs += f' font-size="{size * 0.7 ** abs(level):.1f}"'
        if italic:
            attrs += ' font-style="italic"'
        parts.append(f'<tspan{attrs}>{escape(text)}</tspan>')
    return ''.join(parts)


def plain(markup):
    """Text form of a label, for checking and descriptions."""
    return ''.join(t for t, _, _ in runs(markup))


# --- drawing -------------------------------------------------------------------

class Drawing:
    def __init__(self, width, height):
        self.width, self.height, self.parts = width, height, []

    def add(self, value):
        self.parts.append(value)

    def text(self, x, y, markup, size=FONT, anchor='middle', color=INK):
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="{anchor}" '
                 f'fill="{color}" xml:space="preserve">{tspans(markup, size)}</text>')

    def vtext(self, x, y, markup, size=FONT, color=INK):
        """Text rotated to read upward, centered on (x, y)."""
        self.add(f'<text transform="translate({x:.1f},{y:.1f}) rotate(-90)" font-size="{size}" '
                 f'text-anchor="middle" fill="{color}" xml:space="preserve">{tspans(markup, size)}</text>')

    def rect(self, x, y, w, h, stroke=INK, fill='none', width=1.6):
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{width}"/>')

    def circle(self, x, y, r, fill=INK, stroke='none', width=0):
        self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')

    def line(self, x1, y1, x2, y2, color=INK, width=1.6, dash=None):
        extra = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                 f'stroke="{color}" stroke-width="{width}"{extra}/>')

    def path(self, d, fill='none', stroke='none', width=0):
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round"/>')

    def star(self, x, y, r=11):
        pts = []
        for k in range(10):
            rad = r if k % 2 == 0 else r * 0.42
            ang = math.pi / 2 + k * math.pi / 5
            pts.append(f'{x + rad * math.cos(ang):.1f},{y - rad * math.sin(ang):.1f}')
        self.add(f'<polygon points="{" ".join(pts)}" fill="{INK}"/>')

    def svg(self, title, desc):
        return '\n'.join([
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'role="img" aria-labelledby="title desc" font-family="{SERIF}">',
            f'<title id="title">{escape(title)}</title>',
            f'<desc id="desc">{escape(desc)}</desc>',
            f'<rect width="{self.width}" height="{self.height}" fill="#fff"/>',
            *self.parts, '</svg>', ''])


class Bell:
    """A bell-curve panel; x positions are in standard deviations."""

    def __init__(self, d, left, top, width, height):
        self.d, self.left, self.width = d, left, width
        self.base, self.height = top + height, height

    def X(self, z):
        return self.left + (z + SPAN) / (2 * SPAN) * self.width

    def Y(self, z):
        return self.base - phi(z) / phi(0) * self.height

    def curve_points(self, a, b, n=160):
        return [(self.X(a + (b - a) * k / n), self.Y(a + (b - a) * k / n)) for k in range(n + 1)]

    def level(self, frac):
        """Height above the axis, as a fraction of the curve's peak height."""
        return self.base - frac * self.height

    def draw(self, var, center_label=None, dashed=True, size=FONT):
        d = self.d
        d.line(self.left, self.base, self.left + self.width, self.base)
        if var:
            d.text(self.left + self.width + 14, self.base + 8, f'${var}$', size, 'start')
        if dashed:
            d.line(self.X(0), self.Y(0), self.X(0), self.base, dash='9 8')
        if center_label:
            d.text(self.X(0), self.base + 38, center_label, size)

    def shade(self, side, z):
        a, b = (-SPAN, z) if side == 'L' else (z, SPAN)
        self.shade_between(a, b, edges=[z])

    def shade_between(self, a, b, edges=None):
        """Shade under the curve from a to b; None means the panel edge."""
        a, b = -SPAN if a is None else a, SPAN if b is None else b
        pts = self.curve_points(a, b)
        d = f'M{pts[0][0]:.1f},{self.base:.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts)
        self.d.path(d + f' L{pts[-1][0]:.1f},{self.base:.1f} Z', fill=FILL)
        for z in (edges if edges is not None else [v for v in (a, b) if abs(v) < SPAN]):
            self.d.line(self.X(z), self.Y(z), self.X(z), self.base, CURVE, 1.6)

    def dashed(self, z):
        self.d.line(self.X(z), self.Y(z), self.X(z), self.base, dash='9 8')

    def table_bracket(self, z, to, level, label, size=FONT, foot=None, gap=14):
        """Riser at z, then an arrow to the panel edge: the area to that side of z."""
        x, y = self.X(z), self.level(level)
        end = self.left if to == 'L' else self.left + self.width
        self.d.line(x, self.Y(z) - gap if foot is None else self.level(foot), x, y)
        self.d.line(x, y, end, y)
        arrowhead(self.d, end, y, math.pi if to == 'L' else 0)
        self.label_over(min(x, end), max(x, end), y, label, size)

    def span_bracket(self, z1, z2, level, label, size=FONT, arrows=False, foot=None):
        """A bracket over the curve from z1 to z2, with optional down arrows at its feet."""
        y = self.level(level)
        for z in (z1, z2):
            foot_y = self.Y(z) - 14 if foot is None else self.level(foot)
            self.d.line(self.X(z), y, self.X(z), foot_y)
            if arrows:
                arrowhead(self.d, self.X(z), foot_y, math.pi / 2)
        self.d.line(self.X(z1), y, self.X(z2), y)
        self.label_over(self.X(z1), self.X(z2), y, label, size)

    def label_over(self, x1, x2, y, label, size=FONT, anchor='middle'):
        lines = label if isinstance(label, list) else [label]
        w = max(width(t, size) for t in lines)
        cx = min(max((x1 + x2) / 2, self.left + w / 2), self.d.width - 12 - w / 2)
        for i, t in enumerate(reversed(lines)):
            self.d.text(cx, y - 14 - i * size * 1.15, t, size)

    def leader(self, markup, lz, level, tz, size=FONT, arrow=True, depth=0.45):
        """A label at (lz, level) with an arrow into the shaded area at tz."""
        x, y = self.X(lz), self.level(level)
        self.d.text(x, y, markup, size)
        ty = self.base - phi(tz) / phi(0) * self.height * depth
        sx = x + (self.X(tz) - x) * 0.25
        leader(self.d, sx, y + 14, self.X(tz), ty, arrow)

    def stroke(self):
        pts = self.curve_points(-SPAN, SPAN, 240)
        self.d.path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts), stroke=CURVE, width=4.5)

    def tail_label(self, side, z, markup, size=FONT, lift=0.42):
        """Label above a shaded tail, kept inside the panel, with a leader into the tail."""
        sign = 1 if side == 'R' else -1
        inner = z + sign * min(0.45, max(0.12, (SPAN - abs(z)) / 3))
        tx, ty = self.X(inner), self.base - phi(inner) / phi(0) * self.height * 0.4
        w = width(markup, size)
        edge = self.left + self.width if side == 'R' else self.left
        # Sit just outside the curve near the critical value, but never past the panel edge.
        x = self.X(z + sign * 0.55) + sign * w / 2
        x = min(x, edge - w / 2) if side == 'R' else max(x, edge + w / 2)
        ly = self.base - self.height * lift
        self.d.text(x, ly - 12, markup, size)
        self.d.line(x - sign * w * 0.2, ly, tx, ty, INK, 1.4)


def number_line(d, bell, y, var, bars, ticks, size=FONT, floor=None):
    """Second axis with red rejection intervals closed at the critical values."""
    left, right = bell.left, bell.left + bell.width
    lo = left if floor is None else bell.X(floor)
    d.line(left, y, right, y, INK, 1.6)
    d.text(right + 14, y + 8, f'${var}$', size, 'start')
    for side, z in bars:
        x = bell.X(z)
        a, b = (lo, x) if side == 'L' else (x, right)
        d.line(a, y, b, y, REJECT, 9)
        hook = -12 if side == 'L' else 12
        d.path(f'M{x + hook:.1f},{y - 16} H{x:.1f} V{y + 16} H{x + hook:.1f}', stroke=REJECT, width=1.8)
    for z in ticks:
        d.line(bell.X(z), y - 8, bell.X(z), y + 8, INK, 1.6)


def reject_label(d, bell, side, y, size=FONT, crit=None, avoid=None):
    """'Reject H0' under a bar's outer end, moved aside if it would cross the statistic's tick."""
    label = 'Reject $H_0$'
    w = width(label, size)
    left, right = bell.left, bell.left + bell.width
    if side == 'L':
        candidates = [left + 6, bell.X(crit) - 6 - w] if crit is not None else [left + 6]
        if avoid is not None:
            candidates += [avoid - 16 - w, avoid + 16]
        lo, hi = left, d.width - 10
    else:
        candidates = [right - 6 - w]
        if avoid is not None:
            candidates += [avoid + 16, avoid - 16 - w]
        lo, hi = (bell.X(crit) + 4 if crit is not None else left), d.width - 10
    for x0 in candidates:
        clear = avoid is None or not (x0 - 14 < avoid < x0 + w + 14)
        if clear and lo <= x0 and x0 + w <= hi:
            break
    else:
        x0 = candidates[0]
    d.text(x0, y, label, size, 'start', color=REJECT)


def arrowhead(d, x, y, angle, size=18, color=INK, width=1.6):
    """Open arrowhead with its tip at (x, y), pointing along angle (radians, y down)."""
    for s in (-1, 1):
        a = angle + math.pi + s * 0.42
        d.line(x, y, x + size * math.cos(a), y + size * math.sin(a), color, width)


def leader(d, x1, y1, x2, y2, arrow=False, color=INK):
    d.line(x1, y1, x2, y2, color, 1.4)
    if arrow:
        arrowhead(d, x2, y2, math.atan2(y2 - y1, x2 - x1), 15, color, 1.4)


class Axes:
    """A plot with data coordinates; y runs from 0 at the axis to ymax at the top."""

    def __init__(self, d, left, top, width, height, x0, x1, ymax):
        self.d, self.left, self.top, self.width, self.height = d, left, top, width, height
        self.x0, self.x1, self.ymax, self.base = x0, x1, ymax, top + height

    def X(self, x):
        return self.left + (x - self.x0) / (self.x1 - self.x0) * self.width

    def Y(self, y):
        return self.base - y / self.ymax * self.height

    def points(self, f, a, b, n=240):
        return [(self.X(a + (b - a) * k / n), self.Y(f(a + (b - a) * k / n))) for k in range(n + 1)]

    def curve(self, f, a=None, b=None, color=CURVE, width=4.5):
        pts = self.points(f, self.x0 if a is None else a, self.x1 if b is None else b)
        self.d.path('M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts), stroke=color, width=width)

    def shade(self, f, a, b, edges=True):
        pts = self.points(f, a, b, 120)
        path = f'M{pts[0][0]:.1f},{self.base:.1f} ' + ' '.join(f'L{x:.1f},{y:.1f}' for x, y in pts)
        self.d.path(path + f' L{pts[-1][0]:.1f},{self.base:.1f} Z', fill=FILL)
        if edges:
            for x in (a, b):
                self.d.line(self.X(x), self.Y(f(x)), self.X(x), self.base, CURVE, 1.6)

    def axis(self, var=None, size=FONT, extra=0):
        self.d.line(self.left - extra, self.base, self.left + self.width + extra, self.base)
        if var:
            self.d.text(self.left + self.width + extra + 14, self.base + 8, f'${var}$', size, 'start')

    def dashed(self, x, top):
        self.d.line(self.X(x), self.Y(top), self.X(x), self.base, dash='9 8')


def normal(mu, sigma):
    return lambda x: phi((x - mu) / sigma) / sigma


def t_pdf(df):
    c = math.exp(math.lgamma((df + 1) / 2) - math.lgamma(df / 2)) / math.sqrt(df * math.pi)
    return lambda t: c * (1 + t * t / df) ** (-(df + 1) / 2)


def gamma_pdf(k, theta=1.0):
    c = 1 / (math.gamma(k) * theta ** k)
    return lambda x: c * x ** (k - 1) * math.exp(-x / theta) if x > 0 else 0.0


def uniform_panel(d, left, top, w, h, b, height_label, labels, shade=None, dashed=(), size=FONT, fx=None):
    """Density of the uniform distribution on [0, b]: a flat top, zero elsewhere."""
    ax = Axes(d, left, top, w, h, -0.12 * b, 1.12 * b, 1.18)
    ax.axis()
    x0, xb, base, ytop = ax.X(0), ax.X(b), ax.base, ax.Y(1)
    d.line(x0, base + 0.12 * h, x0, top, INK, 1.6)
    if shade:
        a, c = shade
        d.add(f'<rect x="{ax.X(a):.1f}" y="{ytop:.1f}" width="{ax.X(c) - ax.X(a):.1f}" height="{base - ytop:.1f}" fill="{FILL}"/>')
    for x in (*dashed, b):
        d.line(ax.X(x), ytop, ax.X(x), base, INK, 1.6, '9 8' if size > 20 else '5 5')
    stroke = 6 if size > 20 else 3.5
    d.line(x0, ytop, xb, ytop, CURVE, stroke)
    d.line(ax.left - 0.4 * size, base, x0, base, CURVE, stroke)
    d.line(xb, base, ax.left + w + 0.4 * size, base, CURVE, stroke)
    r = size * 0.32
    for x in (x0, xb):
        d.add(f'<circle cx="{x:.1f}" cy="{base:.1f}" r="{r:.1f}" fill="#fff" stroke="{CURVE}" stroke-width="{stroke * 0.8:.1f}"/>')
    d.text(x0 - size * 0.45, ytop + size * 0.35, height_label, size, 'end')
    for x, label in labels:
        d.text(ax.X(x) - (size * 0.45 if x == 0 else 0), base + size * 1.4, label, size, 'end' if x == 0 else 'middle')
    if fx:
        d.text(left + w, top + size, fx, size, 'end')
    return ax


def bell_figure(spec):
    """A normal curve with shading, labels, a second axis, and area brackets."""
    W, Hc, size = spec.get('width', 1000), 300, spec.get('size', FONT)
    levels = [1.0] + [b[3] if b[0] == 'table' else b[3] for b in spec.get('brackets', [])]
    lines = max([1] + [len(b[4]) if isinstance(b[4], list) else 1 for b in spec.get('brackets', [])])
    top = 20 + (max(levels) - 1) * Hc + (lines * size * 1.15 + 20 if spec.get('brackets') else 0)
    top += spec.get('extra_top', 0)
    base = top + Hc
    H = base + 60 + (80 if 'zaxis' in spec else 0)
    d = Drawing(W, round(H))
    left = spec.get('left', 30)
    bell = Bell(d, left, top, W - left - 70, Hc)
    for a, b in spec.get('shade', []):
        bell.shade_between(a, b)
    bell.stroke()
    bell.draw(spec.get('var'), dashed=False, size=size)
    for z in spec.get('dashed', [0]):
        bell.dashed(z)
    for z in spec.get('ticks', []):
        d.line(bell.X(z), bell.base, bell.X(z), bell.base - 10)
    for z, label in spec.get('labels', []):
        d.text(bell.X(z), bell.base + 40, label, size)
    if 'zaxis' in spec:
        y = bell.base + 85
        d.line(bell.left, y, bell.left + bell.width, y)
        d.text(bell.left + bell.width + 14, y + 8, '$z$', size, 'start')
        for z, label in spec['zaxis']:
            d.line(bell.X(z), y - 8, bell.X(z), y + 8)
            d.text(bell.X(z), y + 40, label, size)
    for b in spec.get('brackets', []):
        if b[0] == 'table':
            bell.table_bracket(*b[1:5], size, *b[5:])
        else:
            bell.span_bracket(*b[1:5], size, *b[5:])
    for item in spec.get('leaders', []):
        bell.leader(*item, size=size)
    for side, z, label in spec.get('tail_labels', []):
        bell.tail_label(side, z, label, size)
    for z, level, label in spec.get('texts', []):
        d.text(bell.X(z), bell.level(level), label, size)
    return d


# --- figure kinds ----------------------------------------------------------------

def single_test(spec):
    """One alternative: shaded tail(s), axis labels, rejection line, test statistic."""
    W = 1000
    has_line = 'bars' in spec
    H = 640 if has_line else 500
    if spec.get('stat_label_row'):
        H += 40
    top = 80 if spec['title'] else 20
    d = Drawing(W, H - (80 - top))
    bell = Bell(d, 30, top, 900, 300)
    if spec['title']:
        d.text(500, 48, spec['title'])
    for side, z in spec.get('tails', []):
        bell.shade(side, z)
    bell.stroke()
    bell.draw(spec['var'])
    for side, z, label in spec.get('tail_labels', []):
        bell.tail_label(side, z, label)
    for z, label, *anchor in spec['axis_labels']:
        d.text(bell.X(z), bell.base + 40, label, anchor=anchor[0] if anchor else 'middle')
    y = bell.base + 100
    if has_line:
        number_line(d, bell, y, spec['var'], spec['bars'], spec.get('line_ticks', [0]))
        for z, label in spec.get('line_labels', []):
            d.text(bell.X(z), y + 44, label)
        row = y + 44 if not spec.get('stat_label_row') else y + 84
        avoid = bell.X(spec['stat'][0]) if 'stat' in spec and not spec.get('stat_label_row') else None
        for side, z in spec['bars']:
            reject_label(d, bell, side, row, FONT, z, avoid)
    if 'stat' in spec:
        z, label = spec['stat']
        if has_line:
            d.star(bell.X(z), y)
            d.line(bell.X(z), y + 16, bell.X(z), y + 46, INK, 1.6)
            d.text(bell.X(z), y + 82, label)
        else:
            d.star(bell.X(z), bell.base)
            d.text(bell.X(z), bell.base + 40, label)
    return d


def three_forms(spec):
    """Left-, right-, and two-tailed rejection regions for one test (three panels)."""
    W, H = 1100, 800
    d = Drawing(W, H)
    size = 26
    v, crit = spec['var'], spec['crit']
    one, two = 1.645, 1.96
    panels = [
        (20, 60, '<', [('L', -one)]),
        (580, 60, '>', [('R', one)]),
        (300, 440, '≠', [('L', -two), ('R', two)]),
    ]
    for left, top, op, tails in panels:
        bell = Bell(d, left, top + 30, 470, 170)
        d.text(left + 235, top + 8, f'$H_a : {spec["param"]} {op} {spec["param"]}_0$', size)
        for side, z in tails:
            bell.shade(side, z)
        bell.stroke()
        bell.draw(v)
        two_sided = len(tails) == 2
        area = 'α/2' if two_sided else 'α'
        for side, z in tails:
            bell.tail_label(side, z, f'${area}$', size, lift=0.55)
            d.text(bell.X(z), bell.base + 34, crit[(side, two_sided)], size)
        d.text(bell.X(0), bell.base + 34, spec['center'], size)
        y = bell.base + 78
        number_line(d, bell, y, v, tails, [0], size)
        d.text(bell.X(0), y + 38, spec['center'], size)
        for side, _ in tails:
            reject_label(d, bell, side, y + 38, size)
    return d


KINDS = {'single': single_test, 'three': three_forms, 'bell': bell_figure,
         'draw': lambda spec: spec['draw']()}


# --- the figures ----------------------------------------------------------------

def _forms(param, var, center, lo, hi, lo2, hi2):
    return {'kind': 'three', 'param': param, 'var': var, 'center': center,
            'crit': {('L', False): lo, ('R', False): hi, ('L', True): lo2, ('R', True): hi2}}


T4 = t_position(2.132, 4)
T3 = t_position(5.841, 3)

FIGURES = {
    'b91b73d0dbbd53dc069a390a463118a2': {
        'file': 'fig-08-01.svg', 'title': 'Figure 8.1 The density curve for X̄ if H₀ is true',
        'alt': 'A bell-shaped normal density curve for the sample mean, drawn over the x̄ axis and centered at μ₀, '
               'with a dashed vertical line at the center.',
        'kind': 'single', 'title_markup': '', 'var': '\\bar{x}', 'axis_labels': [(0, '$μ_0$')]},
    '72f0cd42fda04cdfb0341bcfe11601c1': {
        'file': 'fig-08-02.svg', 'title': 'Figure 8.2 Rejection regions for the three forms of the alternative hypothesis',
        'alt': 'Three normal curves for the sample mean, each centered at μ₀ on the x̄ axis. For Hₐ: μ < μ₀, the left tail of '
               'area α below the critical value C is shaded, and the rejection region below it is the interval to the left of C. '
               'For Hₐ: μ > μ₀, the right tail of area α above the critical value C′ is shaded, and the rejection region is '
               'the interval to the right of C′. For Hₐ: μ ≠ μ₀, both tails, each of area α/2, are shaded beyond C and C′, '
               'and the rejection region is both outer intervals.',
        **_forms('μ', '\\bar{x}', '$μ_0$', '$C$', "$C'$", '$C$', "$C'$")},
    '6ed58a35480090fa999b53b443a266a5': {
        'file': 'fig-08-03.svg', 'title': 'Figure 8.3 Rejection region for the choice α = 0.10',
        'alt': 'Normal curve for the sample mean, centered at 8.0, for Hₐ: μ ≠ 8.0. Both tails, each of area α/2 = 0.05, are '
               'shaded beyond the critical values 7.89 and 8.11. A number line below marks the rejection region in red: '
               'x̄ ≤ 7.89 and x̄ ≥ 8.11.',
        'kind': 'single', 'title_markup': '$H_a : μ ≠ 8.0$', 'var': '\\bar{x}',
        'tails': [('L', -1.645), ('R', 1.645)],
        'tail_labels': [('L', -1.645, '$α/2 = 0.05$'), ('R', 1.645, '$α/2 = 0.05$')],
        'axis_labels': [(-1.645, '7.89'), (0, '8.0'), (1.645, '8.11')],
        'bars': [('L', -1.645), ('R', 1.645)], 'line_ticks': [0],
        'line_labels': [(-1.645, '7.89'), (0, '8.0'), (1.645, '8.11')], 'stat_label_row': True},
    '526c9e81a596b999ae191031b1b8bc47': {
        'file': 'fig-08-04.svg', 'title': 'Figure 8.4 Distribution of the standardized test statistic and the rejection region',
        'alt': 'Three standard normal curves on the z axis, centered at 0. For Hₐ: μ < μ₀, the left tail of area α below −z_α '
               'is shaded and the rejection region is z ≤ −z_α. For Hₐ: μ > μ₀, the right tail of area α above z_α is shaded '
               'and the rejection region is z ≥ z_α. For Hₐ: μ ≠ μ₀, both tails of area α/2 beyond −z_α/2 and z_α/2 are '
               'shaded and the rejection region is both outer intervals.',
        **_forms('μ', 'z', '0', '$-z_α$', '$z_α$', '$-z_{α/2}$', '$z_{α/2}$')},
    'c18d107b4145b363951540fc519137b2': {
        'file': 'fig-08-05.svg', 'title': 'Figure 8.5 Rejection region and test statistic for Example 4',
        'alt': 'Standard normal curve for Hₐ: μ < 3.5. The left tail of area α = 0.05 is shaded below the critical value '
               '−z_α = −1.645. On the number line below, the rejection region z ≤ −1.645 is red, and the test statistic '
               'Z = −1.886, marked with a star, lies inside it.',
        'kind': 'single', 'title_markup': '$H_a : μ < 3.5$', 'var': 'z',
        'tails': [('L', -1.645)], 'tail_labels': [('L', -1.645, '$α = 0.05$')],
        'axis_labels': [(-1.645, '$-z_α = -1.645$'), (0, '0')],
        'bars': [('L', -1.645)], 'line_labels': [(0, '0')], 'stat': (-1.886, '$Z = -1.886$')},
    '98f4ee32ab4fe3e9766adeca42e127e9': {
        'file': 'fig-08-06.svg', 'title': 'Figure 8.6 Rejection region and test statistic for Example 5',
        'alt': 'Standard normal curve for Hₐ: μ ≠ 8.1. Both tails, each of area α/2 = 0.005, are shaded beyond the critical '
               'values −z_α/2 = −2.576 and z_α/2 = 2.576. On the number line below, the two rejection intervals are red, and '
               'the test statistic Z = 2.49, marked with a star, lies between 0 and 2.576, outside the rejection region.',
        'kind': 'single', 'title_markup': '$H_a : μ ≠ 8.1$', 'var': 'z',
        'tails': [('L', -2.576), ('R', 2.576)],
        'tail_labels': [('L', -2.576, '$α/2 = 0.005$'), ('R', 2.576, '$α/2 = 0.005$')],
        'axis_labels': [(-2.576, '$-z_{α/2} = -2.576$'), (0, '0'), (2.576, '$z_{α/2} = 2.576$')],
        'bars': [('L', -2.576), ('R', 2.576)], 'line_labels': [(0, '0')], 'stat': (2.49, '$Z = 2.49$')},
    '34d69a9504c62766c5a75e20cad436e5': {
        'file': 'fig-08-07.svg', 'title': 'Figure 8.7 Area of the tail for Example 6',
        'alt': 'Standard normal curve for Hₐ: μ ≠ 8.1, with the test statistic Z = 2.49 starred on the z axis. The right tail '
               'beyond it is shaded and labeled area = 0.0064.',
        'kind': 'single', 'title_markup': '$H_a : μ ≠ 8.1$', 'var': 'z',
        'tails': [('R', 2.49)], 'tail_labels': [('R', 2.49, 'area = 0.0064')],
        'axis_labels': [(0, '0')], 'stat': (2.49, '$Z = 2.49$')},
    '6c41ed97cffe263a3c04b5f649f640d7': {
        'file': 'fig-08-08.svg', 'title': 'Figure 8.8 Test statistic for Example 7',
        'alt': 'Standard normal curve for Hₐ: μ < 202.5, with the test statistic Z = −1.55 starred on the z axis. The left tail '
               'below it is shaded and labeled area = 0.0606.',
        'kind': 'single', 'title_markup': '$H_a : μ < 202.5$', 'var': 'z',
        'tails': [('L', -1.55)], 'tail_labels': [('L', -1.55, 'area = 0.0606')],
        'axis_labels': [(0, '0')], 'stat': (-1.55, '$Z = -1.55$')},
    'f1c4577bbb5541d6829e57597570bc47': {
        'file': 'fig-08-09.svg', 'title': 'Figure 8.9 Test statistic for Example 8',
        'alt': 'Standard normal curve for Hₐ: μ > 67, with the test statistic Z = 3.15 starred on the z axis. The right tail '
               'beyond it is shaded and labeled area = 0.0008.',
        'kind': 'single', 'title_markup': '$H_a : μ > 67$', 'var': 'z',
        'tails': [('R', 3.15)], 'tail_labels': [('R', 3.15, 'area = 0.0008')],
        'axis_labels': [(0, '0')], 'stat': (3.15, '$Z = 3.15$')},
    'd3f75c51124aea89828bc106da10a29c': {
        'file': 'fig-08-10.svg', 'title': 'Figure 8.10 Test statistic for Example 9',
        'alt': 'Standard normal curve for Hₐ: μ ≠ 7.4, with the test statistic Z = 3.29 starred on the z axis. The right tail '
               'beyond it is shaded and labeled area = 0.0005.',
        'kind': 'single', 'title_markup': '$H_a : μ ≠ 7.4$', 'var': 'z',
        'tails': [('R', 3.29)], 'tail_labels': [('R', 3.29, 'area = 0.0005')],
        'axis_labels': [(0, '0')], 'stat': (3.29, '$Z = 3.29$')},
    'ecf5f771ca148089665859c88d8679df': {
        'file': 'fig-08-11.svg', 'title': 'Figure 8.11 Distribution of the standardized test statistic and the rejection region',
        'alt': 'Three bell-shaped Student t curves on the t axis, centered at 0. For Hₐ: μ < μ₀, the left tail of area α below '
               '−t_α is shaded and the rejection region is t ≤ −t_α. For Hₐ: μ > μ₀, the right tail of area α above t_α is '
               'shaded and the rejection region is t ≥ t_α. For Hₐ: μ ≠ μ₀, both tails of area α/2 beyond −t_α/2 and t_α/2 '
               'are shaded and the rejection region is both outer intervals.',
        **_forms('μ', 't', '0', '$-t_α$', '$t_α$', '$-t_{α/2}$', '$t_{α/2}$')},
    '37a4f201cad923d15a8bfab828bd7640': {
        'file': 'fig-08-12.svg', 'title': 'Figure 8.12 Rejection region and test statistic for Example 10',
        'alt': 'Student t curve with 4 degrees of freedom for Hₐ: μ < 179. The left tail of area α = 0.05 is shaded below the '
               'critical value −t_α = −2.132. On the number line below, the rejection region t ≤ −2.132 is red, and the test '
               'statistic T = −2.152, marked with a star, lies just inside it.',
        'kind': 'single', 'title_markup': '$H_a : μ < 179$', 'var': 't',
        'tails': [('L', -T4)], 'tail_labels': [('L', -T4, '$α = 0.05$')],
        'axis_labels': [(-T4, '$-t_α = -2.132$'), (0, '0')],
        'bars': [('L', -T4)], 'line_labels': [(0, '0')], 'stat': (t_position(-2.152, 4), '$T = -2.152$')},
    'ac90ded7d10c3b0d2ccfb5daea47745f': {
        'file': 'fig-08-13.svg', 'title': 'Figure 8.13 Rejection region and test statistic for Example 11',
        'alt': 'Student t curve with 3 degrees of freedom for Hₐ: μ ≠ 0.02. Both tails, each of area α/2 = 0.005, are shaded '
               'beyond the critical values −t_α/2 = −5.841 and t_α/2 = 5.841. On the number line below, the two rejection '
               'intervals are red, and the test statistic T = 0.877, marked with a star, lies near the center, outside the '
               'rejection region.',
        'kind': 'single', 'title_markup': '$H_a : μ ≠ 0.02$', 'var': 't',
        'tails': [('L', -T3), ('R', T3)],
        'tail_labels': [('L', -T3, '$α/2 = 0.005$'), ('R', T3, '$α/2 = 0.005$')],
        'axis_labels': [(-T3, '$-t_{α/2} = -5.841$'), (0, '0'), (T3, '$t_{α/2} = 5.841$')],
        'bars': [('L', -T3), ('R', T3)], 'line_labels': [(0, '0')], 'stat': (t_position(0.877, 3), '$T = 0.877$')},
    '01fe19537789cf83979f79f172b522c5': {
        'file': 'fig-08-14.svg', 'title': 'Figure 8.14 Distribution of the standardized test statistic and the rejection region',
        'alt': 'Three standard normal curves on the z axis, centered at 0, for tests about a population proportion. For '
               'Hₐ: p < p₀, the left tail of area α below −z_α is shaded and the rejection region is z ≤ −z_α. For '
               'Hₐ: p > p₀, the right tail of area α above z_α is shaded and the rejection region is z ≥ z_α. For '
               'Hₐ: p ≠ p₀, both tails of area α/2 beyond −z_α/2 and z_α/2 are shaded and the rejection region is both '
               'outer intervals.',
        **_forms('p', 'z', '0', '$-z_α$', '$z_α$', '$-z_{α/2}$', '$z_{α/2}$')},
    'e667418a241c22871b5d19c2938793f4': {
        'file': 'fig-08-15.svg', 'title': 'Figure 8.15 Rejection region and test statistic for Example 12',
        'alt': 'Standard normal curve for Hₐ: p > 0.5. The right tail of area α = 0.05 is shaded above the critical value '
               'z_α = 1.645. On the number line below, the rejection region z ≥ 1.645 is red, and the test statistic '
               'Z = 1.789, marked with a star, lies inside it.',
        'kind': 'single', 'title_markup': '$H_a : p > 0.5$', 'var': 'z',
        'tails': [('R', 1.645)], 'tail_labels': [('R', 1.645, '$α = 0.05$')],
        'axis_labels': [(0, '0'), (1.645, '$z_α = 1.645$')],
        'bars': [('R', 1.645)], 'line_labels': [(0, '0')], 'stat': (1.789, '$Z = 1.789$')},
    '22cd2e9cac5d9dac6cd8ee19078f74cb': {
        'file': 'fig-08-16.svg', 'title': 'Figure 8.16 Rejection region and test statistic for Example 13',
        # Source error corrected: the example tests at α = 0.10, so each tail is
        # α/2 = 0.05 (the source figure printed 0.005). See SOURCES.md.
        'alt': 'Standard normal curve for Hₐ: p ≠ 0.5146. Both tails, each of area α/2 = 0.05, are shaded beyond the '
               'critical values −z_α/2 = −1.645 and z_α/2 = 1.645. On the number line below, the two rejection intervals '
               'are red, and the test statistic Z = 1.542, marked with a star, lies just short of 1.645, outside the '
               'rejection region.',
        'kind': 'single', 'title_markup': '$H_a : p ≠ 0.5146$', 'var': 'z',
        'tails': [('L', -1.645), ('R', 1.645)],
        'tail_labels': [('L', -1.645, '$α/2 = 0.05$'), ('R', 1.645, '$α/2 = 0.05$')],
        'axis_labels': [(-1.645, '$-z_{α/2} = -1.645$'), (0, '0'), (1.645, '$z_{α/2} = 1.645$')],
        'bars': [('L', -1.645), ('R', 1.645)], 'line_labels': [(0, '0')], 'stat': (1.542, '$Z = 1.542$')},
    '53ce189932428f408b5b4f0cfa1b7a28': {
        'file': 'fig-08-17.svg', 'title': 'Figure 8.17 P-value for Example 14',
        'alt': 'Standard normal curve for Hₐ: p > 0.5, with the test statistic Z = 1.789 starred on the z axis. The right tail '
               'beyond it is shaded and labeled area = 0.0367.',
        'kind': 'single', 'title_markup': '$H_a : p > 0.5$', 'var': 'z',
        'tails': [('R', 1.789)], 'tail_labels': [('R', 1.789, 'area = 0.0367')],
        'axis_labels': [(0, '0')], 'stat': (1.789, '$Z = 1.789$')},
    '65a0c37cb34d23ad1f8d640e3442bf18': {
        'file': 'fig-08-18.svg', 'title': 'Figure 8.18 P-value for Example 15',
        'alt': 'Standard normal curve for Hₐ: p ≠ 0.5146, with the test statistic Z = 1.542 starred on the z axis. The right '
               'tail beyond it is shaded and labeled area = 0.0618.',
        'kind': 'single', 'title_markup': '$H_a : p ≠ 0.5146$', 'var': 'z',
        'tails': [('R', 1.542)], 'tail_labels': [('R', 1.542, 'area = 0.0618')],
        'axis_labels': [(0, '0')], 'stat': (1.542, '$Z = 1.542$')},
}


# --- batch 1: Chapters 5, 7, 9, and 10 ---------------------------------------------

def fig_5_01():
    d = Drawing(1000, 520)
    f = lambda x: 0.54 * phi((x + 0.41) / 0.32) / 0.32 + 0.46 * phi((x - 0.86) / 0.42) / 0.42
    ax = Axes(d, 30, 100, 900, 350, -2.6, 2.9, f(-0.42) * 1.02)
    ax.shade(f, -0.78, 1.46)
    ax.curve(f)
    ax.axis()
    d.text(ax.X(-0.78), ax.base + 42, '$a$')
    d.text(ax.X(1.46), ax.base + 42, '$b$')
    d.text(40, 50, '$P(a < X < b)$ = area of shaded region', anchor='start')
    d.text(ax.X(1.35), ax.Y(f(-0.42) * 0.78), '$y = f(x)$')
    return d


def fig_5_02():
    d = Drawing(1000, 560)
    uniform_panel(d, 170, 40, 640, 430, 1, '1', [(0, '0'), (1, '1')], fx='$y = f(x)$')
    return d


def fig_5_03():
    d = Drawing(1100, 330)
    panels = [((0.75, 1), (0.75,), [(0, '0'), (0.75, '0.75'), (1, '1')]),
              ((0, 0.2), (0.2,), [(0, '0'), (0.2, '0.2'), (1, '1')]),
              ((0.4, 0.7), (0.4, 0.7), [(0, '0'), (0.4, '0.4'), (0.7, '0.7'), (1, '1')])]
    for i, (shade, dashed, labels) in enumerate(panels):
        left = 60 + i * 360
        uniform_panel(d, left, 30, 280, 210, 1, '1', labels, shade, dashed, size=22)
        d.text(left + 140, 312, f'({"abc"[i]})', 24)
    return d


def fig_5_04():
    d = Drawing(1000, 430)
    uniform_panel(d, 130, 30, 740, 320, 30, '1/30', [(0, '0'), (10, '10'), (30, '30')], (0, 10), (10,))
    return d


def fig_5_05():
    d = Drawing(1000, 520)
    ax = Axes(d, 30, 80, 900, 370, -2.9, 1.9, 1.62)
    for mu, color in ((-2, REJECT), (-1, CURVE), (1, GREEN)):
        f = normal(mu, 0.25)
        ax.curve(f, max(ax.x0, mu - 1.5), min(ax.x1, mu + 1.5), color)
        ax.dashed(mu, f(mu))
        d.text(ax.X(mu), 56, f'$μ = {mu}$')
        d.text(ax.X(mu), ax.base + 42, f'${mu}$')
    ax.axis()
    return d


def fig_5_06():
    d = Drawing(1000, 540)
    ax = Axes(d, 30, 30, 900, 430, 0.6, 11.4, 0.82)
    curves = ((2, GREEN, 9.6, 0.30, 8.9), (1, CURVE, 8.7, 0.47, 7.25), (0.5, REJECT, 8.1, 0.72, 6.55))
    for sigma, color, *_ in curves:
        ax.curve(normal(6, sigma), max(ax.x0, 6 - 5 * sigma), min(ax.x1, 6 + 5 * sigma), color)
    ax.dashed(6, normal(6, 0.5)(6))
    ax.axis()
    for sigma, color, lx, ly, tx in curves:
        d.text(ax.X(lx) + 20, ax.Y(ly), f'$σ = {sigma}$')
        leader(d, ax.X(lx) - 10, ax.Y(ly) + 10, ax.X(tx) + 8, ax.Y(normal(6, sigma)(tx)) + 4, True)
    d.text(ax.X(6), ax.base + 44, '$μ = 6$')
    return d


def fig_5_10():
    d = Drawing(1100, 430)
    size = 24
    # Excerpt of the cumulative table: row 1.4, column 0.08.
    d.path('M20,78 H130 l6,-10 l8,20 l6,-10 H470', stroke=INK, width=2.5)
    d.path('M75,20 V130 l-10,6 l20,8 l-10,6 V410', stroke=INK, width=2.5)
    for x in (325, 405):
        d.line(x, 20, x, 410, CURVE, 1.2)
    for y in (250, 292):
        d.line(20, y, 470, y, CURVE, 1.2)
    for x, y, t in ((270, 60, '⋯'), (365, 60, '0.08'), (440, 60, '⋯'), (45, 200, '⋮'), (365, 200, '⋮'),
                    (45, 280, '1.4'), (270, 280, '⋯'), (365, 280, '0.9306'), (440, 280, '⋯'),
                    (45, 365, '⋮'), (365, 365, '⋮')):
        d.text(x, y, t, size)
    bell = Bell(d, 560, 150, 470, 220)
    bell.shade_between(None, 1.48)
    bell.stroke()
    bell.draw(None, dashed=False)
    d.text(bell.X(0), bell.base + 34, '0', size)
    d.text(bell.X(1.48), bell.base + 34, '1.48', size)
    bell.table_bracket(1.48, 'L', 1.32, 'area of the shaded region = 0.9306', 22)
    return d


def fig_5_14():
    d = Drawing(1100, 560)
    sides = [(0.75, [(-0.825, '$a$'), (0, '$μ$'), (1.575, '$b$')], 'x'),
             (1.0, [(-1.1, '$(a - μ)/σ$'), (0, '0'), (2.1, '$(b - μ)/σ$')], 'z')]
    axes = []
    for i, (sigma, labels, var) in enumerate(sides):
        ax = Axes(d, 30 + i * 560, 120, 460, 350, -3.2, 3.2, 0.56)
        f = normal(0, sigma)
        ax.shade(f, -1.1 * sigma, 2.1 * sigma)
        ax.curve(f)
        ax.axis(var)
        ax.dashed(0, f(0))
        for x, label in labels:
            d.text(ax.X(x), ax.base + 40, label, 26)
        axes.append((ax, f, sigma))
    d.text(550, 45, 'Same shaded area')
    for (ax, f, sigma), sx in zip(axes, (500, 600)):
        tx = 0.9 * sigma
        leader(d, sx, 62, ax.X(tx), ax.Y(f(tx) * 0.5), True)
    return d


def fig_5_19():
    d = Drawing(1000, 330)
    f = gamma_pdf(1.7, 1.25)
    peak = f(0.875)
    for i, (xs, side) in enumerate(((0.55, 'L'), (2.4, 'R'))):
        ax = Axes(d, 40 + i * 490, 20, 420, 220, -0.1, 7.5, peak * 1.05)
        ax.shade(f, *((1e-4, xs) if side == 'L' else (xs, 7.5)))
        ax.curve(f, 1e-4, 7.5, width=3)
        ax.axis()
        d.text(ax.X(xs), ax.base + 34, '$x^*$', 24)
        d.text(ax.X(3.7), 316, f'({"ab"[i]})', 24)
    return d


def interval(d, x, y, E, color, r=8, cap=14, width=2.5, labels=False):
    d.line(x - E, y, x + E, y, color, width)
    for end in (x - E, x + E):
        d.line(end, y - cap, end, y + cap, color, width * 2)
    d.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')
    if labels:
        for dx, t in ((-E, '$\\bar{x} - E$'), (0, '$\\bar{x}$'), (E, '$\\bar{x} + E$')):
            d.text(x + dx, y - 30, t, color=color)


def mu_axis(d, mu, E, y):
    d.line(30, y, 970, y)
    for k, label in ((-1, '$μ - E$'), (0, '$μ$'), (1, '$μ + E$')):
        d.line(mu + k * E, y - 8, mu + k * E, y + 8)
        d.text(mu + k * E, y + 44, label)


def fig_7_01():
    d = Drawing(1000, 340)
    mu, E = 500, 190
    for off, y, color in ((-1.2, 95, REJECT), (0.21, 190, CURVE)):
        interval(d, mu + off * E, y, E, color, labels=True)
    mu_axis(d, mu, E, 270)
    return d


# (x̄ − μ)/E for each simulated interval, top to bottom, measured from the source figure.
OFFSETS_7_2 = [0.157, 0.439, -0.947, 0.213, -0.422, -0.055, -0.75, -0.414, 0.432, 0.185,
               0.023, -0.093, 0.291, -0.732, 0.058, -0.594, 0.101, 0.933, -0.806, -0.125,
               -0.443, -0.337, 0.277, 1.078, 0.058, -0.266, -0.034, 0.101, -0.238, -0.189,
               0.598, -0.492, -0.009, 0.051, -0.083, 0.354, -0.213, -0.453, -1.021, -0.009]


def fig_7_02():
    d = Drawing(1000, 790)
    mu, E = 500, 196
    d.line(mu, 15, mu, 700, INK, 1.4)
    for i, off in enumerate(OFFSETS_7_2):
        interval(d, mu + off * E, 32 + i * 16.4, E, REJECT if abs(off) > 1 else CURVE, 6, 9, 2)
    mu_axis(d, mu, E, 700)
    return d


def fig_7_05():
    d = Drawing(1000, 560)
    ax = Axes(d, 30, 170, 900, 320, -4.3, 4.3, 0.42)
    ax.curve(t_pdf(2), color=BROWN, width=4.5)
    ax.curve(t_pdf(5), color=CURVE, width=4)
    ax.curve(phi, color=REJECT, width=2)
    ax.dashed(0, phi(0))
    ax.axis()
    d.text(ax.X(0), ax.base + 40, '0')
    for i, (label, color) in enumerate((('Standard normal', REJECT), ('$t$-distribution with $df = 5$', CURVE),
                                        ('$t$-distribution with $df = 2$', BROWN))):
        d.text(80, 52 + i * 44, label, 32, 'start', color)
    return d


def two_populations(pop, sample):
    d = Drawing(1000, 680)
    for i, cx in enumerate((250, 750)):
        n = i + 1
        for top, height, half, title, lines in ((72, 180, 180, 'Population', pop), (410, 220, 170, 'Sample', sample)):
            d.text(cx, top - 20, f'{title} {n}', 36)
            d.add(f'<rect x="{cx - half}" y="{top}" width="{2 * half}" height="{height}" fill="none" '
                  f'stroke="{GRAY}" stroke-width="4"/>')
            mid = top + height / 2
            for j, line in enumerate(lines):
                d.text(cx, mid + 10 + (j - (len(lines) - 1) / 2) * 46, line.format(n=n), 30)
        d.line(cx, 272, cx, 340, GRAY, 2)
        arrowhead(d, cx, 340, math.pi / 2, 18, GRAY, 2)
    return d


def fig_9_01():
    return two_populations(['mean: $μ_{n}$', 's.d.: $σ_{n}$'],
                           ['size: $n_{n}$', 'mean: $\\bar{{x}}_{n}$', 's.d.: $s_{n}$'])


def fig_9_07():
    return two_populations(['proportion: $p_{n}$'],
                           ['size: $n_{n}$', 'successes: $x_{n}$', 'proportion: $\\hat{{p}}_{n}$'])


def fig_9_03():
    d = Drawing(1000, 520)
    bell = Bell(d, 30, 140, 900, 300)
    z = 3.2  # Z = 5.684 lies beyond the drawn range, so it is marked near the right end.
    bell.shade_between(z, None)
    bell.stroke()
    bell.draw('z')
    x, y = bell.X(z), 92
    d.line(30, y, x - 3, y)
    d.line(x + 3, y, 990, y)
    for dx in (-3, 3):
        d.line(x + dx, y, x + dx, bell.Y(z) - 10)
    d.text((30 + x) / 2, y - 14, 'area ≈ 1.0000')
    for i, line in enumerate(('area =', '$p$-value', '≈ 0.000')):
        d.text(990, y - 14 - (2 - i) * 28, line, 26, 'end')
    d.text(bell.X(0), bell.base + 40, '0')
    d.text(x - 20, bell.base + 40, '$Z = 5.684$')
    return d


def fig_9_06():
    d = Drawing(1000, 520)
    bell = Bell(d, 30, 50, 900, 330)
    bell.stroke()
    bell.draw('t')
    marks = ((2.306, 0.78, 'area = 0.025', INK), (2.6, 0.52, 'area = $p$-value', REJECT),
             (2.896, 0.27, 'area = 0.010', INK))
    for t, level, label, color in marks:
        z = t_position(t, 8)
        x, y = bell.X(z), bell.level(level)
        d.line(x, bell.base, x, bell.Y(z), REJECT if color == REJECT else CURVE, 1.6)
        d.line(x, bell.Y(z), x, y, color, 1.6)
        d.line(x, y, 990, y, color, 1.6)
        d.text(990, y - 12, label, 26, 'end', color)
    x1, xt, x2 = (bell.X(t_position(t, 8)) for t in (2.306, 2.6, 2.896))
    d.text(bell.X(0), bell.base + 40, '0')
    d.text(xt - 8, bell.base + 40, '2.306', 26, 'end')
    d.text(xt + 8, bell.base + 40, '2.896', 26, 'start')
    d.line(xt, bell.base + 8, xt, bell.base + 54, REJECT, 1.8)
    d.text(xt, bell.base + 90, '$T = 2.6$')
    return d


def _draw(fn):
    return {'kind': 'draw', 'draw': fn}


T15, T8, T3b = t_position(2.947, 15), t_position(1.860, 8), t_position(4.541, 3)

FIGURES.update({
    # Chapter 5
    'a4a078a33c22b212350844a6cd8789b6': {
        'file': 'fig-05-01.svg', 'title': 'Figure 5.1 Probability given as area of a region under a curve',
        'alt': 'A two-humped density curve y = f(x). The region under the curve between the points a and b on the '
               'horizontal axis is shaded; a heading states that P(a < X < b) equals the area of the shaded region.',
        **_draw(fig_5_01)},
    '448f6a710bd6be21e3ed02d391ce7f37': {
        'file': 'fig-05-02.svg', 'title': 'Figure 5.2 Uniform distribution on [0, 1]',
        'alt': 'Graph of the density y = f(x) of the uniform distribution on [0, 1]: a horizontal segment at height 1 '
               'from x = 0 to x = 1, and the value 0 elsewhere along the x-axis, with open circles at 0 and 1.',
        **_draw(fig_5_02)},
    'ac3caf957cb7bb7eea18975c85163769': {
        'file': 'fig-05-03.svg', 'title': 'Figure 5.3 Probabilities from the uniform distribution on [0, 1]',
        'alt': 'Three copies of the uniform density on [0, 1], height 1. In (a) the rectangle from 0.75 to 1 is shaded; '
               'in (b) the rectangle from 0 to 0.2; in (c) the rectangle from 0.4 to 0.7.',
        **_draw(fig_5_03)},
    'e3d67c5e6cd01f669ae7b76b8061c519': {
        'file': 'fig-05-04.svg', 'title': 'Figure 5.4 Probability of waiting at most 10 minutes for a bus',
        'alt': 'Uniform density of height 1/30 on the interval from 0 to 30 minutes. The rectangle from 0 to 10 is shaded.',
        **_draw(fig_5_04)},
    'ea1abb45110eb47d1b8439f5242afaaa': {
        'file': 'fig-05-05.svg', 'title': 'Figure 5.5 Bell curves with σ = 0.25 and different values of μ',
        'alt': 'Three bell curves of the same shape, standard deviation 0.25, centered at μ = −2 (red), μ = −1 (blue), '
               'and μ = 1 (green), with a dashed line at each center.',
        **_draw(fig_5_05)},
    '14fc6536402c36855bba94c6a80f7143': {
        'file': 'fig-05-06.svg', 'title': 'Figure 5.6 Bell curves with μ = 6 and different values of σ',
        'alt': 'Three bell curves all centered at μ = 6. The curve with σ = 0.5 (red) is tall and narrow, σ = 1 (blue) is '
               'intermediate, and σ = 2 (green) is low and wide.',
        **_draw(fig_5_06)},
    'a9f781e1b0891ceedd50cd7fea7d0f39': {
        'file': 'fig-05-07.svg', 'title': 'Figure 5.7 Density function for a normally distributed random variable with mean μ and standard deviation σ',
        'alt': 'A normal density curve with the horizontal axis marked at μ − 3σ, μ − 2σ, μ − σ, μ, μ + σ, μ + 2σ, and '
               'μ + 3σ. Dashed vertical lines rise to the curve at μ − σ, μ, and μ + σ.',
        'kind': 'bell', 'dashed': [-1, 0, 1], 'ticks': [-3, -2, 2, 3],
        'labels': [(-3, '$μ - 3σ$'), (-2, '$μ - 2σ$'), (-1, '$μ - σ$'), (0, '$μ$'), (1, '$μ + σ$'),
                   (2, '$μ + 2σ$'), (3, '$μ + 3σ$')]},
    '84f83698360490b5801c74626547f18e': {
        'file': 'fig-05-08.svg', 'title': 'Figure 5.8 Density function for heights of 25-year-old men',
        'alt': 'A normal density curve centered at μ = 69.75, marked with a dashed line, with standard deviation σ = 2.59.',
        'kind': 'bell', 'labels': [(0, '$μ = 69.75$')], 'texts': [(2.3, 0.85, '$σ = 2.59$')]},
    'e7a042db29b39bb94416c06789301faa': {
        'file': 'fig-05-09.svg', 'title': 'Figure 5.9 Density curve for a standard normal random variable',
        'alt': 'The standard normal density curve, with σ = 1, centered at 0. Dashed vertical lines rise to the curve at '
               '−1, 0, and 1.',
        'kind': 'bell', 'dashed': [-1, 0, 1], 'labels': [(-1, '$-1$'), (0, '0'), (1, '1')],
        'texts': [(2.3, 0.85, '$σ = 1$')]},
    'f6da1521baeec4bd3bc7a7f1ac4b0856': {
        'file': 'fig-05-10.svg', 'title': 'Figure 5.10 Computing probabilities using the cumulative table',
        'alt': 'Left: an excerpt of the cumulative normal table, where the row for 1.4 meets the column for 0.08 at the '
               'entry 0.9306. Right: a standard normal curve shaded to the left of 1.48, labeled as the area of the '
               'shaded region, 0.9306.',
        **_draw(fig_5_10)},
    '825418e6f94fa960122a168586bd6a2a': {
        'file': 'fig-05-11.svg', 'title': 'Figure 5.11 Computing a probability for a right half-line',
        'alt': 'Standard normal curve with the right tail beyond 1.60 shaded. An arrow to the left from 1.60 is labeled '
               'Normal Table: area = 0.9452; an arrow to the right labels the shaded area 1 − 0.9452.',
        'kind': 'bell', 'shade': [(1.60, None)], 'labels': [(0, '0'), (1.60, '1.60')],
        'brackets': [('table', 1.60, 'L', 1.22, 'Normal Table: area = 0.9452'),
                     ('table', 1.60, 'R', 0.5, ['Shaded area =', '1 − 0.9452'])]},
    'dfc636f4179f8c33cf374a1102616139': {
        'file': 'fig-05-12.svg', 'title': 'Figure 5.12 Computing a probability for an interval of finite length',
        'alt': 'Standard normal curve with the region between 0.5 and 1.57 shaded. Arrows to the left from each end are '
               'labeled with the table areas: 0.9418 to the left of 1.57 and 0.6915 to the left of 0.5.',
        'kind': 'bell', 'shade': [(0.5, 1.57)], 'labels': [(0, '0'), (0.5, '0.5'), (1.57, '1.57')],
        'brackets': [('table', 1.57, 'L', 1.45, 'Normal Table: area = 0.9418'),
                     ('table', 0.5, 'L', 1.12, 'Normal Table: area = 0.6915')]},
    '79129be55c91f8e8442bb1ce46d64e75': {
        'file': 'fig-05-13.svg', 'title': 'Figure 5.13 Computing a probability for an interval of finite length',
        'alt': 'Standard normal curve with the region between −2.55 and 0.09 shaded. Arrows to the left from each end '
               'are labeled with the table areas: 0.5359 to the left of 0.09 and 0.0054 to the left of −2.55.',
        'kind': 'bell', 'shade': [(-2.55, 0.09)], 'labels': [(-2.55, '$-2.55$'), (0.09, '0.09')],
        'brackets': [('table', 0.09, 'L', 1.45, 'Normal Table: area = 0.5359'),
                     ('table', -2.55, 'L', 0.92, ['Normal Table:', 'area = 0.0054'])]},
    'f958d10c46786d0d9891e06a1f2994f0': {
        'file': 'fig-05-14.svg', 'title': 'Figure 5.14 Probability for an interval of finite length',
        'alt': 'Left: a normal curve for X on the x axis, shaded between a and b, with its mean μ between them. Right: '
               'the standard normal curve on the z axis, shaded between (a − μ)/σ and (b − μ)/σ, around 0. Arrows from '
               'the heading “Same shaded area” point to both shaded regions.',
        **_draw(fig_5_14)},
    '5a732b9a593ef6f25ed10e15b5cf81db': {
        'file': 'fig-05-15.svg', 'title': 'Figure 5.15 Probability computation for a general normal random variable',
        'alt': 'Normal curve centered at 10 on the x axis, shaded to the left of 14. A z axis below aligns 10 with 0 and '
               '14 with 1.60. An arrow to the left from 14 is labeled Normal Table: area = 0.9452.',
        'kind': 'bell', 'var': 'x', 'shade': [(None, 1.60)], 'labels': [(0, '10'), (1.60, '14')],
        'zaxis': [(0, '0'), (1.60, '1.60')], 'brackets': [('table', 1.60, 'L', 1.18, 'Normal Table: area = 0.9452')]},
    '272b0cb85ce96627d502c2ff029199ad': {
        'file': 'fig-05-16.svg', 'title': 'Figure 5.16 Probability computation for a general normal random variable',
        'alt': 'Normal curve centered at 10 on the x axis, shaded between 8 and 14. A z axis below aligns 8, 10, and 14 '
               'with −0.8, 0, and 1.60. Arrows to the left are labeled with the table areas 0.9452 (from 14) and 0.2119 '
               '(from 8).',
        'kind': 'bell', 'var': 'x', 'shade': [(-0.8, 1.60)], 'labels': [(-0.8, '8'), (0, '10'), (1.60, '14')],
        'zaxis': [(-0.8, '$-0.8$'), (0, '0'), (1.60, '1.60')],
        'brackets': [('table', 1.60, 'L', 1.42, 'Normal Table: area = 0.9452'),
                     ('table', -0.8, 'L', 1.07, 'Normal Table: area = 0.2119')]},
    '2712ed90b9f7e7fd3e0589acd6c734e0': {
        'file': 'fig-05-17.svg', 'title': 'Figure 5.17 Probability computation for tire tread wear',
        'alt': 'Normal curve centered at 37.5 on the x axis, shaded between 30 and 40. A z axis below aligns 30, 37.5, and '
               '40 with −1.67, 0, and 0.56. Arrows to the left are labeled with the table areas 0.7123 (from 40) and '
               '0.0475 (from 30).',
        'kind': 'bell', 'var': 'x', 'shade': [(-1.67, 0.56)], 'labels': [(-1.67, '30'), (0, '37.5'), (0.56, '40')],
        'zaxis': [(-1.67, '$-1.67$'), (0, '0'), (0.56, '0.56')],
        'brackets': [('table', 0.56, 'L', 1.38, 'Normal Table: area = 0.7123'),
                     ('table', -1.67, 'L', 0.78, ['Normal Table:', 'area = 0.0475'])]},
    'f652f315d2286107695053b9212f66de': {
        'file': 'fig-05-18.svg', 'title': 'Figure 5.18 Probability computation for exam scores',
        'alt': 'Normal curve centered at 510 on the x axis, with the small right tail beyond 650 shaded. A z axis below '
               'aligns 510 with 0 and 650 with 2.33. An arrow to the left from 650 is labeled Normal Table: area = 0.9901.',
        'kind': 'bell', 'var': 'x', 'shade': [(2.33, None)], 'labels': [(0, '510'), (2.33, '650')],
        'zaxis': [(0, '0'), (2.33, '2.33')], 'brackets': [('table', 2.33, 'L', 1.18, 'Normal Table: area = 0.9901')]},
    'bbb58b35dd040bcf4d8b4d3f7c72b679': {
        'file': 'fig-05-19.svg', 'title': 'Figure 5.19 Right and left tails of a distribution',
        'alt': 'Two copies of a right-skewed density curve. In (a) the left tail, the region to the left of a point x*, is '
               'shaded. In (b) the right tail, the region to the right of x*, is shaded.',
        **_draw(fig_5_19)},
    '30641707b126e7384ae5b3e6745117f7': {
        'file': 'fig-05-20.svg', 'title': 'Figure 5.20 Z value that produces a known area',
        'alt': 'Standard normal curve with the left tail below an unknown point z* shaded; an arrow labels its area as 0.0125.',
        'kind': 'bell', 'shade': [(None, -2.24)], 'labels': [(-2.24, '$z^*$'), (0, '0')],
        'leaders': [('Area = 0.0125', -2.75, 0.62, -2.55)]},
    'c01e6ac6766ff9e8602e238df3d23be1': {
        'file': 'fig-05-21.svg', 'title': 'Figure 5.21 Z value that produces a known area',
        'alt': 'Standard normal curve with the right tail beyond an unknown point z* shaded and labeled Area = 0.0250. An '
               'arrow to the left from z* is labeled Area = 1 − 0.0250 = 0.9750.',
        'kind': 'bell', 'shade': [(1.96, None)], 'labels': [(0, '0'), (1.96, '$z^*$')],
        'brackets': [('table', 1.96, 'L', 1.18, 'Area = 1 − 0.0250 = 0.9750', 0.72)],
        'leaders': [('Area = 0.0250', 2.8, 0.52, 2.25)]},
    'e4499588e283aa8c3339ac767a95ccef': {
        'file': 'fig-05-22.svg', 'title': 'Figure 5.22 The numbers z_c and −z_c',
        'alt': 'Standard normal curve with both tails shaded, below −z_c and above z_c, symmetric about 0. Each tail is '
               'labeled Area = c.',
        'kind': 'bell', 'shade': [(None, -1.28), (1.28, None)], 'labels': [(-1.28, '$-z_c$'), (0, '0'), (1.28, '$z_c$')],
        'leaders': [('Area = $c$', -2.55, 0.62, -1.75), ('Area = $c$', 2.55, 0.62, 1.75)]},
    '14236fa81644aae933a0c3cab3039fc4': {
        'file': 'fig-05-23.svg', 'title': 'Figure 5.23 Computation of the number z.01',
        'alt': 'Standard normal curve with the right tail beyond z₀.₀₁ shaded and labeled Area = 0.01. An arrow to the left '
               'from z₀.₀₁ is labeled Area = 1 − 0.01 = 0.99.',
        'kind': 'bell', 'shade': [(2.326, None)], 'labels': [(0, '0'), (2.326, '$z_{0.01}$')],
        'brackets': [('table', 2.326, 'L', 1.18, 'Area = 1 − 0.01 = 0.99', 0.72)],
        'leaders': [('Area = 0.01', 2.85, 0.48, 2.55)]},
    'bce69683fbb8a21dbc078449d5aea822': {
        'file': 'fig-05-24.svg', 'title': 'Figure 5.24 Tail of a normally distributed random variable',
        'alt': 'Normal curve with mean 10 and σ = 2.5 on the x axis, shaded to the left of an unknown point x*. A z axis '
               'below aligns 10 with 0 and x* with z*. An arrow to the left from x* is labeled Area = 0.9332.',
        'kind': 'bell', 'var': 'x', 'shade': [(None, 1.5)], 'labels': [(0, '10'), (1.5, '$x^*$')],
        'zaxis': [(0, '0'), (1.5, '$z^*$')], 'brackets': [('table', 1.5, 'L', 1.18, 'Area = 0.9332')],
        'texts': [(2.75, 0.9, '$σ = 2.5$')]},
    'd3132061252ea04fa375f45f9265544e': {
        'file': 'fig-05-25.svg', 'title': 'Figure 5.25 Tail of a normally distributed random variable',
        'alt': 'Normal curve with mean 175 and σ = 12 on the x axis, shaded to the right of an unknown point x* just below '
               'the mean. A z axis below aligns x* with z* and 175 with 0. An arrow to the right from x* is labeled '
               'Area = 0.65, and an arrow to the left is labeled Area = 1 − 0.65 = 0.35.',
        'kind': 'bell', 'var': 'x', 'shade': [(-0.385, None)], 'labels': [(-0.385, '$x^*$'), (0.1, '175')],
        'zaxis': [(-0.385, '$z^*$'), (0, '0')],
        'brackets': [('table', -0.385, 'R', 1.36, 'Area = 0.65'),
                     ('table', -0.385, 'L', 1.07, 'Area = 1 − 0.65 = 0.35')],
        'texts': [(2.4, 0.9, '$σ = 12$')]},
    '41425a476cf02dd0a5716a9b894cb84c': {
        'file': 'fig-05-26.svg', 'title': 'Figure 5.26 Tail of a normally distributed random variable',
        'alt': 'Normal curve with mean 510 and σ = 60 on the x axis, with the right tail beyond an unknown point x* shaded. '
               'A z axis below aligns 510 with 0 and x* with z* = z₀.₀₅. An arrow to the right from x* is labeled '
               'Area = 0.05, and an arrow to the left is labeled Area = 1 − 0.05 = 0.95.',
        'kind': 'bell', 'var': 'x', 'shade': [(1.645, None)], 'labels': [(0, '510'), (1.645, '$x^*$')],
        'zaxis': [(0, '0'), (1.645, '$z^* = z_{0.05}$')],
        'brackets': [('table', 1.645, 'L', 1.2, 'Area = 1 − 0.05 = 0.95'),
                     ('table', 1.645, 'R', 0.42, 'Area = 0.05')],
        'texts': [(2.6, 0.95, '$σ = 60$')]},
    '2854b11aad3fae019aa6ee83b90275ab': {
        'file': 'fig-05-27.svg', 'title': 'Figure 5.27 Distribution of times to run a course',
        'alt': 'Normal curve centered at 29 on the x axis, shaded between x_fast and x_slow, which are symmetric about the '
               'mean. A bracket over the shaded region is labeled Area = 0.75. A z axis below aligns x_fast, 29, and '
               'x_slow with −z₀.₁₂₅, 0, and z₀.₁₂₅.',
        'kind': 'bell', 'var': 'x', 'shade': [(-1.15, 1.15)],
        'labels': [(-1.15, '$x_{fast}$'), (0, '29'), (1.15, '$x_{slow}$')],
        'zaxis': [(-1.15, '$-z_{0.125}$'), (0, '0'), (1.15, '$z_{0.125}$')],
        'brackets': [('span', -1.15, 1.15, 1.2, 'Area = 0.75', True)]},
    # Chapter 7
    '28bf0a4db4415dec382b8a1a07e79927': {
        'file': 'fig-07-01.svg', 'title': 'Figure 7.1 When winged dots capture the population mean',
        'alt': 'Two intervals x̄ − E to x̄ + E drawn as winged dots above an axis marked μ − E, μ, and μ + E. The red '
               'interval, whose x̄ lies farther than E from μ, does not reach μ. The blue interval, whose x̄ lies within E '
               'of μ, contains μ.',
        **_draw(fig_7_01)},
    '7827472ac37fbd53928abecec353fcc4': {
        'file': 'fig-07-02.svg', 'title': 'Figure 7.2 Computer simulation of 40 95% confidence intervals for a mean',
        'alt': 'Forty horizontal confidence intervals of equal width, stacked above an axis marked μ − E, μ, and μ + E, '
               'with a vertical line at μ. Thirty-eight blue intervals cross the line at μ; two red intervals, one far '
               'to each side, miss it.',
        **_draw(fig_7_02)},
    'e3f246f42e1caa418685cbcb55e93279': {
        'file': 'fig-07-03.svg', 'title': 'Figure 7.3',
        'alt': 'Standard normal curve with both tails shaded, below −z_α/2 and above z_α/2, each labeled α/2. The central '
               'region between them is labeled 1 − α.',
        'kind': 'bell', 'var': 'z', 'dashed': [], 'ticks': [0], 'shade': [(None, -1.96), (1.96, None)],
        'labels': [(-1.96, '$-z_{α/2}$'), (0, '0'), (1.96, '$z_{α/2}$')],
        'tail_labels': [('L', -1.96, '$α/2$'), ('R', 1.96, '$α/2$')], 'texts': [(0, 0.45, '$1 - α$')]},
    '9befc784764fb56426a1ba328be4bc98': {
        'file': 'fig-07-04.svg', 'title': 'Figure 7.4',
        'alt': 'Standard normal curve with both tails shaded, below −z₀.₀₂₅ and above z₀.₀₂₅, each labeled α/2 = 0.025. '
               'A bracket over the central region between them is labeled 1 − α = 0.95.',
        'kind': 'bell', 'var': 'z', 'dashed': [], 'ticks': [0], 'shade': [(None, -1.96), (1.96, None)],
        'labels': [(-1.96, '$-z_{0.025}$'), (0, '0'), (1.96, '$z_{0.025}$')],
        'tail_labels': [('L', -1.96, '$α/2 = 0.025$'), ('R', 1.96, '$α/2 = 0.025$')],
        'brackets': [('span', -1.96, 1.96, 1.18, '$1 - α = 0.95$', False, 0.72)]},
    '3435a692ad23c4d5cf2b42e6aa8f5191': {
        'file': 'fig-07-05.svg', 'title': 'Figure 7.5 Student’s t-distribution',
        'alt': 'Three bell-shaped curves centered at 0: the standard normal (red), the t-distribution with 5 degrees of '
               'freedom (blue), and with 2 degrees of freedom (brown). The fewer the degrees of freedom, the lower the '
               'peak and the heavier the tails.',
        **_draw(fig_7_05)},
    # Chapter 9
    '1ad736d4248ac0eb4e843e5bdb063677': {
        'file': 'fig-09-01.svg', 'title': 'Figure 9.1 Independent sampling from two populations',
        'alt': 'Two boxes labeled Population 1 and Population 2, with means μ₁ and μ₂ and standard deviations σ₁ and σ₂. '
               'An arrow from each leads to a box for its sample, Sample 1 or Sample 2, with size n₁ or n₂, mean x̄₁ or '
               'x̄₂, and standard deviation s₁ or s₂.',
        **_draw(fig_9_01)},
    '5b3274bd341a0dedc9193ff3b4afa69a': {
        'file': 'fig-09-02.svg', 'title': 'Figure 9.2 Rejection region and test statistic for Example 2',
        'alt': 'Standard normal curve for Hₐ: μ₁ − μ₂ > 0. The right tail of area α = 0.01 is shaded above the critical '
               'value z_α = 2.326. On the number line below, the rejection region z ≥ 2.326 is red, and the test '
               'statistic Z = 5.684, marked with a star near the right end, lies far inside it.',
        'kind': 'single', 'title_markup': '$H_a : μ_1 - μ_2 > 0$', 'var': 'z',
        'tails': [('R', 2.326)], 'tail_labels': [('R', 2.326, '$α = 0.01$')],
        'axis_labels': [(0, '0'), (2.326, '$z_α = 2.326$')],
        # Z = 5.684 is beyond the drawn range; it is marked near the right end, as in the source.
        'bars': [('R', 2.326)], 'line_labels': [(0, '0')], 'stat': (2.9, '$Z = 5.684$')},
    'dd649c00a430c1f005660c9ed8188d58': {
        'file': 'fig-09-03.svg', 'title': 'Figure 9.3 P-value for Example 3',
        'alt': 'Standard normal curve with the test statistic Z = 5.684 marked near the right end of the z axis. The area '
               'to its left is labeled area ≈ 1.0000; the vanishing tail to its right is labeled area = p-value ≈ 0.000.',
        **_draw(fig_9_03)},
    '829e1f428616582053c27c2d3b8254e8': {
        'file': 'fig-09-04.svg', 'title': 'Figure 9.4 Rejection region and test statistic for Example 5',
        'alt': 'Student t curve with 15 degrees of freedom. Both tails, each of area α/2 = 0.005, are shaded beyond the '
               'critical values −t_α/2 = −2.947 and t_α/2 = 2.947. On the number line below, the two rejection intervals '
               'are red, and the test statistic T = 1.040, marked with a star, lies outside the rejection region.',
        'kind': 'single', 'title_markup': '', 'var': 't',
        'tails': [('L', -T15), ('R', T15)],
        'tail_labels': [('L', -T15, '$α/2 = 0.005$'), ('R', T15, '$α/2 = 0.005$')],
        'axis_labels': [(-T15, '$-t_{α/2} = -2.947$'), (0, '0'), (T15, '$t_{α/2} = 2.947$')],
        'bars': [('L', -T15), ('R', T15)], 'line_labels': [(0, '0')], 'stat': (t_position(1.040, 15), '$T = 1.040$')},
    '65c475a429d83d1c543748d068992428': {
        'file': 'fig-09-05.svg', 'title': 'Figure 9.5 Rejection region and test statistic for Example 8',
        'alt': 'Student t curve with 8 degrees of freedom for Hₐ: μ_d > 0. The right tail of area α = 0.05 is shaded above '
               'the critical value t₀.₀₅ = 1.860. On the number line below, the rejection region t ≥ 1.860 is red, and '
               'the test statistic T = 2.600, marked with a star, lies inside it.',
        'kind': 'single', 'title_markup': '$H_a : μ_d > 0$', 'var': 't',
        'tails': [('R', T8)], 'tail_labels': [('R', T8, '$α = 0.05$')],
        'axis_labels': [(0, '0'), (T8, '$t_{0.05} = 1.860$')],
        'bars': [('R', T8)], 'line_labels': [(0, '0')], 'stat': (t_position(2.600, 8), '$T = 2.600$')},
    '39fabc97b76e2fcd598df4157a5af35c': {
        'file': 'fig-09-06.svg', 'title': 'Figure 9.6 P-value for Example 9',
        'alt': 'Student t curve with 8 degrees of freedom. Vertical lines at 2.306, at the test statistic T = 2.6 (red), '
               'and at 2.896 mark right tails of area 0.025, the p-value, and 0.010, so the p-value lies between 0.010 '
               'and 0.025.',
        **_draw(fig_9_06)},
    '53170ede206ef4a4fcde1a7e4d6d046c': {
        'file': 'fig-09-07.svg', 'title': 'Figure 9.7 Independent sampling from two populations in order to compare proportions',
        'alt': 'Two boxes labeled Population 1 and Population 2, with proportions p₁ and p₂. An arrow from each leads to a '
               'box for its sample, Sample 1 or Sample 2, with size n₁ or n₂, number of successes x₁ or x₂, and sample '
               'proportion p̂₁ or p̂₂.',
        **_draw(fig_9_07)},
    '22ebc3b67649345e707b089c29451d59': {
        'file': 'fig-09-08.svg', 'title': 'Figure 9.8 Rejection region and test statistic for Example 11',
        'alt': 'Standard normal curve for Hₐ: p₁ − p₂ < −0.05. The left tail of area α = 0.10 is shaded below the critical '
               'value −z₀.₁₀ = −1.282. On the number line below, the rejection region z ≤ −1.282 is red, and the test '
               'statistic Z = −1.770, marked with a star, lies inside it.',
        'kind': 'single', 'title_markup': '$H_a : p_1 - p_2 < -0.05$', 'var': 'z',
        'tails': [('L', -1.282)], 'tail_labels': [('L', -1.282, '$α = 0.10$')],
        'axis_labels': [(-1.282, '$-z_{0.10} = -1.282$'), (0, '0')],
        'bars': [('L', -1.282)], 'line_labels': [(0, '0')], 'stat': (-1.770, '$Z = -1.770$')},
    # Chapter 10
    '9f1c174c40e1d4364dca3822c4cc03d5': {
        'file': 'fig-10-09.svg', 'title': 'Figure 10.9 Rejection region and test statistic for Example 8',
        'alt': 'Student t curve with 3 degrees of freedom for Hₐ: β₁ ≠ 0. Both tails, each of area α/2 = 0.01, are shaded '
               'beyond the critical values −t_α/2 = −4.541 and t_α/2 = 4.541. On the number line below, the two rejection '
               'intervals are red, and the test statistic T = 4.914, marked with a star, lies inside the right one.',
        'kind': 'single', 'title_markup': '$H_a : β_1 ≠ 0$', 'var': 't',
        'tails': [('L', -T3b), ('R', T3b)],
        'tail_labels': [('L', -T3b, '$α/2 = 0.01$'), ('R', T3b, '$α/2 = 0.01$')],
        'axis_labels': [(-T3b, '$-t_{α/2} = -4.541$'), (0, '0'), (T3b, '$t_{α/2} = 4.541$')],
        'bars': [('L', -T3b), ('R', T3b)], 'line_labels': [(0, '0')], 'stat': (t_position(4.914, 3), '$T = 4.914$')},
    'da0a5676198f1c1c85bdb57bbd79e2b1': {
        'file': 'fig-10-10.svg', 'title': 'Figure 10.10 Rejection region and test statistic for Example 9',
        'alt': 'Student t curve with 8 degrees of freedom for Hₐ: β₁ < 0. The left tail of area α = 0.05 is shaded below '
               'the critical value −t_α = −1.860. On the number line below, the rejection region t ≤ −1.860 is red, and '
               'the test statistic T = −1.869, marked with a star, lies just inside it.',
        'kind': 'single', 'title_markup': '$H_a : β_1 < 0$', 'var': 't',
        'tails': [('L', -T8)], 'tail_labels': [('L', -T8, '$α = 0.05$')],
        'axis_labels': [(-T8, '$-t_α = -1.860$'), (0, '0')],
        'bars': [('L', -T8)], 'line_labels': [(0, '0')], 'stat': (t_position(-1.869, 8), '$T = -1.869$')},
})


# --- Chapter 11: chi-square and F distributions -----------------------------------------

CYAN = '#13a3c4'


def chi2_pdf(k):
    c = 1 / (2 ** (k / 2) * math.gamma(k / 2))
    return lambda x: c * x ** (k / 2 - 1) * math.exp(-x / 2) if x > 0 else (0.5 if k == 2 else 0.0)


def f_pdf(d1, d2):
    c = math.exp(math.lgamma((d1 + d2) / 2) - math.lgamma(d1 / 2) - math.lgamma(d2 / 2)) * (d1 / d2) ** (d1 / 2)
    return lambda x: c * x ** (d1 / 2 - 1) * (1 + d1 * x / d2) ** (-(d1 + d2) / 2) if x > 0 else (
        1.0 if d1 == 2 else 0.0)


def visible_from(f, cap, hi):
    """Smallest x where a density that blows up at 0 has come down to the plot's top."""
    if f(1e-9) <= cap:
        return 0.0
    lo = 1e-9
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) > cap else (lo, mid)
    return hi


class Skew(Axes):
    """Axes for a density on [0, ∞), cut off at xmax, with the axis starting a little left of 0."""

    def __init__(self, d, left, top, width, height, f, xmax, ymax):
        super().__init__(d, left, top, width, height, -0.05 * xmax, xmax, ymax)
        self.f = f

    def draw(self, var, size=FONT, width=4.5, color=CURVE):
        self.curve(self.f, visible_from(self.f, self.ymax, self.x1), self.x1, color, width)
        self.axis(var, size)

    def tail(self, a, b):
        self.shade(self.f, max(a, visible_from(self.f, self.ymax, self.x1)), b)

    def note(self, markup, lx, ly, tx, size=FONT, depth=0.4):
        """Label at (lx, ly × ymax) with a leader into the shaded area at tx."""
        x, y = self.X(lx), self.Y(ly * self.ymax)
        self.d.text(x, y, markup, size)
        ty = self.Y(min(self.f(tx), self.ymax) * depth)
        sx = x + (self.X(tx) - x) * 0.3
        leader(self.d, sx, y + 12, self.X(tx), ty)


def skew_test(spec):
    """A chi-square or F test drawn with the true density for its degrees of freedom."""
    W, size = 1000, FONT
    top = spec.get('top', 30)
    has_line = 'bars' in spec
    d = Drawing(W, top + 300 + (230 if has_line else 90))
    ax = Skew(d, 30, top, 900, 300, spec['pdf'], spec['xmax'], spec['ymax'])
    for a, b in spec['tails']:
        ax.tail(a, b)
    ax.draw(spec['var'])
    for label in spec['notes']:
        ax.note(*label)
    for x, label in spec['axis_labels']:
        d.text(ax.X(x), ax.base + 42, label)
    if has_line:
        y = ax.base + 100
        number_line(d, ax, y, spec['var'], spec['bars'], [], floor=0)
        avoid = ax.X(spec['stat'][0])
        for side, x in spec['bars']:
            reject_label(d, ax, side, y + 46, FONT, x, avoid)
        x, label = spec['stat']
        d.star(ax.X(x), y)
        d.line(ax.X(x), y + 16, ax.X(x), y + 46, INK, 1.6)
        d.text(ax.X(x), y + 84, label)
    return d


KINDS['skew'] = skew_test


def fig_11_01():
    d = Drawing(1000, 600)
    ax = Axes(d, 70, 20, 830, 480, -0.4, 15.4, 0.52)
    d.line(ax.X(0), ax.base, ax.X(0), ax.top, INK, 1.6)
    curves = ((1, REJECT, 1.9, 0.47), (2, BROWN, 3.2, 0.27), (3, CURVE, 4.4, 0.2), (5, GREEN, 6.6, 0.17),
              (10, CYAN, 12.6, 0.105))
    for k, color, lx, ly in curves:
        f = chi2_pdf(k)
        ax.curve(f, visible_from(f, ax.ymax, 15), 15, color, 4)
        d.text(ax.X(lx), ax.Y(ly), f'$df = {k}$', 34, color=color)
    ax.axis('χ^2')
    for n in range(16):
        d.line(ax.X(n), ax.base, ax.X(n), ax.base - 8)
        d.text(ax.X(n), ax.base + 40, str(n), 26)
    return d


def fig_11_02():
    d = Drawing(1000, 430)
    f = chi2_pdf(5)
    crit = quantile(lambda x: chi2_cdf(x, 5), 0.90)
    ax = Skew(d, 30, 30, 900, 300, f, 18, f(3) * 1.04)
    ax.tail(crit, 18)
    ax.draw('χ^2')
    d.text(ax.X(0), ax.base + 42, '0')
    d.text(ax.X(crit), ax.base + 42, '$χ_c^2$')
    d.text(ax.X(4.2), ax.Y(0.055), '$1 - c$', 38)
    ax.note('$c$', crit + 3.6, 0.5, crit + 1.0, 38)
    return d


def fig_11_07():
    d = Drawing(1000, 600)
    ax = Axes(d, 70, 20, 830, 480, -0.25, 5.3, 0.95)
    d.line(ax.X(0), ax.base, ax.X(0), ax.top, INK, 1.6)
    curves = (((1, 1), REJECT, 1.75, 0.91), ((10, 20), BROWN, 2.6, 0.72), ((5, 4), CURVE, 4.1, 0.15))
    for (d1, d2), color, lx, ly in curves:
        f = f_pdf(d1, d2)
        ax.curve(f, visible_from(f, ax.ymax, 5), 5, color, 4)
        d.text(ax.X(lx), ax.Y(ly), f'$(df_1 = {d1}, df_2 = {d2})$', 32, color=color)
    ax.axis('F')
    for n in range(6):
        d.line(ax.X(n), ax.base, ax.X(n), ax.base - 8)
        d.text(ax.X(n), ax.base + 40, str(n), 26)
    return d


def fig_11_08():
    d = Drawing(1000, 430)
    f = f_pdf(10, 15)
    crit = quantile(lambda x: f_cdf(x, 10, 15), 0.90)
    ax = Skew(d, 30, 30, 900, 300, f, 4.5, 0.82)
    ax.tail(crit, 4.5)
    ax.draw('F')
    d.text(ax.X(0), ax.base + 42, '0')
    d.text(ax.X(crit), ax.base + 42, '$F_c$')
    d.text(ax.X(0.95), ax.Y(0.3), '$1 - c$', 38)
    ax.note('$c$', crit + 0.75, 0.55, crit + 0.3, 38)
    return d


def fig_11_09():
    """Right-, left-, and two-tailed F tests (schematic: F with 15 and 20 degrees of freedom, α = 0.10)."""
    d = Drawing(1100, 820)
    size, f = 24, f_pdf(15, 20)
    cdf = lambda x: f_cdf(x, 15, 20)
    q = lambda p: quantile(cdf, p)
    panels = [
        ('(a)', 20, 50, '$H_a : σ_1^2 > σ_2^2$', [('R', q(0.90))], {('R', q(0.90)): '$F_α$'}, 'α'),
        ('(b)', 580, 50, '$H_a : σ_1^2 < σ_2^2$', [('L', q(0.10))], {('L', q(0.10)): '$F_{1 - α}$'}, 'α'),
        ('(c)', 300, 440, '$H_a : σ_1^2 ≠ σ_2^2$', [('L', q(0.05)), ('R', q(0.95))],
         {('L', q(0.05)): '$F_{1 - α/2}$', ('R', q(0.95)): '$F_{α/2}$'}, 'α/2'),
    ]
    for tag, left, top, title, tails, labels, area in panels:
        ax = Skew(d, left + 40, top + 40, 430, 180, f, 4, 1.02)
        for side, x in tails:
            ax.tail(*((0, x) if side == 'L' else (x, 4)))
        ax.draw('F', size, 3)
        d.text(left + 255, top + 16, title, size)
        d.text(left + 10, top + 120, tag, size, 'start')
        for side, x in tails:
            if side == 'L':
                ax.note(f'${area}$', 0.12, 0.92, x * 0.75, size)
            else:
                ax.note(f'${area}$', x + 0.85, 0.42, x + 0.3, size)
            d.text(ax.X(x) + (12 if side == 'L' else 0), ax.base + 30, labels[(side, x)], size)
        d.text(ax.X(0) - 8, ax.base + 30, '0', size, 'end')
        y = ax.base + 70
        number_line(d, ax, y, 'F', tails, [], size, floor=0)
        for side, x in tails:
            reject_label(d, ax, side, y + 34, size, x)
    return d


def _chi(k):
    return {'pdf': chi2_pdf(k)}


def _f(d1, d2):
    return {'pdf': f_pdf(d1, d2)}


FIGURES.update({
    '5a0c7bbacb4242555e8a85c9767c03ee': {
        'file': 'fig-11-01.svg', 'title': 'Figure 11.1 Many χ² distributions',
        'alt': 'Chi-square density curves for 1, 2, 3, 5, and 10 degrees of freedom on a horizontal axis from 0 to 15. '
               'With 1 or 2 degrees of freedom the curve is highest at 0 and decreases; with more degrees of freedom it '
               'rises to a peak and has a long right tail, and the peak moves right and flattens as df grows.',
        **_draw(fig_11_01)},
    '34d06306c2e726f6d5cd7479d9736e5e': {
        'file': 'fig-11-02.svg', 'title': 'Figure 11.2 χ²_c illustrated',
        'alt': 'A right-skewed chi-square density. The right tail beyond the point χ²_c is shaded and labeled c; the area '
               'to its left is labeled 1 − c.',
        **_draw(fig_11_02)},
    'a2d445829c9e324c32b00dad5870eb22': {
        'file': 'fig-11-03.svg', 'title': 'Figure 11.3 Baby gender prediction',
        'alt': 'Chi-square density with 1 degree of freedom. The right tail of area α = 0.10 beyond the critical value '
               'χ²_α = 2.706 is shaded. On the number line below, the rejection region χ² ≥ 2.706 is red, and the test '
               'statistic χ² = 1.231, marked with a star, lies outside it.',
        'kind': 'skew', **_chi(1), 'xmax': 7, 'ymax': 0.62, 'var': 'χ^2', 'tails': [(2.706, 7)],
        'notes': [('$α = 0.10$', 4.6, 0.42, 3.3)], 'axis_labels': [(0, '0'), (2.706, '$χ_α^2 = 2.706$')],
        'bars': [('R', 2.706)], 'stat': (1.231, '$χ^2 = 1.231$')},
    '68bbab395044eb9d625f2e5d5ad79f81': {
        'file': 'fig-11-04.svg', 'title': 'Figure 11.4 Example 1',
        'alt': 'Chi-square density with 2 degrees of freedom. The thin right tail of area α = 0.01 beyond the critical '
               'value χ²_α = 9.210 is shaded. On the number line below, the rejection region χ² ≥ 9.210 is red, and the '
               'test statistic χ² = 31.75, marked with a star near the right end, lies far inside it.',
        'kind': 'skew', **_chi(2), 'xmax': 14, 'ymax': 0.52, 'var': 'χ^2', 'tails': [(9.210, 14)],
        'notes': [('$α = 0.01$', 11.6, 0.32, 10.2)], 'axis_labels': [(0, '0'), (9.210, '$χ_α^2 = 9.210$')],
        # χ² = 31.75 is beyond the drawn range; it is marked near the right end, as in the source.
        'bars': [('R', 9.210)], 'stat': (13.6, '$χ^2 = 31.75$')},
    '3406a41dcf8b2ad498d3271e90a762c1': {
        'file': 'fig-11-05.svg', 'title': 'Figure 11.5 Balanced die',
        'alt': 'Chi-square density with 5 degrees of freedom. The right tail of area α = 0.10 beyond the critical value '
               'χ²_α = 9.236 is shaded. On the number line below, the rejection region χ² ≥ 9.236 is red, and the test '
               'statistic χ² = 5.6, marked with a star, lies outside it.',
        'kind': 'skew', **_chi(5), 'xmax': 20, 'ymax': 0.16, 'var': 'χ^2', 'tails': [(9.236, 20)],
        'notes': [('$α = 0.10$', 14.5, 0.55, 10.8)], 'axis_labels': [(0, '0'), (9.236, '$χ_α^2 = 9.236$')],
        'bars': [('R', 9.236)], 'stat': (5.6, '$χ^2 = 5.6$')},
    '85a1393f4233c942c36e25df39e0b384': {
        'file': 'fig-11-06.svg', 'title': 'Figure 11.6 Example 2',
        'alt': 'Chi-square density with 5 degrees of freedom. The thin right tail of area α = 0.01 beyond the critical '
               'value χ²_α = 15.086 is shaded. On the number line below, the rejection region χ² ≥ 15.086 is red, and '
               'the test statistic χ² = 651.881, marked with a star near the right end, lies far inside it.',
        'kind': 'skew', **_chi(5), 'xmax': 20, 'ymax': 0.16, 'var': 'χ^2', 'tails': [(15.086, 20)],
        'notes': [('$α = 0.01$', 16.8, 0.4, 15.9)], 'axis_labels': [(0, '0'), (15.086, '$χ_α^2 = 15.086$')],
        # χ² = 651.881 is beyond the drawn range; it is marked near the right end, as in the source.
        'bars': [('R', 15.086)], 'stat': (19.3, '$χ^2 = 651.881$')},
    '75fd6a2d869b9403de8408b42a054db9': {
        'file': 'fig-11-07.svg', 'title': 'Figure 11.7 Many F-distributions',
        'alt': 'F density curves for degrees of freedom (1, 1), (10, 20), and (5, 4) on a horizontal axis from 0 to 5. The '
               '(1, 1) curve is highest at 0 and decreases slowly; the (10, 20) curve has a tall peak near 1; the (5, 4) '
               'curve peaks lower, closer to 0, and has a heavier right tail.',
        **_draw(fig_11_07)},
    '59a41857cbaae56b820472577df06b26': {
        'file': 'fig-11-08.svg', 'title': 'Figure 11.8 F_c illustrated',
        'alt': 'A right-skewed F density. The right tail beyond the point F_c is shaded and labeled c; the area to its left '
               'is labeled 1 − c.',
        **_draw(fig_11_08)},
    'da58e4f2977f4b9644c6f0c320af4429': {
        'file': 'fig-11-09.svg', 'title': 'Figure 11.9 Rejection regions: (a) right-tailed; (b) left-tailed; (c) two-tailed',
        'alt': 'Three F density curves. (a) For Hₐ: σ₁² > σ₂², the right tail of area α above F_α is shaded, and the '
               'rejection region is F ≥ F_α. (b) For Hₐ: σ₁² < σ₂², the left tail of area α below F₁₋α is shaded, and the '
               'rejection region runs from 0 to F₁₋α. (c) For Hₐ: σ₁² ≠ σ₂², both tails, each of area α/2, are shaded, '
               'below F₁₋α/2 and above F_α/2, and the rejection region is both intervals.',
        **_draw(fig_11_09)},
    '5529f95c575a61746d7c6db537493c0f': {
        'file': 'fig-11-10.svg', 'title': 'Figure 11.10 Rejection region and test statistic for Example 6',
        'alt': 'F density with 15 and 20 degrees of freedom. Both tails, each of area α/2 = 0.05, are shaded: below '
               'F₁₋α/2 = 0.43 and above F_α/2 = 2.20. On the number line below, the rejection intervals from 0 to 0.43 '
               'and from 2.20 on are red, and the test statistic F = 1.90, marked with a star, lies between them.',
        'kind': 'skew', **_f(15, 20), 'xmax': 4, 'ymax': 1.02, 'var': 'F', 'top': 60,
        'tails': [(0, 0.43), (2.20, 4)],
        'notes': [('$α/2 = 0.05$', 0.42, 1.12, 0.36), ('$α/2 = 0.05$', 3.0, 0.42, 2.45)],
        'axis_labels': [(0.43, '$F_{1 - α/2} = 0.43$'), (2.20, '$F_{α/2} = 2.20$')],
        'bars': [('L', 0.43), ('R', 2.20)], 'stat': (1.90, '$F = 1.90$')},
    '0dee7b0964c04670ae90832291b81e85': {
        'file': 'fig-11-11.svg', 'title': 'Figure 11.11 Rejection region and test statistic for Example 7',
        'alt': 'F density with 15 and 20 degrees of freedom. The right tail of area α = 0.10 beyond the critical value '
               'F_α = 1.84 is shaded. On the number line below, the rejection region F ≥ 1.84 is red, and the test '
               'statistic F = 1.90, marked with a star, lies just inside it.',
        'kind': 'skew', **_f(15, 20), 'xmax': 4, 'ymax': 1.02, 'var': 'F', 'tails': [(1.84, 4)],
        'notes': [('$α = 0.10$', 2.75, 0.55, 2.1)], 'axis_labels': [(0, '0'), (1.84, '$F_α = 1.84$')],
        'bars': [('R', 1.84)], 'stat': (1.90, '$F = 1.90$')},
    'c89e2a4bd81e46a6967fd270bd1cba69': {
        'file': 'fig-11-12.svg', 'title': 'Figure 11.12 Example 8 rejection region',
        'alt': 'F density with 3 and 40 degrees of freedom. The right tail of area α = 0.05 beyond the critical value '
               'F_α = 2.84 is shaded. On the number line below, the rejection region F ≥ 2.84 is red, and the test '
               'statistic F = 3.232, marked with a star, lies inside it.',
        'kind': 'skew', **_f(3, 40), 'xmax': 6, 'ymax': 0.74, 'var': 'F', 'tails': [(2.84, 6)],
        'notes': [('$α = 0.05$', 4.2, 0.4, 3.2)], 'axis_labels': [(0, '0'), (2.84, '$F_α = 2.84$')],
        'bars': [('R', 2.84)], 'stat': (3.232, '$F = 3.232$')},
    '0cebffc666cda270843e897188456909': {
        'file': 'fig-11-13.svg', 'title': 'Figure 11.13 Example 9 rejection region',
        'alt': 'F density with 2 and 30 degrees of freedom, highest at 0 and decreasing. The thin right tail of area '
               'α = 0.01 beyond the critical value F_α = 5.39 is shaded. On the number line below, the rejection region '
               'F ≥ 5.39 is red, and the test statistic F = 5.65, marked with a star, lies just inside it.',
        'kind': 'skew', **_f(2, 30), 'xmax': 8, 'ymax': 1.02, 'var': 'F', 'tails': [(5.39, 8)],
        'notes': [('$α = 0.01$', 6.6, 0.3, 5.9)], 'axis_labels': [(0, '0'), (5.39, '$F_α = 5.39$')],
        'bars': [('R', 5.39)], 'stat': (5.65, '$F = 5.65$')},
})


# --- data plots and concept sketches: Chapters 1-4, 6, and 10 -------------------------------

LIGHT = '#7f9bd6'   # the source's pale outline blue for schematic histograms
PURPLE = '#9a3f8f'
TEAL = '#00a9c4'
SANS = "'Helvetica Neue',Arial,'Liberation Sans',sans-serif"


def mixture(*parts):
    """Density of a mixture of normals given as (weight, mean, sd) triples."""
    return lambda x: sum(w * phi((x - m) / s) / s for w, m, s in parts)


def mixture_stats(parts):
    mean = sum(w * m for w, m, s in parts)
    var = sum(w * (s * s + m * m) for w, m, s in parts) - mean * mean
    return mean, math.sqrt(var)


def mixture_cdf(parts):
    return lambda x: sum(w * Phi((x - m) / s) for w, m, s in parts)


def frame(d, x, y, w, h, color=GRAY, width=1.6):
    d.rect(x, y, w, h, color, width=width)


def bars(ax, lefts, width, heights, color=CURVE, stroke=1.8, fill='none', clip=None):
    """Histogram bars as outlined rectangles; heights are in data units."""
    for x, h in zip(lefts, heights):
        if h <= 0:
            continue
        x1, x2, y = ax.X(x), ax.X(x + width), ax.Y(h)
        ax.d.add(f'<rect x="{x1:.1f}" y="{y:.1f}" width="{x2 - x1:.1f}" height="{ax.base - y:.1f}" '
                 f'fill="{fill}" stroke="{color}" stroke-width="{stroke}"/>')


def y_ticks(ax, values, labels=None, size=24, right=True, font=None):
    for v, label in zip(values, labels or [f'{v:g}' for v in values]):
        y = ax.Y(v)
        ax.d.line(ax.left, y, ax.left + 8, y)
        if right:
            ax.d.line(ax.left + ax.width, y, ax.left + ax.width - 8, y)
        ax.d.text(ax.left - 8, y + size * 0.35, label, size, 'end')


def x_ticks(ax, values, labels=None, size=24, top=True, dy=34):
    for v, label in zip(values, labels or [f'{v:g}' for v in values]):
        x = ax.X(v)
        ax.d.line(x, ax.base, x, ax.base - 8)
        if top:
            ax.d.line(x, ax.top, x, ax.top + 8)
        ax.d.text(x, ax.base + dy, label, size)


def boxed_axes(d, left, top, width, height, x0, x1, y0, y1):
    """A framed plot whose y range starts at y0 (for scatter plots)."""
    ax = Axes(d, left, top, width, height, x0, x1, y1 - y0)
    ax.y0 = y0
    ax.Y = lambda y, ax=ax: ax.base - (y - ax.y0) / (ax.ymax) * ax.height
    frame(d, left, top, width, height, INK)
    return ax


def dots(ax, pts, r=8, color=CURVE):
    for x, y in pts:
        ax.d.circle(ax.X(x), ax.Y(y), r, color)


def stem_leaf(rows):
    d = Drawing(860, 560)
    for i, (stem, leaves) in enumerate(rows):
        y = 58 + i * 56
        d.text(78, y, str(stem), 42, 'end')
        for j, leaf in enumerate(leaves):
            d.text(140 + j * 72, y, str(leaf), 42)
    d.line(102, 14, 102, 545, INK, 2)
    return d


SCORES = [86, 80, 25, 77, 73, 76, 100, 90, 69, 93, 90, 83, 70, 73, 73, 70, 90, 83, 71, 95,
          40, 58, 68, 69, 100, 78, 87, 97, 92, 74]


def _stems(ordered):
    rows = []
    for stem in range(2, 11):
        leaves = [v % 10 if v < 100 else 0 for v in SCORES if v // 10 == stem]
        rows.append((stem, sorted(leaves) if ordered else leaves))
    return rows


def fig_1_01():
    d = Drawing(900, 700)
    filled = {(0, 0), (0, 7), (1, 1), (2, 2), (3, 4), (4, 0), (6, 4), (6, 5), (7, 5)}
    d.text(170, 42, 'Population', 30)
    frame(d, 20, 60, 300, 300, INK, 1.6)
    for r in range(8):
        for c in range(8):
            on = (r, c) in filled
            d.circle(45 + c * 36, 85 + r * 36, 9, INK if on else '#fff', INK, 1.6)
    d.text(505, 42, 'Sample', 30)
    frame(d, 440, 60, 130, 130, INK, 1.6)
    for r in range(3):
        for c in range(3):
            d.circle(465 + c * 40, 85 + r * 40, 9, INK)
    leader(d, 345, 120, 420, 120, True)
    leader(d, 505, 205, 505, 262, True)
    d.text(505, 300, 'Data', 30)
    d.text(505, 340, '$(x_1, x_2, ⋯, x_n)$', 30)
    leader(d, 505, 365, 505, 422, True)
    d.text(505, 470, 'Statistics', 30)
    d.text(170, 470, 'Parameters', 30)
    for i, (param, stat) in enumerate((('μ', '\\bar{x}'), ('σ^2', 's^2'), ('σ', 's'), ('p', '\\hat{p}'))):
        y = 525 + i * 45
        d.text(170, y, f'${param}$', 32)
        d.text(505, y, f'${stat}$', 32)
        leader(d, 440, y - 10, 250, y - 10, True)
    return d


def score_histogram(relative):
    d = Drawing(1000, 640)
    ymax = 0.4 if relative else 12
    ax = Axes(d, 110, 20, 850, 520, -20, 125, ymax)
    frame(d, ax.left, ax.top, ax.width, ax.height, INK)
    counts = {20: 1, 40: 1, 50: 1, 60: 3, 70: 10, 80: 5, 90: 7, 100: 2}
    bars(ax, [c - 5 for c in counts], 10, [n / 30 if relative else n for n in counts.values()])
    x_ticks(ax, list(range(0, 101, 10)), size=26)
    if relative:
        y_ticks(ax, [k * 0.05 for k in range(9)], [f'{k * 0.05:g}' for k in range(9)], 24)
    else:
        y_ticks(ax, list(range(0, 13, 2)), size=24)
    d.text(ax.X(50), ax.base + 72, 'Score', 28)
    d.vtext(28, ax.top + ax.height / 2, 'Relative Frequency' if relative else 'Frequency', 28)
    return d


def fig_2_05():
    d = Drawing(1000, 760)
    panels = (('(a) Small Sample', [1, 4, 3, 1]), ('(b) Medium Sample', [4, 2, 12, 10, 15, 12, 5, 10, 3, 1]),
              ('(c) Large Sample', None), ('(d) Very Large Sample', None))
    for i, (caption, counts) in enumerate(panels):
        left, top = 40 + (i % 2) * 490, 20 + (i // 2) * 370
        ax = Axes(d, left, top, 440, 280, -3.6, 3.6, 1.0)
        frame(d, left, top, 440, 300)
        d.line(left, ax.base, left + 440, ax.base, GRAY)
        if counts:
            n = len(counts)
            w = 6.0 / n
            peak = max(counts)
            bars(ax, [-3 + k * w for k in range(n)], w, [0.8 * c / peak for c in counts], LIGHT, 2)
        elif i == 2:
            w = 0.15
            ks = range(-20, 20)
            bars(ax, [k * w for k in ks], w, [0.8 * phi(k * w + w / 2) / phi(0) for k in ks], LIGHT, 1.4)
        else:
            ax.curve(lambda x: 0.8 * phi(x) / phi(0), -3, 3, LIGHT, 2.5)
        d.text(left + 220, top + 345, caption, 26)
    return d


def fig_2_06():
    d = Drawing(1000, 560)
    ax = Axes(d, 30, 80, 900, 400, -3.6, 3.6, 0.42)
    a, b, w = -1.1, 1.77, 0.1
    k = a
    while k < b - 1e-9:
        bars(ax, [k], w, [phi(k + w / 2)], CURVE, 1, FILL)
        k += w
    ax.curve(phi, -3.3, 3.3, CURVE, 2)
    ax.axis()
    d.text(ax.X(a), ax.base + 44, '$a$', 34)
    d.text(ax.X(b), ax.base + 44, '$b$', 34)
    d.text(500, 46, 'Shaded Area = Proportion of Data between $a$ and $b$', 32)
    return d


def density_panel(d, left, top, w, h, f, x0, x1, ymax, color=CURVE, width=3, ylabel=True, size=26, below=60):
    ax = Axes(d, left, top, w, h, x0, x1, ymax)
    frame(d, left, top, w, h + below, INK)
    d.line(left, ax.base, left + w, ax.base)
    if ylabel:
        d.vtext(left - 16, top + h / 2, 'Relative Frequency', size)
    return ax


TWO_HUMPS = ((0.35, -0.95, 0.55), (0.65, 0.85, 0.42))


def fig_2_07():
    d = Drawing(1000, 640)
    f, cdf = mixture(*TWO_HUMPS), mixture_cdf(TWO_HUMPS)
    ax = density_panel(d, 70, 20, 900, 520, f, -3.2, 2.6, 0.7)
    ax.curve(f, color=CURVE, width=3)
    m = quantile(cdf, 0.5, -3, 3)
    d.line(ax.X(m), ax.Y(f(m)), ax.X(m), ax.base, CURVE, 2)
    d.text(ax.X(m) - 90, ax.Y(0.2), '50%', 30)
    d.text(ax.X(m) + 90, ax.Y(0.2), '50%', 30)
    d.text(ax.X(m), ax.base + 40, 'Median', 30)
    return d


def fig_2_09():
    d = Drawing(1000, 640)
    f = mixture(*TWO_HUMPS)
    ax = density_panel(d, 70, 20, 900, 520, f, -3.2, 2.6, 0.7)
    ax.curve(f, color=PURPLE, width=3)
    mode = max((x / 1000 for x in range(-3000, 2600)), key=f)
    d.line(ax.X(mode), ax.base, ax.X(mode), ax.base - 12, INK, 6)
    d.text(ax.X(mode), ax.base + 40, 'Mode', 30)
    return d


def fig_2_08():
    d = Drawing(1000, 880)
    g = gamma_pdf(1.3, 1.3)
    gcdf = lambda x: gammainc(1.3, x / 1.3)
    shapes = [
        ('(a) $\\bar{x} = \\tilde{x}$', normal(0, 1), -3.5, 3.5, 0, 0),
        ('(b) $\\bar{x} = \\tilde{x}$', mixture((0.5, -1.2, 0.6), (0.5, 1.2, 0.6)), -3.5, 3.5, 0, 0),
        ('(c) $\\bar{x} > \\tilde{x}$', lambda x: g(x + 0.3), -0.5, 6, quantile(gcdf, 0.5) - 0.3, 1.69 - 0.3),
        ('(d) $\\bar{x} < \\tilde{x}$', lambda x: g(0.3 - x), -6, 0.5, -(quantile(gcdf, 0.5) - 0.3), -(1.69 - 0.3)),
    ]
    for i, (caption, f, x0, x1, med, mean) in enumerate(shapes):
        left, top = 60 + (i % 2) * 480, 15 + (i // 2) * 435
        peak = max(f(x0 + (x1 - x0) * k / 400) for k in range(401))
        ax = density_panel(d, left, top, 420, 260, f, x0, x1, peak * 1.12, size=20)
        ax.curve(f, color=LIGHT, width=2.5)
        d.line(ax.X(med), ax.Y(f(med)), ax.X(med), ax.base, LIGHT, 2)
        if med == mean:
            d.text(ax.X(med), ax.base + 30, '$\\bar{x}$', 22)
            d.text(ax.X(med), ax.base + 54, '$\\tilde{x}$', 22)
        else:
            d.text(ax.X(med), ax.base + 34, '$\\tilde{x}$', 22)
            d.text(ax.X(mean), ax.base + 34, '$\\bar{x}$', 22)
            d.line(ax.X(mean), ax.base, ax.X(mean), ax.base - 8)
        d.text(left + 210, top + 380, caption, 30)
    return d


def fig_2_10():
    d = Drawing(1000, 420)
    sets = (('(a) Set I', [40, 38, 42, 40, 39, 39, 43, 40, 39, 40]),
            ('(b) Set II', [46, 37, 40, 33, 42, 36, 40, 47, 34, 45]))
    for i, (caption, values) in enumerate(sets):
        left = 40 + i * 490
        ax = Axes(d, left, 20, 440, 300, 31, 51, 1)
        frame(d, left, 20, 440, 300, INK)
        x_ticks(ax, list(range(32, 51, 2)), size=20, dy=28)
        for v in sorted(set(values)):
            for k in range(values.count(v)):
                d.circle(ax.X(v), ax.base - 40 - k * 26, 9, CURVE)
        d.text(left + 220, 395, caption, 28)
    return d


def fig_2_11():
    d = Drawing(1000, 880)
    pale = '#8f9fd0'
    cases = (('(a) Two Identical Sets', [(0, 0.5, PURPLE)]),
             ('(b) Locations Differ', [(-0.6, 0.5, pale), (0.6, 0.5, REJECT)]),
             ('(c) Variabilities Differ', [(0, 0.6, pale), (0, 0.3, REJECT)]),
             ('(d) Locations and Variabilities Differ', [(0.5, 0.55, pale), (-0.6, 0.3, REJECT)]))
    for i, (caption, curves) in enumerate(cases):
        left, top = 60 + (i % 2) * 480, 15 + (i // 2) * 435
        ax = density_panel(d, left, top, 420, 260, None, -2.1, 2.1, 1.45, size=20)
        for mu, sigma, color in curves:
            ax.curve(normal(mu, sigma), mu - 3.3 * sigma, mu + 3.3 * sigma, color, 2.5)
        d.text(left + 210, top + 380, caption, 26)
    return d


def fig_2_12():
    d = Drawing(1000, 640)
    ax = density_panel(d, 70, 20, 900, 520, phi, -3.6, 3.6, 0.44)
    ax.curve(phi, -3.3, 3.3, CURVE, 2.5)
    q = 0.6745
    for x in (-q, 0, q):
        d.line(ax.X(x), ax.Y(phi(x)), ax.X(x), ax.base, CURVE, 2)
    for x in (-1.2, -0.34, 0.34, 1.2):
        d.text(ax.X(x), ax.Y(0.06), '25%', 28)
    for x, label in ((-q, '$Q_1$'), (0, '$Q_2$'), (q, '$Q_3$')):
        d.text(ax.X(x), ax.base + 42, label, 32)
    return d


def box_plot(values, labels, size=30, color=GRAY):
    d = Drawing(1000, 300)
    lo, hi = values[0], values[-1]
    X = lambda v: 70 + (v - lo) / (hi - lo) * 860
    xmin, q1, q2, q3, xmax = (X(v) for v in values)
    for x in (xmin, xmax):
        d.line(x, 30, x, 130, color, 2)
    d.line(xmin, 80, q1, 80, color, 2)
    d.line(q3, 80, xmax, 80, color, 2)
    d.rect(q1, 40, q3 - q1, 80, color, width=2)
    d.line(q2, 40, q2, 120, color, 2)
    d.line(20, 200, 980, 200, color, 2)
    for x, label in zip((xmin, q1, q2, q3, xmax), labels):
        d.circle(x, 200, 7, INK)
        d.text(x, 248, label, size)
    return d


def fig_2_14():
    d = Drawing(1000, 660)
    ax = density_panel(d, 70, 20, 900, 400, phi, -4.2, 4.2, 0.43, below=200)
    ax.curve(phi, -3.6, 3.6, CURVE, 4.5)
    d.add(f'<rect x="71" y="{ax.base - 1:.1f}" width="898" height="8" fill="#fff"/>')
    for row, (y, var, labels) in enumerate(((ax.base + 25, 'x', ['μ - 3σ', 'μ - 2σ', 'μ - σ', 'μ', 'μ + σ', 'μ + 2σ', 'μ + 3σ']),
                                             (ax.base + 100, 'z', ['-3', '-2', '-1', '0', '1', '2', '3']))):
        d.line(110, y, 935, y)
        d.text(950, y + 8, f'${var}$', 28, 'start')
        for k, label in zip(range(-3, 4), labels):
            d.line(ax.X(k), y, ax.X(k), y - 10)
            d.text(ax.X(k), y + 36, f'${label}$', 26)
    return d


HEIGHTS = [68.7, 72.3, 71.3, 72.5, 70.6, 68.2, 70.1, 68.4, 68.6, 70.6, 73.7, 70.5, 71.0, 70.9, 69.3, 69.4,
           69.7, 69.1, 71.5, 68.6, 70.9, 70.0, 70.4, 68.9, 69.4, 69.4, 69.2, 70.7, 70.5, 69.9, 69.8, 69.8,
           68.6, 69.5, 71.6, 66.2, 72.4, 70.7, 67.7, 69.1, 68.8, 69.3, 68.9, 74.8, 68.0, 71.2, 68.3, 70.2,
           71.9, 70.4, 71.9, 72.2, 70.0, 68.7, 67.9, 71.1, 69.0, 70.8, 67.3, 71.8, 70.3, 68.8, 67.2, 73.0,
           70.4, 67.8, 70.0, 69.5, 70.1, 72.0, 72.2, 67.6, 67.0, 70.3, 71.2, 65.6, 68.1, 70.8, 71.4, 70.2,
           70.1, 67.5, 71.3, 71.5, 71.0, 69.1, 69.5, 71.1, 66.8, 71.8, 69.6, 72.7, 72.8, 69.6, 65.9, 68.0,
           69.7, 68.7, 69.8, 69.7]


def two_row_labels(d, ax, positions, top, bottom, y, size=26):
    for x, a, b in zip(positions, top, bottom):
        d.text(ax.X(x), y, a, size)
        d.text(ax.X(x), y + size * 1.2, b, size)


def fig_2_15():
    d = Drawing(1000, 640)
    ax = density_panel(d, 70, 20, 900, 500, None, 64.3, 75.7, 0.15, below=100)
    tenths = [round(v * 10) for v in HEIGHTS]
    counts = [sum(655 + 5 * k <= t < 660 + 5 * k for t in tenths) for k in range(20)]
    bars(ax, [65.5 + 0.5 * k for k in range(20)], 0.5, [c / 100 for c in counts], CURVE, 1.8)
    mean, s = 69.92, 1.70
    ks = range(-3, 4)
    for k in ks:
        x = ax.X(mean + k * s)
        d.add(f'<rect x="{x - 4:.1f}" y="{ax.base - 10:.1f}" width="8" height="10" fill="{INK}"/>')
    tops = ['$\\bar{x} - 3s$', '$\\bar{x} - 2s$', '$\\bar{x} - s$', '$\\bar{x}$', '$\\bar{x} + s$', '$\\bar{x} + 2s$', '$\\bar{x} + 3s$']
    two_row_labels(d, ax, [mean + k * s for k in ks], tops, [f'{mean + k * s:.2f}' for k in ks], ax.base + 34)
    return d


SIGMA_TOP = ['$\\bar{x} - 3s$', '$\\bar{x} - 2s$', '$\\bar{x} - s$', '$\\bar{x}$', '$\\bar{x} + s$', '$\\bar{x} + 2s$', '$\\bar{x} + 3s$']
SIGMA_BOTTOM = ['$μ - 3σ$', '$μ - 2σ$', '$μ - σ$', '$μ$', '$μ + σ$', '$μ + 2σ$', '$μ + 3σ$']


def span_arrows(d, x1, x2, y, label, color, size=30):
    """A label between two arrows pointing out to x1 and x2."""
    mid, half = (x1 + x2) / 2, width(label, size) / 2 + 16
    for end, start in ((x1, mid - half), (x2, mid + half)):
        if abs(end - start) > 20:
            leader(d, start, y, end + (8 if end < start else -8), y, True, color)
    d.text(mid, y + size * 0.35, label, size, color=color)


def rule_lines(d, ax, levels, f, size=30, top=None, label_y=None):
    """Vertical lines at ±k standard deviations with the share of data between them."""
    for k, color, label, y in levels:
        for x in (-k, k):
            d.line(ax.X(x), ax.top + (top or 0) + y - 30, ax.X(x), ax.base, color, 2)
        span_arrows(d, ax.X(-k), ax.X(k), ax.top + (top or 0) + y, label, color, size)


GREEN_RULE = '#1a9a48'


def fig_2_16():
    d = Drawing(1000, 660)
    ax = density_panel(d, 70, 20, 900, 520, phi, -3.9, 3.9, 0.72, below=100)
    ax.curve(phi, color=CURVE, width=4.5)
    rule_lines(d, ax, ((3, REJECT, '≈ 99.7%', 40), (2, GREEN_RULE, '≈ 95%', 110), (1, REJECT, '≈ 68%', 180)), phi)
    for k in range(-3, 4):
        d.line(ax.X(k), ax.base, ax.X(k), ax.base - 8)
    two_row_labels(d, ax, list(range(-3, 4)), SIGMA_TOP, SIGMA_BOTTOM, ax.base + 32)
    return d


def fig_2_17():
    d = Drawing(1000, 660)
    ax = density_panel(d, 70, 20, 900, 520, phi, -3.9, 3.9, 0.62, below=100)
    ax.curve(phi, color=CURVE, width=4.5)
    rule_lines(d, ax, ((2, GREEN_RULE, '≈ 95%', 80), (1, REJECT, '≈ 68%', 150)), phi)
    labels = (('$μ - 2σ$', '66.9'), ('$μ - σ$', '68.2'), ('$μ$', '69.6'), ('$μ + σ$', '71.0'), ('$μ + 2σ$', '72.4'))
    for k in range(-2, 3):
        d.line(ax.X(k), ax.base, ax.X(k), ax.base - 8)
    two_row_labels(d, ax, list(range(-2, 3)), [a for a, b in labels], [b for a, b in labels], ax.base + 32)
    return d


def fig_2_18():
    d = Drawing(1100, 520)
    scores = [str(100 + 10 * k) for k in range(-3, 4)]
    for i in range(2):
        left = 70 + i * 530
        ax = density_panel(d, left, 20, 470, 330, phi, -3.9, 3.9, 0.75 if i == 0 else 0.5, size=20, below=70)
        ax.curve(phi, color=CURVE, width=3)
        if i == 0:
            rule_lines(d, ax, ((3, REJECT, '≈ 99.7%', 30), (2, GREEN_RULE, '≈ 95%', 80), (1, '#b3242a', '≈ 68%', 130)),
                       phi, size=20)
        else:
            for k, color, label, y in ((1, '#b3242a', '≈ 16%', 60), (2, GREEN_RULE, '≈ 2.5%', 120), (3, REJECT, '≈ 0.15%', 180)):
                x = ax.X(k)
                d.line(x, ax.top + y - 30, x, ax.base, color, 2)
                d.text(x + 8, ax.top + y - 8, label, 20, 'start', color)
                leader(d, x, ax.top + y, x + 70, ax.top + y, True, color)
        for k in range(-3, 4):
            d.line(ax.X(k), ax.base, ax.X(k), ax.base - 6)
        two_row_labels(d, ax, list(range(-3, 4)), SIGMA_BOTTOM, scores, ax.base + 24, 18)
        d.text(left + 235, 470, ('(a) Whole Spectrum', '(b) Higher End')[i], 28)
    return d


CHEBYSHEV = ((0.32, -1.25, 0.55), (0.68, 0.8, 0.6))


def fig_2_19():
    d = Drawing(1000, 660)
    f = mixture(*CHEBYSHEV)
    mean, sd = mixture_stats(CHEBYSHEV)
    ax = density_panel(d, 70, 20, 900, 520, f, mean - 3.9 * sd, mean + 3.9 * sd, 0.72, below=100)
    ax.curve(f, color=CURVE, width=4.5)
    for k, color, label, y in ((3, REJECT, 'at least 88.89%', 70), (2, GREEN_RULE, 'at least 75%', 130)):
        for x in (mean - k * sd, mean + k * sd):
            d.line(ax.X(x), ax.top + y - 30, ax.X(x), ax.base, color, 2)
        span_arrows(d, ax.X(mean - k * sd), ax.X(mean + k * sd), ax.top + y, label, color)
    xs = [mean + k * sd for k in range(-3, 4)]
    for x in xs:
        d.line(ax.X(x), ax.base, ax.X(x), ax.base - 8)
    two_row_labels(d, ax, xs, SIGMA_TOP, SIGMA_BOTTOM, ax.base + 32)
    return d


def fig_2_ex21():
    d = Drawing(1100, 520)
    f = mixture(*CHEBYSHEV)
    mean, sd = mixture_stats(CHEBYSHEV)
    xs = [mean + k * sd for k in range(-3, 4)]
    lo, hi = xs[1], xs[5]
    for i in range(2):
        left = 70 + i * 530
        ax = density_panel(d, left, 20, 470, 330, f, mean - 3.6 * sd, mean + 3.6 * sd, 0.5, size=20, below=70)
        if i == 0:
            ax.curve(f, lo, hi, CURVE, 3)
            for x in (lo, hi):
                d.line(ax.X(x), ax.Y(f(x)), ax.X(x), ax.base, GREEN_RULE, 1.6)
            lines = ('at least 75%', 'at least 38 obs.')
        else:
            ax.curve(f, ax.x0, lo, CURVE, 3)
            ax.curve(f, hi, ax.x1, CURVE, 3)
            for x in (lo, hi):
                d.line(ax.X(x), ax.Y(f(x)), ax.X(x), ax.base, GREEN_RULE, 1.6)
            lines = ('at most 25%', 'at most 12 obs.')
        for j, t in enumerate(lines):
            d.text(left + 235, 80 + j * 28, t, 22, color=GREEN_RULE)
        for x in xs:
            d.line(ax.X(x), ax.base, ax.X(x), ax.base - 6)
        bottom = [str(v) for v in (19, 22, 25, 28, 31, 34, 37)] if i == 0 else SIGMA_BOTTOM
        two_row_labels(d, ax, xs, SIGMA_TOP, bottom, ax.base + 24, 18)
        d.text(left + 235, 470, ('(a) Within $\\bar{x} ± 2s$', '(b) Outside $\\bar{x} ± 2s$')[i], 28)
    return d


def point(d, x, y, label, size=34, color=INK):
    """An outcome in a sample space: a dot and its label."""
    d.circle(x, y, 2.6, color)
    d.text(x + 10, y + size * 0.3, label, size, 'start', color)


def fig_3_01():
    d = Drawing(1000, 330)
    frame(d, 10, 10, 420, 210, GRAY, 3)
    point(d, 90, 115, '$h$')
    point(d, 320, 115, '$t$')
    frame(d, 560, 10, 420, 210, GRAY, 3)
    d.add(f'<ellipse cx="830" cy="105" rx="115" ry="95" fill="none" stroke="{CURVE}" stroke-width="3"/>')
    d.add(f'<ellipse cx="770" cy="155" rx="160" ry="32" fill="none" stroke="{REJECT}" stroke-width="3"/>')
    for x, y, n in ((640, 65, 1), (745, 65, 3), (850, 65, 5), (640, 162, 2), (745, 162, 4), (850, 162, 6)):
        point(d, x, y, str(n), 30)
    d.text(220, 300, '(a): One Coin Toss', 28)
    d.text(770, 300, '(b): One Die Roll', 28)
    return d


def fig_3_02():
    d = Drawing(820, 640)
    leaves = [30 + k * 82 for k in range(8)]
    mid2 = [(leaves[2 * k] + leaves[2 * k + 1]) / 2 for k in range(4)]
    mid1 = [(mid2[2 * k] + mid2[2 * k + 1]) / 2 for k in range(2)]
    root = sum(mid1) / 2
    size, blue = 48, CURVE
    for y, letter in zip(mid1, 'bg'):
        d.line(20, root, 100, y + (14 if letter == 'b' else -14), INK, 1.6)
        d.text(125, y + 16, f'${letter}$', size, color=blue)
        for y2, l2 in zip(mid2[:2] if letter == 'b' else mid2[2:], 'bg'):
            d.line(150, y, 270, y2, INK, 1.6)
            d.text(295, y2 + 16, f'${l2}$', size, color=blue)
            pair = leaves[:2] if (letter, l2) == ('b', 'b') else leaves[2:4] if (letter, l2) == ('b', 'g') else \
                leaves[4:6] if (letter, l2) == ('g', 'b') else leaves[6:]
            for y3, l3 in zip(pair, 'bg'):
                d.line(320, y2, 420, y3)
                d.text(445, y3 + 16, f'${l3}$', size, color=blue)
                d.text(700, y3 + 16, f'${letter}{l2}{l3}$', size, color=blue)
    return d


def fig_3_03():
    d = Drawing(1000, 400)
    frame(d, 90, 90, 350, 230, GRAY, 4)
    d.text(30, 215, '$S$ :', 34)
    for x, label, top in ((150, 1, True), (255, 2, True), (360, 3, True), (150, 4, False), (255, 5, False)):
        d.line(x, 45 if top else 300, x, 110 if top else 365, INK, 1.6)
        d.text(x, 30 if top else 395, f'$p_{label}$', 32)
    for x, y, label in ((135, 160, '$e_1$'), (240, 160, '$e_2$'), (345, 160, '$e_3$'), (135, 265, '$e_4$'), (240, 265, '$e_5$')):
        point(d, x, y, label, 30)
    d.text(380, 270, '⋯', 30)
    for y, a, b in ((70, '$A$ :', '{$e_1$, $e_2$}'), (115, '$B$ :', '{$e_2$, $e_3$, $e_4$}'),
                    (235, '$P(A)$', '=   $p_1 + p_2$'), (280, '$P(B)$', '=   $p_2 + p_3 + p_4$')):
        d.text(590, y, a, 34, 'end')
        d.text(620, y, b, 34, 'start')
    return d


def venn(fill):
    d = Drawing(1000, 660)
    d.rect(10, 10, 980, 640, CURVE, width=8)
    a, b = (440, 330, 220), (650, 330, 165)
    d.add(f'<defs><clipPath id="inA"><circle cx="{a[0]}" cy="{a[1]}" r="{a[2]}"/></clipPath></defs>')
    if fill == 'union':
        for cx, cy, r in (a, b):
            d.circle(cx, cy, r, TEAL)
    else:
        d.add(f'<circle cx="{b[0]}" cy="{b[1]}" r="{b[2]}" fill="{TEAL}" clip-path="url(#inA)"/>')
    for cx, cy, r in (a, b):
        d.circle(cx, cy, r, 'none', INK, 3)
    d.text(170, 170, '$A$', 60)
    d.text(870, 220, '$B$', 60)
    return d


def venn_points(points, b_shift=0):
    d = Drawing(1000, 520)
    frame(d, 10, 10, 980, 500, GRAY, 6)
    ax_, bx = 380, 560 + b_shift
    d.circle(ax_, 245, 185, 'none', REJECT, 5)
    d.circle(bx, 245, 185, 'none', CURVE, 5)
    for x, y, label in points:
        point(d, x, y, f'${label}$', 64)
    d.text(ax_ - 150, 470, '$A$', 72, color=REJECT)
    d.text(bx + 170, 470, '$B$', 72, color=CURVE)
    return d


def fig_3_06():
    d = Drawing(1000, 560)
    size = 44
    root = (20, 280)
    for y, letter, frac, kids in ((120, 'B', '7/10', (('B', '6/9', 40), ('W', '3/9', 200))),
                                  (440, 'W', '3/10', (('B', '7/9', 360), ('W', '2/9', 520)))):
        d.line(root[0], root[1], 150, y + (14 if letter == 'B' else -24))
        d.text(80, (root[1] + y) / 2 + 8, frac, 24, 'end')
        d.text(175, y + 16, f'${letter}$', size, color=CURVE)
        for kid, kf, ky in kids:
            d.line(200, y, 300, ky - 10)
            d.text(250, (y + ky) / 2 - 6, kf, 24)
            d.text(330, ky + 6, f'${kid}$', size, color=CURVE)
    d.circle(330, 23, 32, 'none', REJECT, 2.5)
    frame(d, 300, 145, 60, 255, GRAY, 3)
    for y, a, b, v in ((40, 'B', 'B', '7/10 · 6/9 = 0.47'), (200, 'B', 'W', '7/10 · 3/9 = 0.23'),
                       (360, 'W', 'B', '3/10 · 7/9 = 0.23'), (520, 'W', 'W', '3/10 · 2/9 = 0.07')):
        d.text(420, y, f'$P({a}_1 ∩ {b}_2)$ = {v}', 34, 'start')
    return d


def prob_histogram(xs, ps, yt, ylabels, xmin, xmax, ymax, shade_upto=None, extra=None, axis_only=False):
    d = Drawing(1000, 640)
    ax = Axes(d, 100, 20, 860, 540, xmin, xmax, ymax)
    d.line(ax.left, ax.base, ax.left + ax.width, ax.base)
    if not axis_only:
        d.line(ax.left, ax.base, ax.left, ax.top)
    for x, p in zip(xs, ps):
        fill = FILL if shade_upto is not None and x <= shade_upto else 'none'
        color = INK if shade_upto is not None and x <= shade_upto else CURVE
        bars(ax, [x - 0.5], 1, [p], color, 1.8, fill)
    if not axis_only:
        y_ticks(ax, yt, ylabels, 24, right=False)
        x_ticks(ax, xs, [str(x).replace('-', '−') for x in xs], 26, top=False)
    if extra:
        extra(d, ax)
    return d


def binom(n, p):
    return [math.comb(n, k) * p ** k * (1 - p) ** (n - k) for k in range(n + 1)]


def fig_4_06():
    ps = binom(15, 0.47)

    def extra(d, ax):
        d.text(ax.X(5), ax.base + 44, '$x$', 34, color=CURVE)
        d.text(ax.X(1.5), ax.Y(0.15), '$P(X ≤ x)$', 36, color=CURVE)
    return prob_histogram(list(range(16)), ps, [], [], -1.2, 15.5, 0.22, shade_upto=5, extra=extra, axis_only=True)


def three_normals(specs, x0, x1, ymax):
    d = Drawing(1000, 560)
    ax = Axes(d, 20, 70, 960, 420, x0, x1, ymax)
    for mu, sigma, color, label in specs:
        f = normal(mu, sigma)
        ax.curve(f, max(x0, mu - 4 * sigma), min(x1, mu + 4 * sigma), color, 4)
        ax.dashed(mu, f(mu))
        d.text(ax.X(mu) + 30, ax.Y(f(mu)) - 14, label, 40)
        d.text(ax.X(mu), ax.base + 42, f'${mu}$', 32)
    ax.axis()
    return d


def fig_6_01():
    d = Drawing(1000, 440)
    for i, (caption, xs, w, ps) in enumerate((('(a) Population', [152, 156, 160, 164], 4, [0.25] * 4),
                                              ('(b) Sample Mean', list(range(152, 165, 2)), 2,
                                               [k / 16 for k in (1, 2, 3, 4, 3, 2, 1)]))):
        left = 100 + i * 470
        ax = Axes(d, left, 30, 400, 300, xs[0] - w * 0.9, xs[-1] + w * 0.9, 0.29)
        frame(d, left, 30, 400, 340)
        d.line(left, ax.base, left + 400, ax.base, GRAY)
        bars(ax, [x - w / 2 for x in xs], w, ps, CURVE, 2.5)
        y_ticks(ax, [0, 0.05, 0.1, 0.15, 0.2, 0.25], ['0', '0.05', '0.10', '0.15', '0.20', '0.25'], 20, right=False)
        x_ticks(ax, xs, size=20, top=False, dy=30)
        d.vtext(left - 70, 180, 'Probability', 22)
        d.text(left + 200, 420, caption, 26)
    return d


def fig_6_02():
    d = Drawing(1000, 480)
    bw, scale, x, base = 14, 700, 40, 400
    for n, color in ((1, BROWN), (5, GREEN), (10, CURVE), (20, REJECT)):
        ps = binom(n, 0.5)
        for k, p in enumerate(ps):
            left = x + k * bw
            if p * scale >= 0.5:
                d.rect(left, base - p * scale, bw, p * scale, color, width=3.5)
            d.line(left + bw / 2, base, left + bw / 2, base + 7, INK, 1.2)
        d.text(x + (n + 1) * bw / 2, base - max(ps) * scale - 22, f'$n = {n}$', 34)
        d.text(x + bw / 2, base + 40, '0', 28)
        d.text(x + (n + 0.5) * bw, base + 40, '1', 28)
        x += (n + 1) * bw + 40
    d.line(20, base, 980, base, INK, 1.6)
    return d


def convolve(a, b):
    out = [0.0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def mean_density(masses, n):
    """Distribution of the mean of n draws from a discretized density (by repeated squaring)."""
    result, power, k = [1.0], masses, n
    while k:
        if k & 1:
            result = convolve(result, power)
        k >>= 1
        if k:
            power = convolve(power, power)
    return result


def sampling_cell(d, left, top, w, h, f, lo, hi, n, var, mean):
    N = 90
    step = (hi - lo) / N
    masses = [f(lo + (k + 0.5) * step) * step for k in range(N)]
    total = sum(masses)
    masses = [m / total for m in masses]
    if n == 1:
        xs = [lo + (k + 0.5) * step for k in range(N)]
        ys = masses
    else:
        dist = mean_density(masses, n)
        xs = [lo + (k / n + 0.5) * step for k in range(len(dist))]
        ys = dist
    peak = max(ys)
    ax = Axes(d, left, top, w, h, lo - 0.08 * (hi - lo), hi + 0.08 * (hi - lo), peak * 1.08)
    pts = [(ax.X(x), ax.Y(y)) for x, y in zip(xs, ys)]
    d.line(ax.left, ax.base, ax.left + w, ax.base, GRAY, 1.4)
    d.path('M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts), stroke=CURVE, width=2)
    if f is UNIFORM:
        for x in (lo, hi):
            d.line(ax.X(x), ax.Y(ys[0]) if n == 1 else ax.base, ax.X(x), ax.base, GRAY, 1.2, '5 4')
    my = max((y for x, y in zip(xs, ys) if abs(x - mean) < step), default=peak)
    d.line(ax.X(mean), ax.Y(my), ax.X(mean), ax.base, GRAY, 1.2, '5 4')
    d.text(ax.left + w + 8, ax.base + 6, f'${var}$', 22, 'start')


UNIFORM = lambda x: 1.0


def fig_6_03():
    d = Drawing(1100, 760)
    rows = (('Population', 'distribution'), ('Sampling', 'distribution', 'of $\\bar{X}$ with', '$n$ = 5'),
            ('Sampling', 'distribution', 'of $\\bar{X}$ with', '$n$ = 30'))
    skew = gamma_pdf(1.6, 1.0)
    bimodal = mixture((0.6, 0.35, 0.07), (0.4, 0.62, 0.09))
    pops = ((UNIFORM, 0, 1, 0.5), (bimodal, 0, 1, 0.6 * 0.35 + 0.4 * 0.62), (skew, 0, 7, 1.6))
    d.rect(5, 5, 1090, 750, INK, width=1.6)
    for x in (230, 517, 805):
        d.line(x, 5, x, 755)
    for r, lines in enumerate(rows):
        top = 30 + r * 245
        for j, t in enumerate(lines):
            d.text(25, top + 70 + j * 34 - (len(lines) - 2) * 17, t, 28, 'start')
        for c, (f, lo, hi, mean) in enumerate(pops):
            left = 255 + c * 288
            sampling_cell(d, left, top + 40, 220, 120, f, lo, hi, (1, 5, 30)[r], 'x' if r == 0 else '\\bar{x}', mean)
    return d


def fig_6_04():
    d = Drawing(1000, 1100)
    rows = (('Population', 'distribution'), ('Sampling', 'distribution', 'of $\\bar{X}$ with', '$n$ = 5'),
            ('Sampling', 'distribution', 'of $\\bar{X}$ with', '$n$ = 30'), ('Distributions', 'superimposed'))
    curves = ((1, BROWN), (1 / math.sqrt(5), REJECT), (1 / math.sqrt(30), CURVE))
    d.line(240, 10, 240, 1090)
    peak = phi(0) * math.sqrt(30)
    for r, lines in enumerate(rows):
        top = 20 + r * 270
        for j, t in enumerate(lines):
            d.text(20, top + 60 + j * 32, t, 26, 'start')
        ax = Axes(d, 290, top + 20, 620, 190, -3.6, 3.6, peak * 1.05)
        chosen = curves if r == 3 else (curves[r],)
        for sigma, color in chosen:
            ax.curve(normal(0, sigma), -3.4, 3.4, color, 2.2)
        ax.dashed(0, peak if r >= 2 else normal(0, curves[r][0])(0))
        ax.axis('x' if r == 0 else '\\bar{x}', 24)
        d.text(ax.X(0), ax.base + 30, '$μ$', 24)
    return d


def p_hat_histogram(d, left, top, w, h, p, n, x0, x1, ticks, lo_label, hi_label, size=22):
    sd = math.sqrt(p * (1 - p) / n)
    ax = Axes(d, left, top, w, h, x0, x1, phi(0) / sd * 1.05)
    ps = binom(n, p)
    bars(ax, [k / n - 0.5 / n for k in range(n + 1)], 1 / n, [q * n for q in ps], REJECT, 2.6)
    ax.curve(normal(p, sd), x0, x1, CURVE, 3)
    ax.axis()
    for v in ticks:
        d.line(ax.X(v), ax.base, ax.X(v), ax.base + 8)
        d.text(ax.X(v), ax.base + 30, f'{v:g}', size)
    for v, label in ((p - 3 * sd, lo_label), (p + 3 * sd, hi_label)):
        d.line(ax.X(v), ax.base - 4, ax.X(v), ax.base + 30, INK, 4.5)
        text = f'$p {"-" if v < p else "+"} 3√(p(1 - p)/n)$ = {label}'
        half = width(text, size) / 2
        d.text(min(max(ax.X(v), half + 4), d.width - half - 4), ax.base + 70, text, size)
    return ax


def fig_6_05():
    d = Drawing(1100, 440)
    p_hat_histogram(d, 30, 20, 500, 260, 0.1, 15, -0.2, 0.55, (0, 0.1, 0.5), '−0.13', '0.33', 20)
    p_hat_histogram(d, 580, 20, 500, 260, 0.1, 100, -0.02, 0.26, (0, 0.1, 0.2), '0.01', '0.19', 20)
    d.text(280, 420, '(a) $p$ = 0.1,  $n$ = 15', 26)
    d.text(830, 420, '(b) $p$ = 0.1,  $n$ = 100', 26)
    return d


def fig_6_06():
    d = Drawing(1000, 420)
    p_hat_histogram(d, 60, 10, 880, 290, 0.5, 15, -0.1, 1.1, (0, 0.5, 1), '0.11', '0.89', 28)
    return d


def arrow_axes(d, left, top, w, h):
    d.line(left, top + h, left + w, top + h, INK, 1.6)
    arrowhead(d, left + w, top + h, 0, 14)
    d.line(left, top + h, left, top, INK, 1.6)
    arrowhead(d, left, top, -math.pi / 2, 14)


def fig_10_01():
    d = Drawing(1000, 720)
    ax = Axes(d, 20, 70, 900, 580, -50, 75, 1)
    Y = lambda y: 650 - (y + 75) / 225 * 580
    d.line(ax.X(-50), Y(0), ax.X(75), Y(0))
    d.line(ax.X(0), Y(-75), ax.X(0), Y(140))
    for v in (-40, -20, 20, 40, 60):
        d.line(ax.X(v), Y(0), ax.X(v), Y(0) - 8)
        d.text(ax.X(v), Y(0) + 36, f'${v}$', 28)
    for v in (-50, 50, 100):
        d.line(ax.X(0), Y(v), ax.X(0) + 8, Y(v))
        d.text(ax.X(0) - 12, Y(v) + 10, f'${v}$', 28, 'end')
    d.text(ax.X(75) + 18, Y(0) + 12, '$x$', 40, 'start')
    d.text(ax.X(0), 40, '$y$', 40)
    for x, y in ((-40, -40), (-15, 5), (0, 32), (20, 68), (50, 122)):
        d.circle(ax.X(x), Y(y), 10, CURVE)
    return d


HEIGHT_WEIGHT = [(68, 151), (69, 146), (70, 157), (70, 164), (71, 171), (72, 160), (72, 163), (72, 180),
                 (73, 170), (73, 175), (74, 178), (75, 188)]
AUTOS = [(2, 28.7), (3, 24.8), (3, 26.0), (3, 30.5), (4, 23.8), (4, 24.6), (5, 23.8), (5, 20.4), (5, 21.6), (6, 22.1)]
ABSENCES = [(2, 76), (7, 29), (2, 96), (7, 63), (2, 79), (7, 71), (0, 88), (0, 92), (6, 55), (6, 70), (2, 80), (2, 75),
            (1, 63), (4, 41), (5, 63), (4, 88), (0, 98), (1, 99), (0, 89), (1, 96), (3, 90), (1, 90), (3, 68), (1, 84),
            (3, 80), (1, 78)]


def least_squares(pts):
    n = len(pts)
    mx, my = sum(x for x, _ in pts) / n, sum(y for _, y in pts) / n
    b1 = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return b1, my - b1 * mx


def scatter(pts, xr, yr, xt, yt, line=None, r=10, size=24, W=1000, H=760, extra=None):
    d = Drawing(W, H)
    ax = boxed_axes(d, 80, 20, W - 120, H - 90, *xr, *yr)
    x_ticks(ax, xt, [str(v).replace('-', '−') for v in xt], size)
    y_ticks(ax, yt, [str(v).replace('-', '−') for v in yt], size)
    if line:
        b1, b0 = line
        d.add('<clipPath id="plot"><rect x="{:.1f}" y="{:.1f}" width="{:.1f}" height="{:.1f}"/></clipPath>'.format(
            ax.left, ax.top, ax.width, ax.height))
        d.add(f'<line x1="{ax.X(xr[0]):.1f}" y1="{ax.Y(b1 * xr[0] + b0):.1f}" x2="{ax.X(xr[1]):.1f}" '
              f'y2="{ax.Y(b1 * xr[1] + b0):.1f}" stroke="{INK}" stroke-width="2.5" clip-path="url(#plot)"/>')
    if extra:
        extra(d, ax)
    dots(ax, pts, r)
    return d


def fig_10_03():
    d = Drawing(1000, 330)
    for i, pts in enumerate((SCATTER_A, SCATTER_B, SCATTER_C)):
        left = 10 + i * 333
        frame(d, left, 10, 315, 250)
        for x, y in pts:
            d.circle(left + x * 315, 10 + (1 - y) * 250, 5, CURVE)
        d.text(left + 157, 315, f'({"abc"[i]})', 40)
    return d


SCATTER_A = [(0.291, 0.703), (0.364, 0.584), (0.383, 0.584), (0.401, 0.584), (0.402, 0.636), (0.419, 0.584),
             (0.446, 0.6), (0.464, 0.6), (0.507, 0.451), (0.539, 0.463), (0.578, 0.408), (0.605, 0.336),
             (0.679, 0.266), (0.679, 0.308), (0.697, 0.266), (0.702, 0.353), (0.714, 0.28), (0.773, 0.266),
             (0.784, 0.218), (0.814, 0.169)]
SCATTER_B = [(0.314, 0.627), (0.388, 0.55), (0.41, 0.69), (0.42, 0.581), (0.426, 0.798), (0.443, 0.387),
             (0.469, 0.597), (0.487, 0.597), (0.531, 0.405), (0.562, 0.283), (0.601, 0.417), (0.628, 0.289),
             (0.702, 0.425), (0.709, 0.203), (0.714, 0.341), (0.725, 0.242), (0.738, 0.303), (0.796, 0.072),
             (0.808, 0.245), (0.838, 0.271)]
SCATTER_C = [(0.342, 0.74), (0.415, 0.65), (0.437, 0.615), (0.45, 0.716), (0.453, 0.348), (0.468, 0.716),
             (0.504, 0.298), (0.508, 0.358), (0.558, 0.79), (0.59, 0.805), (0.629, 0.665), (0.656, 0.458),
             (0.73, 0.246), (0.737, 0.658), (0.742, 0.464), (0.752, 0.555), (0.766, 0.359), (0.824, 0.526),
             (0.835, 0.576), (0.865, 0.27)]
# Figure 10.4 points, as fractions of each panel, measured from the source figure.
R_PANELS = [
    ('$r = -1$', [(0.282, 0.616), (0.333, 0.592), (0.386, 0.567), (0.488, 0.517), (0.592, 0.467), (0.695, 0.417),
                 (0.746, 0.393), (0.798, 0.368), (0.85, 0.342), (0.901, 0.318)]),
    ('$r = -0.94$', [(0.287, 0.815), (0.34, 0.716), (0.417, 0.74), (0.442, 0.641), (0.52, 0.492), (0.52, 0.616),
                     (0.571, 0.467), (0.648, 0.467), (0.726, 0.368)]),
    ('$r = +0.08$', [(0.447, 0.586), (0.447, 0.572), (0.473, 0.492), (0.499, 0.517), (0.551, 0.467), (0.551, 0.592),
                     (0.551, 0.691), (0.602, 0.541), (0.679, 0.517), (0.679, 0.616)]),
    ('$r = +1$', [(0.051, 0.175), (0.076, 0.224), (0.102, 0.275), (0.128, 0.324), (0.153, 0.373), (0.179, 0.423),
                 (0.231, 0.523), (0.282, 0.622), (0.333, 0.722), (0.411, 0.87)]),
    ('$r = +0.86$', [(0.34, 0.448), (0.365, 0.374), (0.417, 0.448), (0.442, 0.572), (0.52, 0.523), (0.571, 0.622),
                     (0.597, 0.523), (0.623, 0.696), (0.675, 0.622), (0.7, 0.697)]),
    ('$r = 0.00$', [(0.344, 0.498), (0.359, 0.583), (0.404, 0.658), (0.473, 0.713), (0.557, 0.743), (0.647, 0.743),
                   (0.73, 0.713), (0.799, 0.657), (0.844, 0.583), (0.859, 0.498)]),
]
# Figure 10.11 points and the line ŷ = ȳ, as fractions of the frame, measured from the source figure.
AROUND_MEAN = [(0.154, 0.469), (0.177, 0.401), (0.231, 0.434), (0.269, 0.583), (0.308, 0.401), (0.308, 0.434),
               (0.308, 0.5), (0.384, 0.517), (0.423, 0.334), (0.461, 0.5), (0.5, 0.667), (0.538, 0.5),
               (0.553, 0.334), (0.576, 0.583), (0.615, 0.434), (0.692, 0.4), (0.73, 0.534), (0.745, 0.457)]


def fig_10_04():
    d = Drawing(1000, 700)
    for i, (label, pts) in enumerate(R_PANELS):
        left, top = 20 + (i % 3) * 330, 10 + (i // 3) * 345
        w, h = 290, 280
        arrow_axes(d, left, top, w, h)
        for x, y in pts:
            d.circle(left + x * w, top + (1 - y) * h, 5.5, INK)
        d.text(left + w / 2, top + h - 18, label, 26)
        d.text(left + w / 2, top + h + 34, f'$({"abcdef"[i]})$', 26)
    return d


def fig_10_05():
    d = Drawing(1000, 560)
    arrow_axes(d, 60, 20, 880, 440)
    line = lambda x: 300 - (x - 150) * 0.28
    d.line(150, line(150), 900, line(900), INK, 1.4)
    for i, x in enumerate((240, 500, 760)):
        c = line(x)
        d.line(x, c - 100, x, c + 100, INK, 1.8)
        pts = [(x + 60 * math.exp(-((k - 60) / 22) ** 2 / 2), c + (k - 60) * 100 / 60) for k in range(121)]
        d.path('M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts), stroke=INK, width=1.8)
        d.line(x, c, x + 60, c, INK, 1.4)
        d.text(x + 60, c + 130, f'$N(β_1 x_{i + 1} + β_0, σ^2)$', 28)
        d.line(x, 460, x, 468)
        d.text(x, 505, f'$x_{i + 1}$', 30)
    d.text(60, 505, '0', 30)
    d.text(930, 505, '$x$', 30)
    d.text(30, 30, '$y$', 30)
    d.text(560, 55, '$E(Y) = β_1 x + β_0$', 30)
    leader(d, 600, 70, 680, line(680) - 6, True)
    return d


def fig_10_06():
    pts = [(2, 0), (2, 1), (6, 2), (8, 3), (10, 3)]

    def extra(d, ax):
        for x, y1, y2 in ((2, 1, 0), (10, 3, 4)):
            d.line(ax.X(x), ax.Y(y1), ax.X(x), ax.Y(y2), INK, 1.6)
        d.text(ax.X(0.9), ax.Y(0.45), '$error_2$', 32)
        d.text(ax.X(11.0), ax.Y(3.55), '$error_5$', 32)
        leader(d, ax.X(6), ax.Y(0), ax.X(4.3), ax.Y(1.07), True)
        d.text(ax.X(8), ax.Y(-0.5), '$\\hat{y}$ = ½$x - 1$', 36)
    return scatter(pts, (0, 12), (-2, 5), list(range(0, 13, 2)), list(range(-2, 6)), (0.5, -1), extra=extra)


def fig_10_11():
    d = Drawing(1000, 790)
    frame(d, 10, 10, 980, 770, INK)
    y_line = 10 + (1 - 0.47) * 770
    d.line(10, y_line, 990, y_line, INK, 2.5)
    for x, y in AROUND_MEAN:
        d.circle(10 + x * 980, 10 + (1 - y) * 770, 12, CURVE)
    d.text(890, y_line - 30, '$\\hat{y} = \\bar{y}$', 44)
    return d


def fig_10_12():
    d = Drawing(1100, 520)
    b1, b0 = least_squares(HEIGHT_WEIGHT)
    ybar = sum(y for _, y in HEIGHT_WEIGHT) / len(HEIGHT_WEIGHT)
    for i in range(2):
        left = 70 + i * 530
        ax = boxed_axes(d, left, 15, 460, 400, 66, 78, 140, 200)
        x_ticks(ax, list(range(66, 79, 2)), size=18, dy=26)
        y_ticks(ax, list(range(140, 201, 10)), size=18)
        fit = (lambda x: ybar) if i == 0 else (lambda x: b1 * x + b0)
        d.add(f'<clipPath id="p{i}"><rect x="{ax.left}" y="{ax.top}" width="{ax.width}" height="{ax.height}"/></clipPath>')
        d.add(f'<line x1="{ax.X(66):.1f}" y1="{ax.Y(fit(66)):.1f}" x2="{ax.X(78):.1f}" y2="{ax.Y(fit(78)):.1f}" '
              f'stroke="{INK}" stroke-width="1.8" clip-path="url(#p{i})"/>')
        for x, y in HEIGHT_WEIGHT:
            d.line(ax.X(x), ax.Y(y), ax.X(x), ax.Y(fit(x)), INK, 1.2)
        dots(ax, HEIGHT_WEIGHT, 5.5)
        d.text(ax.X(73.5), ax.Y(150), '$\\hat{y} = \\bar{y}$' if i == 0 else '$\\hat{y} = β_1 x + β_0$', 24)
        d.text(left + 230, 500, ('(a): Set I', '(b): Set II')[i], 26)
    return d


def _fig(file, title, alt, fn):
    return {'file': file, 'title': title, 'alt': alt, **_draw(fn)}


AUTO_LINE = least_squares(AUTOS)

FIGURES.update({
    '061a9224135424ca4644d6a0bb5f5913': _fig(
        'fig-01-01.svg', 'Figure 1.1 The grand picture of statistics',
        'A population drawn as a grid of 64 circles, nine of them filled, with an arrow to a sample of those nine. '
        'Arrows lead from the sample to its data (x₁, x₂, …, xₙ) and from the data to statistics x̄, s², s, and p̂, '
        'which point back to the population parameters μ, σ², σ, and p that they estimate.', fig_1_01),
    '34d76826b002f2409a8e598177892296': _fig(
        'fig-02-01.svg', 'Figure 2.1 Stem and leaf diagram',
        'Stem and leaf diagram of the 30 test scores, with stems 2 through 10 and leaves in the order the scores '
        'were listed: 2 | 5; 3 | (none); 4 | 0; 5 | 8; 6 | 9 8 9; 7 | 7 3 6 0 3 3 0 1 8 4; 8 | 6 0 3 3 7; '
        '9 | 0 3 0 0 5 7 2; 10 | 0 0.', lambda: stem_leaf(_stems(False))),
    'b62ceb194def760ed76d943233657c53': _fig(
        'fig-02-02.svg', 'Figure 2.2 Ordered stem and leaf diagram',
        'The stem and leaf diagram of the 30 test scores with each row of leaves sorted: 2 | 5; 3 | (none); 4 | 0; '
        '5 | 8; 6 | 8 9 9; 7 | 0 0 1 3 3 3 4 6 7 8; 8 | 0 3 3 6 7; 9 | 0 0 0 2 3 5 7; 10 | 0 0.',
        lambda: stem_leaf(_stems(True))),
    'f518083d74ec994b6c02eb6e18fd5178': _fig(
        'fig-02-03.svg', 'Figure 2.3 Frequency histogram',
        'Frequency histogram of the 30 test scores by tens: 1 score in the 20s, none in the 30s, 1 in the 40s, 1 in '
        'the 50s, 3 in the 60s, 10 in the 70s, 5 in the 80s, 7 in the 90s, and 2 of 100.', lambda: score_histogram(False)),
    '2e988c25b2cf9d6250febacb3b0ff940': _fig(
        'fig-02-04.svg', 'Figure 2.4 Relative frequency histogram',
        'Relative frequency histogram of the same 30 scores: the bar heights are the frequencies divided by 30, '
        'from 1/30 ≈ 0.033 for the 20s up to 10/30 ≈ 0.333 for the 70s.', lambda: score_histogram(True)),
    '3b57db67643235409d2ac7a8573ccda5': _fig(
        'fig-02-05.svg', 'Figure 2.5 Sample size and relative frequency histograms',
        'Four panels. (a) A small sample gives a histogram with four wide, uneven bars. (b) A medium sample gives ten '
        'narrower, still irregular bars. (c) A large sample gives many thin bars that trace a smooth bell shape. '
        '(d) A very large sample is represented by the smooth bell-shaped curve itself.', fig_2_05),
    '7642732fd47c976f06d45da450bfa675': _fig(
        'fig-02-06.svg', 'Figure 2.6 A very fine relative frequency histogram',
        'A bell-shaped curve with a very fine histogram filling the region under it between a and b; the shaded '
        'area equals the proportion of the data between a and b.', fig_2_06),
    '93901701128551a7274badd950102716': _fig(
        'fig-02-07.svg', 'Figure 2.7 The median',
        'A two-humped relative frequency curve with a vertical line at the median, which divides the area under '
        'the curve into two halves labeled 50% and 50%.', fig_2_07),
    '52c5252bed301c7ba46719c5cd5b4ee0': _fig(
        'fig-02-08.svg', 'Figure 2.8 Skewness of relative frequency histograms',
        'Four relative frequency curves. (a) A symmetric bell curve and (b) a symmetric two-humped curve, each with '
        'mean equal to median. (c) A curve skewed right, with a long right tail, has its mean to the right of its '
        'median. (d) A curve skewed left has its mean to the left of its median.', fig_2_08),
    '4a3fe4024f24270667c6a8c260f07ad0': _fig(
        'fig-02-09.svg', 'Figure 2.9 Mode',
        'A two-humped relative frequency curve; the mode is marked on the horizontal axis under its highest peak.',
        fig_2_09),
    '732c760e23369309481d84ec3452fa93': _fig(
        'fig-02-10.svg', 'Figure 2.10 Dot plots of data sets',
        'Dot plots on a scale from 32 to 50. (a) Set I: values tightly clustered at 38, 39, 39, 39, 40, 40, 40, 40, '
        '42, and 43. (b) Set II: values spread out at 33, 34, 36, 37, 40, 40, 42, 45, 46, and 47. Both sets have '
        'mean 40.', fig_2_10),
    '3af2fbfa7c4c956dff2d8aaafa146d2e': _fig(
        'fig-02-11.svg', 'Figure 2.11 Difference between two data sets',
        'Four panels, each with the relative frequency curves of two data sets. (a) The curves coincide. (b) The '
        'curves have the same shape but different centers. (c) The curves have the same center but one is much '
        'narrower. (d) The curves differ in both center and spread.', fig_2_11),
    'bd498ec19e330a43ba648c1e7df70db9': _fig(
        'fig-02-12.svg', 'Figure 2.12 Data division by quartiles',
        'A bell-shaped relative frequency curve divided by vertical lines at the quartiles Q₁, Q₂, and Q₃ into four '
        'regions, each labeled 25%.', fig_2_12),
    'cf516ad64fc6aacd308c937ab4f7bcd5': _fig(
        'fig-02-13.svg', 'Figure 2.13 The box plot',
        'A box plot above a number line marked x_min, Q₁, Q₂, Q₃, and x_max. The box spans Q₁ to Q₃ with a line at '
        'Q₂, and whiskers extend to x_min and x_max.',
        lambda: box_plot([0, 0.357, 0.5, 0.642, 1], ['$x_{\\text{min}}$', '$Q_1$', '$Q_2$', '$Q_3$', '$x_{\\text{max}}$'], 32)),
    '513b9995859fcb622bba8376c09253d8': _fig(
        'fig-02-13b.svg', 'Box plot for the Example 14 data',
        'Box plot of the data, drawn to scale above a number line marked 1.39, 1.90, 2.62, 3.33, and 4.00: whiskers '
        'from 1.39 to 1.90 and from 3.33 to 4.00, and a box from 1.90 to 3.33 with a line at the median 2.62.',
        lambda: box_plot([1.39, 1.90, 2.62, 3.33, 4.00], ['1.39', '1.90', '2.62', '3.33', '4.00'], 30, INK)),
    '26fd571691fc0707b45b01d2c189d453': _fig(
        'fig-02-14.svg', 'Figure 2.14 x-scale versus z-score',
        'A bell curve over two aligned scales. On the x scale the marks are μ − 3σ, μ − 2σ, μ − σ, μ, μ + σ, μ + 2σ, '
        'and μ + 3σ; on the z scale below, the same marks are −3, −2, −1, 0, 1, 2, and 3.', fig_2_14),
    'b1f0ebf6c74ac069e650a08a864bea87': _fig(
        'fig-02-15.svg', 'Figure 2.15 Heights of adult men',
        'Relative frequency histogram of the 100 heights in Table 2.2, in classes half an inch wide from 65.5 to 75.5 '
        'inches, roughly bell-shaped and centered near 70. The axis is marked at x̄ − 3s = 64.82, x̄ − 2s = 66.52, '
        'x̄ − s = 68.22, x̄ = 69.92, x̄ + s = 71.62, x̄ + 2s = 73.32, and x̄ + 3s = 75.02.', fig_2_15),
    '97b4fd107e5c4ef13ba13917c2a260a4': _fig(
        'fig-02-16.svg', 'Figure 2.16 The empirical rule',
        'A bell curve with vertical lines at one, two, and three standard deviations on each side of the mean. '
        'About 68% of the data lie between x̄ − s and x̄ + s (μ − σ and μ + σ), about 95% between x̄ − 2s and x̄ + 2s, '
        'and about 99.7% between x̄ − 3s and x̄ + 3s.', fig_2_16),
    'f69970cbd3a0d6b096373e3825dad1c2': _fig(
        'fig-02-17.svg', 'Figure 2.17 Distribution of heights',
        'A bell curve of heights with vertical lines at μ − 2σ = 66.9, μ − σ = 68.2, μ + σ = 71.0, and μ + 2σ = 72.4, '
        'around μ = 69.6. About 68% of heights lie between 68.2 and 71.0, and about 95% between 66.9 and 72.4.',
        fig_2_17),
    '72a9ca7507e4a5ae776ae9ccaa950617': _fig(
        'fig-02-18.svg', 'Figure 2.18 Distribution of IQ scores',
        'Two bell curves of IQ scores with mean 100 and standard deviation 10, marked at 70, 80, 90, 100, 110, 120, '
        'and 130. (a) Whole spectrum: about 68% of scores lie between 90 and 110, 95% between 80 and 120, and 99.7% '
        'between 70 and 130. (b) Higher end: about 16% of scores lie above 110, 2.5% above 120, and 0.15% above 130.',
        fig_2_18),
    '41250222aa4332d8af126bb8d898dcba': _fig(
        'fig-02-19.svg', 'Figure 2.19 Chebyshev’s theorem',
        'A lopsided two-humped curve, with vertical lines at two and three standard deviations from its mean. '
        'Whatever the shape, at least 75% of the data lie between x̄ − 2s and x̄ + 2s and at least 88.89% between '
        'x̄ − 3s and x̄ + 3s.', fig_2_19),
    'a86d2f0909ac477a1530f7c91e650de8': _fig(
        'fig-02-ex21.svg', 'Example 21: data within and outside x̄ ± 2s',
        'Two copies of a lopsided curve for a sample with mean 28 and standard deviation 3, marked at 19, 22, 25, '
        '28, 31, 34, and 37. (a) Only the part between 22 and 34 is drawn: at least 75%, so at least 38 of the 50 '
        'observations. (b) Only the parts outside that interval are drawn: at most 25%, so at most 12 observations.',
        fig_2_ex21),
    # Chapter 3
    '97b468eaa2da56c52e300c556c23a24f': _fig(
        'fig-03-01.svg', 'Figure 3.1 Venn diagrams for two sample spaces',
        '(a) One coin toss: a rectangle containing the outcomes h and t. (b) One die roll: a rectangle containing '
        'the outcomes 1 through 6, with a blue loop around 3, 4, 5, and 6 and a red loop around 2, 4, and 6.',
        fig_3_01),
    'e9de1d9b1c09ed5a0870567d7e5ad809': _fig(
        'fig-03-02.svg', 'Figure 3.2 Tree diagram for three-child families',
        'A tree diagram with three levels of branches, b (boy) or g (girl) for each child in birth order. Its eight '
        'paths give the outcomes bbb, bbg, bgb, bgg, gbb, gbg, ggb, and ggg.', fig_3_02),
    'b1371037e2e863e76e91bc00adf37f63': _fig(
        'fig-03-03.svg', 'Figure 3.3 Sample spaces and probability',
        'A sample space S drawn as a rectangle containing outcomes e₁, e₂, e₃, e₄, e₅, and more, each tagged with '
        'its probability p₁, p₂, …. For the events A = {e₁, e₂} and B = {e₂, e₃, e₄}, P(A) = p₁ + p₂ and '
        'P(B) = p₂ + p₃ + p₄.', fig_3_03),
    'c839ee4bf3bb6c5efce796861aee5142': _fig(
        'fig-03-04.svg', 'Figure 3.4 The intersection of events A and B',
        'Venn diagram of two overlapping circles A and B in a rectangle; only the overlap, A ∩ B, is shaded.',
        lambda: venn('intersection')),
    '2b9ac417d3f9501644f5bcc1cfdd8ebb': _fig(
        'fig-03-05.svg', 'Figure 3.5 The union of events A and B',
        'Venn diagram of two overlapping circles A and B in a rectangle; everything inside either circle, A ∪ B, '
        'is shaded.', lambda: venn('union')),
    '3ba777e453d1118c377ee69b788d0a74': _fig(
        'fig-03-ex7.svg', 'Venn diagram for Exercise 7',
        'Venn diagram of a sample space with outcomes a, b, c, d, and e and two overlapping events A (red) and B '
        '(blue). The outcome a is outside both events, b is in A only, c is in both A and B, and d and e are in B '
        'only.', lambda: venn_points([(140, 85, 'a'), (265, 230, 'b'), (520, 230, 'c'), (680, 150, 'd'), (680, 300, 'e')])),
    'cd8dc002db8c5f132bed316a3634ec00': _fig(
        'fig-03-ex8.svg', 'Venn diagram for Exercise 8',
        'Venn diagram of a sample space with outcomes a, b, c, and d and two overlapping events A (red) and B (blue). '
        'The outcome a is outside both events, b and c are in both A and B, and d is in B only.',
        lambda: venn_points([(140, 85, 'a'), (470, 175, 'b'), (470, 305, 'c'), (690, 245, 'd')], -60)),
    'd49c86e68633de7735225880cc896d8b': _fig(
        'fig-03-06.svg', 'Figure 3.6 Tree diagram for drawing two marbles',
        'Tree diagram for drawing two marbles without replacement from a jar of 7 black (B) and 3 white (W). The first draw is B with '
        'probability 7/10 or W with probability 3/10; after B, the second is B with probability 6/9 or W with 3/9; '
        'after W, B with 7/9 or W with 2/9. The path probabilities are P(B₁ ∩ B₂) = 0.47, P(B₁ ∩ W₂) = 0.23, '
        'P(W₁ ∩ B₂) = 0.23, and P(W₁ ∩ W₂) = 0.07. The two-blue outcome is circled and the two mixed outcomes are '
        'boxed together.', fig_3_06),
    # Chapter 4
    '5a6f9d6916537351ff23fd52c995f8f2': _fig(
        'fig-04-01.svg', 'Figure 4.1 Probability distribution for tossing a fair coin twice',
        'Probability histogram for the number of heads in two tosses of a fair coin: bars of height 0.25 at 0, 0.50 '
        'at 1, and 0.25 at 2.',
        lambda: prob_histogram([0, 1, 2], [0.25, 0.5, 0.25], [0.25, 0.5], ['0.25', '0.50'], -1, 3, 0.6)),
    '7a7d2ff3f3d6052070731dc4f23e5b15': _fig(
        'fig-04-02.svg', 'Figure 4.2 Probability distribution for tossing two fair dice',
        'Probability histogram for the sum of two fair dice, from 2 to 12: the bar heights rise from 1/36 at 2 to '
        '6/36 at 7 and fall back to 1/36 at 12.',
        lambda: prob_histogram(list(range(2, 13)), [(6 - abs(s - 7)) / 36 for s in range(2, 13)],
                               [k / 36 for k in range(1, 7)], [f'{k}/36' for k in range(1, 7)], 1.3, 12.8, 7.5 / 36)),
    'e9934b4ffecff3624a1002dbfc6a247c': _fig(
        'fig-04-03.svg', 'Figure 4.3 Probability distribution of a discrete random variable',
        'Probability histogram with bars of height 0.2 at −1, 0.5 at 0, 0.2 at 1, and 0.1 at 4; there are no bars at '
        '2 and 3.',
        lambda: prob_histogram([-1, 0, 1, 2, 3, 4], [0.2, 0.5, 0.2, 0, 0, 0.1], [0.1, 0.2, 0.3, 0.4, 0.5],
                               None, -1.6, 5, 0.6)),
    '38928bb96eec1a3decfd6ac8e189a437': _fig(
        'fig-04-04.svg', 'Figure 4.4 Probability distribution for three coins and three children',
        'Probability histogram for the number of heads in three coin tosses, or boys among three children: bars of '
        'height 0.125 at 0, 0.375 at 1, 0.375 at 2, and 0.125 at 3.',
        lambda: prob_histogram([0, 1, 2, 3], [0.125, 0.375, 0.375, 0.125], [0.125, 0.25, 0.375],
                               ['0.125', '0.25', '0.375'], -1, 4, 0.47)),
    '2fcd12630df97eb0e8aebc3dfb3e7887': _fig(
        'fig-04-05.svg', 'Figure 4.5 Probability distribution of the binomial random variable in Example 7',
        'Probability histogram of the binomial distribution with n = 5 and p = 0.17: bars of height 0.3939 at 0, '
        '0.4034 at 1, 0.1652 at 2, 0.0338 at 3, 0.0035 at 4, and 0.0001 at 5.',
        lambda: prob_histogram(list(range(6)), binom(5, 0.17), [0.1, 0.2, 0.3, 0.4, 0.5], None, -0.6, 6, 0.58)),
    'a939536e3189562fdfb0f9323e6c3e68': _fig(
        'fig-04-06.svg', 'Figure 4.6 Cumulative probabilities',
        'Probability histogram of a discrete random variable in which the bars for all values up to and including '
        'x are shaded; the shaded area is the cumulative probability P(X ≤ x).', fig_4_06),
    # Chapter 5 exercises
    'db1dd132366ddd980393bbe96e159b16': _fig(
        'fig-05-ex9.svg', 'Density curves for Exercise 9',
        'Three normal density curves: X_A (red), tall and narrow, centered at 100; X_B (blue), low and wide, '
        'centered at 200; and X_C (green), of intermediate height and width, centered at 300.',
        lambda: three_normals([(100, 7, REJECT, '$X_A$'), (200, 20, CURVE, '$X_B$'), (300, 15, GREEN, '$X_C$')],
                              -40, 440, 0.062)),
    '083b12c9ea22873dfeb903eb53fdebc1': _fig(
        'fig-05-ex10.svg', 'Density curves for Exercise 10',
        'Three normal density curves: X_A (red), of intermediate height, centered at −60; X_B (blue), the tallest '
        'and narrowest, centered at 0; and X_C (green), the lowest and widest, centered at 60.',
        lambda: three_normals([(-60, 10, REJECT, '$X_A$'), (0, 5, CURVE, '$X_B$'), (60, 20, GREEN, '$X_C$')],
                              -110, 145, 0.087)),
    # Chapter 6
    'c3b2aca7c7131e34c962382d64253af6': _fig(
        'fig-06-01.svg', 'Figure 6.1 Distribution of a population and a sample mean',
        '(a) Population: probability 0.25 at each of 152, 156, 160, and 164. (b) Sample mean of two draws: '
        'probabilities 1/16, 2/16, 3/16, 4/16, 3/16, 2/16, and 1/16 at 152, 154, 156, 158, 160, 162, and 164.',
        fig_6_01),
    '1137490f079c63b40d08ff8df24a962b': _fig(
        'fig-06-02.svg', 'Figure 6.2 Distributions of the sample mean',
        'Probability histograms of the sample mean of n draws from a population of 0s and 1s in equal proportion, '
        'each on its own scale from 0 to 1, for n = 1, 5, 10, and 20. For n = 1 there are two equal bars; as n grows '
        'the histogram becomes a narrower, taller bell centered at 0.5.', fig_6_02),
    '17fa70bfc1cbbc6d6476b9f45c9e9d07': _fig(
        'fig-06-03.svg', 'Figure 6.3 Distribution of populations and sample means',
        'A three-by-three grid. The top row shows three populations: uniform, two-humped, and skewed right. Below '
        'each are the distributions of the sample mean for n = 5, already more bell-shaped, and for n = 30, a '
        'narrow bell centered at the population mean in every case.', fig_6_03),
    '86efb32d8f607d8fc448b44f66c8a4c7': _fig(
        'fig-06-04.svg', 'Figure 6.4 Distribution of sample means for a normal population',
        'A normal population centered at μ, then the distributions of the sample mean for n = 5 and n = 30, which '
        'are normal, centered at μ, and progressively narrower and taller, and finally all three superimposed.',
        fig_6_04),
    '1f88d2a9e0be51323bf4afea7ec3a305': _fig(
        'fig-06-05.svg', 'Figure 6.5 Distribution of sample proportions',
        'Histograms of the sample proportion with normal curves overlaid, for p = 0.1. (a) For n = 15 the histogram '
        'is skewed right and the interval p ± 3√(p(1 − p)/n), from −0.13 to 0.33, extends below 0. (b) For n = 100 '
        'the histogram is nearly bell-shaped and the interval, from 0.01 to 0.19, lies within [0, 1].', fig_6_05),
    '50631caf59b26b1b3cdb66efe4c303ac': _fig(
        'fig-06-06.svg', 'Figure 6.6 Distribution of sample proportions for p = 0.5 and n = 15',
        'Histogram of the sample proportion for p = 0.5 and n = 15, symmetric about 0.5, with a normal curve '
        'overlaid; the interval p ± 3√(p(1 − p)/n), from 0.11 to 0.89, lies within [0, 1].', fig_6_06),
    # Chapter 10
    'f6698546a4f99e443e31429904be4b1b': _fig(
        'fig-10-01.svg', 'Figure 10.1 Plot of Celsius and Fahrenheit temperature pairs',
        'Five points on a straight line: (−40, −40), (−15, 5), (0, 32), (20, 68), and (50, 122), Celsius on the '
        'x-axis and Fahrenheit on the y-axis.', fig_10_01),
    '4c2bb10b324e3867ac83a97c18105190': _fig(
        'fig-10-02.svg', 'Figure 10.2 Plot of height and weight pairs',
        'Scatter plot of height (66 to 78 inches) against weight (140 to 200 pounds) for the 12 men in the sample; '
        'the points rise from (68, 151) and (69, 146) to (75, 188), in a loose upward band.',
        lambda: scatter(HEIGHT_WEIGHT, (66, 78), (140, 200), list(range(66, 79, 2)), list(range(140, 201, 10)))),
    '1a22032a1f4d609c4190985036b7f704': _fig(
        'fig-10-03.svg', 'Figure 10.3 Linear relationships of varying strengths',
        'Three scatter plots, each with a downward trend. (a) The points lie in a narrow band, a strong linear '
        'relationship. (b) The band is wider. (c) The points are widely scattered, a weak relationship.', fig_10_03),
    '07aa5db140b70615a15e8631c2d7a2c4': _fig(
        'fig-10-04.svg', 'Figure 10.4 Linear correlation coefficient R',
        'Six scatter plots with their correlation coefficients: (a) r = −1, points exactly on a falling line; '
        '(b) r = −0.94, close to a falling line; (c) r = +0.08, a shapeless cluster; (d) r = +1, exactly on a rising '
        'line; (e) r = +0.86, close to a rising line; (f) r = 0.00, points on an arch, a strong but nonlinear '
        'relationship.', fig_10_04),
    '88a6e0919d8617c025826c1e187ad591': _fig(
        'fig-10-05.svg', 'Figure 10.5 The simple linear model concept',
        'The line E(Y) = β₁x + β₀ rising across the plane. At three values x₁, x₂, and x₃, a normal curve drawn '
        'sideways and centered on the line shows the distribution of y, N(β₁xᵢ + β₀, σ²), with the same spread at '
        'each x.', fig_10_05),
    '2f707e3177c1a3f56b84fb8ded3894aa': _fig(
        'fig-10-06.svg', 'Figure 10.6 Plot of the five-point data and the line ŷ = ½x − 1',
        'The five points (2, 0), (2, 1), (6, 2), (8, 3), and (10, 3) with the line ŷ = ½x − 1. Vertical segments '
        'show error₂, from (2, 1) down to the line, and error₅, from (10, 3) up to the line.', fig_10_06),
    'afedcf81f03671c53e89f2cd1f907135': _fig(
        'fig-10-07.svg', 'Figure 10.7 Scatter diagram for age and value of used automobiles',
        'Scatter plot of age (0 to 8 years) against value (15 to 35 thousand dollars) for the ten automobiles in '
        'Table 10.3; value tends to fall with age.',
        lambda: scatter(AUTOS, (0, 8), (15, 35), list(range(9)), list(range(15, 36, 5)))),
    '9ee6d62cabb1f73795e6b98adf97a7be': _fig(
        'fig-10-08.svg', 'Figure 10.8 Scatter diagram and regression line for age and value of used automobiles',
        'The scatter plot of age against value for the ten automobiles, with the least squares regression line '
        'ŷ = −2.05x + 32.83 falling from about 32.8 at age 0 to about 16.4 at age 8.',
        lambda: scatter(AUTOS, (0, 8), (15, 35), list(range(9)), list(range(15, 36, 5)), AUTO_LINE)),
    'e3940708a65910fcf14d0a5e9ba1f037': _fig(
        'fig-10-11.svg', 'Figure 10.11',
        'Scatter plot of points with no trend, scattered above and below a horizontal line ŷ = ȳ at the mean of '
        'the y values.', fig_10_11),
    'ec63299e191a4e57190a20c7b48bd7ef': _fig(
        'fig-10-12.svg', 'Figure 10.12 Same scatter diagram with two approximating lines',
        'The height and weight data plotted twice. (a) With the horizontal line ŷ = ȳ, with vertical segments from '
        'each point to the line. (b) With the least squares regression line, with much shorter vertical segments.',
        fig_10_12),
    '13a3aacb719bc1a9c4ee14e3c9aef408': _fig(
        'fig-10-13.svg', 'Figure 10.13 Plot of the absence and exam score pairs',
        'Scatter plot of days absent (0 to 7) against final exam score (29 to 99) for the 26 students in Table 10.4; '
        'scores tend to fall as absences rise.',
        lambda: scatter(ABSENCES, (-3, 10), (20, 110), list(range(-2, 11, 2)), list(range(20, 111, 10)))),
})


def render(key):
    """Write one redrawn figure and return its path."""
    spec = FIGURES[key]
    if spec['kind'] == 'single':
        spec = {**spec, 'title': spec['title_markup']}
    d = KINDS[spec['kind']](spec)
    path = OUT / FIGURES[key]['file']
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(d.svg(FIGURES[key]['title'], FIGURES[key]['alt']))
    return path


def main():
    for key in FIGURES:
        path = render(key)
        print(f'{path.relative_to(ROOT)}  {hashlib.sha256(path.read_bytes()).hexdigest()[:12]}')


if __name__ == '__main__':
    main()
