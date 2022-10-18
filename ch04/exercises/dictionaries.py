article = str.lower("Today, at an event at the White House, President Biden sought to draw contrasts between Democratic and Republican policies affecting seniors, suggesting his party is committed to lowering health-care costs while raising fears that GOP plans could jeopardize Medicare and Social Security. With the midterms looming, Biden took aim at three GOP lawmakers by name who he said are putting forward suspect plans: House Minority Leader Kevin McCarthy (Calif.) and Sens. Rick Scott (Fla.) and Ron Johnson (Wis.). The speech had been scheduled for delivery in Florida as part of a trip that was canceled because of Hurricane Ian. Also ahead of the hurricane’s landfall in Florida, the House committee investigating the Jan. 6, 2021, attack on the Capitol postponed its Wednesday hearing, committee leaders announced. On Capitol Hill, Senate Minority Leader Mitch McConnell (R-Ky.) endorsed the bipartisan electoral count reform bill, boosting legislative efforts to stave off another Jan. 6 crisis. The Senate voted to advance a stopgap funding measure to keep the government open beyond Friday after Sen. Joe Manchin III (D-W.Va.) voluntarily removed his language on permitting reform from the bill.")
dictionary = {
    "white house":"Pit of Despair",
    "allegedly":"totally",
    "bill":"snap I didn’t screenshot",
    "official":"puppy",
    "congressional":"spaaaaace",
    "republican":"piano accordionist",
    "democrat":"chromatic button accordionist",
    "senator": "magical wizard",
    "representative": "unmagical wizard",
    "secretary":"eating champion",
    "leaders":"goblins",
    "washington":"Mount Doom",
    "president": "you know, the guy"
}

for key, value in dictionary.items():
  article = article.replace(key, value)

print(article)