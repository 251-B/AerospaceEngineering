# Shared LaTeX fragments for the CL problems (class notation: bars for vectors, double bars for tensors).
import math

GAM = 1.4


def f(x, n=5):
    return f"{x:.{n}g}"


V = r"\bar{v}"
N = r"\bar{n}"
TAU = r"\bar{\bar{\tau}}'"
STEADY = r"\text{steady}"


def crossed(expr, why):
    """A term crossed out with the reason underneath."""
    return r"\underbrace{\cancel{" + expr + r"}}_{" + why + r"}"


# general balances (fixed or moving CV), with the usual crossings
MASS_FIXED = (crossed(r"\frac{d}{dt}\int_{V_c}\rho\,dV", r"0\ (\text{steady})")
              + r" + \int_{\Sigma_c}\rho\,(\bar{v} - " + crossed(r"\bar{v}_c", r"0") + r")\cdot\bar{n}\,d\sigma = 0")

MOM_FIXED_NOG = (crossed(r"\frac{d}{dt}\int_{V_c}\rho\bar{v}\,dV", r"0\ (\text{steady})")
                 + r" + \int_{\Sigma_c}\rho\bar{v}\,[(\bar{v} - " + crossed(r"\bar{v}_c", r"0") + r")\cdot\bar{n}]\,d\sigma"
                 + r" = -\int_{\Sigma_c}(p - p_a)\,\bar{n}\,d\sigma + \int_{\Sigma_c}\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma + "
                 + crossed(r"\int_{V_c}\rho\bar{g}\,dV", r"\text{neglect } \bar{g}"))

COL_MASS = r"\int\rho\,\bar{v}\cdot\bar{n}\,d\sigma"
COL_MFLUX = r"\int\rho\bar{v}\,(\bar{v}\cdot\bar{n})\,d\sigma"
COL_P = r"-\int(p - p_a)\,\bar{n}\,d\sigma"
COL_TAU = r"\int\bar{\bar{\tau}}'\cdot\bar{n}\,d\sigma"
