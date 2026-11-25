from typing import List


def reward_discount_ledger(rewards: List[float], gamma: float) -> float:
    """
    rewards: reward sequence r_0, ..., r_{T-1}, in order.
    gamma: discount factor in [0, 1].

    Compute G_0 = sum_{t=0}^{T-1} gamma**t * r_t, using the reward order as
    supplied (the first reward is discounted least, the last the most).
    """
    # TODO: accumulate the discounted return with a running discount factor.
    g_0, g = 0.0, 0
    
    for i in range (len(rewards)):
        g_0 += rewards[i] * gamma**g
        g += 1
    return g_0
