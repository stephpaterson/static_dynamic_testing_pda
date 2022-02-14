### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    # card.value is being assigned the value 1 with "=" where it should be compared with 1 by using '=='
    if card.value = 1:
      return True
    # Missing ':' after else.
    else
      return False
   
# Spelling error - should be def not dif.
# There is a comma missing between card1 and card2.
# There's an indentation error, lines 32 to 36 should be indented.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
# spelling error, this should say card1, card is not defined
    return card
  else:
    return card2
  


def cards_total(self, cards):
# total is not assigned a value.
  total
  for card in cards:
    total += card.value
# This will return a string where there is no space between 'of' and 'total' therfore it won't read very well.
    return "You have a total of" + total
  
```
