
# Monty Hall

## Description

The Monty Hall problem is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show Let's Make a Deal and named after its original host, Monty Hall. The problem was originally posed (and solved) in a letter by Steve Selvin to the American Statistician in 1975. It became famous as a question from reader Craig F. Whitaker's letter quoted in Marilyn vos Savant's "Ask Marilyn" column in Parade magazine in 1990.

## Problem

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

## Process

Available choices for player: from 1 to 3, each integer refers to a door: first, second or third.  

- User randomly choices to open one of the doors, let it be door A, and the probability that car is behind this door is 33.(3)%
- Probability that car is behind other doors is 66.(6)%
- Host opens one of the other doors, according to following rules:
    - Opened door is not the door selected by user
    - Car is not behind this door
- Calculatingly, from the users point of view, the probability, that car is behind the next closed door is equal to 66.(6)%, because:
    - A vs B + C = 33(3)% vs 66(6)%
    - Door has been opened, but probability still consists, nothing in probability of where the car was changed.
    - Remaining door accumulates the probability of itself and the opened door, which is 66(6)%
- This proves that it is worth to change initial choice

## Consol output

Values my be slightly different, but the ratio is the same for 1000 iterations

```
Win rate if insist = 34.0%
Win rate if not insist = 66.3%
```
