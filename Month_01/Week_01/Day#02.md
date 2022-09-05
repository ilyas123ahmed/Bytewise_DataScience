# Topic: The basics of probability for data science?

## What is probability?
The chance of an event occurring is called Probability. 

### The formula of probability:
The probability formula is defined as the possibility of an event to occur is equal to the ratio of the number of favorable outcomes and the total number of outcomes.
Probability of event to happen P (E) = Number of favorable outcomes / Total Number of outcomes


### Example 1: 
#### Tossing a coin:
Sample space is a possible outcome event that can occur. S = {H, T}
Number of favorable outcomes = 1
Total Number of outcomes = 2 
We put in the formula to get,
Probability of P (H) is = 1 / 2 


### Example 2: 
#### There are 6 pillows in a bed, 3 are red, 2 are yellow and 1 is blue. What is the probability of picking a yellow pillow?
The number of yellow pillows in the bed = 2
The total number of pillows = 6
The probability is equal to the number of yellow pillows in the bed divided by the total number of 
pillows, i.e. 2/6 = 1/3.


## Mutual exclusive event: 
### Example: 
#### Toss a coin:
When the event occurs either we get head or tail it is not possible to occur both events at a time.
The additive rule for the mutual exclusive event: 
P (H or T) = P (H) + P (T)
P (H or T) = 1/2 + 1/2
P (H or T) = 1


## NoN-mutual exclusive event: 
### Example: 
#### Taking a card from the deck:
K & heart
In this type of event, both events can occur at the same time.
The additive rule for the non-mutual exclusive events: Total cards = 52
K cards = 4
Heart cards = 13
P (k or heart) = P (k) + P (heart) – P (HEART and K)
P (heart) = 13/55
P (k) = 4 / 52
P (HEART and K) = 1 / 52
P (k or heart) = 13/ 52 + 4 / 52 – 1/52
P (k or heart) = 16 / 52 


## Multiplicative rule: 
### Independent event 
We call two events independent if the outcome of one of the events doesn't affect the outcome 
of another. 

#### For example: If we throw two dice, the probability of getting a 6 on the second die is the same, no matter what 
we get with the first one- it's still 1/6. 

### Dependent event 
When the probability of one event depends on another, the events are dependent.

#### For example: 
Suppose we have a bag containing 2 red and 2 blue balls. If we pick 2 balls out of the bag, the 
probability that the second is blue depends upon what the color of the first ball picked was. If the 
first ball was blue, there will be 1 blue and 2 red balls in the bag when we pick the second ball. So 
the probability of getting a blue is 1/3. However, if the first ball was red, there will be 1 red and 2 
blue balls left so the probability the second ball is blue is 2/3. 
