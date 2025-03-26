import scipy
from sympy.stats import Exponential
from sympy.stats import density
from sympy.stats import E, cdf, variance
from sympy import Symbol, Implies, And, Or
from sympy.logic.inference import satisfiable

rate = Symbol("lambda", positive=True)
a = Symbol("a")
b = Symbol("b")
X = Exponential("x", rate)

# неравенство Маркова
a_value = 10
rate_value = 5

m_a = E(X).subs(rate, rate_value) / a_value
cdf_a = cdf(X)(a)
cdf_value = cdf_a.subs({rate: rate_value, a: a_value})
print("E(X)/a: ", float(m_a))
print("P(X >= a): ", float(1 - cdf_value))

# неравенство Кантелли
b_value = 5

var = sympy.stats.variance(X).subs(rate, rate_value)
m = E(X).subs(rate, rate_value)
cdf_b = cdf(X - m)(b)
cdf_val = cdf_b.subs({rate: rate_value, b: b_value})
print("var/(var + b^2)", float(var/(var + b_value**2)))
print("P(X - m >= b)", float(1 - cdf_value))

# абдукция
H1 = Symbol("H1")
H2 = Symbol("H2")
H3 = Symbol("H3")
P1 = Symbol("P1")
P2 = Symbol("P2")

rule1 = Implies(P1, Or(H1, H2))
rule2 = Implies(P2, Or(H2, H3))
rule3 = And(P1, P2)

results = satisfiable(rule1 & rule2 & rule3, all_models=True)
for result in results:
    print(result)
