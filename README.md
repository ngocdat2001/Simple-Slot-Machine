Simple Slot Machine

This is a simple slot machine which does not resemble the real machines in a casino. However, it
does demonstrate the concept of probability in an actual slot machine.
Write a program that allows the user to play a simplified version of a slot machine. The user starts
with $10. At the beginning of the program the user is given the following choices:
• Play the slot machine.
• Save game
• Cash out.
Each play costs 25 cents. For each play, the slot machine will output a random three-digit number,
where each digit ranges from 0 to 9. (This can be done by generating three separate integers in
between 0 and 9, inclusive.) The result of playing the slot machine should be outputted along with
what the user won. Here is a chart to indicate the winners earnings:

Combination Winnings
2 of a kind (such as 676 or 112) 50 cents
3 of a kind (000, 111, ..., 999) $10.00

(Thus technically, you make a net earnings of 25 cents if you get a 2 of a kind and a net earnings of
$9.75 when you get 3 of a kind.)
If a player runs out of money, automatically cash them out and tell them that they have no money
left. (Thus, a player, after losing who has 0 cents left should not be prompted with the menu at all.
Rather, they should simply be presented with a message to end the game.) Otherwise, when a
player chooses to cash out, thank them for playing and output how much money they have left.
Function details:
1. The choice entered by the user for the menu will always be valid.
2. If you choice 2, save your money to file. And restore the money in the play next time .
3. If you have no money to play any to more, say good bye.
