def enum(**enums):
    return type('Enum', (), enums)


STOCK_MODEL = enum(BLACK_SCHOLES="black_scholes", BINOMIAL_TREE="binomial_tree", MONTE_CARLO="monte_carlo")

# Constants
DEFAULT_BINOMIAL_TREE_NUM_STEPS = 25
DEFAULT_MONTE_CARLO_NUM_STEPS = 50
DEFAULT_MONTE_CARLO_NUM_PATHS = 100
